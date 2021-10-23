n = int(input('Enter number of Element: '))
list= []

for i in range(n):
    data = int(input('Enter the velue of element ' + str(i+1) + ': '))
    list.extend([data])

target = int(input('Enter the Target value: '))
print('The list of Element ' + str(list) + ' And Target ' + str(target))

def twosum(num, target):
    ans = []
    print(len(num))
    for i in range(len(num)):
        for j in range(1, len(num)):
            if (i != j) and (num[i] + num[j] == target):
                ans.extend([i, j])
                return ans

print(twosum(list, target))

