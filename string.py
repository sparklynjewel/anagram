def find_anagram(word, anagram):
    return sorted(word) == sorted(anagram)


word = input("enter your first word: ")
anagram = input("enter your second word: ")
print(sorted(word), sorted(anagram))

if sorted(word) == sorted(anagram):
    print("the strings are anagram")
else:
    print("the strings are not anagram")

find_anagram(word, anagram)  # able to return true/false on jupyter notebook
