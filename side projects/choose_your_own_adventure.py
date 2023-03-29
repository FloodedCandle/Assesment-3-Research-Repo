name = input('type your name: ')
print('welcome to this choose you own adenture', name ,'!')

answer = input('You are on a dirt road, is has come to an end and you can go left or right. where would you like to go? ').lower

# if answer == 'swim':
#         print('')
#     elif answer == 'walk':
#         print('')
#     else:
#         print('not a valid input.')


if answer == 'left':
    answer = input("you come to a river, you can walk around it or swim across? type walk to go around and swim to swim across: ").lower

    if answer == 'swim':
        print('you swam across the river and got swept away. "YOUR DIED"')
    elif answer == 'walk':
        print('you walked around the river for a couple of hours. you ran out of food rations and starved to death. "YOUr DEAD"')
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