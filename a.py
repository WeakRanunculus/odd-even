
import random
win=0
lose=0
count=0

while True:
    a=(input("odd or even? o/e or quit(q)"))
    if a ==('q'):
        print('game over')
        break

    b = random.randrange(0,10)
    if (b % 2==0):
        if a==('o'):
            print('worng')
            lose+=1
        elif a==('e'):
            print('good')
            win+=1
        else:
            print('U R nerd')
    if b % 2 ==1:
        if a==('o'):
            print('good')
            win+=1
        elif a==('e'):
            print('wrong')
            lose+=1
        else:
            print('U R nerd')
    print(f'number was {b}')
    count+=1
    if count == 10:
        win_rate = (win / (win + lose)) * 100
        print("========== 10 ROUNDS DONE ==========")
        print(f"Wins: {win}")
        print(f"Losses: {lose}")
        print(f"Win rate: {win_rate:.1f}%\n")

        win = 0
        lose = 0
        count = 0