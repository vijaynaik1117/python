try:
    with open('test.txt', 'r') as my_file:
        print ("Reading file content : \n")
        line_number = 1
        for line in my_file:
            print(f"Line {line_number}: {line}")
            line_number += 1
                  

except FileNotFoundError :
    print(f" the file 'test.txt' was not found")





