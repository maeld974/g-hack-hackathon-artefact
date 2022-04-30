# Necessary imports
import io
import os
import csv
from google.oauth2 import service_account
from google.cloud import vision

# Load credentials 
credentials = service_account.Credentials.from_service_account_file('gcloud_key.json')

# Create image annotator client
client = vision.ImageAnnotatorClient(credentials=credentials)

# Input the name of the image file to annotate
input_image = 'sample_images/image_1.jpg'
file_name = os.path.abspath(input_image)

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

# Run the image through google vision API
image = vision.Image(content=content)

# Perform label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

# Get all 

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
