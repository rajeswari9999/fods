import string
from collections import Counter

file_path = r"C:\Users\priyy\Downloads\Documents\Desktop\sample_text.txt"

with open(file_path, "r") as file:
    text = file.read()
    words = text.split()
    word_freq = Counter(words)  

for word, freq in word_freq.items():  
    print(f"{word} : {freq} ") 
