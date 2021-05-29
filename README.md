# Capstone Project

>The Capstone project allows assistants, casting directors,
>
>and executive directors to view and manage movies and actors.
>
> actors and movies can be assigned to each other which creates a
>
> star instance.

## Motivation

>We created capstone to help our directors manage casting roles for all movies
>
>in a convenient way. Capstone allows assistant directors, casting directors, and
>
>executive directors to keep track of all changes without having to be in direct
>
>contact. The database will update any changes that happened in real time to promote
>
>the most accurate information possible
## Roles and Tokens

> There are three roles. casting assistant, casting director, and executive director.
>
> assistants can only view current movies, actors, and stars.
>
>executive director can add, update, delete, actors and movies.
>
> casting director can do everything the executive director can do except
>
> delete and add movies.
### Tokens

`assistant token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJnUlV3QW5kTGhTU1cxY3NXa3REeSJ9.eyJpc3MiOiJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwODljNWRmNGVjY2NiMDA2ZjY5MGY3MSIsImF1ZCI6WyJjYXBzdG9uZV9hcGkiLCJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjI1MTE3OCwiZXhwIjoxNjIyMzM3NTc4LCJhenAiOiJkVk5FdWVVaXpkSU0xTXIyWUZFZ1dFdDd3S2doUVBLcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.j_e5CY4buGC8pG18FkKlkIMgyPx7W7R8haIAUJq4UFwBYd-2Q23P3cV5RAJv1e8_1glTw8IU_0YHLi57VUHbRkXzRFNj13tDI6BMu050Ausa5T9LhI1HwgSb-oEcPA-TRhag0k7hH7SSyGKad0cXJt87bbdkkMlIh81-z-gu_Ohbcq02--4CeQV75UDC2FQPSfNCJ48CCVTaRXmUTduZU3lobBsHRNnjvQhfkjhRsRjhTxAKpWJs6DwwmUdqnI2rAE--zttyDXTh3WhmZ-jPB9FUcZ0gTpoBnlCV3mg1AnMV_27baiqKdbX3Z_Bq5-lLyFJjC-KLSzlKJa5jHef8Rg'`

`executive token= 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJnUlV3QW5kTGhTU1cxY3NXa3REeSJ9.eyJpc3MiOiJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwODljNjE5MGU0ZTAwMDA3MDI2MDcyNSIsImF1ZCI6WyJjYXBzdG9uZV9hcGkiLCJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjI0OTkwMCwiZXhwIjoxNjIyMzM2MzAwLCJhenAiOiJkVk5FdWVVaXpkSU0xTXIyWUZFZ1dFdDd3S2doUVBLcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0OnN0YXJzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwb3N0OnN0YXJzIl19.iffXoxhQZ2CmqpA-G0810RyOOeyF8c0GK-61PGIEsPltfPFwfZ7bBVQgsNIDE1uC0X8R28HckRl-MPFXio0rNPDHo_I_Ev98GgNYQ5VSTkxlliiG_NOtku95sle39mLaEWBBQIXqayJWrdIKGv3hBs6r0-BVBrBYiDpxOJHjtzhNwr6J7r4wnSzxdhBt1iJH4P0UZxzS9aJDRQXw0Pa3MBYWLxckoTzGmXIg51JirGv6dCEWFx_WmztBgGcBOOK3wKhkEd69w4NuBFon22QLstGBdUEWzxHm_V_6G_d6wTvrm5g4I1gNAk1i5aIUyF7oXLlesUaC3oU4rKIdobYXBw'`

### Heroku Url
[https://udacap.herokuapp.com/](https://udacap.herokuapp.com/)

Use the heroku cli in your terminal to update the heroku database by
running **git push heroku main**
and then **heroku run python manage.py db upgrade --app udacap**
to upgrade migrations

## Local Development

### Dependencies

### Python
1. download python from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to download the version that is compatible with your
operating system

## PIP and VituralEnv

1. Use your terminal, in my case, gitbash, to install pip. From the root repository, fresh_capstone, **pip install**.

2. Then run **python3 -m virtualenv env** to create an
    env folder. activate env by using **source env/scripts/activate**
    if using windows. **source env/bin/activate**. use **source env/bin/activate**
    if using mac.

3. Then **pip install -r requirements.txt** to install
    all dependencies.

4. Run **export FLASK_APP=app.py** and then **flask run** to run the
   backend. If you are using windows, you may need to run
   **set FLASK_APP=app.py** instead.

## API/Enpoints

>all enpoints outside of the GET enpoints will require a jwt with the correct
>
>permission. all request are filtered through the auth.py file before sending the
>
>request back to the endpoint.

### Enpoints

**GET**

1. Get all movies from the database, /movies
  Example:
    {
      'success': True,
      'movies': [
        {
          'id': 1,
          'title': 'Heres a title',
          'release_date': 'heres the date',
        },
       {
        'id': 2,
        'title': 'Heres a title 2',
        'release_date': 'another date'
       }
      ]
    }

2. Get all actors from the database, /actors
  Example:
    {
        'success': True,
        'actors': [
          {
            'age': 32,
            'id': 1,
            'gender': 'male',
            'name': 'Aegon Targaryen'
        },
        {
          'age': 36,
          'id': 2,
          'gender': 'Female',
          'name': 'Daenerys Targaryen'
        }
        ]
    }

3. Get all stars from the database, /stars
  Example:
    {
      'success': True,
      'stars': [
        {
          'id': 1,
          'actor_id': 1,
          'movie_id': 1,
        },
        {
          'id': 2,
          'actor_id': 2,
          'movie_id': 2,
        }

        ]
    }

**POST**

1. Create a movie, /movies
  Example:
    {
      'title': 'new title',
      'release_date': 'new date',
    }

2. Create an actor, /actor
  Example:
    {
      'age': 15,
      'gender': 'Male',
      'name': 'teens name',
    }

3. Create a star, /star
  Example:
    {
      'actor_id': 3,
      'movie_id': 3,
    }
**PATCH**

1. Update a movie, /movies/id,
  Example:
    {
      'title': 'updated title',
      'release_date': 'updated date'
    }
2. Update an actor, actors/id,
  Example:
    {
      'age': 16,
      'gender': 'Male',
      'name': 'Updated name'
    }
**DELETE**

1. Delete a movie, /movies/id,
  Example:
    {
      'movie_id': 1,
    }

2. Delete an actor, /actors/id,
  Example:
    {
      'actor_id': 1,
    }
