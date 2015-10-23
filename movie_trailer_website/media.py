"""
This module provides classes to store media-related information.
"""

#------------------------------------------------------------------------------
#
# Sources & References:
#
# Info on args and kwargs taken from:
# http://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/
#
# Pylint: http://www.pylint.org/, http://docs.pylint.org/faq.html
#
#------------------------------------------------------------------------------

class Movie(object):
    """
    A class to store movie-related information.

    Attributes:
        title (str): The title of the movie.
        storyline (str): A brief summary of the movie.
        poster_image_url (str): URL to the movie's poster image.
        trailer_youtube_url (str): Movie trailer's URL on YouTube.
        release_date (Date): The movie's release date.
        cast (str): The movie's leading cast members.
        director (str): The movie's director.
        duration_mins (int): The movie's duration (in mins).
        genre (str): The movie's genre.
        rating (str): The movie's rating.
    """

    def __init__(self, title, storyline, poster_image_url,
                 trailer_youtube_url, release_date, **kwargs):
        """
        Initializes Movie with supplied argument values.

        Args:
            title (str): The title of the movie.
            storyline (str): A brief summary of the movie.
            poster_image_url (str): URL to the movie's poster image.
            trailer_youtube_url (str): Movie trailer's URL on YouTube.
            release_date (Date): The movie's release date.
            **kwargs: Optional keyword args for other class attributes.

        """
        # Required attributes
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date

        # Optional attributes, specified via kwargs
        self.cast = kwargs.get('cast') or ''
        self.director = kwargs.get('director') or ''
        self.duration_mins = str(kwargs.get('duration_mins'))\
            if kwargs.get('duration_mins') is not None else '0'
        self.genre = kwargs.get('genre') or ''
        self.rating = kwargs.get('rating') or ''

    def print_info(self):
        """A simple method to print movie information."""
        print "MOVIE INFORMATION:"
        print "  - Title: " + self.title
        print "  - Storyline: " + self.storyline
        print "  - Poster Image URL: " + self.poster_image_url
        print "  - Trailer URL: " + self.trailer_youtube_url
        print "  - Release Date: " + self.release_date.strftime("%B %d, %Y")
        print "  - Cast: " + self.cast
        print "  - Director: " + self.director
        print "  - Duration: " + str(self.duration_mins) + " min"
        print "  - Genre: " + self.genre
        print "  - Rating: " + self.rating
        return ""
