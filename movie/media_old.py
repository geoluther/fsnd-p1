
import webbrowser


class Movie():
	"""A Movie class containing the movie's title,
	preview url, and box art url"""

	VALID_RATING = ["G", "PG", "PG-13", "R"]

	def __init__(self, title, preview_url, box_art_url):
		self.title = title
		self.trailer_youtube_url = preview_url
		self.poster_image_url = box_art_url

	def show_trailer(self):
		webbrowser.open(self.preview_url)


