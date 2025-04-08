location = [("New York", (40.7128, -74.0060)), 
            ("Tokyo", (35.6895, 139.6917)), 
            ("Delhi", (28.7041, 77.1025))]

def get_location(city):
    for for_name, coord in location:
        if city == for_name:
            return coord
    return None  # Return None if city is not found

city = "New York"
coordinate = get_location(city)

if coordinate:
    print(f"The coordinates of {city} are {coordinate}")
else:
    print(f"Location for {city} not found.")
