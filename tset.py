import matplotlib.pyplot as plt
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u
from astroquery.jplhorizons import Horizons

# User inputs
date_time = '2020-06-30 12:00' # must be in format YYYY-MM-DD HH:MM
location = SkyCoord("20h 00m 26.3s", "+15d 23m 28.2s", frame='icrs') # must be in ICRS coordinates

# Get the map from JPL Horizons
obj = Horizons(id='500@0', location=location, epochs={'start':date_time, 'stop':date_time, 'step':'1m'})
eph = obj.ephemerides(quantities=['delta',' elong',' phase',' longitude',' latitude',' r',' solar_presence',' mag',' solar_distance'],)

# Get the coordinates and map data
lon = eph['longitude']
lat = eph['latitude']
data = np.nan_to_num(eph['mag'])

# Setup the map
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()

# Plot the Deep Star Map
ax.scatter(lon, lat, c=data, cmap='gray_r', transform=ccrs.PlateCarree())

# Set the title
ax.set_title('Deep Star Map for {0}'.format(date_time))

# Show the map
plt.show()