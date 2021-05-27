"""
-----------------------------
CP460 (Fall 2020)
Introductory Project
Name: Andrew Liutiev
Email: liut5320@mylaurier.ca
Student Number: 180635320
-----------------------------
"""
from array import *
import utilities
import math

def load_dictionary(dict_file):
    """
    ----------------------------------------------------
    Parameters:   dict_file (file)
    Return:       array (2d list)
    Description:  Utility function to load a sorted dictionary of words
    ---------------------------------------------------
    """

    infile = open(dict_file, encoding="ISO-8859-15", mode="r")
    array = [[] for y in range(26)]

    # iterating line by line, word by word and then case by case for a-z
    for line in infile:
        for word in line.split():
            if word.startswith("a"):
                array[0].append(word)
            elif word.startswith("b"):
                array[1].append(word)
            elif word.startswith("c"):
                array[2].append(word)
            elif word.startswith("d"):
                array[3].append(word)
            elif word.startswith("e"):
                array[4].append(word)
            elif word.startswith("f"):
                array[5].append(word)
            elif word.startswith("g"):
                array[6].append(word)
            elif word.startswith("h"):
                array[7].append(word)
            elif word.startswith("i"):
                array[8].append(word)
            elif word.startswith("j"):
                array[9].append(word)
            elif word.startswith("k"):
                array[10].append(word)
            elif word.startswith("l"):
                array[11].append(word)
            elif word.startswith("m"):
                array[12].append(word)
            elif word.startswith("n"):
                array[13].append(word)
            elif word.startswith("o"):
                array[14].append(word)
            elif word.startswith("p"):
                array[15].append(word)
            elif word.startswith("q"):
                array[16].append(word)
            elif word.startswith("r"):
                array[17].append(word)
            elif word.startswith("s"):
                array[18].append(word)
            elif word.startswith("t"):
                array[19].append(word)
            elif word.startswith("u"):
                array[20].append(word)
            elif word.startswith("v"):
                array[21].append(word)
            elif word.startswith("w"):
                array[22].append(word)
            elif word.startswith("x"):
                array[23].append(word)
            elif word.startswith("y"):
                array[24].append(word)
            elif word.startswith("z"):
                array[25].append(word)

    infile.close()

    return array


def text_to_words(text):
    """
    ----------------------------------------------------
    Parameters:   text (str)
    Return:       array (list)
    Description:  Utility function to covert text strip words of special characters from start and back
    ---------------------------------------------------
    """
    assert type(text) == str, "text is not str"

    # removing any new lines
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    #creating list of special characters
    my_list = '''!"#$%&'()*+,-./:;<=>?[\]^_`{|}!"#$%&'()*+,-./:;<=>?[\]^_`{|}!"#$%&'()*+,-./:;<=>?[\]^_`{|}'''

    #splitting array into words
    array = text.split()
    aindex = 0

    #for every word, char by char strip right and strip left from special characters
    for element in array:
        for ch in my_list:
            array[aindex] = array[aindex].lstrip(ch)
            array[aindex] = array[aindex].rstrip(ch)
        aindex += 1

    return array

def analyze_text(text, dict_file):
    """
    ----------------------------------------------------
    Parameters:   text (str), dict_file (file)
    Return:       matched (int), matched (int)
    Description:  Utility function to covert analyze text, counting matched & unmatched numbers of words
    ---------------------------------------------------
    """
    assert type(text) == str, "text is not str" #no file path gives error by default

    # 2D array/list of words
    dict_list = load_dictionary(dict_file)
    word_list = text_to_words(text)

    # setting matches
    matched, unmatched = 0, 0

    # iterating word by word
    for word in word_list:
        value = False
        # for each alpha substring check to see if word is contained
        for i in range(26):
            if word.lower() in dict_list[i]:
                value = True  

        # adding to designated count
        if value:
            matched += 1
        else:
            unmatched += 1

    return matched, unmatched

def is_plaintext(text, dict_file, threshold):
    """
    ----------------------------------------------------
    Parameters:   text (str), dict_file (text), threshold (int)
    Return:       True / False (bool)
    Description:  Utility function to check if text is decrypted based on threshold value
    ---------------------------------------------------
    """
    assert type(text) == str and type(threshold) == float, "text is not str or threshold is not int" #no file path gives error by default

    # empty check
    if (text == ""):
        return False

    # setting variables & total
    matches, unmatches = analyze_text(text, dict_file)
    total = matches + unmatches

    # setting threshold limit
    if not (threshold >= 0 and threshold <= 1):
        threshold = 0.9
    
    return True if matches/total >= threshold else False


