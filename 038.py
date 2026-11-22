x = 100

def test_scope():
    x = 50
    print("Inside function (local x):", x)

test_scope()
print("Outside function (global x):", x)