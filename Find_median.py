array1 = dict()
array2 = dict()

x = int(input('Size of arr1'))
y = int(input('Size of arr2'))

for _ in range(x):
    temp = int(input())
    array1[temp] = 1

for _ in range(y):
    temp = int(input())
    array2[temp] = 1

result_arr = []
for key in array1:
    result_arr.append(key)
for key in array2:
    result_arr.append(key)
result_arr.sort()
print(result_arr[int(len(result_arr)/2)])
