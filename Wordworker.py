import string
import time
from os import system
CapTitle = "Wordworker v1"
system("title " + CapTitle)


# intro
print("""
 __          __  _                          _ 
 \ \        / / | |                        | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ |
    \  /\  /  __/ | (_| (_) | | | | | |  __/_|
     \/  \/ \___|_|\___\___/|_| |_| |_|\___(_) to Wordworker!
     
     """)
print("Wordworker is a word managment software made in Python.")
time.sleep(0.3)
print("Locating text files.")  # bait lol
time.sleep(1)
filename = input("Files are located; enter the file name: ")  # get file

with open(filename, 'r') as file:
    contents = file.read().lower()

words = contents.split()

words = [word.translate(str.maketrans('', '', string.punctuation))
         for word in words]

word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1
# print info
print("Total words in ", filename, ": ", len(words))

longest_word = max(words, key=len)
shortest_word = min(words, key=len)
print("Longest word in ", filename, ": ", longest_word)
print("Shortest word in ", filename, ": ", shortest_word)

n = int(input("Enter amount of most frequent words to display: "))
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print("top", n, "Most frequent words in ", filename, ": ")
for word, count in sorted_words[:n]:
    print(word, ":", count)

# letter frequency lol
letter_counts = {}
for letter in contents:
    if letter.isalpha():
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

# print counts
sorted_letters = sorted(letter_counts.items(),
                        key=lambda x: x[1], reverse=True)

print("Letter frequencies in ", filename, ": ")
for letter, count in sorted_letters:
    print(letter, ":", count)

input("Press enter to exit.")
# LIFE LESSON: DO NOT USE +. USE ,
