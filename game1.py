import random
'''
1 for rock 
2 for scissor 
3 for paper
'''
computer =random.choice([1,2,3])
youstr=input("enter your choice(r for rock ,s for scissor , p for paper ) :  ")
youdict={"r":1,"s":2,"p":3}
reversedict={1:"rock",2:"scissor",3:"paper"}

if youstr not in youdict:
   print("Invalid input ❌ please choose r,s,p ")
   exit()

you=youdict[youstr]
print(f"you chose : {reversedict[you]}\n computer chose : {reversedict[computer]}")

if(computer==you):
    print("match draw 😶‍🌫️")
else: 
 if(computer==1 and you==3):
    print("you win 😎")
 elif(you==1 and computer==3):
    print("you lose 😭")
 elif(computer==2 and you==1):
    print("you win 😎")
 elif(you==2 and computer==1):
    print("you lose 😭")
 elif(computer==3 and you==2):
    print("you win 😎")
 elif(you==3 and computer==2):
    print("you lose 😭")
 else:
    print("something went wrong ❌")