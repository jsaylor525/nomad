"""
Install all the packages needed for this application

TODO:
- Add python version check.
"""

if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) > 1:
        if "dev" in sys.argv[1]:
            os.system('pip install -r developer_requirements.txt')
        else:
            raise ValueError(f"Unrecognized input: {sys.argv[1]}")
    else:
        os.system('pip install -r requirements.txt')
