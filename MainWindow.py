import sqlite3

from BookInfo import BookInfo
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from ui.MainWindow_ui import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connection = sqlite3.connect('database/Library_db.sqlite')

        self.data = []

        self.book_info_widget: BookInfo | None = None

        self.view_param_box.currentIndexChanged.connect(self.toggle_stacked_widget)
        self.search_button.clicked.connect(self.search_books)
        self.book_info_list.doubleClicked.connect(self.book_info_list_dobleclicked)
        self.book_info_table.clicked.connect(self.book_info_table_dobleclicked)

    def toggle_stacked_widget(self):
        self.stacked_widget.setCurrentIndex(self.view_param_box.currentIndex())

    def search_books(self):
        param = self.search_param_box.currentText()
        arg = self.search_edit.text()

        if param == 'Автор':
            request = f"""SELECT Book.BookId,
       Book.title,
       Author.title,
       Book.year,
       Genre.title,
       Image.path
  FROM Book
       LEFT JOIN
       Author ON Book.author = Author.AuthorId
       LEFT JOIN
       Genre ON Book.genre = Genre.GenreId
       LEFT JOIN
       Image ON Book.image = Image.ImageId
 WHERE Author.title LIKE '%{arg}%';
"""
        elif param == 'Название':
            request = f"""SELECT Book.BookId,
       Book.title,
       Author.title,
       Book.year,
       Genre.title,
       Image.path
  FROM Book
       LEFT JOIN
       Author ON Book.author = Author.AuthorId
       LEFT JOIN
       Genre ON Book.genre = Genre.GenreId
       LEFT JOIN
       Image ON Book.image = Image.ImageId
 WHERE Book.title LIKE '%{arg}%';
"""
        else:
            request = """"""

        cursor = self.connection.cursor()
        self.data = cursor.execute(request).fetchall()

        self.update_info_widgets()

    def update_info_widgets(self):
        self.update_book_info_table()
        self.update_book_info_list()

    def update_book_info_list(self):
        self.book_info_list.clear()
        self.book_info_list.addItems(map(lambda record: record[1], self.data))

    def update_book_info_table(self):
        self.book_info_table.clear()
        self.book_info_table.setRowCount(0)
        self.book_info_table.setColumnCount(5)
        self.book_info_table.setHorizontalHeaderLabels(('ИД', 'Название', 'Автор', 'Год создания', 'Жанр'))

        for i, record in enumerate(self.data):
            self.book_info_table.setRowCount(self.book_info_table.rowCount() + 1)
            for j, element in enumerate(record):
                self.book_info_table.setItem(i, j, QTableWidgetItem(str(element)))

        self.book_info_table.resizeColumnsToContents()

    def book_info_list_dobleclicked(self):
        self.open_book_info_widget(self.book_info_list.selectedIndexes()[0].row())

    def book_info_table_dobleclicked(self):
        self.open_book_info_widget(self.book_info_table.selectedIndexes()[0].row())
        self.book_info_table.clearSelection()

    def open_book_info_widget(self, row):
        self.book_info_widget = BookInfo(*self.data[row])
        self.book_info_widget.show()

    def closeEvent(self, a0):
        self.connection.close()
