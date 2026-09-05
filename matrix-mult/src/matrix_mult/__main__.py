import argparse
from common_util import matrix_in, matrix_out, print_matrix
from .multiply import multiply_matrices

def setup_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Matrix multiplication using NPUCompute"
    )

    parser.add_argument(
        "left_mat_file",
        type=str,
        help="Path to the file containing the left matrix",
    )

    parser.add_argument(
        "right_mat_file",
        type=str,
        help="Path to the file containing the right matrix",
    )

    parser.add_argument(
        "output_file",
        nargs="?",
        default=None,
        type=str,
        help="Path to the output file where the result will be saved",
    )

    parser.add_argument(
        "--silent",
        action="store_true",
        help="Suppress output messages"
    )

    return parser.parse_args()

def main() -> None:
    args = setup_args()

    # Load matrices from files
    matrix_a = matrix_in(args.left_mat_file)
    matrix_b = matrix_in(args.right_mat_file)

    if not args.silent:
        print("Left matrix:")
        print_matrix(matrix_a)

        print("Right matrix:")
        print_matrix(matrix_b)

    # Perform matrix multiplication
    result = multiply_matrices(matrix_a, matrix_b)
    print("Result:")
    print_matrix(result)

    # Save the result to the output file
    if args.output_file is not None:
        matrix_out(result, args.output_file)

    if not args.silent:
        print(f"Result saved to {args.output_file}")


main()