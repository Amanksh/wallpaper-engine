import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QScrollArea, QGridLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from api import get_wallpapers

class WallpaperSearcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wallpaper Searcher")
        self.setGeometry(100, 100, 800, 600)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Create search box and button
        search_layout = QHBoxLayout()
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Enter a search term")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search_wallpapers)
        search_layout.addWidget(self.search_box)
        search_layout.addWidget(search_button)
        main_layout.addLayout(search_layout)

        # Create scroll area for wallpapers
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # Create widget for wallpapers
        self.wallpaper_widget = QWidget()
        self.wallpaper_layout = QGridLayout(self.wallpaper_widget)
        scroll_area.setWidget(self.wallpaper_widget)

    def search_wallpapers(self):
        search_term = self.search_box.text()
        if not search_term:
            return

        # Clear previous results
        for i in reversed(range(self.wallpaper_layout.count())): 
            self.wallpaper_layout.itemAt(i).widget().setParent(None)

        # Fetch wallpapers (placeholder API call)
        wallpapers = get_wallpapers(search_term)
    
        # Display wallpapers
        for i, wallpaper_url in enumerate(wallpapers):
            label = QLabel()
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(wallpaper_url).content)
            pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(pixmap)
            row, col = divmod(i, 3)
            self.wallpaper_layout.addWidget(label, row, col)

    # def fetch_wallpapers(self, search_term):
    #     # This is a placeholder. In a real application, you would call an actual API here.
    #     # For demonstration, we'll return some placeholder image URLs
    #     return [
    #         "https://via.placeholder.com/400x400.png?text=Wallpaper+1",
    #         "https://w.wallhaven.cc/full/9d/wallhaven-9dqojx.jpg",
    #         "https://w.wallhaven.cc/full/vq/wallhaven-vq898p.png",
    #     ]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WallpaperSearcher()
    window.show()
    sys.exit(app.exec())