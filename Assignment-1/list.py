grocery =  ["lollipop", "vim", "hit" ]      #example 1
#print(grocery)

list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]   #example 2
#print(list)
#print(list[2])                               #accessing the element
#print(list[9])                               #error:out of range

numbers = [ 2, 3 , 4 ,9 , 2]                  #example 3
#numbers.sort()                               #sorting
#print(numbers)
#numbers.reverse()                            #reversing
#print(numbers)

#print(numbers[1:3])                          #slicing

#print(len(numbers))                          #length of list
#print(max(numbers))                          #highest number in list
#print(min(numbers))                          #lowest number in list

numbers.append(8)                             #append
print(numbers)

numbers.insert(6 , 6)             #insert
print(numbers)

numbers.remove(9)                              #delete/remove
print(numbers)

numbers.pop()                                  #pop
print(numbers)
