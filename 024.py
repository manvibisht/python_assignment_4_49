def count_vowels(s):
    count = sum(1 for ch in s.lower() if ch in "aeiou")
    print("Vowel count:", count)

count_vowels("Uttarakhand Technical University")