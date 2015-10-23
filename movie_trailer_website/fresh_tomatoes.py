"""
This module provides logic to generate and open the Fresh Tomatoes Movie
Trailers HTML page.
"""

import os
import re
import webbrowser

# Opening of the HTML page, including styles.
MAIN_PAGE_HEAD = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
    <link href='https://fonts.googleapis.com/css?family=Bangers' rel='stylesheet' type='text/css'>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 76px;
        }
        #trailer .modal-dialog {
            height: 480px;
            margin-top: 200px;
            width: 640px;
        }
        .hanging-close {
            position: absolute;
            right: -12px;
            top: -12px;
            z-index: 9001;
        }
        #trailer-video {
            height: 100%;
            width: 100%;
        }
        #btn-snap-to-top,
        #btn-sort-movies button {
            font-weight: bold;
            margin: 15px 15px 0px 0px;
        }
        #btn-sort-movies .dropdown-menu li > a:hover,
        #btn-sort-movies .dropdown-menu li > a:focus,
        #btn-sort-movies .dropdown-submenu:hover > a {
            background-color: rgba(51, 150, 232, 0.1875);
            background-image: none;
        }
        .sort-active {
            background-color: rgba(51, 150, 232, 0.125);
            font-weight: bold !important;
        }
        #intro-info {
            border-bottom: 1px solid #dedede;
            margin-bottom: 8px;
            padding-bottom: 16px;
            padding-top: 16px;
        }
        #intro-info p {
            font-size: 16px;
        }
        .movie-tile {
            border: 1px solid transparent;
            display: inline-block !important;
            float: none;
            margin: 10px 0;
            padding: 20px;
            position: relative;
            vertical-align: top;
            width: 49.5%;
        }
        .movie-tile:hover {
            background-color: rgba(51, 150, 232, 0.125);
            border: 1px solid rgba(51, 150, 232, 0.225);
            cursor: pointer;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
            -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
            -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.15);
        }
        .movie-poster {
            padding: 0;
        }
        .movie-poster img {
            height: auto;
            padding: 0;
            width: 100%;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.425);
            -moz-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.425);
            -webkit-box-shadow: 0 1px 3px rgba(0, 0, 0, 0.425);
        }
        .movie-tile h2 {
            color: #333;
            font-size: 21px;
            font-weight: normal;
            line-height: 19px;
            margin: 0 0 6px;
        }
        .movie-tile p {
            color: #4e4e4e;
            font-size: 13px;
            margin: 2px 0;
        }
        .movie-info {
            padding: 15px;
        }
        .movie-info-lead {
            border-bottom: 1px solid #dedede;
            margin: 0 0 9px;
            padding-bottom: 3px;
        }
        .movie-release-date {
            color: #6e6e6e;
            font-size: 14px;
        }
        .movie-rating {
            background-color: white;
            border: 1px solid #bebebe;
            font-family: "Times New Roman", Times, serif;
            font-size: 15px;
            font-weight: bold;
            margin-right: 5px;
            padding: 0px 3px;
        }
        .movie-tile .movie-storyline {
            margin-bottom: 12px;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        .footer {
            background-image: -webkit-linear-gradient(top, rgb(24,24,24), rgb(44,44,44));
            background-image: -moz-linear-gradient(top, rgb(24,24,24), rgb(44,44,44));
            background-image: -ms-linear-gradient(top, rgb(24,24,24), rgb(44,44,44));
            background-image: -o-linear-gradient(top, rgb(24,24,24),rgb(44,44,44));
            filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#ff181818', endColorstr='#ff2c2c2c', GradientType=0)
            filter: progid:DXImageTransform.Microsoft.gradient(enabled=false)
            -webkit-box-shadow: 0 -1px 5px rgba(0,0,0,.125);
            box-shadow: 0 -1px 5px rgba(0,0,0,.125);
            border-top: 1px solid black;
            color: #8e8e8e;
            padding: 16px 0;
            text-align: center;
        }
        .footer p {
            margin: 0;
        }
        .footer ul {
            color: #8e8e8e;
            font-size: 24px;
            list-style-type: none;
            margin: 0;
            padding: 0;
        }
        .footer li {
            display: inline;
            list-style-type: none;
            padding: 3px;
        }
        .footer a {
            color: #8e8e8e;
        }
        #source-disclaimer {
            border-top:1px dotted #4e4e4e;
            margin-top:9px;
            padding-top:12px;
        }
        
        /* Bootstrap Overrides */
        .navbar {
            height: auto;
            min-height: auto;
        }
        .navbar-default {
            background-image: -webkit-linear-gradient(top, rgb(248,248,248), rgb(228,228,228));
            background-image: -moz-linear-gradient(top, rgb(248,248,248), rgb(228,228,228));
            background-image: -ms-linear-gradient(top, rgb(248,248,248), rgb(228,228,228));
            background-image: -o-linear-gradient(top, rgb(248,248,248),rgb(228,228,228));
            filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#fff8f8f8', endColorstr='#ffe4e4e4', GradientType=0)
            filter: progid:DXImageTransform.Microsoft.gradient(enabled=false)
            -webkit-box-shadow: 0 1px 5px rgba(0,0,0,.125);
            box-shadow: 0 1px 5px rgba(0,0,0,.125);
            border-bottom: 1px solid #c9c9c9;
        }
        .navbar-header {
            float: none;
            padding: 6px 0;
        }
        .navbar-default .navbar-brand {
            color: #4e4e4e;
            font-family: 'Bangers', 'Helvetica Neue', Helvetica, sans-serif;
            font-size: 36px;
            height: auto;
            padding-bottom: 0;
            padding-top: 0;
            text-shadow: 0 1px 0 white;
        }
        .navbar-default .navbar-brand:hover {
            color: #4e4e4e;
        }
        .navbar-default .navbar-brand:after {
            clear: both;
            content: " ";
            display: block;
            height: 0;
            visibility: hidden;
        }
        .navbar-brand img {
            height: 64px;
            margin-left: 15px;
            margin-right: 8px;
            width: auto;
        }
        .navbar-right {
            float: right !important;
        }
        #btn-sort-movies .dropdown-menu {
            left: auto;
            right: 0;
        }

        /* Media Query Overrides */
        @media (max-width: 767px) {
            body {
                padding-top: 60px;
            }
            #btn-snap-to-top,
            #btn-sort-movies button {
                margin-top: 6px;
            }
            #intro-info h1 {
                font-size: 28px;
            }
            #intro-info p {
                font-size: 14px;
            }
            .movie-tile {
                width: 100%;
            }
            .movie-poster {
                width: 25%;
            }
            .movie-info {
                width: 75%;
            }
            .navbar-default {
                margin-bottom: 0;
            }
            .navbar-default .navbar-brand {
                font-size: 24px;
            }
            .navbar-brand img {
                height: 48px;
                margin-right: 6px;
            }
        }
        @media (max-width: 480px) {
            body {
                padding-top: 48px;
            }
            #btn-snap-to-top,
            #btn-sort-movies button {
                font-size: 12px;
                margin: 4px 10px 0 0;
                padding-bottom: 4px;
                padding-top: 4px;
            }
            .movie-tile {
                width: 100% !important;
            }
            .navbar-default .navbar-brand {
                font-size: 16px;
            }
            .navbar-brand img {
                height: 36px;
                margin-left: 0;
                margin-right: 4px;
            }
            .hide-for-small {
                display: none;
            }
        }
        @media (max-width: 420px) {
            .movie-tile {
                margin: 0 auto;
                width: 100% !important;
            }
            .movie-info,
            .movie-poster {
                width: 100% !important;
            }
        }

    </style>
