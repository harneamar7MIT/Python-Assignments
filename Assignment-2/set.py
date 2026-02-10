set1 = set()
#print(type(set1))

set2 = {1, 2, 3, 4}                                                  #accessing set elements(using loop)
#print("set 2: ",set2)
print("elements in set2: ")
for items in set2:
    print(items)

set3 = (2, 8, 7 , 12)

#set2.add(6)                                                         #addition of new element in set2
#print("set 2: ",set2)

union_set = set2.union(set3)                                         #Union set
#print("union set: ",union_set)

intersection_set = set2.intersection(set3)                           #intersection set
#print("intersection set: ",intersection_set)

#print(len(set2))                                                    #length of a set2

difference_set = set2.difference(set3)                               #difference of sets(set2-set3)
#print("difference of set2 and set3: ",difference_set)
