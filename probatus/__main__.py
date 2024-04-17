import argparse
from probatus.thingamabobber import Thingamabobber

def parse_args():
    parser = argparse.ArgumentParser(description="Probatus: A CLI Python API Testing Tool")
    parser.add_argument(
        '-f', '--filepath',
        type=str,
        required=True,
        help="Path to the configuration file (JSON or YAML) containing the API tests."
    )
    return parser.parse_args()

def main():
    args = parse_args()
    thingamabobber = Thingamabobber()
    try:
        thingamabobber.thingamabob(args.filepath)
    except Exception as e:
        print(f"Error during main execution: {e}")

if __name__ == "__main__":
    main()