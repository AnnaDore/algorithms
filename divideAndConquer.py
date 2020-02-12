def count(list2):
    if list2 == []:
        return 0
    else:
      return list2[0] + count(list2[1:])

print(count([2, 3, 4, 5]))