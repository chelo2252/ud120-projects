#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print len(enron_data)

#print len(enron_data["SKILLING JEFFREY K"])

#len([key for key in enron_data.keys() if enron_data[key]["poi"] == True ])
"""
with open("../final_project/poi_names.txt") as f:
    poiNames = f.readlines()

poi_names = [line.strip() for line in poi_names]
poi_names = poi_names[2:]
poi_names = [line[4:] for line in poi_names]

print len(poi_names)
"""

#print enron_data["PRENTICE JAMES"]["total_stock_value"]

#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

"""
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
"""

#print len([key for key in enron_data.keys() if not enron_data[key]["salary"] == 'NaN'])
#print len([key for key in enron_data.keys() if not enron_data[key]["email_address"] == 'NaN'])

"""
import sys
sys.path.append("../tools/")
import feature_format

features=['poi','salary','bonus']
np_list = feature_format.featureFormat(enron_data, features)

print np_list
"""

#print len([key for key in enron_data.keys() if (enron_data[key]["total_payments"] == 'NaN' and enron_data[key]["poi"] == True)])*100/len(enron_data)


print len(enron_data)+10

print len([key for key in enron_data.keys() if enron_data[key]["total_payments"] == 'NaN' ])+10

