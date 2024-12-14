from aocd import data
import re

data = data.strip()
testdata = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(5,5!9)"

filter = re.split(r'(?=mul())', data)
sum = 0
for d in filter:
    if d.__contains__('mul(') :
        chars_to_remove = "mul("
        pattern = f"[{re.escape(chars_to_remove)}]"  # Create regex pattern
        test = re.sub(pattern, '', d )
        t = test.split(',')
        if len(t) >= 2 and t[1].__contains__(')'):
            nr2 = t[1].split(')')
            if nr2[0].isdigit() and t[0].isdigit():
                sum += int(t[0]) * int(nr2[0])
print("part 1 final sum: ", sum)
