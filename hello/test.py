import nltk
with open("test.txt", "r") as test_file: 
    for line in test_file:
        line = line.lower()
        tokens = nltk.word_tokenize(line)
        print (tokens)