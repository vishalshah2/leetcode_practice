def twosum(num, target):
    list = []
    for i in range(len(num)):
        for j in range(1, len(num)):
            if ((i != j) and (num[i] + num[j] == target)):
                list.extend([i,j])
                return list

n = int(input('Enter a number of elements: '))
input_list = []
for i in range(0, n):
    data = int(input())
    input_list.extend([data])

print(input_list)
target = int(input('Please provide target value: '))

print(twosum(input_list, target))
