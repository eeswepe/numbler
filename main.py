from random import randint

def generate_number():
    return [randint(1,9), randint(1,9), randint(1,9)]

print('='*50)
print("Guess the 3 numbers that are in my mind (1-9)")
print('to exit, input "123"')
print('='*50)

# game loop
while True:
    win = False
    mystery_num = generate_number()
    attempt = 1

    while True:
        cor_num = 0
        cor_pos = 0
        guessed_num = [0, 0, 0]

        # take input from player
        for i in range(0,3):
            try:
                guessed_num[i] = int(input(f'the {i+1} number '))
            except:
                print('input other than int is assumed to be 0')
            if guessed_num[i] == 123:
                exit()

        # check num
        for i in range(0,3):
            if guessed_num[i] in mystery_num:
                cor_num+=1

        for i in range(0, 3):
            if guessed_num[i] == mystery_num[i]:
                cor_pos+=1

        if cor_pos==3 and cor_num==3:
            print('*'*20)
            print(f'you found it in {attempt} attempt')
            print(guessed_num)
            print('*' * 20)
            print('\n')
            win = True
            break
        else:
            print('*' * 20)
            print('your guess result')
            print(guessed_num)
            print(f'there is {cor_num} correct number')
            print(f'there is {cor_pos} number with correct position')
            print('*' * 20)
            print('\n')
            attempt+=1

    if win:
        ask_restart = input('wanna play again? (y/n)')
        if ask_restart == 'y':
            continue
        elif ask_restart == 'n':
            break
        else:
            print("input invalid, program will be ended'")
            break
