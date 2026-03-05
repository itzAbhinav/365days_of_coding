def contains_duplicates(arr):
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i - 1] == arr[i]:
            return True
    return False


arr = [1,2,3,0]

if(contains_duplicates(arr)):
    print("Duplicates exists")
else:
    print("No Duplicates")    
