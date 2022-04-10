# BookFace

Application imitating basic facebook-like features. Developed for uni Flask class.

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
   - hide all posts feature
   - show posts button which redirects to post board with filtered posts of this user
8. Main page
   - Sign in to access information
   - Typical landing page with sign in / sign up buttons
9. Blocked user page
   - information about being blocked
   - some form to contact page administrators?
