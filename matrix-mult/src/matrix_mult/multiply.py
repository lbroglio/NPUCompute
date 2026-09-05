import torch
import openvino as ov
from common_util import build_ov_model, get_ov_result_as_list

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

    model = MatrixMultiplier(torch.tensor(matrix_b))

    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if matrix_a else 0
    input_shape = [rows_a, cols_a]

    input_tensor = torch.tensor(matrix_a, dtype=torch.float32)

    # Build compiled OpenVINO model
    compiled_model = build_ov_model(model, input_tensor, input_shape)

    result = compiled_model(input_tensor.numpy())

    return get_ov_result_as_list(result)
