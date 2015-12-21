
import webbrowser


class Movie():
	"""docstring for ClassName"""
	def __init__(self, title, preview_url, box_art_url):
		self.title = title
		self.preview_url = preview_url
		self.box_art = box_art_url

	def show_trailer(self):
		webbrowser.open(self.preview_url)


