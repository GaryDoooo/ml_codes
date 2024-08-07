import parsedatetime
import datetime
import gantt
from pandas import read_excel


def remove_nan(input_list):
    return [_ for _ in input_list if str(_) != 'nan']


def split_items_by_comma(input_list):
    splited = [j for _ in input_list for j in _.split(',')]
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
    print("string_to_date parsing", input_string)
    time, status = cal.parse(input_string)
    if status == 0:
        print("Status 0 parsing:", input_string)
    return datetime.date(time[0], time[1], time[2])


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
                    owner_index = find_index(resource_list, str(_))
                    if owner_index >= 0:
                        self.owner_list.append(resource_list[owner_index])

    def add_dependencies(self):
        depend_on = []
        if isnan(self.depend_on):
            self.depend_on = []
            return
        for _ in self.depend_on.split(","):
            task_index = find_index(task_list, str(_), by_task_number=True)
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


# Change font default
gantt.define_font_attributes(
    fill='black',
    stroke='black',
    stroke_width=0,
    font_family="Verdana")

df = read_excel("task.xlsx")  # , sheet_name="Data"¨)

resource_list = []
resources = split_items_by_comma(remove_nan(df['Owner'].unique()))
print("Found resources", resources)
for resource in resources:
    resource_list.append(gantt_resource(resource))

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
for task in task_list:
    task.start_date = get_start_date(task)
    if task.end_date is None:
        if task.duration is not None:
            if not task.is_milestone:
                task.end_date = task.start_date + \
                    datetime.timedelta(days=task.duration)
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
    task.generate_task_object()

# test printing
p = gantt.Project(name="test")
#  for task in task_list:
#  p.add_task(task.task)
p.add_task(task_list[0].task)
p.add_task(task_list[1].task)
p.add_task(task_list[2].task)
p.add_task(task_list[4].task)
p.add_task(task_list[3].task)

p.make_svg_for_tasks(
    filename='test2.svg',
    today=datetime.date(2020, 1, 31),
    scale=gantt.DRAW_WITH_MONTHLY_SCALE)
