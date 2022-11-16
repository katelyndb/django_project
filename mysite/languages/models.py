from django.db import models
# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.FilePathField(path="/img")
    syntax = models.TextField()
    history = models.TextField()
    rating_reasoning = models.TextField()
    example = models.TextField()
    rating_choice = (
    (1, "Top Tier"),
    (2, "Mid Tier"),
    (3, "Low Tier"),
  )
    rating = models.CharField(max_length=1, choices=rating_choice)
    @classmethod
    def create(cls, name,description,image,syntax,history,rating_reasoning,example,rating):
        created_lang = cls(name=name,description=description,image=image,syntax=syntax,history=history,rating_reasoning=rating_reasoning,example=example,rating=rating)
        # do something with the book
        return created_lang

'''
#Creates the languages in the database
language = Language.create("Python",
"High level programming language with easy readability and is extremely popular.",
"python.png","Python does not use brackets or keywords, instead it uses indentation. It is case sensitive and the assignment statement is an '='.",
"Python was first released in 1991",
"I've spent the most time programming in Python and it was an approachable language to start with.",
"<span class='colored_code'> text </span> = 'Hello World' <br> print(<span class='colored_code'>text</span>)",
1)
language = Language.create("SQL",
"AKA Structured Query Language. It is used for managing data in relational databases.",
"sql.png",
"This languages uses Expressions, Clauses, Queries, and Statements.",
"SQL first appeared in 1974",
"I enjoyed working with databases and this language made a lot of initial sense to me. Now I can use it in other projects easily which is very useful",
"SELECT firstname <br> FROM client <br> WHERE lastname = 'Johnson'",
1)
language = Language.create("Javascript",
"High level programming language often used in Web Development alongside HTML.",
"js.png",
"All statements in Javascript must end with a semicolon. In this language variables are declared using the keywords let, const, and var.",
"Javascript first appeared in 1995",
"I have used this language often in my position at Brigham Young University Idaho and it is very useful.",
 "let <span class='colored_code'>text </span> = 'Hello World'; <br> console.log(<span class='colored_code'>text</span>);",
 2)
language = Language.create("PHP",
"PHP stands for Hypertext Preprocessor. It is usually used on web servers.",
"php.png",
"PHP can be interpreted in HTML documents by using delimiters, '<?php' and '?>'. Variables are declared with a '$' and statements in PHP must end with a semicolon.",
"PHP first appeared in 1995",
"I really enjoyed using this language in my backend web classes. I also felt like I was able to learn this language very quickly with my experience with Javascript and Python.",
 "<?php <br> <span class='colored_code'>$text</span> = 'Hello World' <br> echo <span class='colored_code'>$text </span><br> ?>",
 2)
 '''




    