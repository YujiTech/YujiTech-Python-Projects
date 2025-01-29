# This code is made by YujiTech
# Packages needed:
# pip install langdetect
# It will print the first two letters of the language
from langdetect import detect

text = input("Enter any text in any language: ")
# Specifying the language for
# detection
print(detect(text))
