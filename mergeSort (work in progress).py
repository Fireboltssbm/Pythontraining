# mergesort algorithm borrowed: GeeksforGeeks (https://www.geeksforgeeks.org/merge-sort/)
# researched random number generation in python as well as writing to files for the project
# lines 6 to 46 is the algorithm

# Instructions are in ReadMe
# utilized "random" module to create randomly generated number array
# utilized "time" module to compute running time up to 8 decimal places
# utilized excel to create plots that are then put into a word document for the report
# creation time: 4/25/2022


from random import randint
import time

MAX_RANGE = 10000
# Python program for implementation of MergeSort (start of borrowed snippet)
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # recursively sorting the first half until there's no need to
        mergeSort(L)
  
        # recursively sorting the second half until there's no need to
        mergeSort(R)
        
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[], conjoining to a final array[k]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left between the two temporary arrays
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
# end of borrowed code snippet    
    
# Driver Code
if __name__ == '__main__':
    
    #initalizing an empty array for the generations
    arr = []
    
    #choice between random numbers or the same number
    choice = int(input("choose between random number generation [1] or same number [2]: "))
    
    #start of if block for choice 1
    if choice == 1:
        n = int(input("Choose a number of integers to generate: "))
        #nested if for the various test cases
        if n == 10:
            #adds randomly generated numbers for the array
            for _ in range(n):
                value = randint(0, MAX_RANGE)
                arr.append(value)
            print("given array is: ", end='\n')
            printList(arr)
            print('\n')
            
            #starts and ends timing the computation
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            
            print("sorted array is: ", end='\n')
            printList(arr)
            print('\n\n')
            
            #prints the time taken to compute to 10 decimal places
            total_time = end - start
            print('%.10f' % total_time)
            
        #else if for the other test cases (94 --> 152)
        elif n == 100:
            for _ in range(n):
                value = randint(0, MAX_RANGE)
                arr.append(value)
            
            # opens a file to write the arrays to
            file = open('100numbers.txt', 'w')
            file.write('given array is: ' + str(arr))
            file.write('\n\n')
            file.close()
            
            #computes running time for algorithm
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            #opens file again to write the final sorted array
            file = open('100numbers.txt', 'a')
            file.write("sorted array is: " + str(arr))
            file.write('\n\n')
            file.close()
            print("success! Check the local directory for the file")
            
            #prints computational time to the command line
            total_time = end - start
            print('%.10f' % total_time)
            
        elif n == 1000:
            for _ in range(n):
                value = randint(0, MAX_RANGE)
                arr.append(value)
            
            file = open('1000numbers.txt', 'w')
            file.write('given array is: ' + str(arr))
            file.write('\n\n')
            file.close()
            
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            file = open('1000numbers.txt', 'a')
            file.write("sorted array is: " + str(arr))
            file.write('\n\n')
            file.close()
            
            total_time = end - start
            print('%.10f' % total_time)
            print("\nsuccess! Check the local directory for the file")
        
        elif n == 10000:
            for _ in range(n):
                value = randint(0, MAX_RANGE)
                arr.append(value)
            
            file = open('10000numbers.txt', 'w')
            file.write('given array is: ' + str(arr))
            file.write('\n')
            file.write('\n')
            file.close()
            
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            file = open('10000numbers.txt', 'a')
            file.write("sorted array is: " + str(arr))
            file.write('\n\n')
            file.close()
            
            total_time = end - start
            print('%.10f' % total_time)
            print("\nsuccess! Check the local directory for the file")
            
        #just for the sake of completion, added a final generalized case
        else:
            print("Warning: out of bounds for the particular assignment\n")
            for _ in range(n):
                value = randint(0, MAX_RANGE)
                arr.append(value)
            print("given array is: ", end='\n')
            printList(arr)
            print('\n')
            mergeSort(arr)
            print("sorted array is: ", end='\n')
            printList(arr)
            
    #repeat above comments for second option        
    elif choice == 2:
        n = int(input("Choose a number of integers to generate: "))
        x = int(input("Choose which number to generate " + str(n) + " times: " ))
        if n == 10:
            for _ in range(n):
                # generates same number "x" amount of times
                value = (x)
                arr.append(value)
            print("given array is: ", end='\n')
            printList(arr)
            print('\n')
            
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            print("sorted array is: ", end='\n')
            printList(arr)
            total_time = end - start
            print('%.10f' % total_time)
        
        elif n == 100:
            for _ in range(n):
                value = (x)
                arr.append(value)
            
            file = open('100numbers(same).txt', 'w')
            file.write('given array is: ' + str(arr))
            file.write('\n\n')
            file.close()
            
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            file = open('100numbers(same).txt', 'a')
            file.write("sorted array is: " + str(arr))
            file.write('\n\n')
            file.close()
            
            total_time = end - start
            print('%.10f' % total_time)
            print("\nsuccess! Check the local directory for the file")
        
        elif n == 1000:
            for _ in range(n):
                value = (x)
                arr.append(value)
            
            file = open('1000numbers(same).txt', 'w')
            file.write('given array is: ' + str(arr))
            file.write('\n')
            file.write('\n')
            file.close()
            
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            file = open('1000numbers(same).txt', 'a')
            file.write("sorted array is: " + str(arr))
            file.write('\n\n')
            file.close()
            
            total_time = end - start
            print('%.10f' % total_time)
            print("\nsuccess! Check the local directory for the file")        
        
        elif n == 10000:
            for _ in range(n):
                value = (x)
                arr.append(value)
            
            file = open('10000numbers(same).txt', 'w')
            file.write('given array is: ' + str(arr))
            file.write('\n\n')
            file.close()
            
            start = time.time()
            mergeSort(arr)
            end = time.time()
            
            file = open('10000numbers(same).txt', 'a')
            file.write("sorted array is: " + str(arr))
            file.write('\n\n')
            file.close()
            
            total_time = end - start
            print('%.10f' % total_time)
            print("\nsuccess! Check the local directory for the file")        
        
        else:
            print("WARNING: OUT OF BOUNDS FOR ASSIGNMENT\n")
            for _ in range(n):
                value = (x)
                arr.append(value)
            print("given array is: ", end='\n')
            printList(arr)
            print('\n')
            mergeSort(arr)
            print("sorted array is: ", end='\n')
            printList(arr)
    
    #for completion sake
    else:
        print('invalid selection, please run again with correct selection')
        quit()