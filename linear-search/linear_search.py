def linear_search(lst, to_find):
  if to_find in lst:
    return lst.index(to_find)
  return -1

test
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
