#-----------------------------------------------------------------------
# Pylint in Makefile: http://stackoverflow.com/a/23140239/1914233
#-----------------------------------------------------------------------
lint:
	@for py in movie_trailer_website/*.py; \
	do \
		echo "Linting File: $$py";\
		pylint --rcfile=config.pylintrc $$py; \
	done

launch: movie_trailer_website;
	python movie_trailer_website