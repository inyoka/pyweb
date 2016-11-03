import webbrowser

class Movie():
    '''Provides information related to Movies'''
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, video_reference):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = 'http://img.youtube.com/vi/'+video_reference+'/0.jpg'
        self.trailer_youtube_url ='https://www.youtube.com/watch?v='+video_reference

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
