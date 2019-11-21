list_one = [1,1]
for i in range(1, 99):
    list_one.append(list_one[i] + list_one[i-1])
print(list_one)
