"""
Generate a Latex Project Structure

- <proj-name>
    - write_up
       - <proj-name>.tex
       - <proj-name>.bib (optional)
    - Makefile
"""
from contextlib import contextmanager
from shutil import copyfile
import os

from pathlib import Path

from colorama import Fore, Style, init, deinit


from .options import Options
from .tex_parts import Lists, GRAPHIC, EQUATION, BIBTEX


@contextmanager
def windows_support():
    """Windows cmd does does not support these colors"""
    init()
    yield
    deinit()


def generate(options: Options):
    """Generate Project Structure"""
    with windows_support():
        _generate(options)


def _generate(options: Options):
    root = Path(options.project_name)

    if root.exists():
        print(
            "{}Folder with name {} exists already.{}".format(
                Fore.RED, str(root), Style.RESET_ALL
            )
        )
        return

    root.mkdir()

    write_up_folder = root / "write_up"
    write_up_folder.mkdir()

    tex_file = write_up_folder / (options.project_name + ".tex")

    tex_content = setup_template(options)

    with open(str(tex_file), "w") as t_file:
        t_file.write(tex_content)

    if options.include_bib:
        copyfile(
            "./latex_up/templates/bib.bib",
            write_up_folder / (options.project_name + ".bib"),
        )

    cls_file = "./latex_up/templates/{cls}/{cls}.cls".format(cls=options.template)

    if os.path.isfile(cls_file):
        copyfile(
            cls_file,
            write_up_folder
            / (options.project_name)
            / "{}.cls".format(options.template),
        )


def setup_template(options: Options) -> str:
    """Read in template and collect all parts which should be added into latex document"""
    template_content = []

    with open(
        "./latex_up/templates/{cls}/{cls}.tex".format(cls=options.template), "r"
    ) as template_file:
        template_lines = template_file.read()

    if options.include_enumerate:
        template_content.extend(Lists.ENUMERATE)
    if options.include_itemize:
        template_content.extend(Lists.ITEMIZE)
    if options.include_description:
        template_content.extend(Lists.DESCRIPTION)
    if options.include_graphic:
        template_content.extend(GRAPHIC)
    if options.include_equation:
        template_content.extend(EQUATION)
    if options.include_bib:
        bibtex = []
        for line in BIBTEX:
            if "<project_name>" in line:
                line = line.replace("<project_name", options.project_name)
            bibtex.append(line)
        template_content.extend(bibtex)

    template_lines = template_lines.replace("{{SAMPLES}}", "\n".join(template_content))

    return template_lines
