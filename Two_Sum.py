def twosum(num, target):
    list = []
    for i in range(len(num)):
        for j in range(1, len(num)):
            if ((i != j) and (num[i] + num[j] == target)):
                list.extend([i,j])
                return list


print(twosum([1,2,3,5,6], 7))
