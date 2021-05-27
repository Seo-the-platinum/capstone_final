# Capstone Project

>The Capstone project allows assistants, casting directors,
>
>and executive directors to view and manage movies and actors.
>
> actors and movies can be assigned to each other which creates a
>
> star instance.

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

`assistant token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJnUlV3QW5kTGhTU1cxY3NXa3REeSJ9.eyJpc3MiOiJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwODljNWRmNGVjY2NiMDA2ZjY5MGY3MSIsImF1ZCI6WyJjYXBzdG9uZV9hcGkiLCJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE0ODQ3OSwiZXhwIjoxNjIyMjM0ODc5LCJhenAiOiJkVk5FdWVVaXpkSU0xTXIyWUZFZ1dFdDd3S2doUVBLcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.EN9kcuaW06iBZj549PfmJNW50TBk_YQlEc61cjF6fzBDU03yUWTtDr_v3KqqxDYlj0R0_WKCufB34PXaqYFNbjzVg_IZ-ZaocCn_wGkZjtoAaOtvwWVxcECrctSTAOEyqwp0LJ3FULGXDcFRSyVH2ZAfngObvkCpLOxHaCrHCVpqjV2mo8Ouvgwsr54oP2-Iu2uajWFuJjHV8GhK2YZVJTQLo1Jls-OGMkV311okSV5tluaoHq3U-TW-uRwpqfMv4bQ0--nmGwFhfxzY_SrT9eqvsWB14mPboJAtkoo64k47nqTDSuz-FnGGlrHotVf3WAeHF4LUBup1XX4QCYUGVA'`

`executive token= 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJnUlV3QW5kTGhTU1cxY3NXa3REeSJ9.eyJpc3MiOiJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwODljNjE5MGU0ZTAwMDA3MDI2MDcyNSIsImF1ZCI6WyJjYXBzdG9uZV9hcGkiLCJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjE0ODU5NSwiZXhwIjoxNjIyMjM0OTk1LCJhenAiOiJkVk5FdWVVaXpkSU0xTXIyWUZFZ1dFdDd3S2doUVBLcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0OnN0YXJzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwb3N0OnN0YXJzIl19.XmeJFlyP8_DDq9oZpNUdWIfesXPQpEyG-QSPg1aEOTvcFOHXG3_y3KgFXAnfU3I3O7y-TDitMz74-R5c00GRaTPBPYzypztAqUObPB9OKtnBPZzmz9qnQAY9ttJ89Oi-FHfxNXmHt8xNLtPPXlCd6tvRQmQ2NNu7NsmN-LD963814iZT1OQtiD3taNTGlRsXe8wPtM_ODTi-EWujtw6NWSHe0nOOjsuLUAgkYdSG6ZOTVy82j92ZTJsfm1At5Dx-jh-UF_OJ_ZeToapRWDHkeWYBqPZpVBdJae1XHyszH7ByZUgwm-yugY2dtVweEmt0U6-bq6YH0NhYdGbKoGx3Xw'`

### Heroku Url

[https://udacap.herokuapp.com/](https://udacap.herokuapp.com/)

## Local Development

### Dependencies

### Python
1. download python from [https://www.python.org/downloads/](https://www.python.org/downloads/). Make sure to download the version that is compatible with your
operating system

## PIP and VituralEnv

1. Use your terminal, in my case, gitbash, to install pip. From the root repository, fresh_capstone, **pip install**.

2. Then run **python -m virtualenv env** to create an
    env folder. activate env by using **source env/scripts/activate**
    if using windows. **source env/bin/activate**. use **source env/bin/activate**
    if using mac.

3. Then **pip install -r requirements.txt** to install
    all dependencies.

4. Run **export FLASK_APP=app.py** and then **flask run** to run the
   backend

## API/Enpoints

>all enpoints outside of the GET enpoints will require a jwt with the correct
>
>permission. all request are filtered through the auth.py file before sending the
>
>request back to the endpoint.

### Enpoints

**GET**

1. Get all movies from the database, /movies

2. Get all actors from the database, /actors

3. Get all stars from the database, /stars

**POST**

1. Create a movie, /movies

2. Create an actor, /actor

3. Create a star, /star

**PATCH**

1. Update a movie, /movies/id,

2. Update an actor, actors/id,

**DELETE**

1. Delete a movie, /movies/id,

2. Delete an actor, /actors/id, 
