# 1. Ask name and year of birth, then tell their age
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
age = 2025 - birth_year
print(f"Hello {name}, you are {age} years old.")

# 2. Extract car names from this text
txt = 'LMaasleitbtui'
# Let's assume car names: "Lamborghini", "Tesla", "BMW", "Audi"
# We'll try to extract them by manually checking substrings (just an illustrative example)
print("Car names found in text:")
cars = ["Lamborghini", "Tesla", "BMW", "Audi"]
for car in cars:
    if all(letter in txt for letter in car.lower()):
        print(car)

# 3. Take string input, print length, uppercase and lowercase
string = input("\nEnter a string: ")
print("Length:", len(string))
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())

# 4. Check if a string is a palindrome
pal = input("\nEnter a string to check palindrome: ")
if pal == pal[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

# 5. Count vowels and consonants
text = input("\nEnter a string to count vowels and consonants: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for ch in text if ch in vowels)
consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# 6. Check if one string contains another
main_str = input("\nEnter the main string: ")
sub_str = input("Enter the string to search for: ")
if sub_str in main_str:
    print("Yes, it contains the string.")
else:
    print("No, it does not contain the string.")

# 7. Replace a word in a sentence
sentence = input("\nEnter a sentence: ")
word_to_replace = input("Word to replace: ")
replacement = input("Replace with: ")
new_sentence = sentence.replace(word_to_replace, replacement)
print("Updated sentence:", new_sentence)

# 8. Print first and last character
str_input = input("\nEnter a string: ")
if len(str_input) >= 1:
    print("First character:", str_input[0])
    print("Last character:", str_input[-1])
else:
    print("String is empty.")

# 9. Print reversed string
rev_input = input("\nEnter a string to reverse: ")
print("Reversed:", rev_input[::-1])

# 10. Count number of words in a sentence
sentence = input("\nEnter a sentence: ")
word_count = len(sentence.split())
print("Number of words:", word_count)

# 11. Check if string contains any digits
check_digits = input("\nEnter a string: ")
contains_digit = any(ch.isdigit() for ch in check_digits)
print("Contains digits?" , contains_digit)

# 12. Join list of words with a character
words = input("\nEnter words separated by space: ").split()
separator = input("Enter separator character: ")
joined = separator.join(words)
print("Joined string:", joined)

# 13. Remove all spaces from string
no_space_str = input("\nEnter a string with spaces: ")
print("Without spaces:", no_space_str.replace(" ", ""))

# 14. Check if two strings are equal
s1 = input("\nEnter first string: ")
s2 = input("Enter second string: ")
print("Strings are equal?" , s1 == s2)

# 15. Create acronym
sentence = input("\nEnter a sentence to create acronym: ")
acronym = ''.join(word[0].upper() for word in sentence.split() if word)
print("Acronym:", acronym)

# 16. Remove all occurrences of a character
main_str = input("\nEnter a string: ")
char_to_remove = input("Enter character to remove: ")
print("Updated string:", main_str.replace(char_to_remove, ""))

# 17. Replace vowels with a symbol
text = input("\nEnter a string: ")
symbol = input("Enter a symbol to replace vowels with: ")
vowels = "aeiouAEIOU"
replaced = ''.join(symbol if ch in vowels else ch for ch in text)
print("Updated string:", replaced)

# 18. Check if a string starts and ends with specific words
text = input("\nEnter a sentence: ")
start_word = input("Starts with: ")
end_word = input("Ends with: ")
print("Starts with given word?" , text.startswith(start_word))
print("Ends with given word?" , text.endswith(end_word))
