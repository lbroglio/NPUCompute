import random

def generate_matrix(rows: int, cols: int, value_min: int = 0, value_max: int = 50) -> list:
    """
    Generates a matrix with the specified number of rows and columns and 
    fills it with random float values between value_min and value_max.

    Args:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        value_min (int): The minimum value for the random integers. Default is 0.
        value_max (int): The maximum value for the random integers. Default is 50.

    Returns:
        list: A 2D list representing the generated matrix.
    """
    matrix = []
    for _ in range(rows):
        row = [random.randint(value_min, value_max) for _ in range(cols)]
        matrix.append(row)
    
    return matrix