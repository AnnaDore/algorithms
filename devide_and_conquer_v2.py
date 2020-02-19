def max(list3):
    if len(list3) == 2:
        if list3[0] > list3[1]:
            return list3[0]
        else:
            return list3[1]
    sub_max = max(list3[1:])
    if list3[0] > sub_max:
        return list3[0]
    else:
        return sub_max

print(max([2,7,3]))