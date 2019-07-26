# Instagram Clone
IP for Django module week 2 that involves creating a clone of the photo app Instagram.

#### By **Philip Kariuki**


## Description
This app involves creating an Instagram clone using Django.

Live link : https://phillmatic.herokuapp.com

## User Stories
As a user, I would like to be able to do the following:
* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.

## Specifications
| Behaviour | Input | Output |
| --------------- | :----------:| --------: |
| Display all photos | On home page load | Loads all the available photos |
| Zoom in on image | Click on a particular image | Single image zooms in |
| View image details | Click on the particular image | Image descriptions display on top of and below the image |
| Search for image | Enter image description in search box | Matching images return as search results else 0 matching images found |


## Setup/Installation Requirements
To clone this repo, open terminal in your desired folder then run:

        $ git clone https://github.com/philipkariuki/django-photos/
        $ cd /django-photos

To create and activate the virtual environment and install pip:

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python


To install all the required pip modules for proper functionality:

        (virtual)$ python3.6 -m pip install -r requirements.txt

To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
To run unittests:

        $ python3.6 manage.py test philmatic

## Known Bugs

No known bugs

## Technologies Used

* HTML
* CSS
* Python3.6
* Pip
* Django v 2.2.3
* MDBootstrap
* Postgres Database
* gunicorn


## Contributors
<a href="https://github.com/philipkariuki">philipkariuki</a>

## Support and contact details
To support me, you can contact me at <a href="https://www.gmail.com">philippokar@hotmail.co.uk</a>

## License
[MIT © 2019](https://github.com/philipkariuki/instagram-clone/blob/master/LICENSE)

