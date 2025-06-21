my_list = [1,2,3,4,5,6,7,8,9]
          #0,1,2,3,4,5,6,7,8 index value 
my_list2 = [11,12,13,14,15,16,17,18,19]
print(my_list)
print(my_list[3])
merger_list = my_list + my_list2
print(merger_list)

# enter int o list
my_list.append(20)
print(my_list)
my_list.remove(20)
print(my_list)
del my_list2[0:2]
print(my_list2)
#my_list2.clear()
print(my_list2) 
#my_list2.pop(3)
print(my_list2) 
my_list2.append(1)
print(my_list2) 
my_list2.sort()
print(my_list2) 
print(len(my_list2))
my_list2.extend(21)
print(my_list2) 

