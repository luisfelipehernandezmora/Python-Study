# Use a quotes API, e.g. http://quotes.stormconsultancy.co.uk/random.json
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://blogs.unimelb.edu.au/sciencecommunication/2016/10/22/how-to-speak-doge/)
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_qoge_image_url` ruote` and `despectively.
# Then write the `html` string to a `.html` file and look at it in your browser.


from random import choice
import requests

quote_url="http://quotes.stormconsultancy.co.uk/random.json"
quote=requests.get(quote_url).json()["quote"]
doge=quote.split()
largo=len(doge)
new=[]
for i in range(0,largo):
    nueva=""
    bank=["Much","Many","So","Such","Very"]
    nueva=choice(bank)+" "+doge[i]
    new.append(nueva)
new

image_url="http://shibe.online/api/shibes"
image_link=requests.get(image_url).json()[0]

# this is for writting in the HTML    insert= f'<img src="{image_link}"">'
insert= f'''<div class="container">
  <img src="{image_link}"">
  <div class="text-block">
    <p>{new[0]}</p>
    <p>{new[1]}</p>
    <p>{new[2]}</p>
    <p>{new[3]}</p>
    <p>{new[4]}</p>
    <p>{new[5]}</p>
    <p>{new[6]}</p>
    <p>{new[7]}</p>
    <p>{new[8]}</p>
    <p>{new[9]}</p>
    <p>{new[10]}</p>
    <p>{new[11]}</p>
  </div>
</div>   
'''
with open ("Doge_quotes.html","w") as file:
    file.write(insert)