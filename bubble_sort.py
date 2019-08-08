#Bubble sort by Spencer
from sense_emu import SenseHat
from time import sleep
from random import *

random_list = [0,0,0,0,0,0,0,0]

print (random_list)
sorted = False
pointer = 0
passes=(len(random_list)-1)
temp = 0
swap_made = True
my_pass = 0

hat = SenseHat()
hat.clear()
colour = (0,0,0)
hat.set_pixel(0,1,colour)

def populate_list():
    count = 0
    while count <=7: # This number can change if you are not using the SenseHat
        random_list[count]=randint(0,10)
        count +=1
    print (random_list)
    check_pixel()

def check_pixel():
    count = 0
    while count <= passes:
        if random_list[count] == 0:
            colour = (255,0,0)
        if random_list[count] == 1:
            colour = (255,204,153)
        if random_list[count] == 2:
            colour = (255,255,153)
        if random_list[count] == 3:
            colour = (204,255,153)
        if random_list[count] == 4:
            colour = (153,255,153)
        if random_list[count] == 5:
            colour = (153,255,204)
        if random_list[count] == 6:
            colour = (153,255,255)
        if random_list[count] == 7:
            colour = (153,204,255)
        if random_list[count] == 8:
            colour = (153,255,255)
        if random_list[count] == 9:
            colour = (153,153,255)
        if random_list[count] == 10:
            colour = (204,153,255)
        row = 2
        while row <=4:
            hat.set_pixel(count,row,colour)
            row +=1
        count +=1


populate_list()
while swap_made !=False:
    print ("New loop")
    pointer = 0
    swap_made = False
    while pointer <= passes-1:
        hat.set_pixel(pointer,1,255,255,255)
        hat.set_pixel(pointer+1,1,255,255,255)
        item_1 = random_list[pointer]
        item_2 = random_list[pointer+1]
        if item_1 > item_2:
            swap_made = True
            temp = item_1
            item_1 = item_2
            item_2 = temp
            random_list[pointer]  = item_1
            random_list[pointer+1] = item_2
            print (random_list)
            check_pixel()
        sleep(0.5)
        hat.set_pixel(pointer,1,0,0,0)
        hat.set_pixel(pointer+1,1,0,0,0)
        pointer +=1

print ("Done")



