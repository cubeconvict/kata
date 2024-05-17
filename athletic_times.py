# kata: https://www.codewars.com/kata/55b3425df71c1201a800009c/python

def stat(strg):

    import pandas as pd
    import datetime
    import math

    def format_seconds(my_seconds):
        #a function for converting seconds to the desired format with pipes
        my_hours = math.trunc(my_seconds/3600)
        my_minutes = math.trunc((my_seconds - my_hours*3600)/60)
        my_seconds = math.trunc(my_seconds - my_hours*3600 - my_minutes*60)
        if my_hours < 10:
            my_hours = str(my_hours)
            my_hours = "0"+my_hours
        if my_minutes < 10:
            my_minutes = str(my_minutes)
            my_minutes = "0"+my_minutes
        if my_seconds < 10:
            my_seconds = str(my_seconds)
            my_seconds = "0"+my_seconds
        my_time = str(my_hours)+"|"+str(my_minutes)+"|"+str(my_seconds)
        return my_time

    
    #check for empty string
    if strg == "":
        return strg
    
    #begin parsing the string
    mylist = strg.split(',')
    timelist_seconds = []
    #convert each time to seconds
    for each in mylist:
        x= each.split('|')
        seconds = int(x[0])*3600+int(x[1])*60+int(x[2])
        timelist_seconds.append(int(seconds))

    #calculate the average and format it
    total = sum(timelist_seconds)
    my_average_seconds = total/len(timelist_seconds)
    my_average = format_seconds(my_average_seconds)


    #calculate the range and format it
    range = max(timelist_seconds) - min(timelist_seconds)
    my_range = format_seconds(range)

    #median
    timelist_seconds.sort() 
    mid = len(timelist_seconds) // 2
    median_seconds = (timelist_seconds[mid] + timelist_seconds[~mid]) / 2
    my_median = format_seconds(median_seconds)

    my_answer = "Range: "+my_range+" Average: "+my_average+" Median: "+my_median
    return my_answer