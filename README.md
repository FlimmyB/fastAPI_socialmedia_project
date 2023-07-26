
# fastAPI Social media app!
== 
This app lets you register and authentificate. You can create posts, edit or delete them. This app is a test fastAPI social media app.

# Installation:

1) Install the requirements
2) This app uses postgreSQL database. To connect to your database, enter the required information into the .env file
3) run `alembic init`
4) run `alembic revision --autogenerate -m "Initial migration"
5) run `alembic upgrade head`
6) Enter the src directory by running `cd src`
7) Now you can start the app by running `uvicorn run main.py:app --reload`
8) Succes! Your fastAPI server is up and runnig!

