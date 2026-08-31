def matrix_in(filepath: str) -> list[list[float]]:
    """
    Reads a matrix from a file and returns it as a list of lists of floats.

    Args:
        filepath (str): The path to the file containing the matrix.
    
    Returns:
        list[list[float]]: The matrix read from the file.
    """

    matrix = []
    with open(filepath, 'r') as file:
        for line in file:
            row = [float(num) for num in line.split()]
            matrix.append(row)
    return matrix

def matrix_out(matrix: list[list[float]], filepath: str) -> None:
    """
    Writes a matrix to a file.

    Args:
        matrix (list[list[float]]): The matrix to write to the file.
        filepath (str): The path to the file where the matrix will be written.
    """

    with open(filepath, 'w') as file:
        for row in matrix:
            line = ' '.join(str(num) for num in row)
            file.write(line + '\n')
