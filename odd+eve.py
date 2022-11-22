import random

bat_or_bowl = ["Bating","Bowling"]
rand_index = bat_or_bowl[random.randint(0, 1)]
print("-"*50,"ODD-EVEN-GAME","-"*50)
odd_eve = input("Odd or Eve (O for odd E for eve)? ")
comp = random.randint(1, 6)
plyr = int(input("Enter number between 1 to 6: "))
print("My number: ",comp)
sum = comp + plyr
if 'e' in odd_eve or 'E' in odd_eve:
    if sum%2==0:
        x = input("You won! Choose bowling or bating (bowl for bowling or bat for bating): ")
        if "bat" in x:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while player != computer:
                sum2 = sum2 + player
                print("Runs made: ",sum2)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number: ",c)
                player = p
                computer = c
            else:
                computer = 1
                player = 0
                print("You are out, Now I am bating")
                while computer != player:
                    print("Runs made: ",sum3)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number:", c)
                    sum3 = sum3 + c
                    player = p
                    computer = c
                    if sum3>sum2:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("I win")
                        break
                    if player == computer:
                        print("I am Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum2>sum3:
                            print("You win")
                            break
                        else:
                            print("Draw")
                            break
        elif "bowl" in x:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while computer != player:
                print("Runs made: ",sum3)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number:", c)
                sum3 = sum3 + c
                player = p
                computer = c
            else:
                print("I am Out!")
                player = 0
                computer = 1
                while player != computer:
                    sum2 = sum2 + player
                    print("Runs made: ",sum2)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number: ",c)
                    player = p
                    computer = c
                    if sum2>sum3:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("I win")
                        break
                    if player == computer:
                        print("You are Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum3>sum2:
                            print("I win")
                            break
                        else:
                            print("Draw")
                            break
        else:
            print("Please try again!")
    else:
        print("I won! I choose",rand_index)
        if "Bat" in rand_index:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while computer != player:
                print("Runs made: ",sum3)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number:", c)
                sum3 = sum3 + c
                player = p
                computer = c
            else:
                print("I am Out!")
                player = 0
                computer = 1
                while player != computer:
                    sum2 = sum2 + player
                    print("Runs made: ",sum2)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number: ",c)
                    player = p
                    computer = c
                    if sum2>sum3:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("I win")
                        break
                    if player == computer:
                        print("You are Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum3>sum2:
                            print("I win")
                            break
                        else:
                            print("Draw")
                            break
        else:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while player != computer:
                sum2 = sum2 + player
                print("Runs made: ",sum2)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number: ",c)
                player = p
                computer = c
            else:
                computer = 1
                player = 0
                print("You are out, Now I am bating")
                while computer != player:
                    print("Runs made: ",sum3)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number:", c)
                    sum3 = sum3 + c
                    player = p
                    computer = c
                    if sum3>sum2:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("I win")
                        break
                    if player == computer:
                        print("I am Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum2>sum3:
                            print("You win")
                            break
                        else:
                            print("Draw")
                            break
elif 'o' in odd_eve or 'O' in odd_eve:
    if sum%2!=0:
        x = input("You won! Choose bowling or bating (bowl for bowling or bat for bating): ")
        if "bat" in x:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while player != computer:
                sum2 = sum2 + player
                print("Runs made: ",sum2)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number: ",c)
                player = p
                computer = c
            else:
                computer = 1
                player = 0
                print("You are out, Now I am bating")
                while computer != player:
                    print("Runs made: ",sum3)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number:", c)
                    sum3 = sum3 + c
                    player = p
                    computer = c
                    if sum3>sum2:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("I win")
                        break
                    if player == computer:
                        print("I am Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum2>sum3:
                            print("You win")
                            break
                        else:
                            print("Draw")
                            break
        elif "bowl" in x:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while computer != player:
                print("Runs made: ",sum3)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number:", c)
                sum3 = sum3 + c
                player = p
                computer = c
            else:
                print("I am Out!")
                player = 0
                computer = 1
                while player != computer:
                    sum2 = sum2 + player
                    print("Runs made: ",sum2)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number: ",c)
                    player = p
                    computer = c
                    if sum2>sum3:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("I win")
                        break
                    if player == computer:
                        print("You are Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum3>sum2:
                            print("I win")
                            break
                        else:
                            print("Draw")
                            break
        else:
            print("Please try again!")
    else:
        print("I won! I choose",rand_index)
        if "Bat" in rand_index:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while computer != player:
                print("Runs made: ",sum3)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number:", c)
                sum3 = sum3 + c
                player = p
                computer = c
            else:
                print("I am Out!")
                player = 0
                computer = 1
                while player != computer:
                    sum2 = sum2 + player
                    print("Runs made: ",sum2)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number: ",c)
                    player = p
                    computer = c
                    if sum2>sum3:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("I win")
                        break
                    if player == computer:
                        print("You are Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum3>sum2:
                            print("I win")
                            break
                        else:
                            print("Draw")
                            break
        else:
            computer = 1
            player = 0
            sum2 = 0
            sum3 = 0
            while player != computer:
                sum2 = sum2 + player
                print("Runs made: ",sum2)
                p = int(input("Enter number between 1 to 6: "))
                c = random.randint(1, 6)
                print("My number: ",c)
                player = p
                computer = c
            else:
                computer = 1
                player = 0
                print("You are out, Now I am bating")
                while computer != player:
                    print("Runs made: ",sum3)
                    p = int(input("Enter number between 1 to 6: "))
                    c = random.randint(1, 6)
                    print("My number:", c)
                    sum3 = sum3 + c
                    player = p
                    computer = c
                    if sum3>sum2:
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        print("You win")
                        break
                    if player == computer:
                        print("I am Out!")
                        print("Your runs: ",sum2)
                        print("My runs: ",sum3)
                        if sum2>sum3:
                            print("You win")
                            break
                        else:
                            print("Draw")
                            break