import sys
import string
import random
import pyperclip
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QTextEdit

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 400, 300)
        # self.setWindowIcon(QIcon('lock_icon.png'))

        # Örnek QSS (Qt Style Sheets) kullanımı
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLineEdit {
                background-color: white;
                color: black;
                border: 1px solid gray;
            }
            QLabel {
                font-family: Arial, sans-serif;
                font-size: 18px;
                color: #333;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()

        label = QLabel('Password Generator', self)
        label.setFont(QFont('Courier', 20))
        label.setStyleSheet('color: black;')
        label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label)

        self.password_entry = QLineEdit(self)
        self.password_entry.setFont(QFont('Courier', 16))
        self.password_entry.setStyleSheet('background-color: white; color: black; border: 1px solid gray;')
        vbox.addWidget(self.password_entry)

        hbox = QHBoxLayout()
        length_label = QLabel('Password Length:', self)
        length_label.setFont(QFont('Courier', 12))
        length_label.setStyleSheet('color: black;')
        hbox.addWidget(length_label)
        self.length_entry = QLineEdit(self)
        self.length_entry.setFont(QFont('Courier', 12))
        self.length_entry.setFixedWidth(50)
        self.length_entry.setStyleSheet('background-color: white; color: black; border: 1px solid gray;')
        hbox.addWidget(self.length_entry)
        spacer = QSpacerItem(50, 1, QSizePolicy.Expanding, QSizePolicy.Fixed)
        hbox.addSpacerItem(spacer)
        vbox.addLayout(hbox)

        generate_button = QPushButton('Generate Password 🚀', self)
        generate_button.setFont(QFont('Courier', 12))
        generate_button.setStyleSheet('background-color: #4CAF50; color: white; border: none; padding: 10px 20px;')
        generate_button.clicked.connect(self.generate_password)
        vbox.addWidget(generate_button)

        copy_button = QPushButton('Copy to Clipboard 📋', self)
        copy_button.setFont(QFont('Courier', 12))
        copy_button.setStyleSheet('background-color: #008CBA; color: white; border: none; padding: 10px 20px;')
        copy_button.clicked.connect(self.copy_password)
        vbox.addWidget(copy_button)

        discord_button = QPushButton('Discord 👾', self)
        discord_button.setFont(QFont('Courier', 12))
        discord_button.setStyleSheet('background-color: #7289DA; color: white; border: none; padding: 10px 20px;')
        discord_button.clicked.connect(self.open_discord_invite)
        vbox.addWidget(discord_button)

        help_button = QPushButton('Klavuz ℹ️', self)
        help_button.setFont(QFont('Courier', 12))
        help_button.setStyleSheet('background-color: #2196F3; color: white; border: none; padding: 10px 20px;')
        help_button.clicked.connect(self.show_help)
        vbox.addWidget(help_button)

        central_widget.setLayout(vbox)

        self.help_window = None
        
        exit_button = QPushButton('Çıkış 🚪', self)
        exit_button.setFont(QFont('Courier', 12))
        exit_button.setStyleSheet('background-color: #f44336; color: white; border: none; padding: 10px 20px;')
        exit_button.clicked.connect(self.exit_application)
        vbox.addWidget(exit_button)

    def exit_application(self):
        reply = QMessageBox.question(self, 'Çıkış', 'Uygulamayı kapatmak istiyor musunuz?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()

    def generate_password(self):
        length = int(self.length_entry.text())
        if length <= 0:
            QMessageBox.warning(self, 'Warning', 'Password length must be greater than 0.', QMessageBox.Ok)
            return

        characters = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.setText(password)

    def copy_password(self):
        password = self.password_entry.text()
        if password:
            pyperclip.copy(password)
            QMessageBox.information(self, 'Info', 'Password copied to clipboard!', QMessageBox.Ok)

    def open_discord_invite(self):
        discord_invite_link = "https://discord.gg/your_discord_invite_link"
        webbrowser.open(discord_invite_link)

    def show_help(self):
        if not self.help_window:
            self.help_window = HelpWindow()
        self.help_window.show()

class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Klavuz')
        self.setGeometry(150, 150, 400, 300)
        self.setWindowIcon(QIcon('help_icon.png'))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()

        label = QLabel('Kullanım Klavuzu', self)
        label.setFont(QFont('Courier', 20))
        label.setStyleSheet('color: black;')
        label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(label)

        help_text = QTextEdit(self)
        help_text.setFont(QFont('Courier', 12))
        help_text.setReadOnly(True)
        help_text.setPlainText("Bu bir şifre oluşturma uygulamasıdır. İşte nasıl kullanılacağı:\n\n"
                               "1. 'Password Length' (Şifre Uzunluğu) kutusuna istediğiniz şifre uzunluğunu girin.\n"
                               "2. 'Generate Password' (Şifre Oluştur) düğmesine tıklayın.\n"
                               "3. Oluşturulan şifreyi 'Copy to Clipboard' (Panoya Kopyala) düğmesi ile kopyalayın. Kopyalandığında 'Kopyalandı' mesajı gösterilir.\n\n"
                               "Ayrıca 'Discord' düğmesi ile Discord sunucumuza katılabilir ve destek alabilirsiniz.\n\n"
                               "Herhangi bir sorunuz veya geri bildiriminiz varsa lütfen bizimle iletişime geçin!\n\n"
                               "Daha fazla bilgi için akdemirferit.rf.gd adresini ziyaret edebilirsiniz.")

        help_text.setStyleSheet('background-color: white; color: black; border: 1px solid gray;')
        vbox.addWidget(help_text)

        central_widget.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
