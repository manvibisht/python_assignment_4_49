def case_counts(text):
    upper = sum(1 for ch in text if ch.isupper())
    lower = sum(1 for ch in text if ch.islower())
    return upper, lower

u, l = case_counts("Python Programming 101")
print("Uppercase:", u, "Lowercase:", l)