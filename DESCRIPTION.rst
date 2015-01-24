transposer
==========
You got columnar data? Turn that into row-wise data!! You got
row-wise data?? Turn it into columnar data!!! SAY WUT?!?

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

But, Keith
----------
It's so easy to transpose that kind of data by hand. Why would I want to use 
a library for it?

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


License
-------
This is licensed under the BSD 3-Clause License. Feel free to fork, tweak, do 
whatever, as long as you attribute me. Or just rip it off, it's not like this
code is earth-shattering.
