

#  todo Who Left the List?
# ? You are given two lists. The elements in lst1 threw a party and started to mix around. However, one of the elements got lost! Your task is to return the element which was lost.

# * Examples
# ? missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]) ➞ 2

# ? missing([True, True, False, False, True], [False, True, False, True]) ➞ True

# ? missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]) ➞ "ugly"

# ? missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]) ➞ (5,)
# ! Notes
# !Assume that the first list always contains 1 or more elements.
# !Elements are always lost.
# !An element can also have duplicates.


def missing(lst1, lst2):
    for x in lst1:
      if lst1.count(x) > lst2.count(x):
         return x
print(missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]))
print(missing([True, True, False, False, True], [False, True, False, True]))
print(missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]))