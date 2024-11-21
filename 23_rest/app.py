from flask import Flask, render_template
import urllib.request
import urllib.parse
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('key_nasa.txt', 'r') as f:
        nasa_api_key = f.read().strip()
    
    base_url = "https://api.nasa.gov/planetary/apod"
    params = urllib.parse.urlencode({
        'api_key': nasa_api_key
    })
    full_url = f"{base_url}?{params}"

    with urllib.request.urlopen(full_url) as response:
        apod_data = json.loads(response.read().decode('utf-8'))
        
        # Extract relevant information
    image_url = apod_data.get('url', '')
    image_title = apod_data.get('title', 'NASA Astronomy Picture of the Day')
    image_explanation = apod_data.get('explanation', 'No explanation available.')
        
        # Render template with API data
    return render_template('main.html', team_name='TNPG: ', member1 = 'Tahmim Hassan',member2 = 'Anastasia Lee',image_url=image_url,image_title=image_title,image_explanation=image_explanation)
    

if __name__ == '__main__':
    app.run(debug=True)