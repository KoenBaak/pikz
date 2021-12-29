import os

from .abc import Fillable
from .compile import compile_latex
from .secret_dir import _secret_dir


class Figure:

    def __init__(self,
                 name: str = 'pikzfig') -> None:

        self._elements = []
        self.name = name

    @property
    def elements(self):
        return self._elements

    def add(self, *args):
        self._elements.extend(args)

    def tikzpicture_body(self) -> str:
        lines = []
        for e in self._elements:
            lines.append(e.tikz_draw())
            if isinstance(e, Fillable):
                lines.append(e.tikz_fill())
        return "\n".join(lines)

    def to_latex(self) -> str:
        lines = [
            "\\documentclass{standalone}",
            "\\usepackage{tikz}",
            "\\begin{document}",
            "\\begin{tikzpicture}",
            self.tikzpicture_body(),
            "\\end{tikzpicture}",
            "\\end{document}"
        ]

        return "\n".join(lines)

    def save_tex(self,
                 filename: str = None) -> str:

        filename = filename or f"{self.name}.tex"

        if not filename.endswith('.tex'):
            filename += '.tex'

        path = os.path.join(os.getcwd(), filename)

        with open(path, 'w') as f:
            f.write(self.to_latex())

        return path

    def build(self,
              name: str = None,
              tex_dir: str = None,
              outputdir: str = None,
              clean_files: bool = True) -> str:

        name = name or self.name
        tex_dir = tex_dir or os.getcwd()
        outputdir = outputdir or tex_dir

        latex_path = os.path.join(tex_dir, f"{name}.tex")
        latex_path = self.save_tex(latex_path)

        return compile_latex(filepath=latex_path,
                             outputdir=outputdir,
                             clean_files=clean_files)

    def _repr_html_(self):
        pdf_path = self.build(tex_dir=_secret_dir())
        rel_path = os.path.relpath(pdf_path)
        return f'<iframe> src="{rel_path}" width=300 height=300></iframe>'

    def __repr__(self):
        return f"<pikz.figure.Figure '{self.name}' with {len(self._elements)} elements>"