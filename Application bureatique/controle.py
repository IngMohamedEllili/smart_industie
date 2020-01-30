import ventilateur1 , buzzer1 , lampe_administration1 , lampe_externe1 , lampe_interne1 , lampe_entree1
from PyQt4 import QtCore,QtGui


if __name__ == "__main__":
    import sys
    import subprocess
    subprocess.Popen(["python","ventilateur1.py"], shell=False)
    subprocess.Popen(["python","buzzer1.py"], shell = False)
    subprocess.Popen(["python","lampe_administration1.py"], shell=False)
    subprocess.Popen(["python","lampe_interne1.py"], shell=False)
    subprocess.Popen(["python","lampe_externe1.py"],shell=False)
    subprocess.Popen(["python","lampe_entree1.py"],shell=False)
