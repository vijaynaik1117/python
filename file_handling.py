# my_file = open('test.txt', 'r')

#with open('test.txt', 'r') as my_file:

#read a file 
'''
my_file = open('test.txt', 'r') 
    reading_file = my_file.read(3)
    print(reading_file)
    my_file.close()
'''
with open('test.txt', 'r') as my_file:
    reading_file = my_file.read()
    print(reading_file) 
'''
my_file = open('test.txt', 'w') 
writing_file = my_file.write('i am appending the file')
print(writing_file)
my_file.close()
'''
my_file = open('test.txt', 'a') 
writing_file = my_file.write('i am appending the file')
print(writing_file)
my_file.close()
