# DROP TABLES

songplay_table_drop = "drop table if exists songplay"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists song"
artist_table_drop = "drop table if exists artist"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists songplay(songplay_id serial  PRIMARY KEY, 

start_time TIMESTAMP Not NULL,
user_id int Not NULL, 
level varchar ,
song_id varchar ,
artist_id varchar,
session_id varchar Not NULL,
location varchar , 
user_agent varchar )
""")

user_table_create = (""" create table if not exists users(user_id int  PRIMARY KEY, 
first_name  varchar,
last_name  varchar, 
gender varchar  ,
level varchar )
""")

song_table_create = ("""create table if not exists song(song_id  varchar  PRIMARY KEY ,
title  varchar ,
artist_id  varchar Not NULL, 
year  int  ,
duration  float )
""")

artist_table_create = ("""create table if not exists artist(artist_id varchar   PRIMARY KEY, 
name  varchar , 
location  varchar ,
latitude  float ,
longitude  float )
""")

time_table_create = ("""create table if not exists time(start_time TIMESTAMP PRIMARY KEY,
hour  int , 
day  int ,
week int  ,
month  int ,
year  int ,
weekday  int )
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay (
start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")



user_table_insert = ("""insert into users
values(%s,%s,%s,%s,%s)
ON CONFLICT (user_id) 
DO UPDATE  SET level  = EXCLUDED.level
   

""")

song_table_insert = ("""insert into song
values(%s,%s,%s,%s,%s)
ON CONFLICT(song_id) DO NOTHING;
""")

artist_table_insert = ("""insert into artist
values(%s,%s,%s,%s,%s)
ON CONFLICT(artist_id) DO NOTHING;
""")


time_table_insert = ("""insert into time
values(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT(start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""select s.song_id,a.artist_id
from song as s
join artist as a
on s.artist_id=a.artist_id

where s.title=%s
and a.name=%s
and s.duration=%s
;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]