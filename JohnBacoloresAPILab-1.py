# Option No. 2: API browsing application
# Choose an API to work with from common lists of free APIs. 
# Make sure the API has easily accessible routes for your "index" and "show" routes of a specific resource.
# API = https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=ce3dde60&app_key=23ab186f36f767814e36b2fc01a22761&what=ux%20designer
# app_id = [redacted]
# app_key = [redacted]

import requests

url = 'https://api.adzuna.com/v1/api/jobs/us/search/1?app_id=ce3dde60&app_key=23ab186f36f767814e36b2fc01a22761&results_per_page=50&what_and=software%20engineer&max_days_old=3&category=it-jobs'
response = requests.get(url)
dataset = response.json()

# API query requires a page number so I selected page 1 only. 

from flask import Flask, render_template, request 


app = Flask(__name__) # invoke the Flask class
# Set up your Flask index route and template to display the collection of data, including links to individual resources


@app.route("/anitasoftwarejob/<where>") 
def show_route(where): 
    print(dataset['results'])
    for data in dataset['results']:
        # print(data)
        if where in data['location']['area']:
            return render_template("show.html", dataset=data)
    return f'{where} not found on this page. Please check another page.'

# Include query parameters in your index route that allow users to perform a more specific search for data matching their parameters
# Will build one to search my location. 
# Create a route with the url anitasoftwarejobs/<where>, where is a route variable
# Render the show.html template, providing the jobs page 
# For each job, show display_name and title as an h1 element, area as h2, created as h3, salary_min and salary_max as h4, redirect_url as an a element and description as a paragraph element.

        #     print(data['location']['area'][3])
        #     print(data['location']['area'][2]) 
        #     return f'not found {where}'
        # Tried to find out why API only returned first item in API call. Return was indented within if statement instead of with for statement
        # how to return city with spaces? results -> location -> area[3] Show is only look at one piece, not everything like an index

@app.route("/anitasoftwarejob")
def index_route():
    return render_template("index.html", dataset=dataset['results'])

# Create a route with the url "anitasoftwarejob"
# Render the index.html template, providing the entire list of jobs as a keyword argument
# For each job, show display_name and job title as an h1 element, location as h2, created as h3, salary_min and salary_max as h4, redirect_url as an h5 element and description as a paragraph element.

# Complete your show route that allows users to view details of each individual item in the API results

if __name__ == '__main__':
    app.run(debug=True) # Start the server listening for requests