"""

    LatexUp - Setup Latex Projects Quickly

    Patrick Haller
    patrickhaller40@googlemail.com

    License MIT

"""

import os
import sys

from bullet import Bullet, Check, Input, VerticalPrompt
from simple_parsing import ArgumentParser

from frosch import hook

from .generator import generate
from .options import Options


hook()


def run_cli() -> Options:
    """
    Run CLI and return options
    """

    cli = VerticalPrompt(
        [
            Input("Project Name? ", default="latex_project", strip=True),
            Bullet(
                "Which template to use?",
                choices=[t for t in os.listdir("./latex_up/templates") if "." not in t],
            ),
            Check(
                "Include lists? (Press Space to check/uncheck)",
                ["Enumerate", "Itemize", "Description"],
            ),
            Check(
                "Choose other latex structures to include. (Press Space to check/uncheck)",
                ["Graphic", "Bibtex", "Equation"],
            ),
        ],
        spacing=1,
    )

    result = cli.launch()

    return Options.from_args(result[0][1], result[1][1], *result[2][1], *result[3][1])


def arg_parser() -> Options:
    """Retrieve all options from command line"""
    parser = ArgumentParser()
    parser.add_arguments(Options, dest="options")
    args = parser.parse_args()
    return args.options


def main():
    """Entry Point"""
    options = run_cli() if len(sys.argv) == 1 else arg_parser()
    generate(options)


if __name__ == "__main__":
    main()
