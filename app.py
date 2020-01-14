# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import sys 

# create instance of Flask app
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#conn = "mongodb://localhost:27017"
#client = pymongo.MongoClient(uri)
# create instance of Flask app



# create route that renders index.html template
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    #mars= mongo.db.mars
    mars = scrape_mars.scrape_info()
    mongo.db.mars.update({}, mars, upsert=True)
    return redirect("/")


    


if __name__ == "__main__":
    app.run(port=5001)