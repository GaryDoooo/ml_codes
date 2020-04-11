def at(a, b):
    if "+" in a or "-" in a:
        a = "(%s)" % a
    if "+" in b or "-" in b:
        b = "(%s)" % b
    return "2x" + a + "+2x" + b


print(at("R", "T"))
print(at(at("A", "B"), "C"))