</head>
'''


# The main HTML page layout and content, including scripts.
MAIN_PAGE_CONTENT = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&amp;h=24" alt="Close"/>
                </a>
                <div class="scale-media" id="trailer-video-container">
                </div>
            </div>
        </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
        <div class="navbar navbar-default navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <div class="navbar-brand"><img src="data:image/png;base64,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" alt="Fresh Tomatoes Movie Trailers" />Fresh Tomatoes Movie Trailers</div>
                    <div class="navbar-right">
                        <!--<button id="btn-snap-to-top" class="btn btn-default navbar-btn" style="display:none;"><span class="hide-for-small">Top </span><i class="fa fa-caret-up"></i></button>-->
                        <div id="btn-sort-movies" class="btn-group">
                            <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                Sort <!--<span id="sort-button-value">Title</span>--><span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu">
                                <li><a href="#" class="sort-by sort-active" data-sort="title">Title</a></li>
                                <li><a href="#" class="sort-by" data-sort="release_date">Release Date</a></li>
                                <li><a href="#" class="sort-by" data-sort="duration_mins">Duration</a></li>
                                <li><a href="#" class="sort-by" data-sort="rating">Rating</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div id="intro-info" class="container">
        <div class="col-md-12">
            <h1>Fresh 25 Movies</h1>
            <p>From classics to recent films, dramas to comedies, this is a list of 25 of my favorite movies. You can browse the list to learn more about each film, and even watch the theatrical trailers by clicking on one of the movie tiles. Enjoy!</p>
        </div>
    </div>

    <div id="movie-tile-container" class="container">
        {movie_tiles}
    </div>

    <footer class="footer">
        <div class="container">
            <div class="footer-info">
                <p>A Udacity Project by Anthony Hessler</p>
                <ul>
                    <li><a href="https://www.github.com/hessler" title="Fork me on GitHub" target="_blank"><i class="fa fa-github-square"></i></a></li>
                    <li><a href="https://www.twitter.com/hessler" title="Follow @hessler on Twitter" target="_blank"><i class="fa fa-twitter-square"></i></a></li>
                    <li><a href="http://gplus.to/hessler" title="Connect with me on Google+" target="_blank"><i class="fa fa-google-plus-square"></i></a></li>
                    <li><a href="http://www.linkedin.com/in/anthonyhessler" title="Connect with me on LinkedIn" target="_blank"><i class="fa fa-linkedin-square"></i></a></li>
                </ul>
            </div>
        </div>
        <div id="source-disclaimer" class="container">
            <p><em>Movie information, including poster images and descriptions, courtesy of <a href="http://www.imdb.com/" title="IMDb - Movies, TV and Celebrities" target="_blank">IMDb</a>.</em></p>
        </div>
    </footer>

    <script type="text/javascript">

        var allMovies = [{all_movies}],
            sortedBy = "title";

        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {{
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        }});

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {{
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {{
                'id': 'trailer-video',
                'type': 'text-html',
                'src': sourceUrl,
                'frameborder': 0
            }}));
        }});

        // Scroll handler for "top" link
        function onScroll(event) {{
            if (window.pageYOffset >= 150) {{
                $("#btn-snap-to-top").show();
            }} else {{
                $("#btn-snap-to-top").hide();
            }}
        }}

        // Custom sort method to sort array by key value.
        // Source: http://stackoverflow.com/a/16648532/1914233
        Array.prototype.sortOn = function(key) {{
            this.sort(function(a, b) {{
                if (a[key] < b[key]) {{
                    return -1;
                }} else if (a[key] > b[key]) {{
                    return 1;
                }}
                return 0;
            }});
        }}

        // Sort movie tiles by given movie attribute and re-populate tiles onto page.
        function sortMovies(sortKey) {{
            if (sortKey !== sortedBy) {{
                sortedBy = sortKey;
                allMovies.sortOn(sortKey);
                content = "";
                for (var i = 0; i < allMovies.length; i += 1) {{
                    content += document.getElementById(allMovies[i]['movie_tile_id']).outerHTML;
                }}
                $("#movie-tile-container").html(content);
            }}
        }}

        // Initial actions and setup when the page loads
        $(document).ready(function () {{
            $("#btn-snap-to-top").on('click', function (event) {{
                $('html,body').animate({{
                    scrollTop: 0
                }}, 1000);
            }});
            $(".sort-by").on('click', function (event) {{
                //$("#sort-button-value").html($(this).html());
                $(".sort-by").each(function() {{
                    $(this).removeClass("sort-active");
                }});
                $(this).addClass("sort-active");
                sortMovies($(this).data("sort"));
            }});
            //window.addEventListener("scroll", onScroll);
        }});

    </script>

  </body>
</html>
'''


