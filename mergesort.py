def ASSIGNMENT(new_list, i, old_list, j):
    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    if (
        len(list_to_sort_by_merge) > 1
        and not len(list_to_sort_by_merge) < 1
        and len(list_to_sort_by_merge) != 0
    ):
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        mergeSort(left)
        mergeSort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
                l += 1
            else:
                ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


import matplotlib.pyplot as plt

""" 
- We print two plots next to each other: one before sorting and one after sorting.
- Since the values are discrete, it makes more sense to display them as bars.
- We also add the values on top of the bars to make it easier to track specific values.
- We use different colors for the two plots to make it easier to distinguish them.
"""
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

for ax in [ax1, ax2]:
    ax.set_xticks(x)
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.grid(True, axis="y", alpha=0.3)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)


# Plotting the original list before sorting
bars1 = ax1.bar(x, my_list, color="firebrick")
ax1.set_title("Before sorting", color="firebrick")
ax1.bar_label(bars1, padding=3, color="firebrick")
mergeSort(my_list)

# Plotting the sorted list after applying merge sort
bars2 = ax2.bar(x, my_list, color="green")
ax2.set_title("After sorting", color="green")
ax2.bar_label(bars2, padding=3, color="green")
plt.tight_layout()
plt.show()
