n = int(input("Please Enter the length of your snake: "))
list = []

while len(list) < n:
    list.append("#")
    list.append("*")

for i in range (n):
    print(list[i], end =" ")