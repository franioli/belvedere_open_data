import json
import argparse


def parse_command_line() -> str:
    """
    parse_command_line Parse command line input

    Returns:
        str:
    """
    parser = argparse.ArgumentParser(
        description="""Read point cloud metadata in a Python Dictionary"""
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Path of json file to read",
    )
    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        help="Path of the folder containing metadata json file to read",
        default=None,
    )
    args = parser.parse_args()

    if args.file is not None:
        data = args.file
    elif args.dir is not None:
        data = args.file
    else:
        raise ValueError(
            "Not enough input arguments. Specify the json file to read or the directory containing metadata. Use --help (or -h) for help."
        )

    return data


if __name__ == "__main__":
    # data = parse_command_line()

    fdict = {0: None}

    metadata = {}
    for k, v in fdict.items():
        with open("example.json", "r") as f:
            metadata[k] = json.load(f)

    print(metadata)
