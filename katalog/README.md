[Heroku Catalog App](https://catalog-assignment2.herokuapp.com/katalog/)
1. Models --> Views --> urls -->HTML
2. A virtual environment is used to execute the django application. It is also used to manage
	python packages for different projects so python doesnt download a package globally and
	clash with other projects. Yes you can create a django app without venv but it is not recommended to do so.
3. I finished and copied the steps from lab 1
	the steps are as followed:
		-copy the template repo
		-initializ a virtual environment and run it
		-install the requirement with pi
		-made migrations then loaded the catalog data
		-added several lines to the HTML used for iterating the catalog data
		-made a function on views to render to an HTML, imported the catalog from models, and added context and
			catalog items to the function
		-routed the views function in urls
		-added,commited, and pushed all changes to github
		-made a new app on heroku, added the api key and app name to github secrets, deployed the app.