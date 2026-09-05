import torch
import openvino as ov

def build_ov_model(pytorch_model: torch.nn.Module, example_input: torch.Tensor, input_shape: list) -> ov.Model:
    """
    Converts a PyTorch model to OpenVINO format, properly shapes its, and
    then compiles it for execution on the NPU.

    Args:
        pytorch_model: The PyTorch model to convert.
        example_input: An example input tensor for the model.
        input_shape: The desired input shape for the OpenVINO model.

    Returns:
        The compiled OpenVINO model.
    """
    pytorch_model.eval() 

    # Convert the PyTorch model to OpenVINO format
    ov_model = ov.convert_model(
        pytorch_model,
        example_input=example_input
    )

    # Reshape the OpenVINO model to the desired input shape
    ov_model.reshape({ov_model.inputs[0]: input_shape})

    core = ov.Core()
    compiled_model = core.compile_model(
        ov_model,
        "NPU"
    )

    return compiled_model

def get_ov_result_as_list(result: dict) -> list[list[float]]:
    """
    Extracts the result from the OpenVINO model output and converts it to a list of lists.

    Args:
        result: The output from the OpenVINO model.
    Returns:
        A list of lists representing the result matrix.
    """

    arr = next(iter(result.values()))
    return arr.tolist()