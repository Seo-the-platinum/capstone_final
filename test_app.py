import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Star, Movie, Actor, db

execHeader = {
    'Authorization': os.environ['EXEC_HEADER'],
    'Content-Type': 'application/json'
    }
assissHeader = {
    'Authorization': os.environ['ASSISS_HEADER'],
    'Content-Type': 'application/json'
    }


database_path = os.environ['TEST_DATABASE_PATH']


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            # very important, when it was self.db=SQLAlchemy(),
            # tables were not being generated. Not sure why but ask mentor
            self.db = db
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
            'actor_id': 4,
            'movie_id': 4,
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

# ---------------TEST GET ENDPOINTS--------------------
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_failed_get_movies(self):
        res = self.client().get('/movies/1001')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_failed_get_actors(self):
        res = self.client().get('/actors/1001')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_get_stars(self):
        res = self.client().get('/stars')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['stars']))

    def test_failed_get_stars(self):
        res = self.client().get('/stars/1010')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'File Not Found')

# ------------TEST POST ENDPOINTS----------------------

    def test_add_movie(self):
        res = self.client().post(
            '/movies',
            headers=execHeader,
            json=self.newMovie
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_failed_to_add_movie(self):
        res = self.client().post(
            '/movies/1010',
            headers=execHeader,
            json=self.newMovie
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_unauthed_to_add_movie(self):
        res = self.client().post(
            '/movies',
            headers=assissHeader,
            json=self.newMovie
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')

    def test_add_actor(self):
        res = self.client().post(
            '/actors',
            headers=execHeader,
            json=self.newActor
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_failed_to_add_actor(self):
        res = self.client().post(
            '/actors/1173',
            headers=execHeader,
            json=self.newActor
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method Not Allowed')

    def test_unauthed_to_add_actor(self):
        res = self.client().post(
            '/actors',
            headers=assissHeader,
            json=self.newActor
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')

    def test_add_star(self):
        res = self.client().post(
            '/stars',
            headers=execHeader,
            json=self.newStar
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_failed_to_add_star(self):
        res = self.client().post(
            '/stars/1173',
            headers=execHeader,
            json=self.newStar
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'File Not Found')

    def test_unauthed_to_add_star(self):
        res = self.client().post(
            '/stars',
            headers=assissHeader,
            json=self.newStar
            )
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unauthorized Permission or Token')

# ----------------TEST DELETE ENDPOINTS---------------------

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

# --------------TEST PATCH ENDPOINTS--------------------

    def test_update_movie(self):
        res = self.client().patch(
            '/movies/4',
            headers=execHeader,
            json=self.updatedMovie
            )
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
        res = self.client().patch(
            '/actors/4',
            headers=execHeader,
            json=self.updatedActor)
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
