import webbrowser
import fresh_tomatoes

''' define a Movie class that takes in the movie title, movie story,
post image and trailor link
'''


class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailor_youtube_url):
        # attributes to the class
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailor_youtube_url

    # define a method show_trailer which opens the trailor url
    def show_trailer(self):
        webbrowser.open(self.trailor_youtube_url)

# first movie instance, forest gump
gump = Movie("Forrest Gump", "A guy called Forrest Gump",
             "https://www.artjobs.com/sites/default/files/styles/750/public/project_work/2781/Forrest-Gump-poster-WEB-1400.jpg?itok=F6nso_v6",  # noqa
             "https://www.youtube.com/watch?v=bLvqoHBptjg")

# Second movie instance, before sunrise
before_sunrise = Movie("Before Sunrise", "An american guy met a french women",
                       "https://m.media-amazon.com/images/M/MV5BZDdiZTAwYzAtMDI3Ni00OTRjLTkzN2UtMGE3MDMyZmU4NTU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,672,1000_AL_.jpg",  # noqa
                       "https://www.youtube.com/watch?v=25v7N34d5HE&t=20s")

# Third movie instance, pianist
pianist = Movie("The Pianist", "Polish pianist life story under war",
                "http://2.bp.blogspot.com/-UYpsaO3k3vQ/ViftzQtuoXI/AAAAAAABeX8/h-dX5tZOoBw/s1600/the-pianist-poster.jpg",  # noqa
                "https://www.youtube.com/watch?v=CIRLLPa-j9o")

# Hold movies instances in a list
movies = [gump, before_sunrise, pianist]

# open the movies page
fresh_tomatoes.open_movies_page(movies)
