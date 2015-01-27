#!/usr/bin/env python


from flask import Flask
from flask.ext.restful import reqparse
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)



example_post_args = reqparse.RequestParser()
example_post_args.add_argument("name", type=str, location="form", required=True)
example_post_args.add_argument("id", type=int, location="form", required=True)



class ExamplePost(restful.Resource):
        def post(self):
            args = example_post_args.parse_args()
            print args


class ExampleApi(restful.Resource):
        def get(self):

            return {"error": False,
                    "success": True,
                    "data": [{"eatery_id": 12121, "eatery_name": "delhi height"}]
                    }


api.add_resource(ExampleApi, "/example_api")
api.add_resource(ExamplePost, "/example_post")

if __name__ == "__main__":
    app.run(port=5000, debug=True)


