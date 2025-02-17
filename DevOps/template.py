filename = input("Enter the filename (without extension): ")
filename = filename if filename.endswith(".py") else filename + ".py"

purpose = input("Enter the purpose of the file: ")

with open(filename, "w") as file:
    file.write(f"""# Purpose: {purpose}\n""")

print(f"File '{filename}' has been created successfully.")
