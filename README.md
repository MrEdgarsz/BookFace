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
   - show posts button which redirects to post board with filtered posts of this user
8. Main page
   - Sign in to access information
   - Typical landing page with sign in / sign up buttons
9. Blocked user page
   - information about being blocked
   - some form to contact page administrators?
   - 404 page


### TODO
| Finished           | Task                                                                                                                                                                                                                                         | Person        |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| :white_check_mark: | Finish authorization                                                                                                                                                                                                                         | Edgar         |
|                    | Create 404 page                                                                                                                                                                                                                              | Babcia Jadzia |
| :white_check_mark: | Add "Promote to Moderator/Administrator function"                                                                                                                                                                                            |               |
|                    | remove prefixes from routes (aka /auth/login should be just /login)                                                                                                                                                                          | Wujek Zdzichu |
| :white_check_mark: | create a first page (the one that users sees depending if he is signed in or not etc                                                                                                                                                         |               |
|                    | all function routes should be behind basic and role authorization (like /block_user)                                                                                                                                                         | Dawca         |
|                    | add a "blocked user page" that we show to a user that is blocked                                                                                                                                                                             | Stopkarz       |
| :white_check_mark: | fix page titles depending on location and current user (I would opt for just "BookFace - Lose time with your friends" everywhere                                                                                                             |               |
|                    | clean project architecture to follow the same syntax as auth (for example posts should have pages folder and store all views there)                                                                                                          | Pan Majster   |
| :white_check_mark: | Make sure that all forms properly handle errors and are informative for users                                                                                                                                                                |               |
|                    | Change all urls to some user-friendly simple urls and do more behind users back (first page should be posts automatically we don't want to redirect user and function pages aka /block_user should redirect back to page that you came from) |               |
|                    | Have Fun Coding :tada:                                                                                                                                                                                                                       | Daniel, Radek |
