import urllib.parse
import sys

arguments = len(sys.argv)

if arguments != 2:
        print( "Error parsing \nExpected Use case\npython3 urlencode.py \"some&&&&&texttoencode???\"")
        exit()
new_string= urllib.parse.quote_plus(sys.argv[1])

print(new_string)
