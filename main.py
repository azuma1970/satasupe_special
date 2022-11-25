""" 
This program is a dice program

"""

import sys, random

dice_num1 = 0
dice_num2 = 0

def main():
    print('dice program')  

    while True:
        print('Please input')
        var = input('1d6 or 2d6 or exit : ')

        if var == '1d6':
            dice_num1 = random.randrange(1, 6, 1)
            print('%s = %d' %(var, dice_num1))
        
        elif var == '2d6':
            dice_num1 = random.randrange(1, 6, 1)
            dice_num2 = random.randrange(1, 6, 1)
            tmp = dice_num1 + dice_num2
            print('%s = %d + %d = %d' %(var, dice_num1, dice_num2, tmp))
            if tmp == 2:
                print('！！ファンブル！！')
        elif var == 'exit':
            sys.exit()

        else:
            print("エラー")



if __name__ == "__main__":
    main()