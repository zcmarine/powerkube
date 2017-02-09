import os
import sys

# Add the package to the Python path so just running `pytest` from the top-level dir works
HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.dirname(HERE))
