#from Selection_Sort import selection_sort
#from Bubble_sort import bubble_sort
#from Merge_Sort import merge_sort

def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
                temp = a_list[fill_slot]
                a_list[fill_slot] = a_list[pos_of_max]
                a_list[pos_of_max] = temp
     
def bubble_sort(a_list):
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
            

def merge_sort(a_list):
    #print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0 
        j=0 
        k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half): 
            a_list[k] = left_half[i] 
            i=i+1
            k=k+1
        while j < len(right_half): 
            a_list[k] = right_half[j] 
            j=j+1
            k=k+1
    #print("Merging ", a_list)
    



#===============================================================================
import random
import time

def main():
    print("Selection sort")
    list_size = 10000
    my_list = []
    total_time = 0

    while total_time < 60:
        my_list = []

        for i in range(list_size):
            my_list.append(random.randint(1,1000))
        start_time = time.time()
        selection_sort(my_list)
        stop_time = time.time()

        total_time = stop_time - start_time
        print(f"list size = {list_size}; execution time = {total_time:0.2f}")
        list_size = list_size + 10000

    print("Bubble sort")
    list_size = 10000
    my_list = []
    total_time = 0

    while total_time < 60:
        my_list = []

        for i in range(list_size):
            my_list.append(random.randint(1,1000))
        start_time = time.time()
        bubble_sort(my_list)
        stop_time = time.time()

        total_time = stop_time - start_time
        print(f"list size = {list_size}; execution time = {total_time:0.2f}")
        list_size = list_size + 10000
        
    print("Merge sort")
    list_size = 10000
    my_list = []
    total_time = 0

    while total_time < 60:
        my_list = []

        for i in range(list_size):
            my_list.append(random.randint(1,1000))
        start_time = time.time()
        merge_sort(my_list)
        stop_time = time.time()

        total_time = stop_time - start_time
        print(f"list size = {list_size}; execution time = {total_time:0.2f}")
        list_size = list_size + 10000

main()
        
