from PyQt6 import QtWidgets
from gui import Gui

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FinalVote = QtWidgets.QDialog()
    ui = Gui()
    ui.setupUi(FinalVote)
    FinalVote.show()
    sys.exit(app.exec())
