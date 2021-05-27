import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Star, Movie, Actor, db

execHeader= { 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJnUlV3QW5kTGhTU1cxY3NXa3REeSJ9.eyJpc3MiOiJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwODljNjE5MGU0ZTAwMDA3MDI2MDcyNSIsImF1ZCI6WyJjYXBzdG9uZV9hcGkiLCJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjA3NzE3MCwiZXhwIjoxNjIyMTYzNTcwLCJhenAiOiJkVk5FdWVVaXpkSU0xTXIyWUZFZ1dFdDd3S2doUVBLcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwiZ2V0OnN0YXJzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwb3N0OnN0YXJzIl19.Sg5W7UYClNUMk4e8tS7tIx0gxciWWVTfoF5ONrLnoa136vRoASfubvwEV7bW59j6gAamKyI9rqe2_zs_laihN1ewEo4umBFj6iZoxjQU9PW5eF9ZyHn5xFcgJYwHJRz66n1TGg8b4OG7ay4FM9326wH5s3LCtNVXYCb-hUnpy_GgHLAtmnQka_qGFVxGpwT7jGilDvvFricHmZ-oxvZSCNJ4rL2mCsW6nIRxkuDUsoRSMfDuyjhSy0YNOR-LL2DGSIF8rqlu4SFV-FpDKixxAjUnnS4iHUflQKZJHUa0lMzi3a8LYtgKoTDH2hX4jM6wnKF4XC_us-uNMQFFgz2TGg",
'Content-Type': 'application/json' }

assissHeader = { 'Authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJnUlV3QW5kTGhTU1cxY3NXa3REeSJ9.eyJpc3MiOiJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwODljNWRmNGVjY2NiMDA2ZjY5MGY3MSIsImF1ZCI6WyJjYXBzdG9uZV9hcGkiLCJodHRwczovL2F1dGgwcHJhY3RpY2UudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMjA3Njc3OSwiZXhwIjoxNjIyMTYzMTc5LCJhenAiOiJkVk5FdWVVaXpkSU0xTXIyWUZFZ1dFdDd3S2doUVBLcyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.TQClhfgGKnX5uI3pv_0tGsfK2AzEfLNGwq23a8jf6ZStRtaDnVCDmlWS3AdCgB5DIeBgBbvfGVatsFIy1Xl4zGx7A8UF4Wjwwe3xElqDeCGQfUJ_gRibmHTI-YqUT7TlrEFB9ZgWXUZpWBbfOQJCAehrkRNVPYTB1tKC6P0lS7-TaxHZTFt5NkRn822kzyx7S3HElR23dZP0EhaQoUGQrxiqaxTwN4_-AqM7TA9Wl8Xv4tSMRqka_lnPD_ayOgMtkjUl0e1jQF35bWwDQJjHhT0fOflfMsxMqsgBPNyPeohZXoPdyyUq90RNM2BHW5vNFTtXCINErtR4Mgcjc9T2fg",
'Content-Type': 'application/json' }

database_path = 'postgresql://postgres:seoisoe5i73@localhost:5432/capstonedb_test'

class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app=create_app()
        self.client=self.app.test_client
        self.database_path=database_path
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            #very important, when it was self.db=SQLAlchemy(),
            #tables were not being generated. Not sure why but ask mentor
            self.db=db
            self.db.init_app(self.app)
            self.db.create_all()

        self.newMovie = {
            'release_date': '01/01/2023',
            'title': 'New Journey',
        }

        self.newActor = {
            'age': 1,
            'gender': 'male',
            'name': 'Cloud',
        }

        self.newStar = {
            'actor_id':4,
            'movie_id':4,
        }

        self.updatedMovie = {
            'release_date': '12/16/2025',
            'title': 'The Boy Who Cried Cheat'
        }

        self.updatedActor = {
            'age': 45,
            'gender': 'male',
            'name': 'George Toldedo',
        }

    def tearDown(self):
        """Executed after reach test"""
    pass

#---------------TEST GET ENDPOINTS--------------------
    def test_get_movies(self):
        res= self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_failed_get_movies(self):
        res = self.client().get('/movies/1001')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_actors(self):
        res= self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_failed_get_actors(self):
        res = self.client().get('/actors/1001')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_stars(self):
        res= self.client().get('/stars')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['stars']))

    def test_failed_get_stars(self):
        res = self.client().get('/stars/1010')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'File Not Found')

#------------TEST POST ENDPOINTS----------------------

    def test_add_movie(self):
        res = self.client().post('/movies', headers=execHeader,json=self.newMovie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_failed_to_add_movie(self):
        res = self.client().post('/movies/1010', headers=execHeader,json=self.newMovie)
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_unauthed_to_add_movie(self):
        res = self.client().post('/movies', headers=assissHeader,json=self.newMovie)
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')


    def test_add_actor(self):
        res = self.client().post('/actors', headers=execHeader,json=self.newActor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_failed_to_add_actor(self):
        res = self.client().post('/actors/1173', headers=execHeader,json=self.newActor)
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_unauthed_to_add_actor(self):
        res = self.client().post('/actors', headers=assissHeader,json=self.newActor)
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')

    def test_add_star(self):
        res = self.client().post('/stars', headers=execHeader, json=self.newStar)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_failed_to_add_star(self):
        res = self.client().post('/stars/1173', headers=execHeader, json=self.newStar)
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'File Not Found')

    def test_unauthed_to_add_star(self):
        res = self.client().post('/stars', headers=assissHeader, json=self.newStar)
        data= json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')

#----------------TEST DELETE ENDPOINTS---------------------

    def test_delete_movie(self):
        res = self.client().delete('/movies/15', headers=execHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie'], 15)

    def test_delete_movie_failed(self):
        res = self.client().delete('/movies/1000', headers=execHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_unauthed_delete_movie_failed(self):
        res = self.client().delete('/movies/20', headers=assissHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')

    def test_delete_actor(self):
        res = self.client().delete('/actors/15', headers=execHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor'], 15)

    def test_delete_actor_failed(self):
        res = self.client().delete('/actors/1000', headers=execHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_unathed_delete_actor_failed(self):
        res = self.client().delete('/actors/20', headers=assissHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')

#--------------TEST PATCH ENDPOINTS--------------------

    def test_update_movie(self):
        res = self.client().patch('/movies/4', headers=execHeader, json=self.updatedMovie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movie']))

    def test_upate_movie_failed(self):
        res = self.client().patch('/movies/1000', headers=execHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_update_actor(self):
        res = self.client().patch('/actors/4', headers=execHeader, json=self.updatedActor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actor']))

    def test_upate_actor_failed(self):
        res = self.client().patch('/actors/1010', headers=execHeader)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

if __name__ == "__main__":
    unittest.main()
