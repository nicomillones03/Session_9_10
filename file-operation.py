file_name = "x-file.txt"
fd = open(file_name, "a")  # "a" to append, w to write, r to read
while True:
    line = input("Enter a line (or just press Enter to quit): ")
    if line:
        fd.write(line + "\n")
    else:
        break

fd.close()
