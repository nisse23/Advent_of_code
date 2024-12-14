from aocd import data

report = [list(map(int, line.split())) for line in data.strip().split('\n')]

def safeReport(list) -> bool:
    if len(list) <= 1:
        return True
    decrease = list[0] > list[1]
    for x in range(1, len(list)):
        if abs (list[x] - list[x-1]) > 3 or list[x] == list[x-1]:
            return False
        if list[x-1] < list[x] and decrease:
            return False 
        if list[x-1] > list[x] and not decrease:
            return False
    return True

testReport = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]

safe = 0
for x in testReport:
    if safeReport(x):
        safe += 1
#print(safe)

def compList(list) -> bool:
    if len(list) <= 1:
        return True
    decr = list[0] > list[1]
    for x in range(1, len(list)):
        if not comp(list[x], list[x-1], decr):
            return False
    return True

def comp (number1, number2, decr) -> bool:
    if not checkDiff(number1, number2):
        return False
    if decr :
        return number1 < number2
    return number1 > number2

def checkDiff (number1, number2) -> bool:
    x = abs (number1 - number2)
    if x > 3 or number1 == number2:
        return False
    return True

testReport = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]]

#compListAll(testReport[3])
print(testReport)
safe = 0
for x in report:
    if not compList(x):
        i = 0
        while i < len(x):
            removed = x.pop(i)
            if not compList(x):
                x.insert(i, removed)
            else:
                safe += 1
                break
            i += 1
    else :
        safe += 1
print(safe)