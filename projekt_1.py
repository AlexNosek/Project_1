"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Alexandr Nosek
email: alexandr.nosek51@gmail.com
discord: Vintag#
"""
from pprint import pprint
oddelovac = "-" * 40
registered_users = {
    "bob" : "123", 
    "ann" : "pass123", 
    "mike" : "password123", 
    "liz" : "pass123"
    } 

nickname = input("Hello, please enter your username to continue: ") 

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

# ověření hesla
password = input("Enter your password: ")
print(oddelovac)
cnt = 0
while registered_users.get(nickname) != password:
    if cnt == 2:
        print("Too many incorrect attempts!")
        exit()
    
    else:        
        password = input("Enter your password again: ")
        
    cnt += 1
else:
    print("Welcome to the app,",nickname,"\nWe have 3 texts to be analyzed.")
    print(oddelovac)

#ověření vstupu uživatele
chosen_text = input("Enter a number btw. 1 and 3 to select: ")
print(oddelovac)
if not chosen_text.isdigit():
    print("You have entered an unauthorized character, terminating the program..")
    exit()
elif int(chosen_text) < 1 and int(chosen_text) > 3:
    print("You picked a number in the wrong range, terminating the program..")
    exit()

#počet slov v textu
words_count = len(texts[int(chosen_text) - 1].split())
print(f"There are {words_count} words in the selected text.")

#for loop pro počet velkých písmen
titlecase_words_list = []
titlecase_words = texts[int(chosen_text) - 1].split()
for titlecase in titlecase_words:
    if titlecase[0].isupper():
        titlecase_words_list.append(titlecase)
print(f"There are {len(titlecase_words_list)} titlecase words.")

#for loop pro počet slov psaných velkým a malým písmem

uppercase_words_list = []
lowercase_words_list = []
upper_lowercase_words = texts[int(chosen_text) - 1].split()

for word in upper_lowercase_words:
    if all(letter.isupper() for letter in word):
        uppercase_words_list.append(word)
    elif all(letter.islower() for letter in word):
        lowercase_words_list.append(word)
print(f"There are {len(uppercase_words_list)} uppercase words.")
print(f"There are {len(lowercase_words_list)} lowercase words.")

#for loop pro počet čísel
numbers_list = []
numbers = texts[int(chosen_text) - 1].split()
for word in numbers:
    if word.isdigit():
        word = int(word)
        numbers_list.append(word)
print(f"There are {len(numbers_list)} numeric strings")

#součet všech čísel
print(f"The sum of all the numbers {sum(numbers_list)}")

#graf
print(oddelovac)
print("LEN|  OCCURENCES  |NR.")
print(oddelovac)


    







    





        

    
    
    


    




