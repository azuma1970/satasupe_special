""" 
This program is a dice program

"""

import random
dice_num1 = 0
dice_num2 = 0

def main():
    print('dice program')    
    var = input("Please input : ")

    if var == '1d6':
        dice_num1 = random.randrange(1, 6, 1)
        print('%s = %d' %(var, dice_num1))
    


    else:
        print("エラー")



if __name__ == "__main__":
    main()