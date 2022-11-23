import random
words_bank=["Tree","Book","car","COMPUTER","Hospital","WATER","happy man"]
user_mistakes=0
good_chars=[]
bad_chars=[]


word=random.choice(words_bank)
word=word.lower()

while user_mistakes <6:
    
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
        else:    
            print("_",end=" ")

    user_char=input("please enter your guess : ")
    user_char=user_char.lower()
    if len(user_char)==1: 
        if user_char in word:
            good_chars.append(user_char)
            print("✅")
        else:
            bad_chars.append(user_char)
            user_mistakes +=1
            print("❌")   
    else:
        print('please enter correct character') 
if user_mistakes==6:
    print("Game Over !!!") 

     

