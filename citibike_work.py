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
file_loc = '~/Dropbox/GA_Data_Science/'
the_file = file_loc + file_name				# Because it's clear that way.
the_file = os.path.expanduser(the_file)		# Maybe? Please? PITA.

output_filename = 'my_citibike.csv'
output_file = os.path.expanduser(file_loc + output_filename)


# Script no fancy function stuff.
with open(the_file, 'r') as f:
	bike_data = json.load(f)
print 'Opened and read file.'
# print bike_data							# Ok!

# print json.dump(bike_data, sort_keys=True, indent=1)

# print "Type of bike_data object: ", type(bike_data) 	# Ok is dict


with open(output_file, 'w') as f:
	x = 1
	bike_riter = csv.writer(f) 		# Bike riter! Get it?
	pita_object = bike_data.get('stationBeanList')
#	print 'Type of actual_dict is: ', type(actual_dict)		# List, what? List of dicts where the keys are all the same.
	for thing in pita_object:
		thing = dict(thing)
#		print thing
		if (x == 1):
			bike_riter.writerow(thing.keys())
			x = x + 1
		bike_riter.writerow(thing.values())

print 'DONE FINALLY!'

