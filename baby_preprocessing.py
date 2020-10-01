# Created 9/28/2020
# Author: Gabrielle Viray
# CMPE 255: Preprocessing Baby Feeds Data

# QUESTIONS:
    # How many total feeds are there?
        # ANSWER: 776 total feeds
    # How many total diaper changes?
        # ANSWER: 1123 diaper changes
    # What day had the most actions in a given hour (diaper changes + feeds)?
        # ASSUMPTION: Compare the total actions of each day in a given hour.
        # ANSWER:
            # List of dates with the most actions within a given hour:                            
            # {                                         
            #   "0": [                                  
            #     "Mon June 22",                        
            #     "Thur June 18"                        
            #   ],                                      
            #   "1": [                                  
            #     "Mon July 20",                        
            #     "Sun July 19",                        
            #     "Fri July 17",                        
            #     "Wed July 2",                         
            #     "Sun June 28",                        
            #     "Thur June 25",                       
            #     "Tue June 23",                        
            #     "Sun June 21",                        
            #     "Wed June 10",                        
            #     "Sat June 6",                         
            #     "Sat 5/22",                           
            #     "Fri 5/21",                           
            #     "Sat 5/16",                           
            #     "Thur 5/14"                           
            #   ],                                      
            #   "2": [                                  
            #     "Fri July 10",                        
            #     "Tue June 23",                        
            #     "Sat June 20",                        
            #     "Tue June 16",                        
            #     "Sun June 14",                        
            #     "Mon June 8",                         
            #     "Sun June 7",                         
            #     "Wed June 3",                         
            #     "5/25 Mon",                           
            #     "Thurs 4/29",                         
            #     "Mon 4/26"                            
            #   ],                                      
            #   "3": [                                  
            #     "Fri 5/15"                            
            #   ],                                      
            #   "4": [                                  
            #     "Tue 5/12"                            
            #   ],                                      
            #   "5": [                                  
            #     "Fri July 17",                        
            #     "Wed June 17",                        
            #     "Tues Jun 2",                         
            #     "Sun 4/25"                            
            #   ],                                      
            #   "6": [                                  
            #     "Sun June 28",                        
            #     "5/25 Mon"                            
            #   ],                                      
            #   "7": [                                  
            #     "Tue June 16",                        
            #     "Sun June 14",                        
            #     "Sun June 7",                         
            #     "Wed 4/28"                            
            #   ],                                      
            #   "8": [                                  
            #     "Wed July 155",                       
            #     "Tue July 14",                        
            #     "Mon July 13",                        
            #     "Sun July 12",                        
            #     "Tue July 7",                         
            #     "Sun July 5",                         
            #     "Wed June 24",                        
            #     "Sun June 21",                        
            #     "Mon June 15",                        
            #     "Thur June 11",                       
            #     "Tue June 9",                         
            #     "Mon June 8",                         
            #     "Sat June 6",                         
            #     "Thur 5/28",                          
            #     "Sun 5/17",                           
            #     "Sat 5/16",                           
            #     "Wed 5/13",                           
            #     "Mon 4/26",                           
            #     "Fri 4/24"                            
            #   ],                                      
            #   "9": [                                  
            #     "Sat July 18",                        
            #     "Sat June 13"                         
            #   ],                                      
            #   "10": [                                 
            #     "Sun July 19",                        
            #     "Thur July 16",                       
            #     "Sun June 21",                        
            #     "Tue June 16"                         
            #   ],                                      
            #   "11": [                                 
            #     "Tue July 21",                        
            #     "Sat July 4",                         
            #     "Sat June 20",                        
            #     "Sun 5/3"                             
            #   ],                                      
            #   "12": [                                 
            #     "Sat June 27",                        
            #     "Thur June 11",                       
            #     "Sat 5/30",                           
            #     "Sat 5/22"                            
            #   ],                                      
            #   "13": [                                 
            #     "Sat July 11",                        
            #     "Sat 4/25"                            
            #   ],                                      
            #   "14": [                                 
            #     "Tue June 23",                        
            #     "Thurs 4/29"                          
            #   ],                                      
            #   "15": [                                 
            #     "Sat 5/22",                           
            #     "Tue 5/12"                            
            #   ],                                      
            #   "16": [                                 
            #     "Sun 05/31",                          
            #     "Thur 5/28",                          
            #     "Wed 5/27"                            
            #   ],                                      
            #   "17": [                                 
            #     "Wed July 2",                         
            #     "Fri Jun 12",                         
            #     "Thur 5/14"                           
            #   ],                                      
            #   "18": [                                 
            #     "Mon June 22",                        
            #     "Thur 5/14"                           
            #   ],                                      
            #   "19": [                                 
            #     "Tue June 23",                        
            #     "Sun 05/31",                          
            #     "Sun 5/17",                           
            #     "Mon 5/4",                            
            #     "Sun 4/25"                            
            #   ],                                      
            #   "20": [                                 
            #     "Sat July 11",                        
            #     "Sat July 4",                         
            #     "Thurs July 2",                       
            #     "Wed July 2",                         
            #     "Tue June 30",                        
            #     "Thur June 25",                       
            #     "Tue 5/19",                           
            #     "Thur 5/7"                            
            #   ],                                      
            #   "21": [                                 
            #     "Fri 5/29",                           
            #     "Wed 5/6"                             
            #   ],                                      
            #   "22": [                                 
            #     "Tue June 16",                        
            #     "Wed 5/27",                           
            #     "Fri 5/1"                             
            #   ],                                      
            #   "23": [                                 
            #     "Mon June 15",                        
            #     "Fri Jun 12",                         
            #     "Wed June 10",                        
            #     "Fri 5/21",                           
            #     "Tue 5/12",                           
            #     "Sat 5/9",                            
            #     "Wed 4/28",                           
            #     "Tues 4/27",                          
            #     "Mon 4/26",                           
            #     "Fri 4/24"                            
            #   ]                                       
            # }   
    # Graph the feeds per day over time
        # ANSWER: Need to install 'xlsxwriter package'. Automatically generates Graph.xlsx. 
    # Graph the diaper changes per day over time
        # ANSWER: Need to install 'xlsxwriter package'. Open Graph.xlsx 

