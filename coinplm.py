# You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z.
#The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins.
#How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.


def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    five = int(rupees_to_make / 5)  #checking boundary case
    one_needed = rupees_to_make % 5  # checking boundary case


# checking possible  conditions ............................
    if five<= no_of_five:   # what we have is sufficient tto full fill requirements
        five_needed=five
    else:
        five_needed = no_of_five   # what we have is less than requirement so jitna hai dedo baaki ka one rupee coin se lelega
        if (five > no_of_five):
            one_needed = rupees_to_make - 5 * no_of_five # how many one rupee coin needed l



    if one_needed > no_of_one:  # what happen if we have less one rupee coin we reqiure throw -1
        print("-1")
    else:
        print("one coin : {}\n five coin is: {}".format(one_needed,five_needed))

make_amount(100, 21, 5)