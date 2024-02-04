# book it
#### Video Demo: https://youtu.be/qXxA4oaRb2I
#### Description:
'book it' is a web app for a school that offers primay dance classes to handle or manage enrolments. in 'book it' a parent can register and book classe for their child. Right now, it only assumes one email address per parent-student.

**app.py**
1. Contains functions:
    - register: It requires that user enters the first and last name of student, their name (parent/guardian), email address, password and confirmation. Will present different error message depending on issue. Will return message if name fields are empty, if email is already registered, if password field is empty, if password and confirmation do not match. Passwords are hashed before storing to gds.db (more on this on gds.db section). After successful registration, user is logged in.
    - login: Requires that user enter email address and password to log in. Will return error if user did not enter email and/or password. Checks the database for the email address and if password is correct and set session id as user id.
    - logout: Forgets user and redirect user to index.
    - home: Query database to get the parent or guardian name for greeting. Will show any upcoming classes if there is any. Otherwise will show 'no upcoming classes'.
    - book: Handles 



