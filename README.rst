transposer
==========
You got columnar data? Turn that into row-wise data!! You got
row-wise data?? Turn it into columnar data!!! WUT?!?

(transposer transposes columns and rows in delimited text files)

What It Does
------------ 
transposer is a one-trick pony, but it's a good one-trick pony.
A simple command-line tool that can be used to effectively
transpose columnar data in a delimited file to row-wise data. EPIC.

Consider these three rows of data:

::

   FirstName|LastName|Age|Weight
   Sam|Simms|52|176
   Jane|Franklin|35|125

transposer would take these three rows, and transpose the data as follows:

::

   FirstName|Sam|Jane
   LastName|Simms|Franklin
   Age|52|35
   Weight|176|125

If you wanted to transform the row-wise data back into its former columnar self,
you would just run transposer against the transposed data.

transposer also works well with different types of delimiters, you just need
to declare which type you are working with (default is comma-separated).

But, Keith
----------
It's so easy to transpose that kind of data by hand. Why would I want to use 
a package for it?

Yeah, transposing three rows is easy to do by hand. Try 100,000. transposer will
do that work for you so you can do better things like watch reruns of The
Shawshank Redemption. You don't even have to write the data out to another file
you can also just hold onto it to do some wicked transforms before you dump
it to a flatfile. Up to you.

Installing
----------
Installing is easy, just use pip:

::
   
   $ pip install transposer

Or grab this repo and run:

::

   $ python setup.py install

Using
-----
transposer can be used both on the command line as well as in a Python project.

Command Line
~~~~~~~~~~~~

::

   $ transposer -i 'my_file.csv' -o 'out_file.csv'
   $ transposer -i 'my_file.txt' -d '|'
   $ transposer --in 'my_file.txt' -d '\t'

Module-based
~~~~~~~~~~~~
In your project file:

.. code-block:: python

   import transposer

   # this will output a file.
   transposer.transpose(i='cols.csv', o='rows.csv')
   
   # this will just keep the transposition in memory
   rows = transposer.transpose(i='cols.csv', o=None)

   # so will this
   rows = transposer.transpose(i='cols.csv')

   # the delimiter defaults to a comma. Use pipes too.
   transposer.transpose(i='cols.txt', o='rows.txt', d='|')


License
-------
transposer uses the MIT license, and is free for you.
