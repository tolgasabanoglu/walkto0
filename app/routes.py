# routes.py

from flask import render_template, request, redirect, url_for
from app import app

# In-memory storage for location data (can be replaced with a database or session later)
location_data = {}

@app.route('/')
def home():
    return render_template('home.html', location=location_data)

@app.route('/location', methods=['POST'])
def location():
    try:
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        
        # Save the location data (here, in a dictionary)
        location_data['latitude'] = latitude
        location_data['longitude'] = longitude

        return redirect(url_for('home'))  # Redirect back to the home page after saving the location
    except Exception as e:
        print(f"Error processing form data: {e}")
        return "Error in processing location data", 500  # Send a server error message
