"""
-------------------------------------------------------
[assignment generator for html school assignment creating multiple instances of a random file]
-------------------------------------------------------
Author: Andrew Liutiev
__updated__ = "2018-09-17"
-------------------------------------------------------
"""

from random import randint

fh = open("sample.txt", "r")

fh.seek(0)

my_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(my_list)
random = randint(0, length - 1) 

my_string_1 = ""
my_string_2 = ""
my_string_3 = ""
 
for i in range(26):
    my_string_1 += my_list[random]
    random = randint(0, len(my_list) - 1) 
    
for i in range(26):
    my_string_2 += my_list[random]
    random = randint(0, len(my_list) - 1) 
    
for i in range(26):
    my_string_3 += my_list[random]
    random = randint(0, len(my_list) - 1) 
    

name = input("Enter name: ")
student_number = input("Student Number: ")

# randomzing dimensions
rand_1 = str(randint(6, 12))
rand_2 = str(randint(1, 4))
rand_3 = str(randint(1, 4))
rand_4 = str(randint(3, 15))
rand_5 = str(randint(40, 70))
rand_6 = str(randint(4, 7))

print("\n \n \n")

# replacing all strings

for line in fh:
    temp = str(line)

    temp = temp.replace("'Name'", name)
    temp = temp.replace("'Student Number'", student_number)
    
    temp = temp.replace("'abc'", "'{}_1'".format(my_string_1))
    temp = temp.replace("'bcd'", "'{}_2'".format(my_string_1))
    temp = temp.replace("'cde'", "'{}_3'".format(my_string_1))
    temp = temp.replace("'def'", "'{}_4'".format(my_string_1))
    temp = temp.replace("'efg'", "'{}_5'".format(my_string_1))
    temp = temp.replace("'fgh'", "'{}_6'".format(my_string_1))
    temp = temp.replace("'ghi'", "'{}_7'".format(my_string_1))
    temp = temp.replace("'hij'", "'{}_8'".format(my_string_1))
    temp = temp.replace("'ijk'", "'{}_9'".format(my_string_1))
    temp = temp.replace("'jkl'", "'{}_10'".format(my_string_1))
    temp = temp.replace("'klm'", "'{}_11'".format(my_string_1))
    temp = temp.replace("'lmn'", "'{}_12'".format(my_string_1))
    temp = temp.replace("'mno'", "'{}_13'".format(my_string_1))
    temp = temp.replace("'nop'", "'{}_14'".format(my_string_1))
    temp = temp.replace("'opq'", "'{}_15'".format(my_string_1))
    temp = temp.replace("'pqr'", "'{}_16'".format(my_string_1))
    
    temp = temp.replace("func_1()", "{}_1()".format(my_string_2))
    temp = temp.replace("func_2()", "{}_2()".format(my_string_2))
    temp = temp.replace("func_3()", "{}_3()".format(my_string_2))
    temp = temp.replace("func_4()", "{}_4()".format(my_string_2))
    temp = temp.replace("func_5()", "{}_5()".format(my_string_2))
    temp = temp.replace("func_6()", "{}_6()".format(my_string_2))
    temp = temp.replace("func_7()", "{}_7()".format(my_string_2))
    temp = temp.replace("func_8()", "{}_8()".format(my_string_2))

    temp = temp.replace("var_1", "{}_1".format(my_string_3))
    temp = temp.replace("var_2", "{}_2".format(my_string_3))
    temp = temp.replace("var_3", "{}_3".format(my_string_3))
    temp = temp.replace("var_4", "{}_4".format(my_string_3))
    temp = temp.replace("var_5", "{}_5".format(my_string_3))
    temp = temp.replace("var_6", "{}_6".format(my_string_3))
    temp = temp.replace("var_7", "{}_7".format(my_string_3))
    temp = temp.replace("var_8", "{}_8".format(my_string_3))
    
    temp = temp.replace("size = '7'", "size = '{}'".format(rand_1))
    temp = temp.replace("cellpadding= '3'", "cellpadding= '{}'".format(rand_2))
    temp = temp.replace("border = '2'", "border = '{}'".format(rand_3))
    temp = temp.replace("rows = '5'", "rows = '{}'".format(rand_4))
    temp = temp.replace("cols = '65'", "cols = '{}'".format(rand_5))
    temp = temp.replace("size = '6'", "size = '{}'".format(rand_6))
     
    print(temp)
    
fh.close()
