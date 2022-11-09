# Data Modeling(Sparkify):
 the use case of database to help our business to make analysis and future goal so we used starschema
 to make your goal simple
 we made etl to extract and trasform&process data and load in database
 
 # the project divide to 4 files:
 
 # 1-sql_queries.py
 
we made the schema that contains of fact table ,3 dimension by star schema.
The Fact table provides the metric of the business process.
- fact table(
songplays
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)

- dimension_table(
users - <users in the app>(
user_id, first_name, last_name, gender, level)
    
songs - <songs in music database>(
song_id, title, artist_id, year, duration)
    
artists - <artists in music database>(
artist_id, name, location, latitude, longitude)
    
time - <timestamps of records in songplays broken down into specific units>
(start_time, hour, day, week, month, year, weekday
)
    
so we make queries for drop ,create , insert .
    
# 2.create_tables.py :
    
we used sql postgres to create and insert but first we made connect to database and make database
    
# 3.etl.ipynb:
    
it is import part in project i used notebook first to visualize and validate code then will put it in
python code .
    
first I made function to extract all files and read it .
    
then extract features and process it  then load in database ,we used song_data to extract song and artist table.
we used log_data to extract time,songplay,user tables .
    
# 4.test.pynb:
    
in this file ensure my data it is correct and show my tables.
    
# 5.elt.py :
    
after we saw data and validate it  we can gather all data in python code I run code by terminal 
and type python etl.py.
    

#  5.requirements.txt:
pandas==0.23.3
psycopg2==2.9.5
    
    
# How to run project?
    
- I ran by jupyter notebook ,termial to run python files.
    
- I used psycopg2 to run postgres server and make queries.
- pandas to read json files and process data.
- os,glob to extract all files from dirs.
    
 
    
[link](D:\Data_Modeling\Screenshot 2022-11-09 190054.png)
    

   

 
 