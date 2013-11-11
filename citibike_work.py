# Python, Nov 2013, for General Assembly class.
# Convert a JSON version of the Bike Data to a CSV.
# Should be easy except I have to learn the JSON parser!
# Funfun.


# Libraries
import json			# Do or die!
import os			# What? Killin' me.
import csv			# Ah right.


# Variables
actual_dict = dict()
file_name = 'citibike.json'
file_loc = '~/Dropbox/GA_Data_Science/GADS_week_one/'	# Moved for github
the_file = file_loc + file_name							# Because it's clear that way.
the_file = os.path.expanduser(the_file)					# Ah important.

output_filename = 'my_citibike.csv'
output_file = os.path.expanduser(file_loc + output_filename)

these_fields = ['id', 'stationName', 'statusKey', 'availableBikes', 'availableDocks', 'totalDocks', 'latitude', 'longitude']
		# These fields, not some other fields, and in this order.


# Linear script, no fancy function stuff.
with open(the_file, 'r') as f:
	bike_data = json.load(f)
print 'Opened and read file.'

# print bike_data											# Ok!
# print json.dump(bike_data, sort_keys=True, indent=1)
# print "Type of bike_data object: ", type(bike_data)	 	# Ok is dict.


with open(output_file, 'w') as f:
	bike_riter = csv.writer(f) 			# Bike riter! Get it?
	bike_riter.writerow(these_fields)	# Initing the header.

	list_of_dicts = bike_data.get('stationBeanList')			# The actual dicts are in a sub-dict (a list of dicts).
#	print 'Type of list_of_dicts is: ', type(list_of_dicts)		# List of dicts where the keys are all the same.
	for little_dict in list_of_dicts:
		correct_line = []									# Blank the new correct line each time, init.
		for item in these_fields:
			correct_line.append(little_dict[item])			# Build line from wanted items in order.
		bike_riter.writerow(correct_line)					# Writes the line.

print 'Done!'

