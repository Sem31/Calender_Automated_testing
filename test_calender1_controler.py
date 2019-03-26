import unittest
from date import Date_input
from controler2_check_dates import Date_events

class Check_data_events(unittest.TestCase):
    def test_check_data(self):
        #take date from the date UI
        date = Date_input.date_data()
        self.assertEqual(2,date)
        
        #check date have events or not
        k = Date_events.check_events(date)
        print("updated date = ",k)

if __name__ == "__main__":
    unittest.main()    