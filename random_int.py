import random

while True:
 n=int(input("please enter number of random_int : "))
 numlst = list(range(n)) 
 random.shuffle(numlst) 
 print(end=" "" ".join(list(map(str, numlst)))) 
 print("\n") 


 

 