import random

"""
print("Guess Number")
secret=random.randint(1,100)
num=input('输入一个数字\n')
guess=int(num)
while guess!=secret:
    print('wrong!')
    num=input(' try again.\n')
    guess=int(num)
    if guess==secret:
        print('rigth')
    else:
        if(guess>secret):
            print("larger than that num")
        else:
            print('smaller than that num') 
print('game over')
"""


#改进版
    
print("Guess Number")
secret=random.randint(1,100)
# print(secret)
while True:
    
    num=input('输入一个数字\n')
    guess=int(num)
    if guess==secret:
        print('rigth')
        break
    else:
        if(guess>secret):
            print("larger than that num")
        else:
            print('smaller than that num')
print('Game Over!')
