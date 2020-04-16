#The amount of variables to be set to upper case--------------
#In put the strings myself------------------------------------
#Prints out the uper case strings-----------------------------

#Sets the number of times you want to loop--------------------
num = int(input("How many strings to upper case? "))

#Set the default integer as zero for a comparison to your num
i = 0

#While in the 'with open('uppercase.txt', 'r+') as uppering'
#it allows for the funtions to work and write in the txt file
with open('uppercase.txt', 'r+') as uppering:

    #VERY IMPORTANT goes to the last line by going backwards
    #if not, then it will write over the first lines
    uppering.readlines()[-1]

    while i < num:
        i += 1
        the_uppercase = input('string you wish to upper? ')
        print(the_uppercase.upper())

        #Writes in the txt file
        uppering.write(the_uppercase.upper() + '\n')
