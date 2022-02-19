import os
import streamlit.bootstrap
from streamlit import config as _config
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Data tagging tool.")
    subparsers = parser.add_subparsers(help="Tagging mode.", dest="mode", required=True)

    choice_parser = subparsers.add_parser(
        "choice", help="Classify data in non-overlapping classes."
    )
    choice_parser.add_argument("path", type=str, help="Path to the *csv file to label")
    choice_parser.add_argument(
        "--source", type=str, help="Name of the column to be labelled", required=True
    )
    choice_parser.add_argument(
        "--target",
        type=str,
        help="Name of the column to store labels to",
        required=True,
    )
    choice_parser.add_argument(
        "--labels", type=str, help="Comma separated labels", required=True
    )
    return parser.parse_args()


def cli():
    args = parse_arguments()
    if args.mode == "choice":

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "choice.py")

        print(filename)

        _config.set_option("server.headless", False)
        st_args = [args.path, args.source, args.target, args.labels]

        # streamlit.cli.main_run(filename, args)
        streamlit.bootstrap.run(filename, "", st_args, flag_options={})
    else:
        raise ValueError(f"Unkown mode: {args.mode}")