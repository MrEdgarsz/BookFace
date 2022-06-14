# BookFace

Application imitating basic facebook-like features. Developed for uni Flask class.

# Contents
1. Project structure
   1. Main functions
   2. Page concepts
2. Installation
   1. Requirements
   2. Installation in Visual Code Studio
3. Links

## Project structure

### Main functions

1. Authorization
   1. Sign Up
   2. Sign In
2. Post Board
   1. Add Post
   2. Show all posts
3. Administration
   1. Manage Users
4. Misc
   1. Blocked user page
   2. Main page (seen when user is not signed in)

### Page concepts

1. Main template:
   - Nagivation bar:
     - Logo
     - Current user name (&& ||) authorization options
     - administration panel button
   - Footer with authors and copyrights
2. Authorization options:
   - Sign in
   - Sign up
   - Logout if user is signed in
3. Sign Up
   - login
   - password
   - password_confirmation
   - `sign up` button
4. Sign In
   - login
   - password
   - `sign in` button
5. Post Board
   - add post form
   - all posts
6. Post
   - [WYSIWG post editor]("https://www.tiny.cloud/")
   - edit button:
     - remove (role specifc)
     - block user (role specific)
7. Manage users
   - Table with all users
   - Each row is a form able to edit user when you click edit button
   - edit button becomes save button when editing is enabled
   - block/unblock button
   - show posts button which redirects to post board with filtered posts of this user
8. Main page
   - Sign in to access information
   - Typical landing page with sign in / sign up buttons
9. Blocked user page
   - information about being blocked
   - some form to contact page administrators?
   - 404 page

## Installation

### Requirements

- Python
- Visual Studio Code
- Python and Pylance extensions for VSC

### Installation in Visual Code Studio

1. Open the project in VSC.
2. Open terminal `Terminal->New terminal`.
3. Install flask `pip install flask`.
4. Create a virtual python environment `python -m venv env`.
5. Activate environment in PowerShell `. ./env/Scripts/activate.ps1`.
6. Install requirements `pip install -r requirements.txt`.
7. Select previously created virtual environment as the default runtime environment for the project by using `CTRL+Shift+P`, selecting the `Select inerpreter` option and specifying the path to python - `/env/Scripts/python.exe`.
8. Run the project using console command `python app.py` or by clicking the `play` button in the top right corner of the screen.
9. Have fun!

## Links
- [Bootstrap v5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)