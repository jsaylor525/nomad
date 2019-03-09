"""
Install all the packages needed for this application

TODO:
- Add python version check.
"""

if __name__ == '__main__':
   import os
   try:
      os.system('activate nomad-venv && pip install -r requirements.txt')
   except:
      print("You need to install conda to develop nomad. https://www.anaconda.com/")
