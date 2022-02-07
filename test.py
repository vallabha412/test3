input_array = input().split(",")
row = input().split(",")
col = input().split(",")
num = input().split()
key = input()
print(input_array)
print(key)
for i in input_array:
    for j in key:
        if j in i:
            k = i.index(j)
            print(k)
        else:
            pass
