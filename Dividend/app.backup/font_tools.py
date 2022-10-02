
def parantheses(num):
    return ' {0:.2f} '.format(
        num) if num >= 0 else ' ({0:.2f}) '.format(abs(num))


def red_highlight(inp_string):
    return "<font color='red'>" + inp_string + "</font>"
