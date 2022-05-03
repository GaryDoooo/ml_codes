# Copyright 2017 Garry Du
from stat_by_yf import question_gen
#  from markdown import markdown
#  import random
#  from page_key import page_key_compress as encode_key
#  from page_key import page_key_decompress as decode_key
#


def html_output(input_str):
    #  return markdown(input_str, extensions=['tables'])
    return input_str.replace('\n', '<br>')


def dispatch():
    ##### Generate problems. #####
    problem_list = question_gen()
    #  question_type_list_string, problem_num, page_key)

    return problem_list


if __name__ == "__main__":
    #  main()
    # TabNine::semSemantic completion enabled.
    print(dispatch())
