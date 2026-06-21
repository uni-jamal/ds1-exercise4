# 1. It's conventional to list all imports at the top of the file.
import matplotlib.pyplot as plt


# 2. Renamed function (ASSIGNMENT => assign)
def assign(new_list, i, old_list, j):
    new_list[i] = old_list[j]


# 3. Turned function name to snake case (mergeSort => merge_sort)
# 4. Renamed parameter (list_to_sort_by_merge => input_list)
def merge_sort(input_list):
    # 5. Refactored the condition. We return early if the list has <= 1 element
    #    This makes the code easier to read
    if len(input_list) <= 1:
        return

    mid = len(input_list) // 2
    # 6. Renamed variables (left => left_list, right => right_list)
    left_list = input_list[:mid]
    right_list = input_list[mid:]

    merge_sort(left_list)
    merge_sort(right_list)

    # 7. Extracted the merging logic to a separate function (merge)
    merge(input_list, left_list, right_list)


def merge(input_list, left_list, right_list):
    # We could also rename the variables (l, r, i) to be more descriptive (left_index, right_index, merged_index)
    # But subjectively in my opinion, they look better as they are, so I will keep them as is
    l = 0
    r = 0
    i = 0

    while l < len(left_list) and r < len(right_list):
        if left_list[l] <= right_list[r]:
            # 8. No need to use kwargs here
            assign(input_list, i, left_list, l)
            l += 1
        else:
            # 8. No need to use kwargs here
            assign(input_list, i, right_list, r)
            r += 1
        i += 1

    while l < len(left_list):
        input_list[i] = left_list[l]
        l += 1
        i += 1

    while r < len(right_list):
        input_list[i] = right_list[r]
        r += 1
        i += 1


""" 
- We print two plots next to each other: one before sorting and one after sorting.
- Since the values are discrete, it makes more sense to display them as bars.
- We also add the values on top of the bars to make it easier to track specific values.
- We use different colors for the two plots to make it easier to distinguish them.
"""
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
indices = range(len(my_list))

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

for ax in [ax1, ax2]:
    ax.set_xticks(indices)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.grid(True, axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


# Plotting the original list before sorting
bars1 = ax1.bar(indices, my_list, color="firebrick")
ax1.set_title("Before sorting", color="firebrick")
ax1.bar_label(bars1, padding=3, color="firebrick")
merge_sort(my_list)

# Plotting the sorted list after applying merge sort
bars2 = ax2.bar(indices, my_list, color="green")
ax2.set_title("After sorting", color="green")
ax2.bar_label(bars2, padding=3, color="green")
plt.tight_layout()
plt.show()
