# Project Name

This project tailors a users resume based on the the job description provided and it sends an email with the google doc link of the resume

## Features

- You can create new users and add a resume to their account
- Got to the specific user using the user ID and create a tailored for them.

## How to Run
Please create a .env file and add credentials for the email sender and recepient of your choice
Thsi project requires google doc api authentication which can be found in the google doc api site  (https://developers.google.com/workspace/docs/api/reference/rest)

```bash
# example command to run your project
cd into the backend folder and run 
python manage.py runserver 
the path to tailor the resume is "api/users/<uuid:id>/tailor"
