
try:
    user_input = input("Enter text to write to the file: : \n")
    with open('output.txt','w')as my_file: 
        my_file.write(user_input + '\n')
        print("Data Successfully written to output.txt\n") 
   

    append_input = input("Enter additional text to append: \n")
    with open('output.txt','a') as append_file:
        append_file.write(append_input + '\n')
        print("Data Successfully appended to output.txt \n")

    print("Final content of output.txt:")
    with open('output.txt','r') as read_file:
        for line in read_file:
            print(line) 
       

except FileNotFoundError:
    print(" file output.txt is not found ")

