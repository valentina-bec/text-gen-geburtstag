import os
import csv

directory = r'\Geburtstag_data'

fields = ['filename', 'greeting']
with open(r'\Geburstagsgruesse.csv', 'w', encoding='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter='|')
    writer.writeheader()
    for filename in os.listdir(directory):
        files_greetings = os.path.join(directory + '/' + filename)
        with open(files_greetings, 'r', encoding='UTF-8') as txt:
            corpus = txt.read()
            writer.writerow({'filename': filename, 'greeting': corpus})

corpuses = []
for filename in os.listdir(directory):
    files_greetings = os.path.join(directory + '/' + filename)
    with open(files_greetings, 'r', encoding='UTF-8') as file:
        corpus = file.read()  # .lower()
    corpuses.append(corpus)

print(len(corpuses))
print(type(str(corpuses)))
