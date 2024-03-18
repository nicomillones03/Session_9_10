file_name = "x-file.txt"
fd = open(file_name)  # r is inplicit
print("Here are the contents of the file:")

# another way is to read it line by line
for line in fd:
    print(line, end="")
fd.close()

print("")

with open(file_name) as fd:
    print("Here are the 3 letter words:")
    for line in fd:
        words = line.split()
        for word in words:
            if len(word) == 3:
                print(word)
