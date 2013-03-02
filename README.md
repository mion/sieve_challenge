# Sieve Challenge

Make sure you're connected to the Interwebs, then run:

	$ python script.py

And you should see my answer to the challenge :-)

HTTP handling is done via [Requests](http://docs.python-requests.org/en/latest), so make sure you have it installed.

## A few notes
* The ``Price`` class (implemented in ``price.py``) is responsible for price parsing;
* A small suite of tests is provided in ``test_price.py``;
* I'm only parsing the HTTP response text in one shot because I know there's only *one price* in it. In a real life situation, putting it through some XML/HTML parsing library beforehand would be required;
* You could parse the price using a *regular expression*, but I think it would be more error-prone in this (simple) case;

## Output
File ``output.txt`` contains the output on my machine (Ubuntu 12.10, Python 2.7.3).
