# test_with_unittest.py
from unittest import TestCase
from datahandler import datahandler
import pandas as pd

#create a datahandler object
data_handler = datahandler()

df1 = pd.DataFrame({
    "id": [1],
    "email":["a@gmail.com"],
    "firstname": ["Kenath"],
    "lastname":["Perera"]

})

df2 = pd.DataFrame({
    "id": [5,6,7],
    "email":["e@gmail.com","f@gmail.com","a@gmail.com"],
    "firstname": ["Robin","Kate","Kenath"],
    "lastname":["Griggs","Lewis","Perera"]

})

frames = [df1, df2]
concatResult = pd.concat(frames)

class MyTest(TestCase):
   def testRemoveDuplicatesByEmail(self):
      actualResult = data_handler.removeDuplicates(concatResult,'email')
      expectedResult = 3
      self.assertEqual(len(actualResult.index), expectedResult)

   def testRemoveDuplicatesByfirstName(self):
       actualResult = data_handler.removeDuplicates(concatResult, 'firstname')
       expectedResult = 3
       self.assertEqual(len(actualResult.index), expectedResult)

   def testRemoveDuplicatesById(self):
       actualResult = data_handler.removeDuplicates(concatResult, 'id')
       expectedResult = 4
       self.assertEqual(len(actualResult.index), expectedResult)

   def testRemoveDuplicates(self):
       actualResult = data_handler.removeDuplicates(concatResult, None)
       expectedResult = 4
       self.assertEqual(len(actualResult.index), expectedResult)