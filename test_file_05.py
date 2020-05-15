
#### KDR edited this on the remote in the branch: NEW_DEVELOP to test the git fetch, diff, and pull 
#### -*- coding: utf-8 -*-
####
#### Created on Thu Apr 23 15:02:41 2020

####@author: kdrah
####

# test_file_05.py
#
# -*- coding: utf-8 -*-


# This code is used to practice extracting and using data from a .csv file
# This code is generated using Chapter 16 - WORKING WITH CSV FILES AND JSON DATA
# from https://automatetheboringstuff.com/2e/chapter16/

# To read a CSV file with the csv module, first open it using the open() function ➋,
# just as you would any other text file. But instead of calling the read() or
# readlines() method on the File object that open() returns, pass it to the
# csv.reader() function ➌. This will return a reader object for you to use.
# Note that you don’t pass a filename string directly to the csv.reader() function.
#
# The most direct way to access the values in the reader object is to convert it
# to a plain Python list by passing it to list() ➍. Using list() on this reader
# object returns a list of lists, which you can store in a variable like exampleData.
# Entering exampleData in the shell displays the list of lists ➎


# Remember that if you want to reuse the csv file, 
# you have to make a input_file.fseek(0), because when you use
# a list for the reader_file, it reads all file, and the pointer
# in the file change its position


import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader) 
print(exampleData)
print('\n')

# if the exampleData = list(exampleReader) is used then
# then using 'list' again will cause issues. 
#lines_in_exampleReader= len(list(exampleReader))
lines_in_exampleReader= len(exampleData)




print('\n')

# NOTE: IF THE LIST IS USED ABOVE TO GENERATE exampleData 
# rows in a csv file
# https://kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python



print('The number of lines in csv file is: ' + str(lines_in_exampleReader))
    
print('\n')












# print('\n')
# print(exampleData[0][0])
# print('\n')
# #'4/5/2015 13:34'
# print(exampleData[0][1])
# print('\n')
# #'Apples'
# print(exampleData[0][2])
# print('\n')
# #'73'
# print(exampleData[1][1])
# print('\n')
# #'Cherries'
# print(exampleData[6][1])
print('\n')
       

print('**********************************************************')
# Note when "exampleData = list(exampleReader)" is added it
# causes the for loop below not to execute correctly
# somehow adding that line advances the row to the end ???? KDR
# I verified this by respecifying opening the file and reading it into
# exampleReader 


exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile) 


for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
        print('in for loop')

# for row in exampleData:
#         print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
#         print('in for loop')
  


        
print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV') 

## STEP ONE
## USE THIS SECTION OF CODE TO DETERMINE SIZE OF CSV FILE

c=0
field={}

with open('example.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        field[c]=row
        print(field[c])
        c=c+1

columns=len (field[0])
rows=len(field)

csvFile.close()

print('\n')
print('The number of rows: ' + str(rows))
print('The number of columns: ' + str(columns))
print('\n')

print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')

# Grab information by index
# Print [ROW] [COLUMN]  index starts at 0, 0 
print(exampleData[1][2])
print(exampleData[rows-1][columns-1])

# NEXT STEP 
# Write this information to an EXcel File 


