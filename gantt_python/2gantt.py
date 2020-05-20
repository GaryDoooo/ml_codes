import parsedatetime
import datetime
import gantt
from pandas import read_excel
import argparse
import sys


def remove_nan(input_list):
    return [_ for _ in input_list if str(_) != 'nan']


def split_items_by_comma(input_list):
    splited = [j.replace(' ', '') for _ in input_list for j in _.split(',')]
    _set = set(splited)
    return list(_set)


class gantt_resource:
    def __init__(self, resource_name):
        self.name = resource_name
        self.resource = gantt.Resource(self.name)


def calendar_day_to_working_day(duration, start_date):
    day_of_week = start_date.weekday()
    weekend_days = int((day_of_week + duration) / 7) * 2
    if (day_of_week + duration) % 7 > 4:
        weekend_days = weekend_days + (day_of_week + duration) % 7 - 4
    if day_of_week > 4:
        weekend_days = weekend_days - (day_of_week - 4)
    if weekend_days > 0:
        duration = duration - weekend_days
    return duration


def find_index(input_class_list, name_to_find, by_task_number=False):
    if by_task_number:
        for i in range(len(input_class_list)):
            if input_class_list[i].task_number == name_to_find:
                return i
    else:
        for i in range(len(input_class_list)):
            if input_class_list[i].name == name_to_find:
                return i
    return -1


def isnan(x):
    return str(x) == "nan"


def string_to_date(input_string):
    cal = parsedatetime.Calendar()
    #  print("string_to_date parsing", input_string)
    time, status = cal.parse(input_string)
    if status == 0:
        print("Status 0 parsing:", input_string)
    return datetime.date(time[0], time[1], time[2])


def get_start_date(task):
    if task.start_date is not None:
        return task.start_date
    latest_end_date = None
    for _ in task.depend_on:
        start_date = get_start_date(_)
        if not isnan(_.duration):
            _.duration = int(_.duration)
            end_date = start_date + datetime.timedelta(days=_.duration)
        else:
            end_date = start_date
        if latest_end_date is None:
            latest_end_date = end_date
        else:
            timegap = latest_end_date - end_date
            if timegap.days < 0:
                latest_end_date = end_date
    # The depend on tasks end last is the earliest start date of this task
    return latest_end_date


class gantt_task:
    def __init__(
            self,
            task_number,
            name,
            start_date,
            end_date,
            duration,
            done,
            owner_list,
            priority,
            depend_on):
        global resource_list

        self.task_number = task_number
        self.name = name
        self.start_date = None
        self.end_date = None
        self.duration = duration
        self.done = 0
        self.owner_list = []
        self.priority = priority
        self.depend_on = depend_on
        if isnan(start_date) and isnan(end_date) and isnan(duration):
            self.is_milestone = True
        else:
            self.is_milestone = False
            if (not isnan(start_date)):
                self.start_date = string_to_date(start_date)
                if (not isnan(end_date)):
                    self.end_date = string_to_date(end_date)
                    self.duration = self.end_date - self.start_date
                    self.duration = self.duration.days
                elif (not isnan(duration)):
                    self.duration = int(duration)
                    self.end_date = self.start_date + \
                        datetime.timedelta(days=self.duration)
            elif (not isnan(end_date)) and (not isnan(duration)):
                self.end_date = string_to_date(end_date)
                self.duration = int(duration)
                self.start_date = self.end_date - \
                    datetime.timedelta(days=self.duration)
            if isnan(done):
                self.done = 0
            else:
                self.done = int(done)
            if not isnan(owner_list):
                for _ in owner_list.split(','):
                    owner_index = find_index(
                        resource_list, str(_).replace(' ', ''))
                    if owner_index >= 0:
                        self.owner_list.append(resource_list[owner_index])

    def add_dependencies(self):
        global task_list

        depend_on = []
        if isnan(self.depend_on):
            self.depend_on = []
            return
        for _ in self.depend_on.split(","):
            task_index = find_index(
                task_list, str(_).replace(
                    ' ', ''), by_task_number=True)
            if task_index >= 0:
                depend_on.append(task_list[task_index])
        self.depend_on = depend_on
        #  print("Added dependencies for", self.name, "with", self.depend_on)

    def generate_task_object(self):
        if self.priority == "High":
            color = "#FF8080"
        elif self.done == 100:
            color = "#808080"
        else:
            color = "#80FF80"
        try:
            if not self.is_milestone:
                self.task = gantt.Task(
                    name=self.name,
                    start=self.start_date,
                    duration=calendar_day_to_working_day(
                        self.duration + 1, self.start_date - datetime.timedelta(days=1)),
                    percent_done=self.done,
                    #  resources=self.owner_list,
                    color=color,
                    depends_of=[_.task for _ in self.depend_on])
            else:
                self.task = gantt.Milestone(
                    name=self.name,
                    depends_of=[_.task for _ in self.depend_on])
            return 1
        except AttributeError:
            return 0


