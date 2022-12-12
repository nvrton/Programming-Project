import math

def miles_to_longitude_latitude(distance, direction):
    # Define the bearing based on the direction of the new point
    if direction == "north":
        bearing = 0
    elif direction == "east":
        bearing = 90
    elif direction == "south":
        bearing = 180
    elif direction == "west":
        bearing = 270

    # Convert distance from miles to meters
    distance_in_meters = distance * 1609.34

    # Calculate the latitude and longitude values of the new point
    new_latitude = math.asin(math.sin(current_latitude) * math.cos(distance_in_meters / 6371) + math.cos(current_latitude) * math.sin(distance_in_meters / 6371) * math.cos(bearing))
    new_longitude = current_longitude + math.atan2(math.sin(bearing) * math.sin(distance_in_meters / 6371) * math.cos(current_latitude), math.cos(distance_in_meters / 6371) - math.sin(current_latitude) * math.sin(new_latitude))

    # Wrap the longitude value so that it is between -180 and 180 degrees
    new_longitude = (new_longitude + math.pi) % (2 * math.pi) - math.pi

    # Convert latitude and longitude values from radians to degrees
    new_latitude_degrees = new_latitude * 180 / math.pi
    new_longitude_degrees = new_longitude * 180 / math.pi

    # Return the new latitude and longitude values
    return new_latitude_degrees, new_longitude_degrees




current_latitude = 30.2672
current_longitude = -97.7431

new_coordinates = miles_to_longitude_latitude(100, "east")
print(new_coordinates)