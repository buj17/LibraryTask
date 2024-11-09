from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QWidget
from ui.BookInfo_ui import Ui_Form


class BookInfo(QWidget, Ui_Form):
    def __init__(self, book_id: int, title: str, author: str, year: int, genre: str, image: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.book_id = book_id
        self.book_title = title
        self.book_author = author
        self.book_year = year
        self.book_genre = genre
        self.book_image = image

        source_image = QImage(f'database/images/{image}')
        clue_image = source_image.scaled(self.label.size().width(), self.label.size().height())
        pixmap = QPixmap.fromImage(clue_image)

        self.title_label.setText(title)
        self.author_label.setText(author)
        self.year_label.setText(str(year))
        self.genre_label.setText(genre)
        self.label.setPixmap(pixmap)
