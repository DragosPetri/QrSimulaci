import sys
from ui import App
from PySide6.QtWidgets import QApplication 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())