import matplotlib.pyplot as plt
import mplleaflet

# Define latitude and longitude coordinates for cities
latitudes = [40.7128, 34.0522, 51.5074, -33.8688]
longitudes = [-74.0060, -118.2437, -0.1278, 151.2093]
cities = ['New York', 'Los Angeles', 'London', 'Sydney']

# Create a scatter plot of the cities
plt.figure(figsize=(10, 6))
plt.scatter(longitudes, latitudes, c='blue', edgecolor='black', s=100, alpha=0.75)

# Add city names as labels
for i, city in enumerate(cities):
    plt.text(longitudes[i], latitudes[i], city, fontsize=12, ha='right')

# Add title and labels
plt.title('World Cities')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Convert the plot to an interactive Leaflet map
mplleaflet.show()

# You can also save the map as an HTML file
# mplleaflet.show(path='cities_map.html')
