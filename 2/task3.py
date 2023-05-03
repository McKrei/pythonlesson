def is_pythagorean_triple(x,y,z):
    return True if (z**2 - y**2)**0.5 == x else False

assert is_pythagorean_triple(3, 4, 5) == True
assert is_pythagorean_triple(5, 12, 13) == True
assert is_pythagorean_triple(7, 8, 9) == False  
