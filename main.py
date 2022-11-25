""" 
This program is a dice program

"""

import random
#dice_num = 0

def main():
    print('dice program')
    """
    var = input("Please input : ")
    print(var)
    """
    dice_num = random.randrange(1, 6, 1)
    print(dice_num)



if __name__ == "__main__":
    main()