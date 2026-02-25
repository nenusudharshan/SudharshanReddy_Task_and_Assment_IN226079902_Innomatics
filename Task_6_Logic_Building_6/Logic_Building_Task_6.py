#%% [markdown]
# ASSIGNMENT 6 – Real-World System-Based Function Problems

#%% [markdown]
# Problem Statement 1: Smart Parking Lot Management System
# Design a function to manage a smart parking lot.
# The system should:
# - Accept vehicle entry and exit logs
# - Calculate total parked vehicles
# - Identify peak parking usage
# - Alert if parking exceeds capacity

#%%
def smart_parking(capacity, logs):
    current = 0
    peak = 0
    
    # Loop through vehicle logs
    for entry in logs:
        if entry == "IN":
            current += 1
        elif entry == "OUT":
            current -= 1
        
        # Track peak usage
        if current > peak:
            peak = current
    
    # Parking status
    if current > capacity:
        status = "Over Capacity Alert"
    else:
        status = "Available"
    
    return current, peak, status


capacity = 50
vehicle_logs = ["IN", "IN", "IN", "OUT", "IN", "IN", "OUT"]

current, peak, status = smart_parking(capacity, vehicle_logs)

print("Currently Parked Vehicles:", current)
print("Peak Usage:", peak)
print("Parking Status:", status)


#%% [markdown]
# Problem Statement 2: Online Food Delivery Time Estimator
# Estimate delivery time based on:
# - Distance
# - Traffic level
# - Weather condition

#%%
def delivery_time_estimator(distance, traffic, weather):
    base_time = distance * 5  # 5 minutes per km
    
    # Traffic adjustment
    if traffic == "High":
        base_time += 15
    elif traffic == "Medium":
        base_time += 8
    
    # Weather adjustment
    if weather == "Rainy":
        base_time += 10
    elif weather == "Storm":
        base_time += 20
    
    return base_time


eta = delivery_time_estimator(8, "High", "Rainy")
print("Estimated Delivery Time:", eta, "minutes")


#%% [markdown]
# Problem Statement 3: Movie Theatre Seat Occupancy Analyzer
# Analyze seat booking data:
# - Calculate occupancy percentage
# - Determine if show is Housefull
# - Suggest opening additional shows

#%%
def seat_occupancy(total_seats, booked_seats):
    booked_count = len(booked_seats)
    
    occupancy = (booked_count / total_seats) * 100
    
    if occupancy == 100:
        status = "Housefull"
    elif occupancy >= 75:
        status = "Almost Full"
    else:
        status = "Seats Available"
    
    return occupancy, status


total_seats = 200
booked = [1] * 150

occupancy, status = seat_occupancy(total_seats, booked)

print("Occupancy:", str(int(occupancy)) + "%")
print("Show Status:", status)


#%% [markdown]
# Problem Statement 4: Cloud Server Load Classification System
# Classify server load based on CPU usage readings:
# - Average CPU < 50% → Normal
# - 50%–80% → Warning
# - >80% → Critical

#%%
def server_load(cpu_readings):
    total = 0
    
    # Calculate average
    for value in cpu_readings:
        total += value
    
    average = total / len(cpu_readings)
    
    if average < 50:
        status = "Normal"
    elif average <= 80:
        status = "Warning"
    else:
        status = "Critical"
    
    return average, status


cpu_data = [45, 60, 70, 85, 90]

avg_cpu, server_status = server_load(cpu_data)

print("Average CPU Load:", str(int(avg_cpu)) + "%")
print("Server Status:", server_status)


#%% [markdown]
# Problem Statement 5: Smart Classroom Resource Usage Monitor
# Track usage of classroom resources and detect overuse.

#%%
def classroom_usage(resources):
    overused = []
    
    # Threshold for overuse (8 hours)
    for resource, hours in resources.items():
        if hours > 8:
            overused.append(resource)
    
    if overused:
        alert = "Yes"
    else:
        alert = "No"
    
    return overused, alert


usage_data = {
    "Projector": 6,
    "AC": 9,
    "Lights": 4
}

overused_resources, energy_alert = classroom_usage(usage_data)

print("Overused Resources:", ", ".join(overused_resources))
print("Energy Alert:", energy_alert)


#%% [markdown]
# Problem Statement 6: Online Event Registration Capacity Controller
# Manage event registrations:
# - Track registrations
# - Prevent overbooking
# - Trigger waitlist mode

#%%
def event_registration(capacity, registrations):
    
    if registrations <= capacity:
        confirmed = registrations
        waitlisted = 0
        status = "Open"
    else:
        confirmed = capacity
        waitlisted = registrations - capacity
        status = "Closed"
    
    return confirmed, waitlisted, status


confirmed, waitlisted, status = event_registration(100, 105)

print("Confirmed Registrations:", confirmed)
print("Waitlisted Users:", waitlisted)
print("Registration Status:", status)