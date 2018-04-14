# adapted from my homework 2

# import package to read sqlite3 data 
import sqlite3
# import pandas to create dataframes 
import pandas as pd
# import os for operating system 
import os 

# define a function to read in the database 
# input: dbConn (the path to the .db file containing the database)
# output: dataframe of data from class.db reformatted into one dataframe with 
# a new column for language 
def create_dataframe(dbConn):
    # check that the file exists
    # adapted from 07-Exceptions
    if not os.path.exists(dbConn):
        raise ValueError("file doesn't exist: "+str(dbConn))
    # reading in the sql database adapted from https://www.dataquest.io/blog/python-pandas-databases/
    db = sqlite3.connect(dbConn)
    # create a curser object to run sql against the database
    ex = db.cursor()
    # execute sql on the database 
    query="select us.video_id, us.category_id, 'us' as language from USvideos as us"
    query=query+" union select de.video_id, de.category_id, 'de' as language from DEvideos as de"
    query=query+" union select gb.video_id, gb.category_id, 'gb' as language from GBvideos as gb"
    query=query+" union select ca.video_id, ca.category_id, 'ca' as language from CAvideos as ca"
    query=query+" union select fr.video_id, fr.category_id, 'fr' as language from FRvideos as fr;"
    sql = ex.execute(query)
    # fetch all the data 
    data = pd.DataFrame(ex.fetchall())
    data.columns = ("video_id","category_id","langauge")
    # test statements to check the output 
    # close the connection 
    ex.close()
    db.close()
    return(data)