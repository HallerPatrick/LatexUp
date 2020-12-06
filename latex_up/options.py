"""

    LatexUp - Setup Latex Projects Quickly

    Patrick Haller
    patrickhaller40@googlemail.com

    License MIT

"""

from dataclasses import dataclass


@dataclass
class Options:
    """
    Options with can either be retrieved from parsing args or by the
    interaction with the interactive CLI
    """

    project_name: str
    template: str
    include_graphic: bool
    include_enumerate: bool
    include_itemize: bool
    include_description: bool
    include_bib: bool
    include_equation: bool

    @classmethod
    def from_args(cls, project_name: str, template: str, *args):
        """Create class from command line args"""
        return cls(
            project_name,
            template,
            "Graphic" in args,
            "Enumerate" in args,
            "Itemize" in args,
            "Description" in args,
            "Bibtex" in args,
            "Equation" in args,
        )
