import argparse
from common_util import matrix_out, print_matrix
from .generate import generate_matrix

def setup_args():
    parser = argparse.ArgumentParser(description="Input Generator")

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show verbose output."
    )

    subparsers = parser.add_subparsers(dest="matrix", help="Subcommands for generating matrices")

    # Matrix generation subcommand
    matrix_parser = subparsers.add_parser("matrix", help="Generate a random matrix")
    matrix_parser.add_argument(
        "rows",
        type=int,
        help="Number of rows in the generated matrix."
    )
    matrix_parser.add_argument(
        "cols",
        type=int,
        help="Number of columns in the generated matrix."
    )
    matrix_parser.add_argument(
        "--value-min",
        type=float,
        default=0,
        help="Minimum value for the random floats in the matrix."
    )
    matrix_parser.add_argument(
        "--value-max",
        type=float,
        default=1000,
        help="Maximum value for the random floats in the matrix."
    )
    matrix_parser.add_argument(
        "--output-file",
        "-o",
        type=str,
        default="matrix.txt",
        help="Output file to save the generated matrix."
    )
    matrix_parser.add_argument(
        "--decimal-places",
        type=int,
        default=2,
        help="Number of decimal places to round the random floats in the matrix."
    )


    return parser.parse_args()

def main():
    args = setup_args()

    if args.matrix == "matrix":

        # Validate arguments
        if args.rows <= 0 or args.cols <= 0:
            print("Error: Rows and columns must be positive integers.")
            return

        if args.verbose:
            print(f"Generating a {args.rows}x{args.cols} matrix with values between {args.value_min} and {args.value_max}.")
            print(f"Rounding values to {args.decimal_places} decimal places.")

        matrix = generate_matrix(args.rows, args.cols, args.value_min, args.value_max, round_to=args.decimal_places)

        if args.verbose:
            print("Generated Matrix:")
            print_matrix(matrix)

        if args.output_file:
            matrix_out(matrix, args.output_file)
       
main()