def e_eatbash(plaintext, key):
    """
    ----------------------------------------------------
    Parameters:   plaintext (text), key (int)
    Return:       ciphertext (text)
    Description:  Utility function to covert encrypt atbash
    ---------------------------------------------------
    """
    assert type(plaintext) == str and type(key) == int, "cipher or key is not valid" 
    
    # setting base string and message
    base_string, ciphertext = "", ""

    # Getting base string
    if key % 5 == 0:
        base_string = utilities.get_base("lower")
    if key % 5 == 1:
        base_string = utilities.get_base("upper")
    if key % 5 == 2:
        base_string = utilities.get_base("alpha")
    if key % 5 == 3:
        base_string = utilities.get_base("alphanum")
    if key % 5 == 4:
        base_string = utilities.get_base("all")

    # duplicating string
    temp_string = base_string

    # Creating a new dictionary with keys in reverse order
    new_dict = {base_string[index]: temp_string[len(base_string) - 1 - index] for index in range(len(base_string))}

    # iterating character by character, checking for space, if dne and if it is contained 
    for ch in plaintext:
        if (ch == " "):
            ciphertext += " "
        elif not ch in new_dict:
            ciphertext += ch
        else:
            ciphertext += new_dict[ch]

    return ciphertext

def d_eatbash(ciphertext, key):
    """
    ----------------------------------------------------
    Parameters:   ciphertext (text), key (int)
    Return:       plaintext (text)
    Description:  Utility function to covert decrypt atbash
    ---------------------------------------------------
    """
    assert type(ciphertext) == str and type(key) == int, "cipher or key is not valid" 

    base_string, plaintext = "", ""

    if key % 5 == 0:
        base_string = utilities.get_base("lower")
    if key % 5 == 1:
        base_string = utilities.get_base("upper")
    if key % 5 == 2:
        base_string = utilities.get_base("alpha")
    if key % 5 == 3:
        base_string = utilities.get_base("alphanum")
    if key % 5 == 4:
        base_string = utilities.get_base("all")

    temp_string = base_string
    
    # dictionary is flipped around for decrypting, temp & base
    new_dict = {temp_string[index]: base_string[len(base_string) - 1 - index] for index in range(len(base_string))}

    for ch in ciphertext:
        if (ch == " "):
            plaintext += " "
        elif not ch in new_dict:
            plaintext += ch
        else:
            plaintext += new_dict[ch]
            
    return plaintext
    
        

def cryptanalysis_eatbash(ciphertext):
    """
    ----------------------------------------------------
    Parameters:   ciphertext (text), key (int)
    Return:       key (int), plaintext (text)
    Description:  Utility function to covert break ciphertet
    ---------------------------------------------------
    """
    assert type(ciphertext) == str, "cipher is not valid" 
    
    # setting default in case nothing changes
    key = None
    plaintext = ""

    # iterating through keys
    for i in range(5):
        plaintext = d_eatbash(ciphertext, i)

        # verifying plaintext
        if is_plaintext(plaintext, "C:\\Users\Andrew\CP460\Assignment1\src\engmix.txt", 0.8):
            key = i
            break

    return key, plaintext

def e_scytale(plaintext, key):
    """
    ----------------------------------------------------
    Parameters:   plaintext (text), key (int)
    Return:       ciphertext (text)
    Description:  Utility function to encrypt plaintext
    ---------------------------------------------------
    """
    assert type(plaintext) == str and type(key)==int , "cipher or key is not valid" 

    index = 0
    # getting number of columns
    cols = math.ceil(len(plaintext)/key)

    ciphertext = ""

    #  looping in range of columns while iterating through each plaintext char and adding it to the cipher
    for i in range(cols):
        index = 0 + i
        while(index < len(plaintext)):
            ciphertext = ciphertext + plaintext[index]
            index += cols
    
    return ciphertext.rstrip(" ")
   
def d_scytale(ciphertext, key):
    """
    ----------------------------------------------------
    Parameters:   ciphertext (text), key (int)
    Return:       plaintext (text)
    Description:  Utility function to decrypt scytale
    ---------------------------------------------------
    """
    assert type(ciphertext) == str and type(key)==int , "cipher or key is not valid" 

    # Getting columns, emtpy spaces & placholders
    cols = math.ceil(len(ciphertext)/key)
    spaces = (cols * key) - len(ciphertext)
    count = spaces
    placeholders = (key - 1) + (key*(cols-spaces))

    plaintext = ""
    
    #  filling in empty spaces at end of cipher
    while count > 0:
        ciphertext = ciphertext[:placeholders] + "*" + ciphertext[placeholders:]
        count -= 1
        placeholders = placeholders + key
    
    # iterating through number of rows then columns
    for i in range(key):
        for j in range(cols):
            if (j * key + i >= len(ciphertext)):
                continue
            else: 
                plaintext += ciphertext[j*key + i]

    # if spaces stil isn't 0, strip
    if spaces != 0:
        plaintext = plaintext[:-spaces]

    return plaintext

