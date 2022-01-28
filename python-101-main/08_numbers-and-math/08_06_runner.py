# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)
mi=10
km=mi*1.6
min=30
seg=30
hour=(min*60+seg)/3600
#print(km/hour)
print('''If a runner runs 10 miles in 30 minutes and 30 seconds,
The average speed in kilometers per hour is:''',round(km/hour,2),"km/hr")