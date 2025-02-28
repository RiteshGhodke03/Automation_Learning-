#open the file in read mode
file = open("test_file.txt","r")

#read data from the file
content = file.read()
print(content)

#file close
file.close()