# book it
#### Video Demo: https://youtu.be/qXxA4oaRb2I
#### Description:
'book it' is a web app for a school that offers primay dance classes to handle or manage enrolments. in 'book it' a parent can register and book classe for their child. Right now, it only assumes one email address per parent-student.

**app.py**
1. Contains functions:
    - register: It requires that user enters the first and last name of student, their name (parent/guardian), email address, password and confirmation. Will present different error message depending on issue. Will return message if name fields are empty, if email is already registered, if password field is empty, if password and confirmation do not match. Passwords are hashed before storing into *students* table in gds.db (more on this on gds.db section). After successful registration, user is logged in.
    - login: Requires that user enter email address and password to log in. Will return error if user did not enter email and/or password. Checks the database for the email address and if password is correct and set session id as user id.
    - logout: Forgets user and redirect user to index.
    - home: Requires user is logged in. Query database to get the parent or guardian name for greeting. Will show any upcoming classes if there is any. Otherwise will show 'no upcoming classes'.
    - book: Renders book.html where user can select which class they want to book. Requires user is logged in.
    - confirm: Gets selected class after user confirms. Will check if user already booked the class by querying the database, if so, will show message 'already enrolled'. Otherwise, will try to update the *enrolments* table except if there are any errors. Requires user is logged in.
    - about: Just renders about.html.
    - change_password: Allows user to change their password. Requires that user is logged in. Requires that user enters old password and confirm the old password, then nominate a new password. If a field is empty it will show an error message. Query the database for username (or email) and checks that the password is correct. Will check if old password and confirmation matches, if not, will show an error message. If matches, will proceed to hash the new password and update the hashed password in students table.

    



