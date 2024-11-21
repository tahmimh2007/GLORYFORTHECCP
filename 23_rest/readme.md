Team Astros
Andy Shyklo and Abidur Rahman
November 20, 2024

DISCO: 
The format that we are using is https://api.nasa.gov/planetary/apod?api_key=KEY
This is our HTTP Request.
When we go here, we can see something with 3 areas to look at: JSON, Raw Data, and Headers, which display the same information but in different ways.
Since we went to /planetary, we see the results here that are relative to planetary from our API key.
To actually get the information from the url, use urllib.request.urlopen(url + api)
From that, use .read() to actually be able to put that information into a usable file. 
To use the json file that we got from this, we have to convert it from text. The end of this one in this case has a \n at the end of it. 
This means that we need to take string[:-1] of that, and then put that into json.loads(), which will actually convert it into a json format.
From this, use it as a dictionary by requesting the value for "url", which in this case would be the image url.
Now, just input this into a template for flask, and display it on your website.
