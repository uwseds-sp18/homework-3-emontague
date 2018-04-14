import unittest
import homework3 as hw3
import numpy as nm

# adapted from class 3 lecture - structure of unit tests 
# adapted from my homeowork 2 - the tests completed 

# Define a class in which the tests will run
class Homework3Test(unittest.TestCase):

    def test_smoke(self):
        hw3.create_dataframe("../homework1/class.db")

    # column names
    def testColumns(self):
        test=hw3.create_dataframe("../homework1/class.db")
        # check that the columns are named correctly 
        # they are in the correct order
        # and that there are exactly three columns 
        self.assertTrue(test.columns[0]=='video_id' and test.columns[1]=='category_id' and test.columns[2]=='langauge' and len(test.columns)==3)
    
    # number of rows
    def testRows(self):
        # confirm the number of rows in the resulting data frame 
        self.assertTrue(hw3.create_dataframe("../homework1/class.db").shape[0]==35950)

    # check keys 
    def testKeys(self):
        test=hw3.create_dataframe("../homework1/class.db")
        # check that all three together are a key 
        self.assertTrue(len(test.groupby(['video_id','category_id','langauge']).groups) == test.shape[0])

    # test the type of error that is created when the path is incorrect 
    def testFile(self):
        try: 
            # supply an invalid path 
            hw3.create_dataframe("test")
        except Exception as err:
            self.assertTrue(isinstance(err,ValueError))

    
if __name__ == '__main__':
    unittest.main()