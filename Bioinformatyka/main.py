
f = open("temp.txt","w+")
f2 = open("list.txt", "r")
contents = f2.read()
for i in range(len(contents) - 9):
    for j in range(10):
        f.write(contents[i+j])
    f.write('\n')
f.close()
f2.close()