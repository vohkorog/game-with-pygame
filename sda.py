import random
import os
num = random.randrange(1,5)
user_num = 101010101
count = 0

while user_num != num:
    
    os.system("cls")
    print("искомое число", num)
    print("кол-во попыток: ", count)
    user_num = input("введите число: ")

    if int(user_num) > num:
        print("число меньше")
        
    if int(user_num) < num:
        print("число больше")
        
    if int(user_num) == num:
        print("вы угадали!")
        break
    count+=1
    
    input("нажмите enter ")
    