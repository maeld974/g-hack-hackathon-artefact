# Necessary imports
import io
import os
import csv
# import tempfile

from google.oauth2 import service_account
from google.cloud import vision
from google.cloud import storage
# from wand.image import Image

storage_client = storage.Client()

def return_labels(file_data):
	
    file_name = file_data['name']
    bucket_name = file_data['bucket']

    blob = storage_client.bucket(bucket_name).get_blob(file_name)
    file_name = blob.name

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

# def return_labels(data, context):
# 	file_data = data

#     file_name = file_data['name']
#     bucket_name = file_data['bucket']

#     blob = storage_client.bucket(bucket_name).get_blob(file_name)
#     file_name = blob.name
#     _, temp_local_filename = tempfile.mkstemp()

#     # Download file from bucket.
#     current_blob.download_to_filename(temp_local_filename)
#     print(f'Image {file_name} was downloaded to {temp_local_filename}.')

#     # Load credentials 
# 	credentials = service_account.Credentials.from_service_account_file('gcloud_key.json')

# 	# Create image annotator client
# 	client = vision.ImageAnnotatorClient(credentials=credentials)

# 	# Input the name of the image file to annotate
# 	input_image = 'sample_images/image_1.jpg'
# 	file_name = os.path.abspath(temp_local_filename)

# 	# Loads the image into memory
# 	with io.open(file_name, 'rb') as image_file:
# 	    content = image_file.read()

# 	# Run the image through google vision API
# 	image = vision.Image(content=content)

# 	# Perform label detection on the image file
# 	response = client.label_detection(image=image)
# 	labels = response.label_annotations

# 	# Get all 

# 	# Create CSV file with output labels
# 	with open('labels.csv', 'w') as file:
# 		header = ['label', 'score']

# 		# CSV writer
# 		writer = csv.writer(file)

# 		# Write header
# 		writer.writerow(header)

# 		# For label extracted with the API, create a new row in the outputs datset
# 		for label in labels:
# 			writer.writerow([label.description, label.score])

