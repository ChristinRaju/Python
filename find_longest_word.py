#Implement a function that finds the longest word in a given sentence in Python.

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Example usage
sentence = "student of nitte mangalore"
longest_word = find_longest_word(sentence)
print("Longest word:", longest_word)




