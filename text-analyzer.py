text = input("Enter a text: ")
words = text.split()

print("Number of words:", len(words))
print("Number of characters:", len(text))
print("Number of 'python':", text.lower().count("python"))

longest_word = max(words, key=len)
print("Longest word:", longest_word)

