import media
import fresh_tomatoes

google_python_class_1 = media.Movie('Google Python Class, Part 1: Introduction and Strings',
                        'Google Python Class Day 1 Part 1: Introduction and Strings.',
                        'http://img.youtube.com/vi/tKTZoB2Vjuk/0.jpg',
                        'https://www.youtube.com/watch?v=tKTZoB2Vjuk')

google_python_class_2 = media.Movie('Google Python Class, Part 2: Lists, Sorting, and Tuples.',
                        'Google Python Class Day 1 Part 2: Lists, Sorting, and Tuples.',
                        'http://img.youtube.com/vi/EPYupizJYQI/0.jpg',
                        'https://www.youtube.com/watch?v=EPYupizJYQI')

google_python_class_3 = media.Movie('Google Python Class, Part 3: Dicts and Files.',
                        'Google Python Class Day 1 Part 3: Dicts and Files.',
                        'http://img.youtube.com/vi/haycL41dAhg/0.jpg',
                        'https://www.youtube.com/watch?v=haycL41dAhg')

google_python_class_4 = media.Movie('Google Python Class, Part 4: Regular Expressions.',
                        'Google Python Class Day 2 Part 1: Regular Expressions.',
                        'http://img.youtube.com/vi/kWyoYtvJpe4/0.jpg',
                        'https://www.youtube.com/watch?v=kWyoYtvJpe4')

google_python_class_5 = media.Movie('Google Python Class, Part 5: Utilities: OS and Commands.',
                        'Google Python Class Day 2 Part 2: Utilities: OS and Commands.',
                        'http://img.youtube.com/vi/uKZ8GBKmeDM/0.jpg',
                        'https://www.youtube.com/watch?v=uKZ8GBKmeDM')

google_python_class_6 = media.Movie('Google Python Class, Part 6: Utilities: URLs and HTTP, Exceptions.',
                        'Google Python Class Day 2 Part 3: Utilities: URLs and HTTP, Exceptions.',
                        'http://img.youtube.com/vi/Nn2KQmVF5Og/0.jpg',
                        'https://www.youtube.com/watch?v=Nn2KQmVF5Og')

google_python_class_7 = media.Movie('Google Python Class, Part 7: Closing Thoughts.',
                        'Google Python Class Day 1 Part 1 Closing Thoughts.',
                        'http://img.youtube.com/vi/IcteAbMC1Ok/0.jpg',
                        'https://www.youtube.com/watch?v=IcteAbMC1Ok')

discovering_python = media.Movie('Discovering Python',
                        'What happens when you lock a Python programmer in a secret vault containing 1.5 TBytes of C++ source code and no internet connection?',
                        'http://img.youtube.com/vi/RZ4Sn-Y7AP8/0.jpg',
                        'https://youtu.be/RZ4Sn-Y7AP8')

movies = [discovering_python, google_python_class_1, google_python_class_2, google_python_class_3, google_python_class_4, google_python_class_5, google_python_class_6, google_python_class_7]
fresh_tomatoes.open_movies_page(movies)
