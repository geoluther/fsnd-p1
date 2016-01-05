
import fresh_tomatoes
import media

# instantiate movie objects
hateful_eight = media.Movie("The Hateful Eight", 
	"https://youtu.be/nIOmotayDMY",
	"https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/The_Hateful_Eight.jpg/220px-The_Hateful_Eight.jpg") #noqa


rock_the_kasbah =  media.Movie("Rock The Kasbah", 
	"https://www.youtube.com/watch?v=jtvcb5N_kek",
	"https://upload.wikimedia.org/wikipedia/en/thumb/7/78/Rock_the_Kasbah.jpg/220px-Rock_the_Kasbah.jpg") #noqa

last_witchhunter = media.Movie("The Last Witch Hunter", 
	"https://www.youtube.com/watch?v=xsuG2JUgs_8",
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/The_Last_Witch_Hunter_poster.jpg/220px-The_Last_Witch_Hunter_poster.jpg") #noqa

# build list of movie list
movies = [ hateful_eight, rock_the_kasbah, last_witchhunter]

# build the webpage with movie previews
fresh_tomatoes.open_movies_page(movies)
