import os
import subprocess
import shutil

AUX_EXTENSIONS = [
    "aux", "log"
]


class LatexCompileError(RuntimeError):
    pass


def _clean_files(dir: str, basename: str) -> None:
    for ext in AUX_EXTENSIONS:
        target = f"{basename}.{ext}"
        os.remove(os.path.join(dir, target))


def compile_latex(filepath: str,
                  outputdir: str = None,
                  clean_files: bool = True) -> str:

    if not os.path.exists(filepath):
        raise FileNotFoundError

    if shutil.which("pdflatex") is None:
        raise RuntimeError(f"pdf latex needs to be installed")

    outputdir = outputdir or os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    base, _ = os.path.splitext(filename)

    command = f"pdflatex -output-directory={outputdir} -interaction=nonstopmode {filepath}".split()

    compile_process = subprocess.run(command,
                                     stderr=subprocess.PIPE,
                                     stdout=subprocess.PIPE,
                                     universal_newlines=True)

    if compile_process.returncode != 0:
        out = compile_process.stdout
        error_msg = out[out.find("!"):]
        if clean_files:
            _clean_files(outputdir, base)
        raise LatexCompileError(error_msg)

    if clean_files:
        _clean_files(outputdir, base)

    return os.path.join(outputdir, f"{base}.pdf")