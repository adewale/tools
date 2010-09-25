import simplejson
import httplib2
import sys 
print 'args were: %s' % str(sys.argv)
USAGE = """
Script for checking if a given path into a JSON object actually does what I think it does
python testpath.py <someurl for json data> <some path into the resulting json object>

Example:
python testpath.py "https://www.googleapis.com/buzz/v1/people/adewale/@self?alt=json" "['data']['kind']"
python testpath.py "https://www.googleapis.com/buzz/v1/people/adewale/@self?alt=json" "['data']['displayName']"

"""

if len(sys.argv) < 3:
	print USAGE
	sys.exit(1)


h = httplib2.Http(".cache")
resp, content = h.request(sys.argv[1], "GET")
json = simplejson.loads(content)
print json['data']['kind']
print eval("""json%s""" % sys.argv[2])

