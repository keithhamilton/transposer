import os.path
import unittest

import transposer


class TestTransposer(unittest.TestCase):


    def test_column_to_row_with_write(self):
        test_in_file = '/tmp/in.csv'
        test_out_file = '/tmp/rows.csv'
        
        test_in_data = [
            ['FirstName', 'LastName', 'Age'],
            ['Frank', 'Jones', '42'],
            ['Samantha', 'Clemons', '24'],
            ['Keith', 'Hamilton', '35'],
        ]

        # write test in data
        f = open(test_in_file, 'w')
        for l in test_in_data:
            f.write(','.join(l) + '\n')
        f.close()
        
        out_data = transposer.transpose(i=test_in_file, o=test_out_file, d=',')
        
        # read in output
        f = open(test_out_file, 'r')
        lines = f.readlines()
        f.close()

        self.assertEqual(['FirstName', 'Frank', 'Samantha', 'Keith'], 
                         lines[0].strip().split(','))
        self.assertEqual('LastName,Jones,Clemons,Hamilton', lines[1].strip())
        self.assertEqual('Age,42,24,35', lines[2].strip())

        for i, x in enumerate(out_data):
            self.assertEqual(out_data[i], lines[i].strip())


    def test_row_to_column_no_write(self):
        original_in_file = '/tmp/in.csv'
        test_in_file = '/tmp/rows.csv'
        test_out_file = '/tmp/cols.csv'
        
        out_data = transposer.transpose(i=test_in_file, o=None, d=',')
        
        self.assertFalse(os.path.exists(test_out_file))

        # read in original input
        g = open(original_in_file, 'r')
        original_lines = g.readlines()
        g.close()
        
        for i, x in enumerate(out_data):
            self.assertEqual(out_data[i].strip(), original_lines[i].strip())
        

    def test_auto_detect_delimiter(self):
        tab_delimited = 'FirstName\tLastName\tAge\tWeight'
        comma_delimited = 'FirstName,LastName,Age,Weight'
        pipe_delimited = 'FirstName|LastName|Age|Weight'
        
        csv_with_quotes = '"FirstName","LastName","Weight"'

        self.assertEqual(transposer.detect_delimiter(tab_delimited), '\t')
        self.assertEqual(transposer.detect_delimiter(comma_delimited), ',')
        self.assertEqual(transposer.detect_delimiter(pipe_delimited), '|')
        self.assertEqual(transposer.detect_delimiter(csv_with_quotes), ',')
        
if __name__ == '__main__':
    unittest.main()
