l = [ 9, 5, 2, 12, 3, 1, 3, 4, 7] # unsorted list

print(l)

def bubble_sort(lst):
    for outer_index in range(len(lst)-1): # len() starts counting form 1
        for inner_index in range(len(lst)-outer_index-1): # Left most item sorted first
            if lst[inner_index] > lst[inner_index + 1]: # compare
                lst[inner_index], lst[inner_index + 1] = lst[inner_index + 1], lst[inner_index] # swap

bubble_sort(l) # apply bubble sort to list
print(l)
