import os
from flask import Flask, render_template,request,jsonify,url_for
import stripe,json,requests
from flask_json import FlaskJSON, JsonError, json_response
app = Flask(__name__)

print(os.environ.get('PUB_API_KEY'))
print(os.environ.get('SEC_API_KEY'))

stripe_keys = {
  'secret_key': os.environ['SEC_API_KEY'],
  'publishable_key': os.environ['PUB_API_KEY']
}

stripe.api_key = stripe_keys['secret_key']

@app.route('/')
def list_customer():
	list1=stripe.Customer.list(limit=100)
	return jsonify(list1)

@app.route('/plan')
def list_plan():
	listplan=stripe.Plan.retrieve("silver-complete")
	return jsonify(results = listplan)



if __name__ == '__main__':
	app.run(debug=True)