# 1. It's conventional to list all imports at the top of the file.
import matplotlib.pyplot as plt

# 2. Renamed function (ASSIGNMENT => assign)
def assign(new_list, i, old_list, j): 
    new_list[i] = old_list[j]

# 3. Turned function name to snake case (mergeSort => merge_sort)
# 4. Renamed parameter (list_to_sort_by_merge => list)
def merge_sort(list): 
    # 5. Refactored the condition. We return early if the list has <= 1 element
    #    This makes the code easier to read
    if len(list) <= 1:
        return 

    mid = len(list) // 2
    # 6. Renamed variables (left => left_list, right => right_list)
    left_list = list[:mid]
    right_list = list[mid:]

    merge_sort(left_list)
    merge_sort(right_list)

    # 7. Extracted the merging logic to a separate function (merge)
    merge(list, left_list, right_list)

def merge(list, left_list, right_list):
    # We could also rename the variables (l, r, i) to be more descriptive (left_index, right_index, merged_index)
    # But subjectively in my opinion, they look better as they are, so I will keep them as is
    l = 0
    r = 0
    i = 0

    while l < len(left_list) and r < len(right_list):
        if left_list[l] <= right_list[r]:
            # 8. No need to use kwargs here
            assign(list, i, left_list, l)
            l += 1
        else:
            # 8. No need to use kwargs here
            assign(list, i, right_list, r)
            r += 1
        i += 1

    while l < len(left_list):
        list[i] = left_list[l]
        l += 1
        i += 1

    while r < len(right_list):
        list[i] = right_list[r]
        r += 1
        i += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# 9. Renamed variable (x => indices)
indices = range(len(my_list))

# 10. Changed the plot to a bar chart, as it is more appropriate for visualizing the list before and after sorting
plt.bar(indices, my_list)
plt.show()
merge_sort(my_list)
# 11. Removed the reassignment of indices.
plt.bar(indices, my_list)
plt.show()
