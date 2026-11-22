def is_palindrome(s):
    s_clean = s.lower()
    print("Palindrome" if s_clean == s_clean[::-1] else "Not Palindrome")

is_palindrome("Madam")