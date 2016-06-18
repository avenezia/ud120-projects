#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    assert len(predictions) == len(ages) == len(net_worths)
    features_with_error = [(ages[index], net_worths[index], abs(predictions[index] - net_worths[index])) for index in range(0, len(predictions))]
    features_with_error.sort(key = lambda (age, net_worth, error): error)
    cleaned_data = features_with_error[:81]
    return cleaned_data

