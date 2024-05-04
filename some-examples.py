from pytest import approx

def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    return multiply(subtract(fahrenheit, 32), 9 / 5) # <-- Fix this in step 7


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    assert abs(add(0.1, 0.2) - 0.3) <= pow(10,-6)
    assert add(0.1, 0.2) == approx(0.3)

