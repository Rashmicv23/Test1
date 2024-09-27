#Creating list
#First method
x = list(range(0,101,2))
print(x)

#Second method
x =[]
for i in range(0,101,2):
    x.append(i)
print(x)

#Third method
x = [i for i in range(0,101,2)]
print(x)

a = [i for i in range(0,101,2)]
b = []
for i in a:
    if i % 8 == 0:
        b.append(i)
print(b)

y = [i for i in x if i % 8 == 0]
print(y)

#print the elements of list which are in odd position
c = [12,23,34,45,56,67]
d = [c[i] for i in range(len(c)) if i % 2 != 0]
print(d)