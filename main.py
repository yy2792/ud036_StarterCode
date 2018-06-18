import webbrowser
import fresh_tomatoes


class Movie():
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailor_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailor_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailor_youtube_url)

gump = Movie("Forrest Gump", "A guy called Forrest Gump",
             "https://www.artjobs.com/sites/default/files/styles/750"+
             "/public/project_work/2781/Forrest-Gump-poster-WEB-1400"+
             ".jpg?itok=F6nso_v6",
             "https://www.youtube.com/watch?v=bLvqoHBptjg")


before_sunrise = Movie("Before Sunrise", "An american guy met a french women",
                       "https://m.media-amazon.com/images/M/MV5BZDdiZTAwYzAt"+
                       "MDI3Ni00OTRjLTkzN2UtMGE3MDMyZmU4NTU4XkEyXkFqcGdeQXVyNjU"
                       +"0OTQ0OTY@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=25v7N34d5HE&t=20s")


pianist = Movie("The Pianist", "Polish pianist life story under war",
                "http://2.bp.blogspot.com/-UYpsaO3k3vQ/ViftzQtuoXI/"+
                "AAAAAAABeX8/h-dX5tZOoBw/s1600/the-pianist-poster.jpg",
                "https://www.youtube.com/watch?v=CIRLLPa-j9o")

movies = [gump, before_sunrise, pianist]

fresh_tomatoes.open_movies_page(movies)
