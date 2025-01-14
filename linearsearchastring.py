def string(arr,target):
    for i  in range(len(arr)):
        if arr[i]==target:
            return i
        else:
            print('not found')


arr='rohan'
target=str(input('enter the string'))

print(string(arr,target))