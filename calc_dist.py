from math import *

# opening files
f_cities = open('cities', 'r')
f_ll = open('cities_long_lat', 'r')
fout = open('amtrak_euc', 'w')

# writing city list - cities
buf = f_cities.readlines()
cities = [x.rstrip() for x in buf]
f_cities.close()

def haversines(la1, la2, lo1, lo2):
	p = pi/180
	a = 0.5 - cos((la2 - la1) * p)/2 + cos(la1 * p) * cos(la2 * p) * (1 - cos((lo2 - lo1) * p)) / 2
	return 12742 * asin(sqrt(a))

# writing long-lat list - long-lat
buf = f_ll.readlines()
f_ll.close()

long_lat = {}
for x in buf:
	x = x.rstrip().split(' ')
	long_lat[x[0]] = [x[1], x[2]]
for x in long_lat:
	long_lat[x][0] = float(long_lat[x][0])
	long_lat[x][1] = float(long_lat[x][1])
#print(long_lat.items())
# Haversines
for x in cities:
	for y in cities:
		if x == y:
			continue
		dist = haversines(long_lat[x][0], long_lat[y][0], long_lat[x][1], long_lat[y][1])
		print(x, y, dist, file=fout)
fout.close()
