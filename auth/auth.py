import os
import json
from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = os.environ['AUTH0_DOMAIN']
ALGORITHMS = os.environ['ALGORITHMS']
API_AUDIENCE = os.environ['API_AUDIENCE']
CLIENT_ID = os.environ['CLIENT_ID']
#creates function to let us know when authorization fails

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

#get json web token from auth header using function.
# when a request to one of our endpoints is made, that
# request will be handed off to this function to check
# the headers prop in the request for a "Authorization"
# prop.

def get_token_auth_header():
    #if 'Authorization' prop is not found in request.headers
    #throw an error using authError. We pass an object for the
    # error parameter and 401 for the status_code. We use 401
    # because it translates to an unathorized request
    if 'Authorization' not in request.headers:
        raise AuthError({
            'success': False,
            'message': 'AUTH NOT IN HEADER',
            'error': 401,
        }, 401)
        abort(401)
    #store the value of 'authorization' if it exists,
    # it should contain a bearer id and a token.
    auth_header = request.headers['Authorization']
    # because it contains 2 elements, we must split them.
    # this line seperates the bearer portion from the actual
    # json web token and stores them in a list name header_parts.
    header_parts = auth_header.split(' ')

    #check that our header_parts list has exactly 2 items,
    # if not, throw an auth error with 401 status_code
    if len(header_parts) != 2:
        raise AuthError({
            'success': False,
            'message': 'JWT NOT FOUND',
            'error': 401
        }, 401)
    #verify that the first item in our list is a string with
    # a value of 'bearer'
    elif header_parts[0].lower() != 'bearer':
        raise AuthError({
            'success': False,
            'message': 'JWT NOT FOUND',
            'error': 401,
        }, 401)
    # once we've verified that the request header we recieved
    # is 2 parts and contains a bearer token and json web token,
    # we return the jwt to be used by another function
    return header_parts[1]

#the check_permissions function should be passed a permission
# whenever a request is sent to an endpoint. Every user will have
# an assigned role, i.e admin is a type of role,and each role is
#granted access to enpoints. not all endpoints are accessible
#by all roles.inside our Jwt there is a payload object.
#We check to see if the payload contains a permissions prop,
#if it does check that the desired permission/endpoint is listed
# inside the payloads permissions. if not, deny with error
def check_permissions(permission, payload):
    if 'permissions' in payload:
        if permission in payload['permissions']:
            return True
    raise AuthError({
        'success': False,
        'message': 'PERMISSION NOT FOUND IN JWT',
        'error': 401,
    }, 401)

#get_token_auth_header retreieves the request
# and verifies the bearer token. then it returns the header
# which will then be passed to verify_decode_jwt so we can
# decipher it.
def verify_decode_jwt(token):
    #we use the urlopen function to retrieve the public
    # key from our auth0 account domain. Once we retrieve it,
    # we store it in the jsonurl variable. We need the public
    # key in order to decode the jwt
    jsonurl = urlopen(
    f'http://auth0practice.us.auth0.com/.well-known/jwks.json'
    )
    jwks = json.loads(jsonurl.read())
    #pass the token to the jwt.get_unverified_header function
    # and store to unverified_header var. This will contain
    # the decoded version of our jwt
    unverified_header= jwt.get_unverified_header(token)
    rsa_key={}
    #checks for property 'kid' in the header, if none ,error
    if 'kid' not in unverified_header:
        raise AuthError({
            'success': False,
            'message': 'AUTHORIZATION MALFORMED',
        },401)
    #for loop over the public keys provided by auth0
    # and checks if the 'kid' in our unverified_header
    # matches any of the  public keys from auth0
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'success': False,
                'message': 'Token expired',
                'error': 401,
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'success': False,
                'message': 'Incorrect claims. Please, check the audience and issuer',
                'error': 401,
            }, 401)

        except Exception:
            raise AuthError({
                'success': False,
                'message': 'Unable to parse authentication token',
                'error': 400,
            }, 400)

    raise AuthError({
        'success': False,
        'message': 'Unable to find the appropriate key',
        'error': 400,
    }, 400)

#puts everything together. Wraps endpoints in app.py that
#require authorization. when an enpoint received a request,
# the permission that the endpoint needs is passed as a string
# to our permission parameter.
def requires_auth(permission=''):
    #this part builds our wrapper function so we can
    #use requires auth above our endpoint and pass
    # the necessary arguments through to our enpoint.
    def requires_auth_decorator(f):
        @wraps(f)
        #first we retrieve the token from get_token_auth_header
        #then we pass the token to verify_decode_jwt so we can
        #decode it and get the payload. Then pass both payload and
        # permission to check_permissions
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator
