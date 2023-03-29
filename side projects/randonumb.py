import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger then 0 next time.")
        quit()
else:
    print("please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guesses = input('make a guess: ')
    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else:
        print('please type a number next time.')
        continue

    if user_guesses == random_number:
        print('You got it!')
        break
    elif user_guesses > random_number:
        print('you were above the number!')        
    else:
        print('you were below the number!')


print('you got it in',guesses,'guesses!')
