for i in range(10, 21):
    print(i)

########
index = 0
for i in range(10, 21):
    print(f"{index}: Value = {i}")
    index += 1
#############
for index, value in enumerate(range(10, 21)):
    print(f"Index {index}: Value = {value}")