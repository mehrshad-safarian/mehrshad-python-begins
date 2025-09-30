a = [5, 10]
print(id(a)) #large number represents location in memory

a = [5, 10]
b = a
# understanding how lists are stored 
a = [5, 10 ]
b = a
print("a:{}\t b: {}".format(a, b))
print("location a[0]: {}\t Location b[0]: {}".format ( id(a[0]), id(b[0] )))
a[0] = 20 #re-declaring the value of a[0] also changes b[0]
print( "a: {}\t b: {}".format(a, b))

# using [:] to copy a list 
data = [5,10,15,20]
data_copy = data [  :  ] # a single colon copies the list 
data[0] = 50
print( "data: {}\t data_copy: {}". format(data, data_copy) )