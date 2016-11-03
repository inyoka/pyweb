#!/usr/bin/env python3
import media
import fresh_tomatoes

discovering_python = media.Movie('Title', 'Description','RZ4Sn-Y7AP8')
    #    discovering_python = media.Movie('Discovering Python', 'What in a source code and no internet connection?', 'RZ4Sn-Y7AP8')
movies = [discovering_python]

fresh_tomatoes.open_movies_page(movies)
