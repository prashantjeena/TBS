from flask_restplus import Namespace, fields


class MovieDto:
    api = Namespace('movie', description='Movie related operations')
    movie = api.model('movie', {
    	'title':fields.String(required=True, description='movie title'),
        'user_ratings': fields.String( description='user ratings'),
        'cast': fields.String( description='cast of the movie'),
        'director': fields.String( description='director of the movie'),
        'duration_min':fields.Integer( description='duration of the movie'),
        'description': fields.String( description='description of the movie'),
        'price_movie' : fields.Integer( description='price of the movie'),
        'public_id': fields.String(description='Movie Identifier'),
        'released_on': fields.datetime(description='release date and time'),
        'languages': fields.String( description='languages available in')
    })