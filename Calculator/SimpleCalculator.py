class SimpleCalculator:

    # Addition
    def add(self, a: int, b: int):
        return a + b

    # Subtraction
    def subtract(self, a: int, b: int):
        return a - b

    # Multiplication
    def multiply(self, a: int, b: int):
        return a * b

    # Division
    def divide(self, a: int, b: int):
        # Edge Case
        if b == 0:
            raise ZeroDivisionError("Denominator cannot be 0")

        return a / b

    # Special No Negative Functions
    def no_negative_add(self, a: int, b: int):

        if a < 0 or b < 0:
            raise ValueError("This method does not support negatives")
            return -1

        return a + b
