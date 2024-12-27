a = input('enter list of numbers')
list1 = a.split()
for i in range(0, len(list1)):
    for j in range(0,len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)


b = input('enter list of numbers')
list2 = b.split()
for x in range(0, len(list2)):
    for y in range(0,len(list2)-1):
        if list2[y] < list2[y+1]:
            list2[y], list2[y+1] = list2[y+1], list2[y]
print(list2)

c = input('enter list of words')
list3 = c.split()
for z in range(0, len(list3)):
    for v in range(0,len(list3)-1):
        if len(list3[v]) > len(list3[v+1]):
            list3[v], list3[v+1] = list3[v+1], list3[v]
print(list3)