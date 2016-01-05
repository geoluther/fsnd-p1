
import webbrowser


class Movie():
	"""A Movie class that contains the movie's title,
	preview url, and box art url
	"""

	def __init__(self, title, preview_url, box_art_url):
		self.title = title
		self.trailer_youtube_url = preview_url
		self.poster_image_url = box_art_url
