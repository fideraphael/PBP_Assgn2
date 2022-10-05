[Heroku Watchlist App](https://pbdassignment3.herokuapp.com/mywatchlist/html/)
1.	-JSON (JavaScript Object Notation) is a lightweight data-interchange format and it completely language independent. It is based on the JavaScript programming language and easy to understand and generate.
	-XML (Extensible markup language) defines a set of rules for encoding documents in a format that is both human-readable and machine-readable made with simplicity in mind.
	-HTML (Hypertext Markup Language) is a language that is used to create the structure and content of web pages. It is typically used in conjunction with CSS (Cascading Style Sheets) to style the page, and JavaScript to add interactivity.

	○JSON & XML are data storage formats while HTML is used to show these data as web pages.
2.[Postman screenshots](https://drive.google.com/drive/folders/1HpWbvgG0u-7E3A4qQguA7ydkpA9TKzqv?usp=sharing)

[Heroku Todolist App](https://pbdassignment3.herokuapp.com/todolist)
	1. a CSRF token is an alphanumeric code or random secret value used by a specific site to avoid malicious attacks.
	2. Yes we can. we can do it by using {{ form.name_of_field }} 
	3. The user inputs data to the HTML which is then taken by my_form function in views, posted onto the database and then rendered back into the HTML.
	4. I searched around and read the given articles on how to create the foreign key and found how to add the 		user parameter to the foreign key. added all of these to models then moved on to views where i made some changes to show_todolist and created a new my_forms function used to read the data added from the HTML. The login, register, and logout functions are copied from the third lab. then i made a new html named csv-forms where the user is asked for title and description of the task and a new button on the todolist html which redirectsa the user to csv-forms. then i routed every function to a url. i pused the new changes to github, then deployed to heroku.