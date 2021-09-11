import random
import time


def naive_search(l, target):
    for element in range(len(l)):
        if l[element] == target:
            return element
    return -1


def binary_search(l, target, low=None, high=None):
    if high is None:
        high = len(l) - 1 
    if low is None:
        low = 0
        
    if high < low:
        return -1
        
    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] > target:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high) 
        

if __name__ == '__main__':
    # target = 10
    # l = [2, 3, 5, 7, 8, 10, 17, 23]
    # print(naive_search(l, target))
    # print(binary_search(l, target))
    
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list)) 
    
    start = time.time() # gets the current time
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print('Naive search time: ' , (end - start) / length , ' seconds')
    
    start = time.time() # gets the current time
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('Binary search time: ' , (end - start) / length , ' seconds')
    
    