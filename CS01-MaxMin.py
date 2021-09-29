i = int(input('Enter Your Loop : '))
a = []
for q in range(i):
    num = int(input('Enter Your Number : '))
    a += [num]
print(min(a))
print(max(a))