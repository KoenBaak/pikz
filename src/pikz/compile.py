import os
import subprocess

AUX_EXTENSIONS = [
    "aux", "log"
]


def compile(filepath: str,
            outputdir: str = None,
            clean_files: bool = True) -> str:

    if outputdir is None:
        outputdir = os.path.dirname(filepath)

    command = f"pdflatex -output-directory={outputdir} {filepath}".split()

    subprocess.check_call(command)

    basename = os.path.basename(filepath)
    base, _ = os.path.splitext(basename)

    if clean_files:
        for ext in AUX_EXTENSIONS:
            target = f"{base}.{ext}"
            os.remove(os.path.join(outputdir, target))

    return os.path.join(outputdir, f"{base}.pdf")