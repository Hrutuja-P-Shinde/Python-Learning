# tuples are immutable
a = (1 , 32, 342 , False , "Raj" , "Sham" )

print(a)
print(type(a))

number = a.count(1)
i =  a.index("Sham")

print(number)
print(i)

tuple1 = (1,2,3)
tuple2 = (4,5,6)
concatenated = tuple1 + tuple2
print(concatenated)

my_tuple = (1,2,3,4,4)
print(len(my_tuple))

t = (1,2,3)
repeated = t*3
print(repeated)


t_tuple = (0,1,2,3,4)
print(3 in t_tuple)
print(8 in t_tuple)