#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *
 
# Create an PyQT4 application object.
a = QApplication(sys.argv)       
 
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
 
# Show a message box
result = QMessageBox.question(w, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

# Just a warning
warning = QMessageBox.warning(w, "Message", "Are you sure you didn't want butter?")

# Information box
infaaa = QMessageBox.information(w,"message", "An informational message")

criti = QMessageBox.critical(w,"message", "But like seriously, this is bad. You sure you wanna do this?")

ab = QMessageBox.about(w, "About", "An example messagebox @ pythonspot.com ")
 
if result == QMessageBox.Yes:
    print 'Yes.'
else:
    print 'No.'

# Show window
w.show() 
 
sys.exit(a.exec_())