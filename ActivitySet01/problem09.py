# Lists



lst = list()
filename = "dataset/romeo.txt"
fname = input(filename)

fh = open(filename)

for line in fh:

    for word in line.split( ):

        if word not in lst:

            lst.append(word)

lst.sort()

print(lst)
  
