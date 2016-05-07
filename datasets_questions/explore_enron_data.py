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

import math
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people with a known salary", sum([1 for (person, feature) in enron_data.iteritems() if feature["salary"] != "NaN"])
print "Number of people with a known email", sum([1 for (person, feature) in enron_data.iteritems() if feature["email_address"] != "NaN"])
people_with_unknown_total_payments = sum([1 for (person, feature) in enron_data.iteritems() if feature["total_payments"] == "NaN" and feature["poi"]])
print "Number of people with unknown total_payments {}, representing the {} %".format(
    people_with_unknown_total_payments, people_with_unknown_total_payments * 100.0 / len(enron_data.keys()))
