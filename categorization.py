from PIL import Image, ImageOps #Install pillow instead of PIL
import numpy as np
import urllib.request
from flask import jsonify
import ssl
import json
import requests
from tfserving import TF_SERVING_IP

ssl._create_default_https_context = ssl._create_unverified_context


def categorization(img_url):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the labels
    class_names = open('labels.txt', 'r').readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    urllib.request.urlretrieve(img_url, 'img')
    image = Image.open('img').convert('RGB')
    # image = Image.open('/home/ubuntu/scrapping-server/test.png').convert('RGB')

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Pass to TF Serving
    data = json.dumps({"instances" : data.tolist()})
    headers = {"content-type" : "application/json"}
    json_response = requests.post(TF_SERVING_IP, data=data, headers=headers)
    prediction = json.loads(json_response.text)

    index = np.argmax(prediction['predictions'][0])

    # # run the inference
    # prediction = model.predict(data)
    # index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction['predictions'][0][index]

    print('Class:', class_name, end='')
    print('Confidence score:', confidence_score)
    return jsonify({'imgUrl': img_url, 'category':class_name.strip()})
