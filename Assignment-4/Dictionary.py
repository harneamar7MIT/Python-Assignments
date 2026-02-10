d1 = {}
#print(type(d1))

d2 = { "Raju": "apple" , "Aman": "banana" , "Rahul": "guava" }
#print(d2)
#print(d2["Raju"])                                                      #we can use either line 6 or 7 ,output will be same
#print(d2.get("Raju"))

d2["Ankit"] = "kiwi"                                                    #addition of new key pair in dictionary
print(d2)

del d2["Ankit"]                                                         #removing/deleting of key pair
#print(d2)

print(d2.copy())                                                        #create shallow copy of dictionary
print(d2)


d2.update({"Raju": "papaya"})                                           #updating the dictionary with new word
print(d2)

#print(d2.keys())                                                       #display all keys in the dictionary

#print(d2.values())                                                     #display all values from the dictionary

#print(d2.items())                                                      #display all key-value pairs


