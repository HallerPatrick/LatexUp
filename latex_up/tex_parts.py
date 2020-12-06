"""

    LatexUp - Setup Latex Projects Quickly

    Patrick Haller
    patrickhaller40@googlemail.com

    License MIT

"""


class Lists:
    """
    https://texblog.org/2008/10/16/lists-enumerate-itemize-description-and-how-to-change-them/
    """

    ENUMERATE = [
        r"",
        r"\begin{enumerate}[I] % For capital roman numbers, '[(a)]' for small alpha-characters",
        r"\item Some Item",
        r"\item Other Item",
        r"\end{enumerate}",
        r"",
    ]
    ITEMIZE = [
        r"",
        r"\begin{itemize}",
        r"\item Some Item",
        r"\item Other Item",
        r"\end{itemize}",
        r"",
    ]
    DESCRIPTION = [
        r"",
        r"\begin{description}",
        r"\item[Item1] Some Item",
        r"\item[Item2] Other Item",
        r"\end{description}",
        r"",
    ]


GRAPHIC = [
    r"",
    r"\begin{figure}[t]",
    r"\caption{Some Sample Caption}",
    r"\includegraphics[width=8cm]{<path_to_img>}",
    r"\centering",
    r"\end{figure}",
    r"",
]

EQUATION = [
    r"",
    r"\begin{equation} \label{eq1}",
    r"\begin{split}",
    r"A & = \frac{\pi r^2}{2} \\",
    r" & = \frac{1}{2} \pi r^2",
    r"\end{split}",
    r"\end{equation}",
    r"",
    r"\begin{equation} \label{eu_eqn}",
    r"e^{\pi i} + 1 = 0",
    r"\end{equation}",
    r"",
    r"The beautiful equation \ref{eu_eqn} is known as the Euler equation",
    r"",
]

BIBTEX = [
    r"",
    r"This is a sentece witch include a citation from \cite{turing}",
    r"\bibliography{<project_name>}",
    r"",
]
