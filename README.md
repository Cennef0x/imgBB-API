#Copyright (C) 2020  Cennef0x
# imgBB API Script
imgBB API / send screenshots & get the link

This program is free software: you can redistribute it and/or modify it

In this script I used imgBB API 
https://api.imgbb.com/

The script use all the following parameters :

Parameters

key (required)
The API key.

image (required)
A binary file, base64 data, or a URL for an image. (up to 32 MB)

name (optional)
The name of the file, this is automatically detected if uploading a file with a POST and multipart / form-data

expiration (optional)
Enable this if you want to force uploads to be auto deleted after certain time (in seconds 60-15552000)

-------------------------------------------------------------------------------------------------------------------

Key - You must put your own API KEY into the code

Image - The image will be encoded in base 64 before we send the request

Name - The name is generated randomly

Expiration - The expiration is set to 7 days (604800 seconds)

-------------------------------------------------------------------------------------------------------------------

How does it work ?

It's not that hard :

STEP 1 - Install the requirements

STEP 2 - Add your imgBB API KEY at line 20

STEP 3 - start the script (python screenshoter.py)

STEP 4 - input your image file path & press ENTER

STEP 5 - The link is now printed into the console
