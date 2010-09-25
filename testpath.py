import simplejson
import httplib2
import sys 
print 'args were: %s' % str(sys.argv)
USAGE = """
Script for checking if a given path into a JSON object actually does what I think it does
python testpath.py <some url for json data|some local file path to a text file containing json data> <some path into the resulting json object>

Example:

Using remote URLs
python testpath.py "https://www.googleapis.com/buzz/v1/people/adewale/@self?alt=json" "['data']['kind']"
python testpath.py "https://www.googleapis.com/buzz/v1/people/adewale/@self?alt=json" "['data']['displayName']"

Working locally
curl -o json.data "https://www.googleapis.com/buzz/v1/people/adewale/@self?alt=json"
python testpath.py json.data "['data']['displayName']"
"""

if len(sys.argv) < 3:
	print USAGE
	sys.exit(1)

content_path = sys.argv[1]
json_path = sys.argv[2]

if content_path.startswith('http'):
	# Note the use of caching
	# This will probably bite me in the future. 
	h = httplib2.Http(".cache")
	resp, content = h.request(content_path, "GET")
	json = simplejson.loads(content)
else:
	json = simplejson.load(file(content_path))
print json['data']['kind']
print eval("""json%s""" % json_path)

