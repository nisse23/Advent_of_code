from aocd import data
import re

data = data.strip()
#print(len(data))
testdata = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(5,59)"

filter = re.split(r'(?=mul())', testdata)
shortlist = filter
sum = 0
i = 0
instructions = []
print(shortlist)
pairs = [[]]
for d in shortlist:
    i += 1
    if d.__contains__('mul(') :
        print(d)
        chars_to_remove = "mul("
        pattern = f"[{re.escape(chars_to_remove)}]"  # Create regex pattern
        test = re.sub(pattern, '', d )
        print(test)
        t = test.split(',')
        if len(t) >= 2:
            nr2 = t[1].split(')')
            if nr2[0].isdigit() and t[0].isdigit():
                pairs.append([ int(t[0]) , int(nr2[0])])
                sum += int(t[0]) * int(nr2[0])

print(pairs)
print("part 1 final sum: ", sum)
#print(instructions)
sum = 0
for item in instructions:
    try:
        if len(item) == 2:  # Ensure it forms a valid pair
            #print(item[0], " * " , item[1])
            sum += int(item[0]) * int(item[1])
    except ValueError:
        # Skip invalid entries
        pass

print(sum)