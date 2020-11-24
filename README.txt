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
