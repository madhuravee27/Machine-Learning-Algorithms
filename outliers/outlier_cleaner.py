#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    import numpy

    from sklearn.metrics import mean_squared_error

    errors = []
    for i in range(len(ages)):

        error = mean_squared_error(y_pred = predictions[i], y_true = net_worths[i])
        errors.append(error)

    #print "error: ", errors

    new_errors = sorted(errors)

    #print errors

    #print new_errors

    temp = []

    for i in range(len(errors)):
        tup = (ages[i], net_worths[i], errors[i])
        temp.append(tup)

    temp_sorted = sorted(temp, key=lambda x: x[2])

    #print temp

    index = int(len(temp_sorted)*0.9 -1)
    cleaned_data = temp_sorted[:index]

    #print len(cleaned_data)

    return cleaned_data

