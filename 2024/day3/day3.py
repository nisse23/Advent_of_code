from aocd import data
import re

#data = data.strip()
testdata = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(5,5!9)"

splitdata = re.split(r'(?=mul())', testdata)
print(splitdata)
sum = 0
for d in splitdata:
    if d.__contains__('mul('):
        chars_to_remove = "mul("
        pattern = f"[{re.escape(chars_to_remove)}]"  # Create regex pattern
        test = re.sub(pattern, '', d )
        t = test.split(',')
        if len(t) >= 2 and t[1].__contains__(')'):
            nr2 = t[1].split(')')
            if nr2[0].isdigit() and t[0].isdigit():
                sum += int(t[0]) * int(nr2[0])
print("part 1 is", sum)
print()

#part 2
testdata = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Split on `mul()`
da = re.split(r'(?=mul())', data)

# Split on `do()` for each part in `da`
dat = [re.split(r'(?=do\(\))', part) for part in da]

# Split on `don't()` for each part in `dat` (flattened)
filter_result = [re.split(r'(?=don\'t\(\))', subpart) for part in dat for subpart in part]

# Flatten final result
final_filter = [item for sublist in filter_result for item in sublist]
sum = 0
do = True
for d in final_filter:
    if d.__contains__("do()"):
        do = True
    if d.__contains__("don't()"):
        do = False
    if d.__contains__("mul(") and do:
        chars_to_remove = "mul("
        pattern = f"[{re.escape(chars_to_remove)}]"  # Create regex pattern
        test = re.sub(pattern, '', d )
        t = test.split(',')
        if len(t) >= 2 and t[1].__contains__(')'):
            nr2 = t[1].split(')')
            if nr2[0].isdigit() and t[0].isdigit():
                sum += int(t[0]) * int(nr2[0])
print("Part 2 is", sum)