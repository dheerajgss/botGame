replay = 'y'
finish = 0
total = 1
print("Total: ",total)
while(replay !='n'):
    player = int(input("Enter your number: "))
    if(player > 0 and player < 11):
        total += player
        print("Total: ",total)
        if(total == 100):
           print("You win!!!")
           finish = 1
        elif(total > 100):
            print("Number exceeded 100... Since you are first to reach 100, you win!!!")
            finish = 1
    else:
        print("Invalid number!")
        break
    if(total != 100):
        bot = 11 - player
        print("Bot's number: ",bot)
        total += bot
        print("Total: ",total)
        if(total == 100):
            print("You lose!!!")
            finish = 1
        elif(total > 100):
            print("Number exceeded 100... Since bot reached the 100 first, you lose!!!")
            finish = 1
    if(finish == 1):
        replay = input("Do you want to play again?(y/n): ")
        if(replay == 'y'):
            total = 1
            finish = 0
            print("Total: ",total)  