# Assume the following
# A row that has the terms pee or poop as one diaper change.
# Any row that is under a date that does not have a time slot can be ignored (see example below: ignore line 2)
    #1034 pee
    #Notice redness behind ear
    #1050 poo
# A row that has pee of poop needs to have a time to count as one.


from pandas import DataFrame
import pandas as pd
import numpy as np
import json
import xlsxwriter



# Clean Data & Organize Data into Nested Dictionary
def cleanNestedDictionary():
    days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    pee_list = ['pre', 'per']
    actions = []
    values = {}

    with open('baby.txt') as file:
        for line in file:
            line = line.rstrip()    # Remove Trailing Whitespaces
            if line:

                # Delete first line since the first line is not a useful key or value in the dictionary.
                # Delete line if item is not associated with time.
                if line == 'pee' or line =='poo' or line == 'poop' or line == 'Hydrocortisone started at 1:30am' or \
                line == '-' or line == '—' or line == 'hairloss' or line == "Baby feeds":
                    del line

                else:

                    # Check if line is a date
                    is_day = False
                    for day in days_list:
                        if day in line:
                            is_day = True
                            break;

                    # If line is a date, pop each action and associate each action
                    # to the time(key) in temporary dictionary called time
                    if is_day:
                        times = {}
                        for action in actions:
                            if action:
                                time = action.pop(0)
                                times[time] = action
                        values[line] = times    # set the date to be the key and nest the times dictionary into the values dictionary
                        actions = []    # clear actions

                    # Line is a time
                    else:

                        is_valid_time = True

                        # Fix time typos. Loop through each digit in the time and check if it is a digit.
                        # If it is not a digit, replace the character with the correct digit, depending on the case.
                        # (Handles 'O' = '0' and 'l' = '1' cases)
                        for i, val in enumerate(line):
                            if not val.isdigit():
                                is_valid_time = False
                                if val == "O":
                                    new = list(line)
                                    new[i] = '0'
                                    line = ''.join(new)
                                if val == "l":
                                    new = list(line)
                                    new[i] = '1'
                                    line = ''.join(new)

                        action = line.split()   # Splits the line into a list

                        # Check if time is larger than the maximum possible time
                        while int(action[0]) > 2359:
                            action[0] = int(action[0]) / 10 # Shift to right
                        actions.append(action) # Append to actions list

    return values

