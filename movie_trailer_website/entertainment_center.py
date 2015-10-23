"""
This module contains a list of movies and logic to trigger opening the
Fresh Tomatoes Movie Trailer page.
"""

#------------------------------------------------------------------------------
#
# Developer Notes:
#
# Even though media.Movie only requires some arguments, I have included all
# optional arguments (kwargs) as well for the sake of consistency in the
# rendered HTML page. However, the logic in the media.Movie class is set up
# to use default values for missing arguments, and the fresh_tomatoes.py file
# is set up to show/hide only included information for each movie object.
#
# I have also included each Movie object in no particular order in the list of
# ALL_MOVIES to show the ability to sort the list alphabetically. I have also
# chosen to populate the ALL_MOVIES list with inline media.Movie instances
# rather than creating a bunch of instance variables of each movie separately,
# and then populating the ALL_MOVIES list with the instance variables.
#
#------------------------------------------------------------------------------

from datetime import date

import fresh_tomatoes
import media


ALL_MOVIES = [
    media.Movie(
        title="The Shawshank Redemption",
        storyline="Two imprisoned men bond over a number of years, finding "\
        "solace and eventual redemption through acts of common decency.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=6hB3S9bIaco",
        release_date=date(1994, 10, 14),
        cast="Tim Robbins, Morgan Freeman",
        director="Frank Darabont",
        duration_mins=142,
        genre="Crime, Drama",
        rating="R"
    ),
    media.Movie(
        title="The Count of Monte Cristo",
        storyline="A young man, falsely imprisoned by his jealous "\
        "\"friend,\" escapes and uses a hidden treasure to exact his revenge.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTg2MTQwMDk4OF5BMl5BanBnXkFtZTYwNzM4NTA5._V1_SY317_CR7,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=L5kCGkvCKpk",
        release_date=date(2002, 1, 25),
        cast="Jim Caviezel, Guy Pierce",
        director="Kevin Reynolds",
        duration_mins=131,
        genre="Action, Adventure, Drama",
        rating="PG-13"
    ),
    media.Movie(
        title="Man of Steel",
        storyline="Clark Kent, one of the last of an extinguished race "\
        "disguised as an unremarkable human, is forced to reveal his "\
        "identity when Earth is invaded by an army of survivors who threaten "\
        "to bring the planet to the brink of destruction.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjI5OTYzNjI0Ml5BMl5BanBnXkFtZTcwMzM1NDA1OQ@@._V1_SY317_CR1,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=T6DJcgm3wNY",
        release_date=date(2013, 6, 14),
        cast="Henry Cavill, Amy Adams",
        director="Zack Snyder",
        duration_mins=143,
        genre="Action, Adventure, Fantasy",
        rating="PG-13"
    ),
    media.Movie(
        title="Singin' in the Rain",
        storyline="A silent film production company and cast make a "\
        "difficult transition to sound.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTUxMTIyNTI4Nl5BMl5BanBnXkFtZTcwNTk1ODQyMg@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=36QiuRc_3I8",
        release_date=date(1952, 4, 11),
        cast="Gene Kelly, Donald O'Connor, Debbie Reynolds",
        director="Stanley Donen, Gene Kelly",
        duration_mins=103,
        genre="Comedy, Musical, Romance",
        rating="G"
    ),
    media.Movie(
        title="The Godfather",
        storyline="The aging patriarch of an organized crime dynasty "\
        "transfers control of his clandestine empire to his reluctant son.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=sY1S34973zA",
        release_date=date(1972, 3, 24),
        cast="Marlon Brando, Al Pacino",
        director="Francis Ford Coppola",
        duration_mins=175,
        genre="Crime, Drama",
        rating="R"
    ),
    media.Movie(
        title="Forrest Gump",
        storyline="Forrest Gump, while not intelligent, has accidentally "\
        "been present at many historic moments, but his true love, Jenny "\
        "Curran, eludes him.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTQwMTA5MzI1MF5BMl5BanBnXkFtZTcwMzY5Mzg3OA@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=uPIEn0M8su0",
        release_date=date(1994, 7, 6),
        cast="Tom Hanks, Robin Wright, Gary Sinise",
        director="Robert Zemeckis",
        duration_mins=142,
        genre="Drama, Romance",
        rating="PG-13"
    ),
    media.Movie(
        title="The Incredibles",
        storyline="A family of undercover superheroes, while trying to live "\
        "the quiet suburban life, are forced into action to save the world.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTY5OTU0OTc2NV5BMl5BanBnXkFtZTcwMzU4MDcyMQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=eZbzbC9285I",
        release_date=date(2004, 11, 5),
        cast="Craig T. Nelson, Samuel L. Jackson, Holly Hunter",
        director="Brad Bird",
        duration_mins=115,
        genre="Animation, Action, Adventure",
        rating="PG"
    ),
    media.Movie(
        title="Ratatouille",
        storyline="A rat who can cook makes an unusual alliance with a young "\
        "kitchen worker at a famous restaurant.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTMzODU0NTkxMF5BMl5BanBnXkFtZTcwMjQ4MzMzMw@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=1yKqLNnxGZw",
        release_date=date(2007, 6, 29),
        cast="Brad Garrett, Lou Romano, Patton Oswalt",
        director="Brad Bird, Jan Pinkava",
        duration_mins=111,
        genre="Animation, Comedy, Family",
        rating="G"
    ),
    media.Movie(
        title="Chef",
        storyline="A chef who loses his restaurant job starts up a food "\
        "truck in an effort to reclaim his creative promise, while piecing "\
        "back together his estranged family.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTY5NTYzNTA1M15BMl5BanBnXkFtZTgwODIwODU1MTE@._V1_SY317_CR1,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=wgFws3AoIUY",
        release_date=date(2014, 5, 30),
        cast="Jon Favreau, Robert Downey Jr., Scarlett Johansson",
        director="Jon Favreau",
        duration_mins=114,
        genre="Adventure, Comedy, Drama",
        rating="R"
    ),
    media.Movie(
        title="What Happens in Vegas",
        storyline="A man and a woman are compelled, for legal reasons, to "\
        "live life as a couple for a limited period of time. At stake is a "\
        "large amount of money.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTIxNzMwOTU3OF5BMl5BanBnXkFtZTcwMzk0NTM2MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=YJGAsbcfuRs",
        release_date=date(2008, 5, 9),
        cast="Cameron Diaz, Ashton Kutcher",
        director="Tom Vaughan",
        duration_mins=99,
        genre="Comedy, Romance",
        rating="PG-13"
    ),
    media.Movie(
        title="The Internship",
        storyline="Two salesmen whose careers have been torpedoed by the "\
        "digital age find their way into a coveted internship at Google, "\
        "where they must compete with a group of young, tech-savvy geniuses "\
        "for a shot at employment.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjM1MzczMDgwOV5BMl5BanBnXkFtZTcwMDM4NjM2OQ@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=cdnoqCViqUo",
        release_date=date(2013, 6, 7),
        cast="Vince Vaughn, Owen Wilson",
        director="Shawn Levy",
        duration_mins=119,
        genre="Comedy",
        rating="PG-13"
    ),
    media.Movie(
        title="The Intern",
        storyline="70-year-old widower Ben Whittaker has discovered that "\
        "retirement isn't all it's cracked up to be. Seizing an opportunity "\
        "to get back in the game, he becomes a senior intern at an online "\
        "fashion site, founded and run by Jules Ostin.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTUyNjE5NjI5OF5BMl5BanBnXkFtZTgwNzYzMzU3NjE@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=ZU3Xban0Y6A",
        release_date=date(2015, 9, 25),
        cast="Robert DeNiro, Anne Hathaway",
        director="",
        duration_mins=121,
        genre="Comedy",
        rating="PG-13"
    ),
    media.Movie(
        title="Casino Royale",
        storyline="Armed with a license to kill, Secret Agent James Bond "\
        "sets out on his first mission as 007 and must defeat a weapons "\
        "dealer in a high stakes game of poker at Casino Royale, but things "\
        "are not what they seem.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTM5MjI4NDExNF5BMl5BanBnXkFtZTcwMDM1MjMzMQ@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=xK7PbujRUOk",
        release_date=date(2006, 11, 17),
        cast="Daniel Craig, Eva Green",
        director="Martin Campbell",
        duration_mins=144,
        genre="Action, Adventure, Thriller",
        rating="PG-13"
    ),
    media.Movie(
        title="Miracle",
        storyline="Miracle tells the true story of Herb Brooks (Russell), "\
        "the player-turned-coach who led the 1980 U.S. Olympic hockey team "\
        "to victory over the seemingly invincible Russian squad.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjEyOTk1OTcyNV5BMl5BanBnXkFtZTYwNjMzNDU3._V1_SY317_CR0,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=v64ofT1rGOw",
        release_date=date(2004, 2, 6),
        cast="Kurt Russell, Patricia Clarkson",
        director="Gavin O'Connor",
        duration_mins=135,
        genre="Biography, Drama, History",
        rating="PG"
    ),
    media.Movie(
        title="No Reservations",
        storyline="The life of a top chef changes when she becomes the "\
        "guardian of her young niece.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTI1NzQ5MzU1OV5BMl5BanBnXkFtZTcwNzExODU0MQ@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=Xy3rdEl0Zro",
        release_date=date(2007, 7, 27),
        cast="Catherine Zeta-Jones, Aaron Eckhart, Abigail Breslin",
        director="Scott Hicks",
        duration_mins=104,
        genre="Comedy, Drama, Romance",
        rating="PG"
    ),
    media.Movie(
        title="Ocean's Eleven",
        storyline="Danny Ocean and his eleven accomplices plan to rob three "\
        "Las Vegas casinos simultaneously.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTY0Mzg4MzgwN15BMl5BanBnXkFtZTgwNDk0MzkxMDE@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=ImMGNQ2OEjo",
        release_date=date(2001, 12, 7),
        cast="George Clooney, Brad Pitt, Julia Roberts",
        director="Steven Soderbergh",
        duration_mins=116,
        genre="Crime, Thriller",
        rating="PG-13"
    ),
    media.Movie(
        title="Fun with Dick and Jane",
        storyline="When an affluent couple lose all their money following a "\
        "series of blunders, they turn to a life of crime to make ends meet.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjE2NzE5MDI4NV5BMl5BanBnXkFtZTcwODYxOTYzMQ@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=4lp6_ySTsQQ",
        release_date=date(2005, 12, 21),
        cast="Jim Carrey, Tea Leoni, Alec Baldwin",
        director="Dean Parisot",
        duration_mins=90,
        genre="Comedy, Crime",
        rating="PG-13"
    ),
    media.Movie(
        title="Back to the Future",
        storyline="A young man is accidentally sent 30 years into the past "\
        "in a time-traveling DeLorean invented by his friend, Dr. Emmett "\
        "Brown, and must make sure his high-school-age parents unite in "\
        "order to save his own existence.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjA5NTYzMDMyM15BMl5BanBnXkFtZTgwNjU3NDU2MTE@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=qvsgGtivCgs",
        release_date=date(1985, 4, 3),
        cast="Michael J. Fox, Christopher Lloyd, Lea Thompson",
        director="Robert Zemeckis",
        duration_mins=116,
        genre="Adventure, Comedy, Sci-Fi",
        rating="PG"
    ),
    media.Movie(
        title="Hitch",
        storyline="While helping his latest client woo the fine lady of his "\
        "dreams, a professional \"date doctor\" finds that his game doesn't "\
        "quite work on the gossip columnist with whom he's smitten.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BNzYyNzM2NzM2NF5BMl5BanBnXkFtZTcwNjg5NTQzMw@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=C9yBwqumFtI",
        release_date=date(2005, 2, 11),
        cast="Will Smith, Eva Mendes, Kevin James",
        director="Any Tennant",
        duration_mins=118,
        genre="Comedy, Romance",
        rating="PG-13"
    ),
    media.Movie(
        title="The Thomas Crown Affair",
        storyline="A very rich and successful playboy amuses himself by "\
        "stealing artwork, but may have met his match in a seductive "\
        "detective.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTI0MzE4ODU0OF5BMl5BanBnXkFtZTYwMTQ4MDk5._V1_SY317_CR0,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=B3AlaszZSJU",
        release_date=date(1999, 8, 6),
        cast="Pierce Brosnan, Rene Ruso, Denis Leary",
        director="John McTiernan",
        duration_mins=113,
        genre="Crime, Romance, Thriller",
        rating="R"
    ),
    media.Movie(
        title="Ironman",
        storyline="After being held captive in an Afghan cave, an "\
        "industrialist creates a unique weaponized suit of armor to fight "\
        "evil.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=8hYlB38asDY",
        release_date=date(2008, 5, 2),
        cast="Robert Downey Jr., Gweneth Paltrow, Terrence Howard",
        director="Jon Favreau",
        duration_mins=126,
        genre="Action, Adventure, Sci-Fi",
        rating="PG-13"
    ),
    media.Movie(
        title="Jobs",
        storyline="The story of Steve Jobs' ascension from college dropout "\
        "into one of the most revered creative entrepreneurs of the 20th c"\
        "entury.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTM5NTQ3MTYxN15BMl5BanBnXkFtZTcwODE2Nzk3OQ@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=FrvkCS0ZGPU",
        release_date=date(2013, 8, 16),
        cast="Ashton Kutcher, Dermot Mulroney",
        director="Joshua Michael Stern",
        duration_mins=128,
        genre="Biography, Drama",
        rating="PG-13"
    ),
    media.Movie(
        title="Star Trek",
        storyline="The brash James T. Kirk tries to live up to his father's "\
        "legacy with Mr. Spock keeping him in check as a vengeful, "\
        "time-traveling Romulan creates black holes to destroy the "\
        "Federation one planet at a time.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjE5NDQ5OTE4Ml5BMl5BanBnXkFtZTcwOTE3NDIzMw@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=3PM1pvOzn_w",
        release_date=date(2009, 5, 8),
        cast="Chris Pine, Zachary Quinto",
        director="J.J. Abrams",
        duration_mins=127,
        genre="Action, Adventure, Sci-Fi",
        rating="PG-13"
    ),
    media.Movie(
        title="Failure to Launch",
        storyline="A thirtysomething slacker suspects his parents of setting "\
        "him up with his dream girl so he'll finally vacate their home.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMTg0OTc2MDQ3NV5BMl5BanBnXkFtZTcwNDUwMjEzMw@@._V1_SX214_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=4KZM3PRV0NM",
        release_date=date(2006, 3, 10),
        cast="Matthew McConaughey, Sarah Jessica Parker",
        director="Tom Dey",
        duration_mins=97,
        genre="Comedy, Romance",
        rating="PG-13"
    ),
    media.Movie(
        title="How to Lose a Guy in 10 Days",
        storyline="Benjamin Barry is an advertising executive and ladies' "\
        "man who, to win a big campaign, bets that he can make a woman fall "\
        "in love with him in 10 days. Andie Anderson covers the \"How To\" "\
        "beat for \"Composure\" magazine and is assigned to write an article "\
        "on \"How to Lose a Guy in 10 days.\" They meet in a bar shortly "\
        "after the bet is made.",
        poster_image_url="http://ia.media-imdb.com/images/M/MV5BMjE4NTA1NzExN15BMl5BanBnXkFtZTYwNjc3MjM3._V1_SY317_CR0,0,214,317_AL_.jpg",
        trailer_youtube_url="https://www.youtube.com/watch?v=EFGr2_cOOTk",
        release_date=date(2003, 2, 7),
        cast="Kate Hudson, Matthew McConaughey",
        director="Donald Petrie",
        duration_mins=116,
        genre="Comedy, Romance",
        rating="PG-13"
    )
]


def create_movies():
    """Function to trigger and open the Movie Trailer page."""

    # Sorting all_movies by title, and replacing "The" from the titles so
    # they are ordered without the leading "The" in affected titles.
    fresh_tomatoes.open_movies_page(
        sorted(ALL_MOVIES, key=lambda t: t.title.lower().replace("the ", ""))
    )


if __name__ == '__main__':
    create_movies()
