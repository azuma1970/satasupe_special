""" 
This program is a dice program

1d6 or 2d6 input
"""

import sys, random


def Funk_dice_roll(str_dice):
    list_int_dice_num = []
    list_dice = list(str_dice)
    print(list_dice)
    dice_num1 = int(list_dice[0])
    dice_num2 = int(list_dice[2])
    for i in range(dice_num1):
        list_int_dice_num.append(random.randrange(1, dice_num2, 1))
    return list_int_dice_num

def main():
    print('dice program')  

    while True:
        print('Please input')
        str_dice = input('1d6 or 2d6 or exit : ')

        if str_dice == '1d6':
            list_int_dice_num = Funk_dice_roll(str_dice)
            print('{} = {}\n'.format(str_dice, list_int_dice_num))

        elif str_dice == '2d6':
            Funk_dice_roll(str_dice)
            list_int_dice_num = Funk_dice_roll(str_dice)
            tmp = 0
            result = 0
            for tmp in list_int_dice_num:
                result = tmp + result
            tmp1 = list_int_dice_num[0]
            tmp2 = list_int_dice_num[1]
            print('%s = %d + %d = %d\n' %(str_dice, tmp1, tmp2, result))
            if result == 2:
                print('！！ファンブル！！\n')

        elif str_dice == 'exit':
            sys.exit()

        else:
            print('入力文字エラー\n')


if __name__ == "__main__":
    main()

