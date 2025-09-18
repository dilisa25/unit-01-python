# Your Code Must Ask For:
# Which library area? (study room, computer lab, reading corner)
# What's the noise level? (number from 1-10)
# What time of day? (morning, lunch, afternoon)
# How many people are in the area?
# Rules You Must Code:
# Study rooms: noise ≤ 4
# Computer labs: noise ≤ 6
# Reading corners: noise ≤ 2
# During lunch: add +2 to all acceptable levels
# More than 10 people: add +1 to acceptable levels
# Test Your Code With These:
# Input: study room, 3, morning, 8 → Should PASS (within limit)
# Input: reading corner, 5, lunch, 15 → Should FAIL (too noisy even with adjustments)
# Input: computer lab, 7, afternoon, 12 → Should PASS (within adjusted limit)

#Ask user for what library area, noise level, time of day, and people 
library_area = input("Which library area(study room, computer lab, reading corner): ")
noise_level = int(input("What's the noise level?(number from 1-10): "))
time = input("What time of day?(morning, lunch, afternoon): ")
people = int(input("How many people are in the area?: "))

#If during lunch add +2 to all acceptable levels
if time == "lunch":
    noise_level =- 2  
# If more than 10 people add +1 to acceptable levels
if people > 10:
    noise_level =- 1
    
#If study room noise level should be ≤ 4, if is print acceptable levels if not print not acceptable levels
if library_area == "study room":
    if noise_level <=4:
        print("Noise level is at acceptable level")
    else:
        print("Noise level is not at acceptable level")
#If computer lab noise level should be ≤ 6 , if is print acceptable levels if not print not acceptable levels
if library_area == "computer lab":
    if noise_level <=6:
        print("Noise level is at acceptable level")
    else:
        print("Noise level is not at acceptable level")
#If reading corner noise level should be ≤ 2 , if is print acceptable levels if not print not acceptable levels
if library_area == "reading corner":
    if noise_level <=2:
        print("Nosie level is at acceptable level")
    else:
        print("Nosie level is not at acceptable level")