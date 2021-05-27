import os
from flask import Flask, request, jsonify, abort
from models import setup_db, Movie, Actor, Star
from flask_cors import CORS
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
#----- CORS ---------
#comeback to this to understand how this works, needed for CORS
#enabled server

    @app.after_request
    def after_request(response):
        response.headers.add(
        'Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add(
        'Access-Control-Allow-Methods', 'GET, DELETE , POST, PATCH')
        return response

#--------- GET ENDPOINTS --------

    @app.route('/movies', methods=['GET'])
    def get_movies():
        try:
            movies = Movie.query.all()
            formatted_movies = [movie.format() for movie in movies]

        except :
            abort(405)

        return jsonify({
            'success': True,
            'movies': formatted_movies,
        })

    @app.route('/actors', methods=['GET'])
    def get_actors():
        try:
            actors = Actor.query.all()
            formatted_actors = [actor.format() for actor in actors]

        except:
            abort(405)

        return jsonify({
            'success': True,
            'actors': formatted_actors,
        })

    @app.route('/stars', methods=['GET'])
    def get_stars():
        try:
            stars = Star.query.all()
            data = []
            for star in stars:
                movie = Movie.query.get(star.movie_id)
                actor = Actor.query.get(star.actor_id)

                data.append({
                    'id': star.id,
                    'movie': movie.format(),
                    'actor': actor.format(),
                })

        except:
            abort(404)

        return jsonify({
            'success': True,
            'stars': data,
        })
#------- POST ENDPOINTS ------

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(token):
        try:
            res = request.get_json()
            movie = Movie(
                release_date = res['release_date'],
                title = res['title'],
            )
            movie.insert()

        except:
            abort(405)

        return jsonify({
            'success': True,
            'movie': movie.id,
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(token):
        try:
            res = request.get_json()
            actor = Actor(
                age = res['age'],
                gender = res['gender'],
                name = res['name']
            )
            actor.insert()

        except:
            abort(405)

        return jsonify({
            'success': True,
            'actor': actor.id,
        })

    @app.route('/stars', methods=['POST'])
    @requires_auth('post:stars')
    def create_star(token):
        try:
            res = request.get_json()
            star = Star(
                actor_id= res['actor_id'],
                movie_id= res['movie_id'],
            )
            star.insert()

        except Exception as e:
            print(e)
            abort(404)

        return jsonify({
            'success': True,
            'star': star.id,
        })

#--------- PATCH ENDPOINTS ------------
    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(token, movie_id):
        res =  request.get_json()
        movie = Movie.query.filter(
        Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(422)

        try:
            movie.title = res['title']
            movie.release_date = res['release_date']
            movie.update()

        except ValueError as e:
            print(e)
            abort(422)

        return jsonify({
            'success': True,
            'movie': movie.format(),
        })

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(token, actor_id):
        res =  request.get_json()
        actor = Actor.query.filter(
        Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(422)

        try:
            actor.age = res['age']
            actor.gender = res['gender']
            actor.name = res['name']
            actor.update()

        except ValueError as e:
            print(e)
            abort(422)

        return jsonify({
            'success': True,
            'actor': actor.format(),
        })

#-------- DELETE ENDPOINTS --------

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(token, movie_id):

        movie = Movie.query.filter(
        Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(422)

        try:
            movie.delete()

        except ValueError as e:
            print(e)
            abort(422)

        return jsonify({
            'success': True,
            'movie': movie_id,
        })

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(token, actor_id):
        actor = Actor.query.filter(
        Actor.id == actor_id).one_or_none()

        if actor is None:
            abort(422)
        try:
            actor.delete()

        except ValueError as e:
            print(e)
            abort(500)

        return jsonify({
            'success': True,
            'actor': actor_id,
        })

#------ ERROR HANDLERS ------

    @app.errorhandler(404)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "File Not Found"
            }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'Method Not Allowed'
        }), 405

    @app.errorhandler(422)
    def unable_to_follow(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "Unprocessable"
        }), 422

    @app.errorhandler(AuthError)
    def unathorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Unauthorized Permission or Token',
        }), 401

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error':500,
            'message': 'Internal Server Error',
        }), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
