# Necessary imports
import io
import os
import csv
# import tempfile

from google.oauth2 import service_account
from google.cloud import vision
from google.cloud import storage

storage_client = storage.Client()

def main(request):
	"""Responds to any HTTP request.
	Args:
		request (flask.Request): HTTP request object.
	Returns:
		The response text or any set of values that can be turned into a
		Response object using
		`make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
	"""
	request_json = request.get_json()

	file_name = request_json['file_name']
	bucket_name = 'input_images_ghack2022'

	blob = storage_client.bucket(bucket_name).get_blob(file_name)
	file_name = blob.name

	credentials = service_account.Credentials.from_service_account_file('gcloud_key.json')
	client = vision.ImageAnnotatorClient(credentials=credentials)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	# Run the image through google vision API
	image = vision.Image(content=content)

	# Perform label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	# Create CSV file with output labels
	with open('labels.csv', 'w') as file:
		header = ['label', 'score']

		# CSV writer
		writer = csv.writer(file)

		# Write header
		writer.writerow(header)

		# For label extracted with the API, create a new row in the outputs datset
		for label in labels:
			writer.writerow([label.description, label.score])

	return 'OK'
	