# Clean up dictionary
def cleanDictionary(values):
    
    for day in values:
        for hour in values[day]:

            # If Action is not assigned to time, delete it
            if hour == 'pee' or hour == 'poo' or hour == 'poop':
                del values[day][hour]

            # Fix typos such as "pre" and "per" and change to "pee"
            for item in values[day][hour]:
                if item == 'pre' or item =='per':
                    values[day][hour] = 'pee'
    return values

def findTotalFeeds(values):
    feeds_count = 0
    for day in values:
        for hour in values[day]:
            for item in values[day][hour]:
                if item == 'eat': # check if 'eat' appears in each hour
                    feeds_count +=1 # increment feed
    print(f"Total Number of Feeds: {feeds_count} feeds")

def findTotalDiaperChanges(values):
    diaper_changes_count = 0
    for day in values:
        for hour in values[day]:
            for item in values[day][hour]:
                if item == 'pee' or item == 'poo'or item == 'poop': # check if pee/poo/poop appear each hour
                    diaper_changes_count +=1    # increment count
    print(f"Total Number of Diaper Changes: {diaper_changes_count} diaper changes")

result = {}
def findMostActions(values):
    for day in values:
        result[day] = {num: 0 for num in range(0,24)} # Create dictionary to store hour counts at each given hour of each date 
        for time in values[day]:
            hour = int(time) // 100 # Get first two digits of hour
            result[day][hour] +=1 # Increment count
    max_actions =  {num: None for num in range(0,24)} # Create dictionary to store hours(as key) and days(values) with max acitons for given hour
    for day in result:
        for hour in result[day]:
            if not max_actions[hour]: 
                max_actions[hour] = [day]
            else:
                max_value_day = max_actions[hour][0] # Only need to compare first item, since every day in an hour have equal number of max actions
                if result[day][hour] > result[max_value_day][hour]: # Compare
                    # new dat is bigger, overwrite
                    max_actions[hour] = [day]
                elif result[day][hour] == result[max_value_day][hour]: 
                    # if equal, append to max_actions dictionary
                    max_actions[hour].append(day)
    return max_actions

def feedsPerDay(values):
    result = {}
    count = 0

    for day in values:
        result[day] = 0
        for time in values[day]:
            if "eat" in values[day][time]:
                result[day] += 1
    days = list(result.keys())
    counts = list(result.values())
    return days, counts

def diaperChangesPerDay(values):
    result = {}
    count = 0

    for day in values:
        result[day] = 0
        for time in values[day]:
            if "pee" or "poo" or 'poop' in values[day][time]:
                result[day] += 1
    diaper_days = list(result.keys())
    diaper_counts = list(result.values())
    return diaper_days, diaper_counts

