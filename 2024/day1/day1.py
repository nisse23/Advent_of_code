from aocd import data
#sorts the list
def quicksort (input_list) :
    if len(input_list) <= 1:
        return input_list
    pivot = len(input_list)//2
    left = []
    right = []
    middle = []
    for index in input_list:
        if index < input_list[pivot]:
            left.append(index)
        if index > input_list[pivot]:
            right.append(index)
        if index == input_list[pivot]:
            middle.append(index)
    return quicksort(left) + middle + quicksort(right)

#takes the absolute value of the difference between two list
def absdifferenceBetweenList(input_list1, input_list2):
    #returns -1 if the lists are different length
    if len(input_list1) != len(input_list2) :
        return [-1]
    #set the length of the final list to the highest list
    diffList = list(None for _ in range(max(len(input_list1), len(input_list2) )))
        
    if len(input_list1) <= len(input_list2):
        x = 0
        while x < len(input_list2):
            diffList[x] = abs(input_list1[x] - input_list2[x])
            x += 1
    return diffList

def sumList ( input_list):
    sum = 0
    for x in input_list:
        sum += x
    return sum

list1 = [3,4,2,1,3,3]
list2 = [4,3,5,3,9,3]

list3, list4 = zip(*[map(int, line.split()) for line in data.splitlines()])

sorted_list3 = quicksort(list3)
sorted_list4 = quicksort(list4)
#diffLis = absdifferenceBetweenList(sorted_list1, sorted_list2)
#print(sumList(diffLis))
#####
# part 2
#[1, 2, 3, 3, 3, 4]
#[3, 3, 3, 4, 5, 9]
sorted_list1 = quicksort(list1)
sorted_list2 = quicksort(list2)
def numberOfTimesInList(num, list1):
    times = 0
    for x in list1:
        if x == num:
            times += 1
    return times

y=0
for x in sorted_list3:
    y += x * numberOfTimesInList(x, sorted_list4)
print(y)