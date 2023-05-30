#!/usr/bin/env python
# coding: utf-8

# In[7]:


def add(a,b):
    x=float(a)
    y=float(b)
    return x+y
a=input("enter the number:")
b=input("enter the number:")
add(a,b)


# In[11]:


def bestFit(blockSize, m, processSize, n):
     
    # Stores block id of the block
    # allocated to a process
    allocation = [-1] * n
     
    # pick each process and find suitable
    # blocks according to its size ad
    # assign to it
    for i in range(n):
         
        # Find the best fit block for
        # current process
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1:
                    bestIdx = j
                elif blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j
 
        # If we could find a block for
        # current process
        if bestIdx != -1:
             
            # allocate block j to p[i] process
            allocation[i] = bestIdx
 
            # Reduce available memory in this block.
            blockSize[bestIdx] -= processSize[i]
 
    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "         ", processSize[i],
                                end = "         ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
 
# Driver code
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
 
    bestFit(blockSize, m, processSize, n)


# In[17]:


def firstFit(blockSize, m, processSize, n):
     
    # Stores block id of the
    # block allocated to a process
    allocation = [-1] * n
 
    # Initially no block is assigned to any process
 
    # pick each process and find suitable blocks
    # according to its size ad assign to it
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                 
                # allocate block j to p[i] process
                
                allocation[i] = j
                # Reduce available memory in this block.
                blockSize[j] = 0
                break
 
    print(" Process No. Process Size      Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i],
                          "         ", end = " ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
 
# Driver code
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
 
    firstFit(blockSize, m, processSize, n)


# In[3]:


list=[100,283,34,45,549]
def func():
    print(list.sort())
    print(sorted(list))
func()    
        


# In[6]:


# Prompt the user to enter a list of numbers
user_input = input("Enter a list of numbers, separated by spaces: ")

# Split the input into individual numbers and convert them to integers
numbers = [int(num) for num in user_input.split()]

# Sort the list of numbers in ascending order
sorted_numbers = sorted(numbers)

# Print the sorted list
print("Sorted list:", sorted_numbers)


# In[ ]:




