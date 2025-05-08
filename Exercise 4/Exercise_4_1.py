from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtWebKitWidgets import QWebView

# Get the district name from the clicked feature
district = '[%"Stat_Name"%]'# Replace with your field name

# Format it for Wikipedia URL (replace spaces with underscores)
district_formatted = district.replace(" ", "_")

# Constructing  the Wikipedia URL
url = QUrl(f"https://en.wikipedia.org/wiki/{district_formatted}")

# Creating a WebView object
web = QWebView()

# Loading the URL into the WebView
web.load(url)
web.resize(800, 600)
# Showing the window
web.show()