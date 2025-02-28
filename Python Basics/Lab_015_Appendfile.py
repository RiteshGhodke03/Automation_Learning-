#file open in append mode
file = open("test_file.txt","a")
file.write("\nAdding new line to the file ")
file.close()

file = open("test_file.txt", "r")
content = file.read()
print(content)
file.close()