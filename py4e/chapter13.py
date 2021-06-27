# Chapter 13 Exercise
import json 
import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Autograder XML
url = "http://py4e-data.dr-chuck.net/comments_1281874.xml"
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = sum([int(a.text) for a in counts])
print(total)

# Autograder JSON
url = "http://py4e-data.dr-chuck.net/comments_1281875.json"
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)
print(sum([int(a["count"]) for a in info["comments"]]))