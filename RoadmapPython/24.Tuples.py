print(20*"=" + "LIST" + 20*"=")
Odd = [1,3,5,7,9]
print(type(Odd)) # look type data
print(dir(Odd))  # knowing anything is can do in type data

# Tuple 
# Tuple Type Data Fix cannot extend,change,appen,remove
# Tuple more lighter than list

print("\n" + 20*"=" + "TUPLES" + 20*"=")
Even = (2,4,6,8)
print(type(Even))
print(dir(Even))

print("\n" + 20*"=" + "TUPLES EXAMPLE" + 20*"=")

print(10*"-" + "Memory Used")
import sys # knowing how much memory from type data

data_list  = [1,2,3,4,5,6,7,8,9]
data_tuple = (1,2,3,4,5,6,7,8,9)

howmuch_list  = sys.getsizeof(data_list)
howmuch_tuple = sys.getsizeof(data_tuple)

print(f"How much memory LIST used  : {howmuch_list}")
print(f"How much memory TUPLE used : {howmuch_tuple}")

print(10*"-" + "Time Used")
import timeit # knowing how much time from type data

howmuch_list2  = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]")
howmuch_tuple2 = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]")

print(f"How much time LIST used  : {howmuch_list2}")
print(f"How much time TUPLE used : {howmuch_tuple2}")


