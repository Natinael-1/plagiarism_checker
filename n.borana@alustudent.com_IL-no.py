# importing modules to use them later
import string
import time
# creating appropriate datastructures, list, dictionary and set
words_list_1 = []
words_list_2 = []
words_dict_1 = {}
words_dict_2 = {}
words_set_1 = set()
words_set_2 = set()
print("Hello, dear user, this is Plagiarism checker!")
# open both files
files_set = {"essay1.txt", "essay2.txt"}
def reader():
    while True:
        input_1 = input("Please enter the name of file to check for plagiarism: ")
        input_2 = input("Please add another file: ")
        if not input_1 in files_set or not input_2 in files_set:
            print("File not found! The files should be exactly named as essay1.txt and essay2.txt ")
            print("The files also should exist in the same folder with this python file")
            continue
        else:
            break
    fi1 = open(input_1, "r")
    fi2 = open(input_2, "r")        
    print("Thank you for entering the files. Let's analyze the contents of the files.\n")
    print("Analyzing in progress..... Please wait a second.")
    time.sleep(4)
    content1 = fi1.read()
    content2 = fi2.read()
    fi1.close()
    fi2.close()
    punct_remove = str.maketrans("","", string.punctuation)
    content1 = content1.translate(punct_remove)
    content2 = content2.translate(punct_remove)
    return (content1, content2)
# a function to split a file in to words, and append them to lists    
def splitter():
    neat_files = reader()
    words_f1 = neat_files[0].split()
    i = 0
    while i < len(words_f1):
        elem1 = words_f1[i].lower()
        words_list_1.append(elem1)
        i = i + 1
    words_f2 = neat_files[1].split()
    j = 0
    while j < len(words_f2):
        elem2 = words_f2[j].lower()
        words_list_2.append(elem2)
        j = j + 1
splitter()
# function to make dictionary and set
def dict_and_set_maker():
    for word in words_list_1:
        words_dict_1[word] = words_dict_1.get(word, 0) + 1
    for woord in words_list_2:
        words_dict_2[woord] = words_dict_2.get(woord, 0) + 1
    for element1 in words_list_1:
        words_set_1.add(element1)
    for element2 in words_list_2:
        words_set_2.add(element2)
dict_and_set_maker()

# finding common words in both files
comm_words = words_set_1 & words_set_2
print(f"There are total of {len(comm_words)} common words found in the essays. They are here below.\n")

comm_words_combined = ", ".join(comm_words)
print(comm_words_combined,"\n")

# Printing the number of times the common words appear in both files
print("The number of times the common words appear in both essays:\n")
for wrd in comm_words:
    val1 = words_dict_1[wrd]
    val2 = words_dict_2[wrd]
    print(f"In Essay_1, {wrd}: {val1} times : In Essay_2, {wrd}: {val2} times")
print()

"""When a user types a word, return the number of times the word appear in both files
Return False if the word is not found in either essay or one of them."""
while True:
    yes_no = input("Whould you like to check how many times a word appear in both files?(yes/no) ").lower()
    if yes_no == "yes":
        word_in_essays = input("Please type the word to check how many times it appear in both files: ")
        word_in_essays = word_in_essays.lower()
        if word_in_essays in comm_words:
            value1 = words_dict_1[word_in_essays]
            value2 = words_dict_2[word_in_essays]
            print("Checking the word......")
            time.sleep(4)
            print(f'"{word_in_essays}" appears {value1} times in essay1.\n"{word_in_essays}" appears {value2} times in essay2. ')
        else:
            print("False")
        break
    elif yes_no == "no":
        break
    else:
        continue
    
    
# Union: All unique words from both essays.
union_of_words = words_set_1 | words_set_2

# plagiarism% = (Number of common words (intersection)/total unique words union)*100
plagiarism = (len(comm_words)/len(union_of_words)) * 100

print("Alright! let's check plagiarism!\n")
print("Checking plagiarism.....")
time.sleep(4)
print(f"Plagiarism percentage is {plagiarism:.2f}% ")
if plagiarism >= 50:
    print("There is plagiarism!")
else:
    print("There is no plagiarism!")



