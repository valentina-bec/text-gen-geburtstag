import pickle
import os
import re
from num2words import num2words


#####
# List of words to replace are previously prepared in prep_list_of_words_to_remove.py
# as pickle and save in \removed_words.txt
# replace_word
# remove_emoji
# remove_numbers
######

def num_to_words(text):
    after_spliting = text.split()
    for index in range(len(after_spliting)):
        if after_spliting[index].isdigit():
            after_spliting[index] = num2words(after_spliting[index], lang='de')
    numbers_to_words = ' '.join(after_spliting)
    return numbers_to_words


def remove_words(text, old_word, new_word):
    replace_words = text.replace(str(old_word), new_word)
    return replace_words


def remove_emoji(text):
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)

def remove_numbers(text):
    number_pattern = r'\d+'
    without_number = re.sub(pattern=number_pattern,
                            repl=" ", string=text)
    return without_number


###########

directory = r'C:\Users\valen\tensorEnv\scrape\Geburtstag_test'
# words to remove


for filename in os.listdir(directory):
    datei = os.path.join(directory + '/' + filename)
    with open(datei, 'r', encoding='UTF-8') as file:
        text = file.read()
        #
        num_to_word= num_to_words(text)
        text_wo_emoji = remove_emoji(text)
        replace_emoji = text.replace(text, text_wo_emoji)
        replace_numbers_by_words = text.replace(text, num_to_word)

        with open(datei, 'w+', encoding='UTF-8') as file:
            file.write(replace_emoji)
            #file.write(replace_numbers)
            file.write(replace_numbers_by_words)

# remove other words
with open(r'\removed_words.txt', 'rb') as file:
    words_to_remove = pickle.load(file)
    for word in words_to_remove:
        with open(datei, 'r', encoding='UTF-8') as file:
            text = file.read()
            text_wo_words = remove_words(text, str(word), ' ')
            replace_words = text.replace(text, text_wo_words)
            for filename in os.listdir(directory):
                datei = os.path.join(directory + '/' + filename)
                with open(datei, 'w+', encoding='UTF-8') as file:
                    file.write(replace_words)

# print final datei
for filename in os.listdir(directory):
    datei = os.path.join(directory + '/' + filename)
    with open(datei, 'r', encoding='UTF-8') as file:
        text = file.read()
        print('================')
        print(datei)
        print('================')
        print(text)
        print('================')
