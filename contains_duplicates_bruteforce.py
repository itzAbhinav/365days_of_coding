def contains_duplicates(arr):

    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                count += 1
    if count > 0:
        return True
    return False            


arr = [1,2,3,1]
if(contains_duplicates(arr)):
    print("Duplicates exists")
else:   
    print("No Duplicates")