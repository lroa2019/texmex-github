file1 = open('recetas.md', 'r')
Lines = file1.readlines()
 
count = 0
for line in Lines:
    count += 1
    print("{}: {}".format(count, line.strip()))