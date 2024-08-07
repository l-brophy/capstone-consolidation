# capstone: consolidation
My submission for the Level 3 Consolidation capstone - my Django project, containerised, Sphinx documentation added.

# running
## in terminal
Make sure that you are running in a [venv](https://docs.python.org/3/library/venv.html). 
Once your venv is set up, navigate to the `yarn_shop` directory in the root, containing the `requirements.txt` file. 
From there, run the command `pip install -r requirements.txt`.

In development, you would have access to a `.env` file containing the applicable secret key. This file is not in the repo,
and the server will not run without that file or without the `SECRET_KEY` variable in `settings.py`/`.env` declared.
Declare that variable, and run `python3 manage.py runserver`.

## with docker
To run using Docker, make sure that you have the Docker daemon running.
Then, anywhere in your Terminal, run the command `docker run -d -p 8000:8000 depechemold/h-consolidation`. 
If everything is as it should be, it will display a set of numbers.

## either or
Navigate to your [local host](http://127.0.0.1:8000/) and the website should be running!
