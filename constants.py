import PyQt4
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

<<<<<<< HEAD
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
=======
HEADFONT	=		30
SUBHEADFONT	=		20
PARAFONT	=		15
>>>>>>> OpenCV

except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
# Important Constants being used:

WIDTH = 1380
HEIGHT = 720
STARTWINDOW = (10,10)
mainTitle = 'NoteCV'


font1 = QtGui.QFont()
font1.setFamily(_fromUtf8("Sawasdee"))
font1.setPointSize(16)
font1.setBold(True)
font1.setWeight(75)
