def bubble_sort(lst):
  for i in range(len(lst)):
    for j in range(1, len(lst)):
      if lst[j] < lst[j - 1]:
        temp = lst[j]
        lst[j] = lst[j - 1]
        lst[j - 1] = temp
    # sort the list via bubble sort
