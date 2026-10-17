#Unique word analyzer
sentence = input("Enter a Sentence: ")
sentence = sentence.lower()
words = sentence.split()
unique_words = set(words)
print("Total words:", len(words))
print("Unique words:", len(unique_words))