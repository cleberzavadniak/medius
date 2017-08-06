# Medius

[![CircleCI](https://circleci.com/gh/cleberzavadniak/medius/tree/master.svg?style=svg)](https://circleci.com/gh/cleberzavadniak/medius/tree/master)

A decent and easy Medium API client for Python.

I create this project because I found the official Medium
SDK for Python badly written and not covering all the endpoints of the
API. Sorry, "official guys", but that's the true... And I wanted something
really simple to use, intended for programatic access first and obeying
a very simple interface.

It **is** opinionated but, at least, it's easy to hack
into the Client and change whatever you need.

## Usage

```python
from medius.client import Client

# In this example, we get the access token from an environment variable:
client = Client(os.environ['MEDIUM_ACCESS_TOKEN'])

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

*Medium* API is not very rich in terms of listing things, so I found most
of the GETs on the endpoints will return `404 Not Found` errors, even when
you are sure there is something that should be listed. It's not Medius
Client fault (I believe).

## A message for Medium

I like Medium very much and I'm sad both the API and the Python SDK are
"less than optimal" the way they are. If you ever want to work into
a `/v2/`, let me know. I would be very glad to help. ;-)

## Requirements

 * `requests` module;
