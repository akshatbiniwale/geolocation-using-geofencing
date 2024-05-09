# Geolocation Tracking Using Geofencing

This project uses a Python script to check if a user's current location is within a specified geofence. The geofence is defined by a set of latitude and longitude coordinates. The project consists of two main files: `picket.py` and `main.py`.

## Files

1. `picket.py`: This file contains the `Fence` class which is used to create a geofence, add points to it, and check if a given point is within the fence.

2. `main.py`: This file uses the `Fence` class from `picket.py` to create a geofence with hardcoded points, get the user's current location, check if the location is within the geofence, and plot the points on a Google Map.

## Installation

You will need Python 3 and the following library: `gmplot`. If these is not already installed, you can add them to your Python environment using pip:

```
pip install gmplot
```

## Running the Project

To run the project, simply run the geofence_check.py script in a Python environment where you can provide user input:

```
python main.py
```

The script will prompt you to enter your current location in degrees, minutes, and seconds format (e.g., 19°07’24.6"N 72°50’06.1"E). It will then check if your location is within the geofence and create an HTML file with a Google Map showing the geofence and your location.

## About Geofencing

Geofencing is a location-based service that creates a virtual geographic boundary, enabling software to trigger a response when a mobile device enters or leaves a particular area. In this project, we use geofencing to check if a user’s current location is within a specified geofence. This could be useful for a variety of applications, such as tracking user location for attendance purposes.
