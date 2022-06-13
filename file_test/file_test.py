file = open('test.txt', "w")
file.write("I am sucess!")
file.flush()
file_out = open('test.txt')
print(file_out.read())
for line in file_out:
    print(line)
file.close()
file_out.close()
