def add_numbers(a, b):
    """
    This function is supposed to add two numbers but has an intentional error.
    It subtracts instead of adding.
    """
    return a - b  # Intentional bug: should be a + b

def divide_numbers(a, b):
    """
    This function divides two numbers but has an intentional error.
    It doesn't handle division by zero properly.
    """
    return a / b  # Intentional bug: no zero division check

def multiply_numbers(a, b):
    """
    This function multiplies two numbers correctly.
    """
    return a * b