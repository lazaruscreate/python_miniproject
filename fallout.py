#!/usr/bin/env python3
import random



brotherhood_count = 0
institute_count = 0
i = 0

questions = ["If they're sentient enough, robots should be considered humans too. (T/F): ", "'Evil' is subjective, and if your agenda is met it doesn't matter who has to be affected (T/F): ", "Technology is the greatest creation from humanity. (T/F): ", "Intelligence is the most important trait one could have. (T/F): "]

print("""######                                             ######                               #####  
#     # #####    ##   # #    #     ####  #####     #     # #####    ##   #    # #    # #     # 
#     # #    #  #  #  # ##   #    #    # #    #    #     # #    #  #  #  #    # ##   #       # 
######  #    # #    # # # #  #    #    # #    #    ######  #    # #    # #    # # #  #    ###  
#     # #####  ###### # #  # #    #    # #####     #     # #####  ###### # ## # #  # #    #    
#     # #   #  #    # # #   ##    #    # #   #     #     # #   #  #    # ##  ## #   ##         
######  #    # #    # # #    #     ####  #    #    ######  #    # #    # #    # #    #    #    """)
print("-------------------------------------------------------------------------------------------")


while i < len(questions):
    
    test = input(questions[i])
    if test.lower() == "t":
        institute_count += 1
        i += 1
    elif test.lower() == "f":
        brotherhood_count += 1
        i += 1
    else:
        print("That is an invalid value")

if institute_count > brotherhood_count:
    print("Mankind Redefined. The Institute welcomes you with open arms. Let's change the world.")
else:
    print ("Ad Victorium Squire, Welcome to the Brotherhood of Steel. Let's get to work.")
