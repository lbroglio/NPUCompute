import random

def generate_matrix(rows: int, cols: int, value_min: float = 0, value_max: float = 1000, round_to: int = 2) -> list:
    """
    Generates a matrix with the specified number of rows and columns and 
    fills it with random float values between value_min and value_max.

    Args:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        value_min (float): The minimum value for the random floats. Default is 0.
        value_max (float): The maximum value for the random floats. Default is 1000

    Returns:
        list: A 2D list representing the generated matrix.
    """
    matrix = []
    for _ in range(rows):
        row = [random.uniform(value_min, value_max) for _ in range(cols)]
        row = [round(x, round_to) for x in row]
        matrix.append(row)
    
    return matrix