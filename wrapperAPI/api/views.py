from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import praw


count = 10
reddit = praw.Reddit(
    client_id="Emqey7GBxcoh1SOgrXgTtw",
    client_secret = "rAyd--sR33HIhX5jWyuR3QfFWQVBAw",
    user_agent="task app"
    )

subreddit = reddit.subreddit("formula1")

@api_view(['GET'])
def getRoutes(requests):
    routes = [
        {
            'Endpoint': '/hot/',
            'method': 'GET',
            'body': None,
            'description': 'Returns the 10 hot posts of Formula1 subreddit'
        },
        {
            'Endpoint': '/new/',
            'method': 'GET',
            'body': None,
            'description': 'Returns the 10 new posts of Formula1 subreddit'
        },
        {
            'Endpoint': '/top/',
            'method': 'GET',
            'body': None,
            'description': 'Returns the 10 top posts of Formula1 subreddit'
        }
    ]
    return Response(routes)

@api_view(['GET'])
def getRoutesHot(requests):
    threads = []
    for submission in subreddit.hot(limit=count):
        threads.append({
            'title': submission.title,
            'url': submission.shortlink,
            'created': submission.created_utc,
            'author': submission.author.name if submission.author else 'Deleted',
        })

    return Response(threads)

@api_view(['GET'])
def getRoutesTop(requests):
    top_posts = subreddit.hot(limit=10)
    threads = []
    for submission in subreddit.top(limit=count):
        threads.append({
            'title': submission.title,
            'url': submission.shortlink,
            'created': submission.created_utc,
            'author': submission.author.name if submission.author else 'Deleted',
        })

    return Response(threads)

@api_view(['GET'])
def getRoutesNew(requests):
    top_posts = subreddit.hot(limit=10)
    threads = []
    for submission in subreddit.new(limit=count):
        threads.append({
            'title': submission.title,
            'url': submission.shortlink,
            'created': submission.created_utc,
            'author': submission.author.name if submission.author else 'Deleted',
        })

    return Response(threads)