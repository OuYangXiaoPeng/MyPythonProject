t1 = ("b", "g", "f", "d", "c", "a", "e")
list1 = list(t1)
# print(list1)

list2 = ["a", "b", "w", "z", "m", "f"]
list3 = []
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)
