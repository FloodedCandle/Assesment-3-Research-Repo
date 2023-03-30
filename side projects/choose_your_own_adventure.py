name = input('type your name: ')
print('welcome to this choose you own adenture', name ,'!')
# if answer == '':
#         print('')
#     elif answer == '':
#         print('')
#     else:
#         print('not a valid input.')

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
            print('')
        else:
            print('not a valid input.')
    else:
        print('not a valid input.')
elif answer == 'right':
    answer = input('you come apon a wobbly looking bridge. do you want to cross it or head back?(cross/back): ').lower

    if answer == 'back':
        print('you walked back to the main road. "END"')
    elif answer == 'cross':
        print('you cross the bridge and fall through one of the cracks. "YOUr DEAD"')
    else:
        print('not a valid input.')
else:
    print('not a valid input.')

print('thank you for trying')