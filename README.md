My first Django Project made in my education period.

Project have custom APP - blogapp
blogapp have models:
-Category
-Tag
-Post

Category have name, desc(description)
Tag have name only
Post have name, text, date of: created, updated, category and tags

blogapp also have django managment commands (python manage.py <command>):
-clear_db: clears all(by blogapp models) tables in DB
-fill_db: fill small amount of data to test DB
