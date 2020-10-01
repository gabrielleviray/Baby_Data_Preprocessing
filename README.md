# Baby_Data_Preprocessing
We are given data of each day when a baby pees, poos, and eats in a given hour. To process the data, I first cleaned the data by fixing typos, and getting rid of invalid 
recordings. Then, using the Python module 'Xlsx Writer,' I generated three graphs that shows Total Feeds Per Day, Total Diaper Changes Per Day, and Both Total Feeds and Total Diaper Changes Per Day(used to observe the relationship between feeding and diaper changing).

# QUESTIONS ANSWERED:
    How many total feeds are there?
        # ANSWER: 776 total feeds
    How many total diaper changes?
        # ANSWER: 1123 diaper changes
    What day had the most actions in a given hour (diaper changes + feeds)?
        # ASSUMPTION: Compare the total actions of each day in a given hour and list the dates for each given hour with the most actions.
        # ANSWER:
            List of dates with the most actions within a given hour:                            
            {                                         
              "0": [                                  
                "Mon June 22",                        
                "Thur June 18"                        
              ],                                      
              "1": [                                  
                "Mon July 20",                        
                "Sun July 19",                        
                "Fri July 17",                        
                "Wed July 2",                         
                "Sun June 28",                        
                "Thur June 25",                       
                "Tue June 23",                        
                "Sun June 21",                        
                "Wed June 10",                        
                "Sat June 6",                         
                "Sat 5/22",                           
                "Fri 5/21",                           
                "Sat 5/16",                           
                "Thur 5/14"                           
              ],                                      
              "2": [                                  
                "Fri July 10",                        
                "Tue June 23",                        
                "Sat June 20",                        
                "Tue June 16",                        
                "Sun June 14",                        
                "Mon June 8",                         
                "Sun June 7",                         
                "Wed June 3",                         
                "5/25 Mon",                           
                "Thurs 4/29",                         
                "Mon 4/26"                            
              ],                                      
              "3": [                                  
                "Fri 5/15"                            
              ],                                      
              "4": [                                  
                "Tue 5/12"                            
              ],                                      
              "5": [                                  
                "Fri July 17",                        
                "Wed June 17",                        
                "Tues Jun 2",                         
                "Sun 4/25"                            
              ],                                      
              "6": [                                  
                "Sun June 28",                        
                "5/25 Mon"                            
              ],                                      
              "7": [                                  
                "Tue June 16",                        
                "Sun June 14",                        
                "Sun June 7",                         
                "Wed 4/28"                            
              ],                                      
              "8": [                                  
                "Wed July 155",                       
                "Tue July 14",                        
                "Mon July 13",                        
                "Sun July 12",                        
                "Tue July 7",                         
                "Sun July 5",                         
                "Wed June 24",                        
                "Sun June 21",                        
                "Mon June 15",                        
                "Thur June 11",                       
                "Tue June 9",                         
                "Mon June 8",                         
                "Sat June 6",                         
                "Thur 5/28",                          
                "Sun 5/17",                           
                "Sat 5/16",                           
                "Wed 5/13",                           
                "Mon 4/26",                           
                "Fri 4/24"                            
              ],                                      
              "9": [                                  
                "Sat July 18",                        
                "Sat June 13"                         
              ],                                      
              "10": [                                 
                "Sun July 19",                        
                "Thur July 16",                       
                "Sun June 21",                        
                "Tue June 16"                         
              ],                                      
              "11": [                                 
                "Tue July 21",                        
                "Sat July 4",                         
                "Sat June 20",                        
                "Sun 5/3"                             
              ],                                      
              "12": [                                 
                "Sat June 27",                        
                "Thur June 11",                       
                "Sat 5/30",                           
                "Sat 5/22"                            
              ],                                      
              "13": [                                 
                "Sat July 11",                        
                "Sat 4/25"                            
              ],                                      
              "14": [                                 
                "Tue June 23",                        
                "Thurs 4/29"                          
              ],                                      
              "15": [                                 
                "Sat 5/22",                           
                "Tue 5/12"                            
              ],                                      
              "16": [                                 
                "Sun 05/31",                          
                "Thur 5/28",                          
                "Wed 5/27"                            
              ],                                      
              "17": [                                 
                "Wed July 2",                         
                "Fri Jun 12",                         
                "Thur 5/14"                           
              ],                                      
              "18": [                                 
                "Mon June 22",                        
                "Thur 5/14"                           
              ],                                      
              "19": [                                 
                "Tue June 23",                        
                "Sun 05/31",                          
                "Sun 5/17",                           
                "Mon 5/4",                            
                "Sun 4/25"                            
              ],                                      
              "20": [                                 
                "Sat July 11",                        
                "Sat July 4",                         
                "Thurs July 2",                       
                "Wed July 2",                         
                "Tue June 30",                        
                "Thur June 25",                       
                "Tue 5/19",                           
                "Thur 5/7"                            
              ],                                      
              "21": [                                 
                "Fri 5/29",                           
                "Wed 5/6"                             
              ],                                      
              "22": [                                 
                "Tue June 16",                        
                "Wed 5/27",                           
                "Fri 5/1"                             
              ],                                      
              "23": [                                 
                "Mon June 15",                        
                "Fri Jun 12",                         
                "Wed June 10",                        
                "Fri 5/21",                           
                "Tue 5/12",                           
                "Sat 5/9",                            
                "Wed 4/28",                           
                "Tues 4/27",                          
                "Mon 4/26",                           
                "Fri 4/24"                            
              ]                                       
            } 
    # Graph the feeds per day over time
        # ANSWER: Need to install 'xlsxwriter package'. Automatically generates Graph.xlsx. 
    # Graph the diaper changes per day over time
        # ANSWER: Need to install 'xlsxwriter package'. Open Graph.xlsx 

# Assume the following
A row that has the terms pee or poop as one diaper change.
Any row that is under a date that does not have a time slot can be ignored (see example below: ignore line 2)
    # 1034 pee
    # Notice redness behind ear
    # 1050 poo
A row that has pee of poop needs to have a time to count as one.
