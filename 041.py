# Creates square_mod.py dynamically and imports it so Q41.py runs standalone
with open("square_mod.py", "w") as f:
    f.write("def square(n):\n    return n * n\n")

import importlib
importlib.invalidate_caches()
square_mod = importlib.import_module("square_mod")
print("Square of 9:", square_mod.square(9))