

#the downloaded zip file is extracted into a new text file
from zipfile import ZipFile
import os
import re
import string
import unidecode









PATH = "."
file_name = os.path.join(PATH, "1976236-bbabb412261386673eff521dddbe1dc815373b1d.zip")

with ZipFile(file_name, 'r') as zip:
    zip.extractall()









#Now the file has to read:

folder_PATH = r"E:\college\python\hangman\1976236-bbabb412261386673eff521dddbe1dc815373b1d"
file_name = os.path.join(folder_PATH, "wiki-100k.txt")
working_file = os.path.join(folder_PATH, "working_file.txt")
wfp = open(working_file, 'w') #dumping words in the file so that the downloaded file doesn't get damaged!



def accent_conversion(str):
    return unidecode.unidecode(str)



#taking words of certain sizes and makinh the words usable.
count = 0
longest_length = 19
longest_word = list()
with open(file_name, 'r', encoding="utf8") as fp:
   for line in fp:
        try:
            line.lower()
            line = accent_conversion(line)
            
            word_length = len(line.strip())
            if not (re.match('^#', line)) and word_length > 4 :
                line = line.translate(str.maketrans('','', string.punctuation))
                if word_length > longest_length:
                    print("1")
                    
                    longest_word = line
                    print(longest_word)
                    continue
                else:     
                    wfp.write(line.lower())
             
        except:
            continue        
wfp.close()
max_word = list()
max_length = 15
with open(working_file, 'r') as wp:
    for line in wp:
        word_length = len(line.rstrip())
        if max_length < word_length:
            max_word.append(line)
            max_length = word_length

print(max_word, max_length)



