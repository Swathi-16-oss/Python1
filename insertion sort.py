def insertion_sort(arr):  
  
        # Outer loop to traverse through 1 to len(list1)  
        for i in range(1, len(arr)):  
  
            value = arr[i]  
  
            # Move elements of list1[0..i-1], that are  
            # greater than value, to one position ahead  
            # of their current position  
            j = i - 1  
            while j>= 0 and value < arr[j]:  
                arr[j + 1] = arr[j]  
                j -= 1  
            arr[j + 1] = value  
        return arr  

n = int(input(""))
  
# Below line read inputs from user using map() function 
arr= list(map(int,input("").strip().split()))[:n]
  

insertion_sort(arr)


for i in range(len(arr)):
    print ("%d" %arr[i],end=" "),
'''o/p:
4
2 5 1 6
1 2 5 6 '''
