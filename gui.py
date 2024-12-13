from PyQt6 import QtCore, QtWidgets
from JesusRamirez1 import Voting


class Gui:
    def __init__(self):
        self.vote_system = Voting()

    def setupUi(self, FinalVote):
        FinalVote.setObjectName("FinalVote")
        FinalVote.setFixedSize(600, 400)
        FinalVote.setStyleSheet("background-color: white;")

        self.title = QtWidgets.QLabel(FinalVote)
        self.title.setText("VOTING")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setGeometry(0, 10, 600, 50)
        self.title.setStyleSheet("color: green; font-size: 24px; font-weight: bold;")

        self.a_button = QtWidgets.QPushButton("A\nVOTE", FinalVote)
        self.a_button.setGeometry(50, 150, 150, 80)
        self.a_button.setStyleSheet("background-color: blue; color: white; font-size: 20px; border-radius: 25px;")
        self.a_button.clicked.connect(self.vote_a)

        self.b_button = QtWidgets.QPushButton("B\nVOTE", FinalVote)
        self.b_button.setGeometry(400, 150, 150, 80)
        self.b_button.setStyleSheet("background-color: red; color: white; font-size: 20px; border-radius: 25px;")
        self.b_button.clicked.connect(self.vote_b)

        self.id_input = QtWidgets.QLineEdit(FinalVote)
        self.id_input.setGeometry(225, 150, 150, 30)
        self.id_input.setPlaceholderText("Enter ID")
        self.id_input.setStyleSheet("color: black; font-size: 16px; border: 2px solid gray; border-radius: 15px;")

        self.clear_button = QtWidgets.QPushButton("CLEAR", FinalVote)
        self.clear_button.setGeometry(250, 300, 100, 40)
        self.clear_button.setStyleSheet("background-color: orange; color: white; font-size: 18px; border-radius: 15px;")
        self.clear_button.clicked.connect(self.clear_votes)

        self.a_votes = QtWidgets.QLabel("0 votes", FinalVote)
        self.a_votes.setGeometry(50, 240, 150, 30)
        self.a_votes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.a_votes.setStyleSheet("background-color: blue; color: white; font-size: 16px; border-radius: 15px;")

        self.b_votes = QtWidgets.QLabel("0 votes", FinalVote)
        self.b_votes.setGeometry(400, 240, 150, 30)
        self.b_votes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.b_votes.setStyleSheet("background-color: red; color: white; font-size: 16px; border-radius: 15px;")

    def vote_a(self):
        voter_id = self.id_input.text().strip()
        if not voter_id:
            self.show_error("Enter id!")
        else:
            success = self.vote_system.vote(1, voter_id)
            if success:
                self.a_votes.setText(f"{self.vote_system.a_votes} votes")
                self.id_input.clear()
                self.check_winner()
            else:
                self.show_error("Already voted!")

    def vote_b(self):
        voter_id = self.id_input.text().strip()
        if not voter_id:
            self.show_error("Enter id!")
        else:
            success = self.vote_system.vote(2, voter_id)
            if success:
                self.b_votes.setText(f"{self.vote_system.b_votes} votes")
                self.id_input.clear()
                self.check_winner()
            else:
                self.show_error("Already voted!")

    def clear_votes(self):
        self.vote_system.reset_votes()
        self.a_votes.setText("0 votes")
        self.b_votes.setText("0 votes")
        self.id_input.clear()

    def show_error(self, message):
        error_dialog = QtWidgets.QMessageBox()
        error_dialog.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        error_dialog.exec()

    def check_winner(self):
        if self.vote_system.a_votes >= 10:
            self.show_winner("A wins!")
            self.clear_votes()
        elif self.vote_system.b_votes >= 10:
            self.show_winner("B wins!")
            self.clear_votes()

    def show_winner(self, message):
        winner_dialog = QtWidgets.QMessageBox()
        winner_dialog.setIcon(QtWidgets.QMessageBox.Icon.Information)
        winner_dialog.setWindowTitle("Winner")
        winner_dialog.setText(message)
        winner_dialog.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        winner_dialog.exec()