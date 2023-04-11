with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

    exp = {}
def assignmentFunction(line):
    line = line.replace(" ","")
    expression = line.split("=")
    print(line)
    # print(expression[0], " = " , expression[1])
    exp[expression[0]] = expression[1]
    print()
for line in lines:
    # print(line)
    if("=" in line):
        assignmentFunction(line)

print(exp)
    # print()