def get_earliest_start_date(task_list):
    earliest = get_start_date(task_list[0])
    for _ in task_list:
        timegap = earliest - get_start_date(_)
        if timegap.days > 0:
            earliest = get_start_date(_)
    return earliest


def get_latest_end_date(task_list):
    task_list = [_ for _ in task_list if not _.is_milestone]
    latest_end_date = task_list[0].end_date
    for _ in task_list:
        timegap = latest_end_date - _.end_date
        if timegap.days < 0:
            latest_end_date = _.end_date
    return latest_end_date


def dispatch(
        inputfile,
        outputfile,
        verbose,
        project_name,
        today,
        prefixdays,
        suffixdays,
        weeklyscale):
    global resource_list
    global task_list

    # Change font default
    gantt.define_font_attributes(
        fill='black',
        stroke='black',
        stroke_width=0,
        font_family="Verdana")

    df = read_excel(inputfile)  # , sheet_name="Data"¨)

    resource_list = []
    resources = split_items_by_comma(remove_nan(df['Owner'].unique()))

    if verbose != "no":
        print("Found resources", resources)

    for resource in resources:
        resource_list.append(gantt_resource(resource))

    if verbose != "no":
        #  print(df[1])
        print(len(df))

    task_list = []
    for i in range(len(df)):
        task = gantt_task(
            df["Task#"][i],
            df["Name"][i],
            df["Start Date"][i],
            df["End Date"][i],
            df["#days long"][i],
            df["%Done"][i],
            df["Owner"][i],
            df["Priority"][i],
            df["Depend On"][i])
        task_list.append(task)
    for task in task_list:
        task.add_dependencies()
    task_index_list = list(range(len(task_list)))
    while len(task_index_list) > 0:
        unfinished_task = []
        for i in task_index_list:
            task = task_list[i]
            task.start_date = get_start_date(task)
            if task.end_date is None:
                if task.duration is not None:
                    if not task.is_milestone:
                        task.end_date = task.start_date + \
                            datetime.timedelta(days=task.duration)
            if verbose != "no":
                print(
                    "Task",
                    task.name,
                    "started at",
                    task.start_date,
                    "end date",
                    "duration", task.duration,
                    task.end_date, "owner",
                    [_.name for _ in task.owner_list],
                    "is milestone", task.is_milestone,
                    "depends_of",
                    [_.name for _ in task.depend_on]
                )
            if task.generate_task_object() == 0:
                unfinished_task.append(i)
        task_index_list = unfinished_task

    # test printing
    p = gantt.Project(name=project_name)
    for task in task_list:
        p.add_task(task.task)

    start_date = get_earliest_start_date(task_list)
    end_date = get_latest_end_date(task_list)
    if weeklyscale == "yes":
        p.make_svg_for_tasks(
            filename=outputfile,
            today=string_to_date(today),
            start=start_date - datetime.timedelta(days=prefixdays),
            end=end_date + datetime.timedelta(days=suffixdays),
            scale=gantt.DRAW_WITH_WEEKLY_SCALE)
    else:
        p.make_svg_for_tasks(
            filename=outputfile,
            today=string_to_date(today),
            start=start_date - datetime.timedelta(days=prefixdays),
            end=end_date + datetime.timedelta(days=suffixdays),
            scale=gantt.DRAW_WITH_DAILY_SCALE)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    parser.add_argument('--inputfile',
                        type=str,
                        help='The input xlsx file.')
    parser.add_argument(
        '--outputfile',
        type=str,
        default='gantt_output.svg',
        help='The output gantt chart file. Defaults to gantt_output.svg.')
    parser.add_argument('--verbose',
                        default="no",
                        type=str,
                        help='Display print output or not. Defaults to False.')
    parser.add_argument(
        '--project_name',
        default="",
        type=str,
        help='Project name displayed on the chart. Defaults to empty string.')
    parser.add_argument('--today',
                        default="today",
                        type=str,
                        help='The TODAY date in the chart. Defaults to today.')
    parser.add_argument(
        '--prefixdays',
        default=0,
        type=int,
        help='The extra days on the chart before the default start date.')
    parser.add_argument(
        '--suffixdays',
        default=10,
        type=int,
        help='The extra days on the chart after the default end date.')
    parser.add_argument(
        '--weeklyscale',
        default="no",
        type=str,
        help='Draw the chart with weekly scale instead of daily scale.')
    parse_args, unknown = parser.parse_known_args()
    dispatch(**parse_args.__dict__)