def Graph(days, counts, diaper_days, diaper_counts):
    workbook = xlsxwriter.Workbook('Graph.xlsx')

    # FEEDS WORKSHEET
    feeds_worksheet = workbook.add_worksheet('Feeds')   
    feeds_columns = ['Date', 'Total Feeds']
    feeds_worksheet.set_column('A:B', 15) 

    feeds_worksheet.write_row('A1', feeds_columns)
    for row_num, data in enumerate(days, 1):
        feeds_worksheet.write(row_num,0,data)
    for row_num, data in enumerate(counts, 1):
        feeds_worksheet.write(row_num,1,data)
    feeds_chart = workbook.add_chart({'type': 'line'})

    # Configure the Feeds Graph
    feeds_chart.add_series({
        'name':'=Feeds!$B$1',
        'categories':'=Feeds!$A$2:$A$90', 
        'values':'=Feeds!$B$2:$B$90',
        'data_labels': {'value': True, 'position': 'above', 'font':{'color': 'blue'}},
        'line': {'none': True},
        'marker': {
            'type': 'diamond',
            'size': '5'

        },
    })

    # Add chart title.
    feeds_chart.set_title({'name': 'Feeds versus Day'})

    # Add x-axis label.
    feeds_chart.set_x_axis({'name': 'Date', 'text_axis': True})

    # Add y-axis label.
    feeds_chart.set_y_axis({'name': 'Total Feeds'})

    # SHEET 2: DIAPERS WORKSHEET
    diapers_worksheet = workbook.add_worksheet('Diapers')    
    diapers_columns = ['Date', 'Total Diaper Changes']
    diapers_worksheet.set_column('A:B', 15) 

    diapers_worksheet.write_row('A1', diapers_columns)
    for row_num, data in enumerate(diaper_days, 1): # Fill column 0 with diaper days data
        diapers_worksheet.write(row_num,0,data)
    for row_num, data in enumerate(diaper_counts, 1): # Fill column 1 with diaper changes count data
        diapers_worksheet.write(row_num,1,data)
    diapers_chart = workbook.add_chart({'type': 'line'})

    # Configure the Diaper Changes Graph
    diapers_chart.add_series({
        'name':'=Diapers!$B$1',
        'categories':'=Diapers!$A$2:$A$90', 
        'values':'=Diapers!$B$2:$B$90',
        'data_labels': {'value': True, 'position': 'above', 'font':{'color': 'blue'}},
        'line': {'none': True},
        'marker': {
            'type': 'diamond',
            'size': '5'
        },
    })

    # Add chart title.
    diapers_chart.set_title({'name': 'Diaper Changes versus Day'})

    # Add x-axis label.
    diapers_chart.set_x_axis({'name': 'Day', 'text_axis': True})

    # Add y-axis label.
    diapers_chart.set_y_axis({'name': 'Total Diaper Changes [diapers]'})


    # SHEET 3: Both Data Graphed on Same Graph
    actions_worksheet = workbook.add_worksheet('FeedsAndDiapers')
    actions_columns = ['Date', 'Total Feeds', 'Total Diaper Changes'] 
    actions_worksheet.set_column('A:C', 15) 

    actions_worksheet.write_row('A1', actions_columns)
    for row_num, data in enumerate(days, 1):  
        actions_worksheet.write(row_num,0,data)
    for row_num, data in enumerate(counts, 1):
        actions_worksheet.write(row_num,1,data)
    for row_num, data in enumerate(diaper_counts, 1):
        actions_worksheet.write(row_num,2,data)
    actions_chart = workbook.add_chart({'type': 'line'})

    # Configure the Feeds Graph
    actions_chart.add_series({
        'name':'=FeedsAndDiapers!$B$1',
        'categories':'=FeedsAndDiapers!$A$2:$A$90', 
        'values':'=FeedsAndDiapers!$B$2:$B$90',
        'data_labels': {'value': True, 'position': 'above', 'font':{'color':'red'}},
        'line': {'none': True},
        'marker': {
                    'type': 'square', 'size': '5',
                    'fill': {'color': 'red'}
        },
    })

    actions_chart.add_series({
        'name':'=FeedsAndDiapers!$C$1',
        'categories':'=FeedsAndDiapers!$A$2:$A$90', 
        'values':'=FeedsAndDiapers!$C$2:$C$90',
        'data_labels': {'value': True, 'position': 'above', 'font':{'color': 'blue'}},
        'line': {'none': True,
                'name': 'Number of Diaper Changes',
        },
        'marker': {
                    'type': 'diamond',
                    'size': '5',
                    'fill': {'color': 'blue'} 
        },
    })

    # Add chart title.
    actions_chart.set_title({'name': 'Actions versus Day'})

    # Add x-axis label.
    actions_chart.set_x_axis({'name': 'Day', 'text_axis': True})

    # Add y-axis label.
    actions_chart.set_y_axis({'name': 'Actions'})


    # Add Charts to Sheet
    feeds_worksheet.insert_chart('D2', feeds_chart, {'x_scale': 3.5, 'y_scale':1})
    diapers_worksheet.insert_chart('D2', diapers_chart, {'x_scale': 3.5, 'y_scale':1})
    actions_worksheet.insert_chart('D2', actions_chart, {'x_scale': 3.5, 'y_scale':1})


    workbook.close()

values = cleanNestedDictionary()
values = cleanDictionary(values)
findTotalFeeds(values)
findTotalDiaperChanges(values)
max_actions = findMostActions(values)
print("Dictionary of dates with the most actions for each hour where the 'key' is the hour.")
print(json.dumps(max_actions, indent=2))
days,counts = feedsPerDay(values)
diaper_days, diaper_counts = diaperChangesPerDay(values)
Graph(days,counts, diaper_days, diaper_counts)


