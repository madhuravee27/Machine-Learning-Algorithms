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

from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print "Enron number of dataset: ", len(enron_data)
#print "Enron features for each data point: ", len(enron_data[(enron_data.keys())[0]])
'''
count = sum(1 for i in enron_data.keys() if enron_data[i]["poi"] == 1 )
print "Number of persons of interest: ", count


num_lines = sum(1 for line in open('C:\Users\\niranjan\Documents\Machine_Learning\\ud120-projects-master\\final_project\poi_names.txt')) - 2

print "Number of lines: ", num_lines
'''
#print (((enron_data).values())[0]).keys()

#print enron_data.keys()

#print "James Prentice total stock value:", enron_data["PRENTICE JAMES"]["total_stock_value"]

#print "Wesley Colwell emails to POI:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#print "Jeffrey K Skilling exercised stocks option:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

'''
name = ""
final_total_payments = 0

for i in enron_data.keys():
    if (i.find("LAY") !=-1 or i.find("SKILLING")!=-1 or i.find("FASTOW")!=-1):
        if (enron_data[i]["total_payments"]>final_total_payments):
            name = i
            final_total_payments = enron_data[i]["total_payments"]

print "The person with largest total payments is ", name
print "with a total of: ", final_total_payments
'''
'''
count_salary = 0
count_email = 0

for i in enron_data.keys():
    if enron_data[i]["salary"] != "NaN":
        count_salary +=1
    if enron_data[i]["email_address"] != "NaN":
        count_email +=1

print "Count of quantified salary: ", count_salary
print "Count of quantified email address: ", count_email
'''

'''
count = 0

for i in enron_data.keys():
    if enron_data[i]["total_payments"] == "NaN":
        count += 1
total = len(enron_data)

#print "Percentage of people with total payments as NaN: ", (count/total)*100
print total+10
print count+10
'''


count = 0
total = 0

for i in enron_data.keys():
    if enron_data[i]["total_payments"] == "NaN" and enron_data[i]["poi"] == 1:
        count += 1
    if enron_data[i]["poi"] == 1:
        total += 1

print total
print count

print "Percentage of people with poi as NaN: ", (count/total)*100
