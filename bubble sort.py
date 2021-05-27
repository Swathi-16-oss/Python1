def bubbleSort(arr):  
    # Outer loop for traverse the entire list  
    for i in range(0,len(arr)-1):  
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
             
    return arr 
  
n=int(input(" "))  
# Below line read inputs from user using map() function 
arr= list(map(int,input("").strip().split()))[:n]
  
 
bubbleSort(arr)

for i in range(len(arr)):
    print ("%d" %arr[i],end=" "),

    '''o/p:
     4
1 5 2 3
1 2 3 5 '''
