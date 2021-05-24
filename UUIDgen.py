import urllib.request		#pip install concat("urllib", number of current version)

my_request = urllib.request.urlopen("https://www.uuidgenerator.net/api/version4")

my_HTML = my_request.read().decode("utf8")

print(my_HTML)