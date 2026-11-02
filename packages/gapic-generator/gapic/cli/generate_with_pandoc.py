import os
import sys

if __name__ == "__main__":
    os.environ["PYPANDOC_PANDOC"] = os.path.join(
        os.path.abspath(__file__).rsplit("gapic", 1)[0], "pandoc"
    )
    os.environ["LC_ALL"] = "C.UTF-8"
    os.environ["PYTHONNOUSERSITE"] = "True"

    entry_point_script = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "generate.py"
    )
    args = [sys.executable, entry_point_script] + sys.argv[1:]

    os.execv(args[0], args)
