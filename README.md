## Formula1 API Django

This is a reddit api wrapper projects which fetches the top news of Formula1 subreddit.




### Setup:
### Backend Setup

1. Clone the repo

   ```sh
   git clone https://github.com/Sujaljp/reddit-api-wrapper
   ``` 

2. Go to the project folder

   ```sh
   cd reddit-api-wrapper
   ```

3. Setting up the virtual environment (Optional)
   ```sh
   # intalling virtual env
   pip install virtualenv

   # virtualenv creation
   virtualenv env

   # activating the env
   env\scripts\activate
   ```

4. Install packages

   ```sh
   pip install -r requirements.txt
   ```

5. Go to the django folder
    ```sh
   cd wrapperAPI
   ```

6. Run the server
    ```sh
   python manage.py runserver
   ```

7. Open your browser and go to http://localhost:8000/


### Opening the Frontend

1. Go to the Frontend folder present in the main directory.
2. Open index.html


## Python packages used 
* [PRAW](https://praw.readthedocs.io/en/latest/) : Package to handle the Reddit API'S 
* [django-cors-header](https://pypi.org/project/django-cors-headers/) : To handle cors error (connecting the backend to frontend)
* [virtualenv](https://virtualenv.pypa.io/en/latest/) : To create the virtual environment.

## API routes

Returns the 10 hot posts of Formula1 subreddit

        {
            'Endpoint': '/hot/',
            'method': 'GET',
        }

Returns the 10 new posts of Formula1 subreddit

        {
            'Endpoint': '/new/',
            'method': 'GET',
        }

Returns the 10 top posts of Formula1 subreddit

        {
            'Endpoint': '/top/',
            'method': 'GET',
        }