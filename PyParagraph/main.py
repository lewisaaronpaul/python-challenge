#################################################################
#Name: Aaron Paul Lewis                                         #
#Rice University: Data Analytics and Visualization Boot Camp    #
#Assignment #3: Python Homework - ExtraContent:- PyParagraph    #
#Date: May 27, 2020                                             #
#################################################################

#Import the csv module to manage CSV files.
import csv

#Now import the os module to facilitate file paths across operating systems.
#This allows for portability between different platforms.
import os

#Import the re module to allow us to search a string using patterns.
import re

#Enter the name of the file.
file_name = input("Please enter the name of the file(with extension): ")

#Link to the relative path of the CSV data file.
file_path = os.path.join('.','raw_data', file_name)

# Open text file and read the it.
with open(file_path) as file_object:
    the_text_file = file_object.read()

#Here we are using a Regular Expression to extract all the sentences from the text file.
pattern_sentence = re.compile("(?<=[.!?])+")

#Extract the sentences from the text file.
#Use a list comprehension to remove any space element from the list.
sentence_list = [sentence for sentence in pattern_sentence.split(the_text_file) if sentence != ""]

#Total number of sentences:
total_sentence = len(sentence_list)

#Regular Expression to extract all the words in a sentence.
#Split at a comma, period, exclamation mark, question mark, space.
pattern_word = re.compile("[,.!?\s]+")

#Extract the words in the paragraph.
#Use a list comprehension to remove any space element from the list.
word_list = [word for word in pattern_word.split(the_text_file) if word != ""]

#Total number of words:
total_word = len(word_list)

total_character = 0
#Find the length of each word, calculate the total for the paragraph.
i = 0
for each_word in word_list:
    i += 1
    total_character = total_character + len(each_word)

#Average characters per word:
avg_character = total_character/total_word

#Average sentence length (in words):
avg_sentence_length = total_word / total_sentence

#Print summary:
print("Paragraph Analysis:")
print("-------------------------------")
print(f"Name of Text File: {file_name}")
print(f"Approximate Word Count: {total_word}")
print(f"Approximate Sentence Count: {total_sentence}")
print(f"Average Letter Count: {avg_character:.1f}")
print(f"Average Sentence Length: {avg_sentence_length:.1f}")

#Create the bank_results.txt file in the Analysis folder, and write the result to it.
results_path = os.path.join('Analysis', f'results_{file_name}')
results_file = open(results_path, 'w')

#Write to bank_results.txt:
results_file.write("Paragraph Analysis: \n")
results_file.write("------------------------------- \n")
results_file.write(f"Name of Text File: {file_name} \n")
results_file.write(f"Approximate Word Count: {total_word} \n")
results_file.write(f"Approximate Sentence Count: {total_sentence} \n")
results_file.write(f"Average Letter Count: {avg_character:.1f} \n")
results_file.write(f"Average Sentence Length: {avg_sentence_length:.1f} \n")
results_file.close



