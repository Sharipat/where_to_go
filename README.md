## Website "Where to go - Moscow through the eyes of Artyom"

A site with tags and descriptions of the most interesting places in Moscow. Artyom's original project.

[Site launch example](http://shirlex.pythonanywhere.com/)

[Admin Panel Example](http://shirlex.pythonanywhere.com/admin/)

## Launch

- Download the repository from Github:

```
git clone https://github.com/Sharipat/where_to_go.git
```


- Install dependencies with the command `pip install -r requirements.txt`
- Create a `.env` file and add environment variables to it. To test functionality, the code works without them
   filling.
- Create a database file and apply all migrations at once with the command `python3 manage.py migrate`
- Start the server with the command `python3 manage.py runserver`
- Load the locations you need by running the `load_place` script in the format 
`python3 manage.py load_place <full link to the json file with location data>`

   Eg:

```
python3 manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA% D0%B0%D1%84%D0%B5%20Bizone.json

```

## Example of using the site

The map allows you to change the scale, shows a description and photo of the location, and you can also walk through some locations
links to the website or social networks of this location

![screenshot](screenshots/place-usage.gif)

## Working with the admin panel

To test the admin panel, you can go to [link](http://shirlex.pythonanywhere.com/admin/) and enter ready-made
login and password:

**Username:** `admin385`

**Password:** `Password321@`

To further create your user on the local machine, use the command:

```
python3 manage.py createsuperuser
```

By logging into the admin panel, you can create a new or edit an old location by clicking on **Locations**

![screenshot](screenshots/admin-place.gif)

To create a new location, click **Add Location**

![screenshot](screenshots/create-place.gif)

In editing mode, you can change text, location coordinates, add and delete photos, and also change them
position when displayed on the site, by dragging the photos with the mouse cursor:
![screenshot](screenshots/change-photo.gif)

## Environment variables

Some of the project settings are taken from environment variables. To define them, create a `.env` file next to `manage.py` and
write the data there in the following format: `VARIABLE=value`.

Variables available:

- `DEBUG` - debug mode. Set to True to see debugging information in case of an error.
- `SECRET_KEY` — secret key of the project
- `ALLOWED_HOSTS` - see [Django documentation](https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts).
- `STATIC_URL`
   — [see Django documentation, default is 'places/static/'](https://docs.djangoproject.com/en/5.1/ref/settings/#static-url)
- `STATIC_ROOT`
   — [see Django documentation](https://docs.djangoproject.com/en/5.1/ref/settings/#static-root)
- `MEDIA_URL`
   - [see Django documentation, default is /media/'](https://docs.djangoproject.com/en/5.1/ref/settings/#std:setting-MEDIA_URL)
- `MEDIA_ROOT`
   — [see Django documentation, default is 'media'](https://docs.djangoproject.com/en/5.1/ref/settings/#std:setting-MEDIA_ROOT)

## Project goals

The code is written for educational purposes - this is a lesson in the course on Python and web development on the site [Devman](https://dvmn.org).

Test data taken from the website [KudaGo](https://kudago.com).