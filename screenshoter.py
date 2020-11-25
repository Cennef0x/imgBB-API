#Copyright (C) 2020  Cennef0x
import pyscreenshot as ImageGrab
import os 
import time
import requests
import random
import base64
import json 

setup(
    name = 'screenshoter.py',
    version = '0.0.1',
    Author = 'Cennef0x',
    GitHub = 'https://github.com/Cennef0x?tab=repositories'
)


def upload_IMG(img_location):
	img_Url = "https://api.imgbb.com/1/upload" # don't change this link
	Api_Key = "a1b2c3d4e5f6g7h8i9j0" #Put your real API KEY GET ONE HERE : https://api.imgbb.com/
	numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # don't change this
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # don't change this
	random_Name = random.sample(alphabet, 5) + random.sample(numbers, 4) # random name 
	name = ''.join([str(elem) for elem in random_Name]) 
	IMG_Link = img_location # image file path
	with open(IMG_Link, "rb") as image_file: # encode the image in base64
		encoded_string = base64.b64encode(image_file.read())
    
    #request parameters
	params = (
    ('expiration', '604800'),# seconds before the image is deleted
    ('key', Api_Key), #don't change this 
    ('image', encoded_string), # your encoded image
    ('name', name) #the image name 
			)
	name2 = "{}.png".format(name)
  # request parameters (name and format/extension)
	image= {
      "filename": name2,
      "name": name,
      "mime": "image/png",
      "extension": "png",
    }
	#Copyright (C) 2020  Cennef0x
	response = requests.post(img_Url, data=params) # the request is sent here
	if response.ok: # if code 200 find the link in the response and return it
		json_response = response.text 
		json_response2 = json.loads(json_response) # transform the str into dict
		TypeOfVar = type(json_response2)
		if "dict" in str(TypeOfVar): # check the type of var
			data_response = json_response2.get('data') 
			final_Url = data_response.get('url_viewer')
			print(final_Url)
		else:
			print("ERROR the var is not dict but {}".format(TypeOfVar))
	else:
		print("ERROR {}".format(response.status_code))


img_location = input("Please enter the image file path: ")

upload_IMG(img_location)
