import gaz1 , temperature1 , humidite1 , presence1 
from PyQt4 import QtCore,QtGui


if __name__ == "__main__":
    import sys
    import subprocess
    subprocess.Popen(["python","gaz1.py"])
    subprocess.Popen(["python","temperature1.py"])
    subprocess.Popen(["python","humidite1.py"])
    subprocess.Popen(["python","presence1.py"])
