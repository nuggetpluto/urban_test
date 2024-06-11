def find_max(list_):
    max_ = 0
    for i in list_:
        if i > max_:
            max_ = i
    return max_
print(find_max([1, 54, 12, -1, 70, 4]))