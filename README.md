![Coolpress Tests](https://github.com/tuxskar/coolpress/actions/workflows/django.yml/badge.svg)


# CoolPress Project
Hey, It's **Nikolai**

CoolPress is an application to show the power of web development using Django

In order to create the project install django (or all the requirements of the project) and run:

```bash
django-admin startproject coolpress
```

## Create the superuser

Run the command:
```
python manage.py createsuperuser
```

Fill the questions to create a user and password for the super user that can access all the system.


## Run the server:

Execute the command
````bash
python manage.py runserver
````
And enter into: http://localhost:8000/

Set it up in pycharm.

Enter into the admin site at:
http://localhost:8000/admin/

It will create the first scaffold of the project and then we can create the app running:
```bash
 python manage.py startapp press
```

Add the models to the press/models.py file and perform the migrations.

Play with the shell to make sure the model is correctly designed.

Register the application models into the admin site.

Create the superuser to enter into the admin site.

After adding the models into the Admin site you can run the migrations and everything else and perform:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py sqlmigrate press 0001
```



```SQL
BEGIN;
--
-- Create model Category
--
CREATE TABLE "press_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "label" varchar(200) NOT NULL);
--
-- Create model CoolUser
--
CREATE TABLE "press_cooluser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "github_profile" varchar(150) NULL, "gh_stars" integer NULL, "gh_repositories" integer NULL, "gravatar_link" varchar(400) NULL, "user_id" integer NOT NULL UNIQUE REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Post
--
CREATE TABLE "press_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(400) NOT NULL, "body" text NOT NULL, "image_link" varchar(400) NULL, "chart_link" varchar(400) NULL, "word_cloud_link" varchar(400) NULL, "source_link" varchar(400) NULL, "source_label" varchar(400) NULL, "status" varchar(32) NOT NULL, "creation_date" datetime NOT NULL, "last_update" datetime NOT NULL, "author_id" bigint NOT NULL REFERENCES "press_cooluser" ("id") DEFERRABLE INITIALLY DEFERRED, "category_id" bigint NOT NULL REFERENCES "press_category" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "press_post_author_id_e18dcdbd" ON "press_post" ("author_id");
CREATE INDEX "press_post_category_id_1abbd97d" ON "press_post" ("category_id");
COMMIT;
```

Create manually the:
 * Categories
 * Groups of permissions such "Editor", "Viewer"


## Get API news

In order to get more information from the API mediastack you need to provide the API_KEY and run the command get_api_news
 
```bash
export MEDIASTACK_KEY=<api_key>
python manage.py get_api_news health,sports,general --limit=30
```

## Dump and load information

```bash
python manage.py dumpdata --all --indent 4 --output sample_posts
python manage.py loaddata sample_posts
```


## Deploying on heroku

Setup on the repository and link it on the UI

You can check the logs with:
```bash
heroku logs --tail -a coolpress
```

Once everything is setup we need to create the superuser such:
```bash
heroku run python coolpress/manage.py createsuperuser -a coolpress
```

Remember to add the CoolUser associated to the superuser, otherwise there will be some surprised while adding some posts

Now you can check the information at: https://coolpress.herokuapp.com/

## Testing and coverage

In order to run the tests you can run the next command:
```bash
python manage.py test
```

And to run the coverage you can run:

```bash
coverage run manage.py test
coverage html
```

or directly:
```bash
coverage run manage.py test && coverage html && open htmlcov/index.html
```

Now you would have a a web page under the file: `coolpress/htmlcov/index.html` with the 
current coverage of the project


## Troubleshooting

Error importing coolpress:
* On pycharm you need to set the folder coolpress as source folder with the right-click on the root folder
* Or on a terminal using: ```export PYTHONPATH=`pwd` ```