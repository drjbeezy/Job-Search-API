# Option No. 2: API browsing application
# Choose an API to work with from common lists of free APIs. 
# Make sure the API has easily accessible routes for your "index" and "show" routes of a specific resource.
# API = https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=ce3dde60&app_key=23ab186f36f767814e36b2fc01a22761&what=ux%20designer
# app_id = ce3dde60
# app_key = 23ab186f36f767814e36b2fc01a22761

# Create functions that successfully use the requests library to make valid API requests and return the relevant data from the response. 
# Don't worry about Flask yet, just make sure the API requests work as intended.
# Different API calls: search for jobs, job categories, top companies
import requests

url = 'https://api.adzuna.com/v1/api/jobs/us/top_companies?app_id=ce3dde60&app_key=23ab186f36f767814e36b2fc01a22761'
response = requests.get(url)
data = response.json()

print(data['leaderboard'][0]['canonical_name'])
# What is the top company in the US to work for? 

import requests

url = 'https://api.adzuna.com/v1/api/jobs/us/categories?app_id=ce3dde60&app_key=23ab186f36f767814e36b2fc01a22761'
response = requests.get(url)
data = response.json()

print(data['results'][1]['label'])
# What is the 2nd type of jobs available for hire? 

import requests

url = 'https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=ce3dde60&app_key=23ab186f36f767814e36b2fc01a22761&what_and=software%20engineer'
response = requests.get(url)
data = response.json()

print(data['results'][0]['company']['display_name'])
print(data['results'][0]['title'])
print(data['results'][0]['salary_max'])
print(data['results'][0]['salary_min'])
print(data['results'][0]['location']['area'])
# What is the first company on the page that is hiring a software engineer in the US, including location and min/max salary bands? 

# Set up your Flask index route and template to display the collection of data, including links to individual resources
from flask import Flask, request # import the Flask class to create an app

app = Flask(__name__) # invoke the Flask class

@app.route("/reviews")
def index_route():
    return render_template("index.html",reviews=reviews)

@app.route("/reviews/<review_id>") 
def show_review(review_id): 
    for review in reviews:
        if review["id"] == review_id:
            return render_template("show.html", review=review)
        else:
            return 'not found'

# # Include query parameters in your index route that allow users to perform a more specific search for data matching their parameters

# # Complete your show route that allows users to view details of each individual item in the API results

# if __name__ == '__main__':
#     app.run(debug=True) # Start the server listening for requests