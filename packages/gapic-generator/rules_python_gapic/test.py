import os
import sys


if __name__ == '__main__':
    os.environ['PYTHONNOUSERSITE'] = 'True'
    entry_point_script = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.path.basename(__file__).replace("_test.py", "_pytest.py"))
    args = [sys.executable, entry_point_script] + sys.argv[1:]
    os.execv(args[0], args)
