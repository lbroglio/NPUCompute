import torch
import openvino as ov

# A dummy PyTorch model that performs matrix multiplication
class MatrixMultiplier(torch.nn.Module):
    def __init__(self, weight):
        super().__init__()
        self.weight = torch.nn.Parameter(weight, requires_grad=False)

    def forward(self, x):
        return x @ self.weight

def multiply_matrices(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    """
    Multiplies two matrices using the NPU and returns the result.

    Args:
        matrix_a (list[list[float]]): The first matrix.
        matrix_b (list[list[float]]): The second matrix.
    
    Returns:
        list[list[float]]: The resulting matrix after multiplication.
    
    Raises:
        ValueError: If the number of columns in matrix_a does not equal the number of rows in matrix_b.
    """

    # Validate inputs 
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in matrix_a must equal number of rows in matrix_b for multiplication.")

    # Set inputs as a PyTorch model
    model = MatrixMultiplier(torch.tensor(matrix_b))

    # Convert the PyTorch model to OpenVINO format
    model.eval()
    input_tensor = torch.tensor(matrix_a, dtype=torch.float32)

    ov_model = ov.convert_model(
        model,
        example_input=input_tensor
    )

    core = ov.Core()

    compiled_model = core.compile_model(
        ov_model,
        "NPU"
    )
    

