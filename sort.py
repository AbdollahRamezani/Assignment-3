print("To finish and print please Type : end")
list = []
while True:
    choice=input("please insert list  : ")
    test_digit=choice.isdigit()
    
    if test_digit==True:
      list.append(int(choice))
    elif choice=="end":
       print(list)
       break

if list==sorted(list):
    print("The list is Ordered in Ascending Order")
elif list!=sorted(list):
    print("The list is Unordered in Ascending Order")        
       
    
    







