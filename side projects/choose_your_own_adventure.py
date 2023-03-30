name = input('type your name: ')
print('welcome to this choose you own adenture', name ,'!')

answer = input('You are on a dirt road, is has come to an end and you can go left or right. where would you like to go?(left,right): ').lower

if answer == 'left':
    answer = input("you come to a lake, you can walk around it or swim across?(walk,swim): ").lower
    if answer == 'swim':
        print('you swam across the lake and got tired and drowned. "YOUR DIED"')
    elif answer == 'walk':
        answer = input('you walked around the lake. while walking you com across a abandon looking cabin. will you continue walking or explore the cabin?(continue,explore): ').lower
        if answer == 'continue':
            print('you deside to walk past the cabin and continue going around the lake.')
        elif answer == 'explore':
            answer = input('you deside to explore the cabin, inside you see that the cabin has been abandoned for quite some time. will you continue exploring or head back?(coninute,back): ').lower
            if answer == 'continue':
                answer = input('while you continue to explore you find a old looking chest and found a "rusty axe" will you take the axe or leave it?(take,leave): ')

            elif answer == 'back':
                print('you return to the lake side and continue walking...')
            else:
                print('not a valid input.')
        else:
            print('not a valid input.')
    else:
        print('not a valid input.')
elif answer == 'right':
    answer = input('you come apon a wobbly looking bridge. do you want to cross it or head back?(cross/back): ').lower

    if answer == 'back':
        print('you walked back to the main road. "END"')
    elif answer == 'cross':
        answer = input('you cross the bridge and see a old traveler with a big bag on there back, on the other side. will you walk past the old traveler or talk to them?(walk,talk): ').lower
    else:
        print('not a valid input.')
else:
    print('not a valid input.')

print('thank you for trying')
