<div align="center">
<img src="static/images/NotInkLogo.png" alt="NotInk Logo" style="height: 90px; display: block; margin: 0 auto"/>
<h1>NotInk</h1>
</div>

NotInk is a beautiful and easy to use online tool that helps you document your day and helps you to write notes

# NotInk Preview

![NotInk_Home_Page](static/images/NotInk_HomePage.jpg)
![NotInk_Detail_Page](static/images/NotInk_DetailPage.jpg)

# Guidelines on how to run locally 💻

## Clone this repository

```
git clone https://github.com/DanAdewole/NotInk.git
```

## Change Directory
Change your directory to where you cloned the repository
```
cd NotInk
```

## Create a virtual environment in the NotInk Directory
Ensure you are in the NotInk directory, run this command to create a virtual environment
```
python -m venv .\venv
```

## Activate the virtual environment
Activate the virtual environment using the following command:
```
venv\scripts\activate
```
Note: Upon running the command **venv\scripts\activate**, if this error shows up:
```
venv\scripts\activate : File C:\Users\Training\Documents\New folder\venv\scripts\Activate.ps1 cannot be loaded because running scripts is 
disabled on this system. For more information, see about_Execution_Policies at http://go.microsoft.com/fwlink/?LinkID=135170.
```
Run this command: 
``` 
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted 
```
Then run the command to activate the virtual environment

## Install all necessary packages
```
pip install -r requirements.txt
```

## Update the database
Copy this snippet and replace it with the database configuration settings in **notink_project/settings.py**, or if you are familiar with Postgres, create a new database and connect it to the app
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## Make migrations
Run the following commands separately to make migrations
```
python manage.py makemigrations
python manage.py migrate
```

## Create a new superuser
Run hte following command to create a new superuser
```
python manage.py createsuperuser
```

## Update debug settings in the project settings file
Go to **notink_project/settings.py** and change DEBUG to True
```
DEBUG = True
```

## Run the project
```
python manage.py runserver
```

# Contribution
Are you interested in making any contributions to the project? See [contibution.md](CONTRIBUTING.md) to get started. If you love this project, kindly give it a star ⭐ and share it with others. 😃

# License
This project is under an [MIT LICENSE](LICENSE)
