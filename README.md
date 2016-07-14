##About
Very secret task

##Requirements

This implementation requires the following:
* Python 2.7
* Django 1.7+
* Django REST Framework
* django-ipware

##Usage 
1. Clone this repository
2. Go to the root folder and run:
<code>python manage.py migrate</code>
to create a new database
3. After that you could run the server:
<code>python manage.py runserver</code>

##Testing
To test, if it correctly adds items in database and if it correctly processes request run:
<code>python manage.py test</code>

Finally, let's test the API itself. We will use <b>httpie</b>, which could be easily installed using pip.

<code>http POST http://127.0.0.1:8000/ip/</code>

<code>
HTTP/1.0 201 Created
...

{
    "ip_address": "127.0.0.1",
    "time": "2016-07-14T18:42:31.954000"
}
</code>

<code>http POST http://127.0.0.1:8000/ip/</code>

<code>
HTTP/1.0 201 Created
...

{
    "ip_address": "127.0.0.1",
    "time": "2016-07-14T18:43:32.168000"
}
</code>

<code>http GET http://127.0.0.1:8000/ip/</code>

<code>
HTTP/1.0 200 OK
...

[
    {
        "ip_address": "127.0.0.1",
        "time": "2016-07-14T18:42:31.954000"
    },
    {
        "ip_address": "127.0.0.1",
        "time": "2016-07-14T18:43:32.168000"
    }
]

</code>
