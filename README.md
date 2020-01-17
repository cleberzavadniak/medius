# Medius

[![CircleCI](https://circleci.com/gh/cleberzavadniak/medius/tree/master.svg?style=svg)](https://circleci.com/gh/cleberzavadniak/medius/tree/master)

A decent and easy Medium API client for Python.

I create this project because I found the official Medium
SDK for Python badly written and not covering all the endpoints of the
API (sorry, Medium team, that's the truth...). And I wanted something
really simple to use, intended for programatic access first through
a very simple interface.

It **is** opinionated but, at least, it's easy to hack
into the Client class and change whatever you need.

## Install

    pip install -U 'git+https://github.com/cleberzavadniak/medius.git'

## Usage

```python
from os import getenv
from medius.client import Client

client = Client(getenv('MEDIUM_ACCESS_TOKEN))

post_data = {
    'title': 'Post Title',
    'content': '<p>Post content</p>',
    'tags': ['cars', 'engines', 'Gurgel']
}

# Create a new post (by default it will be created as "draft"):
new_post = client.post('posts', post_data)

# Create a new post with publication date different than now and into a publication and without notifying the publication followers:
post_data['publishedAt'] = '2017-01-01 12:34:56'
post_data['notifyFollowers'] = False
new_post = client.post_into_publication('<publication_name>', post_data)
```

## Posts

Medius will prepend `<h1>{the_post_title_you_set}</h1>` to your post
content, the way most people do in the online editor.

## Listings

*Medium* API is not very rich in terms of listing things, so I found that most
of the GETs on the endpoints will return `404 Not Found` errors, even when
you are sure there is something that should be listed. It's not Medius
Client fault.
