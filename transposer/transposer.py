#!/usr/bin/python
'''
takes contents of delimited file and transposes columns and rows
outputs to txt file
'''
import argparse

def transpose(i, o=None, d=','):
    f = open (i, 'r')
    file_contents = f.readlines ()
    f.close ()

    out_data = map((lambda x: d.join([y for y in x])),
                   zip(* [x.strip().split(d) for x in file_contents if x]))
    if o:
        f = open (o,'w')

        # here we map a lambda, that joins the first element of a column, the 
        # header, to the rest of the members joined by a comma and a space. 
        # the lambda is mapped against a zipped comprehension on the 
        # original lines of the csv file. This groups members vertically
        # down the columns into rows. 
        f.write ('\n'.join (out_data))
        f.close ()

    return out_data

