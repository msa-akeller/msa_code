
"""
Function to perform quick sort on array
Input: list
Output: sorted list
"""
def quick_sort(arr):
    #create a stack to simulate recursive calls
    stack = []
    #Place list partitions on the stack
    stack.append((0, len(arr) - 1))
    #Inside while loop. Loop runs until stack of partitions is empty
    while stack:
        #Get the next partition to process
        low, high = stack.pop()
        #Partition the array. Find the pivot index for that partition. Call the partition function
        pivot_index = partition(arr, low, high)
        #if there are items on the left of the pivot, put them on the stack
        if pivot_index - 1 > low:
            stack.append(low, pivot_index - 1)
        #if there are items on the right of pivot, put them on the stack
        if pivot_index + 1 < high:
            stack.append((pivot_index + 1, high))

"""
Function to find partition index in a list
Inputs: (list)arr, (int)low, (int)high
Output:(int)partition index
"""
def partition(arr, low, high):
    #Choose the right-most item as the pivot
    pivot = arr[high]
    i = low - 1
    #Create a variable for the border
    for j in range(low, high):
    #loop through the partition to place all items less than or equal to the pivot to the left. And >= pivot to the right
        if arr[high] <= pivot:
            i += 1
            arr[i], arr[high] = arr[high], arr[i]
        #if the current item is <= to the pivot, swap it with the element at the border
    #place pivot in correct position
    #Swap the pivot with the item at the border
    arr[i + 1], arr[high] = arr[high], arr[i +1]

    return i + 1

def main():
    #create a list
    arr = [40, 80, 10, 90, 30, 50, 70]
    quick_sort(arr)
    print(arr)

main()