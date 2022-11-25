""" 
This program is a dice program

"""

import random
dice_num = 0


def main():
    print('dice program')    
    var = input("Please input : ")

    if var == '1d6':
        dice_num = random.randrange(1, 6, 1)
        print(dice_num)

    else:
        print("エラー")



if __name__ == "__main__":
    main()