# BASICS

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

# -------------------------------------------------
# SLICING

# Create another areas list
areasTwo = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areasTwo[:6]

# Use slicing to create upstairs
upstairs = areasTwo[6:]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)

# Add poolhouse data to areas, new list is areas_1
areas_1 = areasTwo + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]