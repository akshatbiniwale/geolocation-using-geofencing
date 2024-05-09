import picket
from datetime import datetime
import re

def convertDMSToDD(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    if direction == 'S' or direction == 'W':
        dd *= -1
    return dd

def get_coordinates(prompt):
    print(prompt)
    dms = input("Enter latitude and longitude in DMS format (e.g., 19°07'24.6\"N 72°50'06.1\"E): ")
    lat_dms, lon_dms = dms.split()
    lat_deg, lat_min, lat_sec, lat_dir = re.split('[°\'\"]', lat_dms)
    lon_deg, lon_min, lon_sec, lon_dir = re.split('[°\'\"]', lon_dms)
    lat_dd = convertDMSToDD(lat_deg, lat_min, lat_sec, lat_dir)
    lon_dd = convertDMSToDD(lon_deg, lon_min, lon_sec, lon_dir)
    return (lat_dd, lon_dd)

# Create a new Fence object
my_fence = picket.Fence()

# Hardcode your provided points for the geofence
coordinates_dms = [
    ("19°07'22.8\"N", "72°50'00.5\"E"),
    ("19°07'22.4\"N", "72°50'14.2\"E"),
    ("19°07'28.9\"N", "72°50'14.8\"E"),
    ("19°07'32.6\"N", "72°50'12.7\"E"),
    ("19°07'33.7\"N", "72°50'02.4\"E")
]

for lat_dms, lon_dms in coordinates_dms:
    lat_deg, lat_min, lat_sec, lat_dir = re.split('[°\'\"]', lat_dms)
    lon_deg, lon_min, lon_sec, lon_dir = re.split('[°\'\"]', lon_dms)
    lat_dd = convertDMSToDD(lat_deg, lat_min, lat_sec, lat_dir)
    lon_dd = convertDMSToDD(lon_deg, lon_min, lon_sec, lon_dir)
    my_fence.add_point((lat_dd, lon_dd))

# Get user input for the current location
current_location = get_coordinates("Enter your current location: ")

# Check if the current location is within the geofence
if my_fence.check_point(current_location):
    print("You are within the geofence.")
else:
    print("You are not within the geofence.")

# Get the fence points
fence_points = my_fence.list_points()

# Add the first point to the end to close the fence in the plot
fence_points.append(fence_points[0])

# Separate the latitudes and longitudes
lats, lons = zip(*fence_points)

from gmplot import gmplot

# Get the fence points
fence_points = my_fence.list_points()

# Add the first point to the end to close the fence in the plot
fence_points.append(fence_points[0])

# Separate the latitudes and longitudes
lats, lons = zip(*fence_points)

# Create a new map centered around the first fence point
gmap = gmplot.GoogleMapPlotter(lats[0], lons[0], 13)

# Plot the fence points as a polygon
gmap.polygon(lats, lons, color='cornflowerblue')

# Plot the current location as a marker
gmap.marker(current_location[0], current_location[1], color='red')

# Get the current date and time
now = datetime.now()

# Format as a string
timestamp = now.strftime("%Y%m%d_%H%M%S")

# Draw the map to an HTML file with a unique name
gmap.draw(f"results/html/output_{timestamp}.html")