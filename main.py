from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QPushButton
import sys
import backend
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatGPT Application")
        self.setFixedSize(700, 500)
        self.chatbot = backend.Chatbot()

        self.chat_area = QTextEdit(self)
        self.input_field = QLineEdit(self)
        self.button_submit = QPushButton("Submit", self)

        self.chat_area.setGeometry(10, 10, 480, 320)
        self.input_field.setGeometry(10, 340, 480, 25)
        self.button_submit.setGeometry(490, 340, 100, 25)

        self.chat_area.setReadOnly(True)
        self.input_field.setPlaceholderText("Enter Something")

        self.show()

        self.button_submit.clicked.connect(self.send_prompt)
        self.input_field.returnPressed.connect(self.send_prompt)

    def send_prompt(self):
        prompt = self.input_field.text()
        self.chat_area.append(f"<p><span style = 'color: blue;'> User: </span> {prompt} </p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(prompt,))
        thread.start()

    def get_bot_response(self, prompt):
        response = self.chatbot.get_response(prompt).strip("\n")
        self.chat_area.append(f"<p><span style = 'color: red;'> Bot: </span> {response} </p>")


application = QApplication(sys.argv)
window = ChatbotWindow()
sys.exit(application.exec())
