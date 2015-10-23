# Udacity Movie Trailer Website
Repository for the Movie Trailer Website project for the [Udacity Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Generating and Viewing the Website
To view and run this project, you will need to do the following:

1. Make sure you have [Python](https://www.python.org/) installed.
2. Clone the repository: `git clone https://github.com/hessler/udacity-movie-trailer-website.git`.
3. Navigate to the cloned repository directory. For example, if you cloned to your Desktop on a Mac: `cd ~/Desktop/udacity-movie-trailer-website/`.
4. Generate and launch the website:
    - Using Makefile: `make launch`, or
    - By triggering the module: `python movie_trailer_website`

## Pylint
If you would like to run a lint check on the project files to ensure code quality, please follow these steps:

1. Install [Pylint](http://www.pylint.org/).
2. Navigate to the cloned repository directory `udacity-movie-trailer-website`.
3. Run the lint command:
    - Using Makefile: `make lint`, or
    - Lint individual files:
        - `pylint --rcfile=config.pylintrc movie_trailer_website/__main__.py`
        - `pylint --rcfile=config.pylintrc movie_trailer_website/entertainment_center.py`
        - `pylint --rcfile=config.pylintrc movie_trailer_website/fresh_tomatoes.py`
        - `pylint --rcfile=config.pylintrc movie_trailer_website/media.py`