def cryptanalysis_scytale(ciphertext):
    """
    ----------------------------------------------------
    Parameters:   ciphertext (text)
    Return:       key (int), plaintext (text)
    Description:  Utility function to break ciphertext
    ---------------------------------------------------
    """
    assert type(ciphertext) == str, "cipher is not valid" 

    key = 1
    plaintext = ""

    # checking possible keys from (1, 100)
    for i in range(1, 100):
        key = i
        plaintext = d_scytale(ciphertext, key)

        # breaks if plaintext is valid
        if is_plaintext(plaintext, "C:\\Users\Andrew\CP460\Assignment1\src\engmix.txt", 0.9):
            break
        

    return key, plaintext


def get_polybius_square(start, size):
    """
    ----------------------------------------------------
    Parameters:   start (char), size (int)
    Return:       polybius (text)
    Description:  Utility function to return polybius square
    ---------------------------------------------------
    """

    assert type(start) == str and type(size)==int, "start and size is not valid" 
    
    #  is valid check
    if (ord(start) + (size * size) > 126) or ord(start) >= 122:
        return ""

    polybius = ""
    
    # for i in range of size, add each character in order
    for i in range(size * size):
        polybius = polybius + chr(ord(start) + i)

    return polybius

def e_polybius(plaintext, key):
    """
    ----------------------------------------------------
    Parameters:   plaintext (text), key (tuple)
    Return:       ciphertext (text)
    Description:  Utility function to encrypt plaintext
    ---------------------------------------------------
    """

    assert type(plaintext) == str and type(key[0]) == str and len(key[0]) == 1 and type(key[1]) == int, "one of your inputs is incorrect"
    #  null & valid check
    if plaintext == "":
        print("Error(e_polybius): invalid polybius square")
        return ""
    else: 
        start, size = key[0], key[1]
        polybius = get_polybius_square(start, size)
        
        if polybius == "":
            print("Error(e_polybius): invalid polybius square")
            return ""
        
    ciphertext = ""  

    # for every char in the text, check if not in polybius, numerate
    for ch in plaintext:
        if not ch in polybius:
            ciphertext += ch
        else:
            # find the position, then remainder & modulus for index number
            position = polybius.find(ch)
            row = (position // size) + 1
            col = (position % size) + 1
        
            ciphertext = ciphertext + str(row) + str(col)

    return ciphertext

def d_polybius(ciphertext, key):
    """
    ----------------------------------------------------
    Parameters:   ciphertext (text), key (tuple)
    Return:       plaintext (text)
    Description:  Utility function to decrypt ciphertext
    ---------------------------------------------------
    """

    assert type(ciphertext) == str and type(key[0]) == str and len(key[0]) == 1 and type(key[1]) == int, "one of your inputs is incorrect"

    # null & valid check
    if ciphertext == "":
        print("Error(d_polybius): invalid polybius square")
        return ""
    else: 
        start, size = key[0], key[1]
        polybius = get_polybius_square(start, size)
        
        if polybius == "":
            print("Error(d_polybius): invalid polybius square")
            return ""
        
    plaintext = ""
    poly_index = 0
    
    # loop entirety of string while < len of loop
    while (poly_index < len(ciphertext)):
        # checking if index is an int, if not catch error
        try:
            # if number is int
            if int(ciphertext[poly_index]):
                
                # getting index from row & col, reversing modulus & remainder calculations
                row = (int(ciphertext[poly_index]) - 1) * size
                col = int(ciphertext[poly_index + 1]) - 1
                index = row + col

                plaintext += polybius[index]
                poly_index += 2

        except ValueError:
            # if the char is a space add, else add the char that is not in polybius
            if ciphertext[poly_index] == " ":
                plaintext += " "
            else:
                plaintext += ciphertext[poly_index]
            poly_index += 1

    return plaintext

def cryptanalysis_polybius(ciphertext, size):
    """
    ----------------------------------------------------
    Parameters:   ciphertext (text)
    Return:       plaintext (text), ley (tuple)
    Description:  Utility function to break cyphertext polybius
    ---------------------------------------------------
    """

    assert type(ciphertext) == str and type(size) == int, "one of your inputs is incorrect"

    # null case
    key = (None,None)
    plaintext = ""
    
    # get starting character list
    start_list = ""
    for i in range(126-32):
        start_list += chr(32+i)
        


    # looping in range of start list & creating plaintext for everycase
    for j in range(len(start_list)):
        key = (start_list[j], size)

        plaintext = d_polybius(ciphertext, key)

        #  if plaintext is true, break and return
        if is_plaintext(plaintext, "C:\\Users\Andrew\CP460\Assignment1\src\engmix.txt", 0.93):
            break

    return key, plaintext
