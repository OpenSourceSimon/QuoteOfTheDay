# Import the random module
import random
# Import the json module
import json
# Import the time module
import time
# Import the requests module
import requests

# Open the quotes.json file
with open('quotes.json', encoding='utf-8') as f:
    # Load the quotes.json file
    quotes = json.load(f)

# Create a list of the random quotes and authors for the next year
random_quotes = []
for i in range(365):
    random_quotes.append(random.choice(quotes))

# Get a random background image from source.unsplash.com
resolution = '1920x1080'
category = 'nature'
background = requests.get(f'https://source.unsplash.com/random/{resolution}?{category}', stream=True)
# Copy the image to a file
with open('quoteoftheday/background.jpg', 'wb') as f:
    f.write(background.raw.read())
    f.close()

# Save the following to an HTML file
with open('quoteoftheday/index.html', 'w') as f:
    f.write(f'''
<html>
   <head>
      <title>Quote of the day</title>
      <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@300&display=swap" rel="stylesheet">
   </head>
   <style>
      body {{
      background-image: url("https://opensourcesimon.github.io/QuoteOfTheDay/quoteoftheday/background.jpg");
      background-size: cover;
      background-position: center;
      font-family: 'Roboto Slab';
      color: white;
      text-align: center;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      padding-left: 50px;
      padding-right: 50px;
      }}
      h1 {{
      font-size: 50px;
      }}
   </style>
   <div style="position: absolute; top: 40%">
      <h1>{random_quotes[0]["content"]}</h1>
      <h2>– {random_quotes[0]["author"]}</h2>
   </div>
   <!-- Create a footer with the date -->
   <div style="position: absolute; bottom: 0; width: 100%; text-align: center; font-size: 20px">
      <p>{time.strftime("%d %B %Y")}</p>
      <!-- Share to Facebook -->
   </div>
</html>
    ''')
    f.close()