# A single movie entry html template
MOVIE_TILE_CONTENT = '''
        <div id="{movie_tile_id}" title="Watch the trailer for {movie_title} &rtrif; " class="col-md-6 col-lg-6 col-sm-6 col-xs-12 movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
            <div class="movie-poster col-md-5 col-sm-5 col-xs-12"><img src="{poster_image_url}" alt="{movie_title}" /></div>
            <div class="movie-info col-md-7 col-sm-7 col-xs-12">
                <div class="movie-info-lead">
                    <h2><strong>{movie_title}</strong> <span class="movie-release-date">({release_date_year})</span></h2>
                    <p>{rating} {duration_mins}</p>
                    <p><em>{genre}</em></p>
                </div>
                <p class="movie-storyline">{storyline}</p>
                {director}
                {cast}
            </div>
        </div>
'''


# A single JavaScript object entry template
JS_MOVIE_OBJECT_CONTENT = '''
{{movie_tile_id: "{movie_tile_id}", title: "{movie_title}", release_date: {movie_release_date}, duration_mins: {movie_duration_mins}, genre: "{movie_genre}", rating: "{movie_rating}"}},
'''


def create_movie_tiles_content(movies):
    """
    Function to generate content for movie tiles for the HTML page.

    Args:
        movies (List[Movie]): A list of Movie objects.

    Returns:
        String of HTML content for Movie objects in the supplied list.
    """

    # The HTML content
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in.
        content += MOVIE_TILE_CONTENT.format(

            # Movie tile id, used for JS sort logic. Remove non-alphanumeric
            # characters and convert to lowercase.
            movie_tile_id=re.sub('[^0-9a-zA-Z]+', '', movie.title).lower(),

            # Required attributes. These will always be present.
            movie_title=movie.title,
            storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            release_date=movie.release_date,

            # Create separate item for release date year
            release_date_year=movie.release_date.year,

            # Optional attributes. Note some of these use conditional checks to
            # set their values so style-specific items don't show up if blank.
            genre=movie.genre,
            cast='<p><strong>Cast:</strong> ' + movie.cast + '</p>'\
                if movie.cast else '',
            director='<p><strong>Director:</strong> ' + movie.director + \
                '</p>' if movie.director else '',
            duration_mins=movie.duration_mins + ' min'\
                if movie.duration_mins != '0' else '',
            rating='<span class="movie-rating">' + movie.rating + '</span>'\
                if movie.rating else ''
        )
    return content


def create_js_movie_content(movies):
    """
    Function to create JavaScript content for the HTML page.

    Args:
        movies (List[Movie]): A list of Movie objects.

    Returns:
        String of JavaScript content to be added to the HTML page.
    """

    # The JS content for the JS allMovies array of movie objects.
    # For movie_tile_id, use RegEx to strip non-alphanumeric characters for
    # safe "id" attribute value. For movie_title, strip out leading "the" if
    # found (for alphabetical sort).
    content = ''
    for movie in movies:
        content += JS_MOVIE_OBJECT_CONTENT.format(
            movie_tile_id=re.sub('[^0-9a-zA-Z]+', '', movie.title).lower(),
            movie_title=movie.title if movie.title.lower().find("the ") < 0\
                else movie.title[4:],
            movie_release_date=movie.release_date,
            movie_duration_mins=movie.duration_mins,
            movie_genre=movie.genre,
            movie_rating=movie.rating
        )
    return content


def open_movies_page(movies):
    """
    Function to generate and open the main HTML page for Fresh Tomatoes
    Movie Trailers.

    Args:
        movies (List[Movie]): A list of Movie objects.
    """

    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies),
        all_movies=create_js_movie_content(movies))

    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    output_file.close()

    # Open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
