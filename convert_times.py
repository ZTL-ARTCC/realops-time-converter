import requests
import datetime as dt

uri = 'https://airplanemanager.com/flightcalculator'
airport_filename = 'airports.csv'
flights_filename = 'flights.csv'
airports = {}

def generate_airports():
    global airports

    f = open(airport_filename, 'r')

    i = 0
    for line in f:
        if i == 0:
            i = 1
            continue

        line_s = line.split(',')
        airports[line_s[13].strip('"')] = line_s[12].strip('"')

    f.close()

def generate_request(dep, arr):
    return {"token":None,"icaos":[airports[dep], airports[arr]],"deptDate":"2022-12-26","aircraftType":2,"windType":2,"runwayMinimumFT":0,"aircraftID":0}

def make_request(dep, arr):
    resp = requests.post(uri, json=generate_request(dep, arr))
    return resp.json()['minutes']

def run():
    flights = []
    f = open(flights_filename, 'r')
    for line in f:
        line_s = line.split(',')
        dep = line_s[3].split(' ')[-1].strip('(').strip(')')
        arr = line_s[4].split(' ')[-1].strip('(').strip(')')
        print(dep, arr)
        year = int(line_s[0].split('-')[0])
        mo = int(line_s[0].split('-')[1])
        day = int(line_s[0].split('-')[2])
        hr = int(line_s[5].strip().split(':')[0])
        mi = int(line_s[5].strip().split(':')[1])

        date = dt.datetime(year, mo, day, hr, mi) - dt.timedelta(minutes=make_request(dep, arr))

        flights.append([date.strftime('%Y-%m-%d'), line_s[1], date.strftime('%H:%M'), line_s[3], line_s[4], '', line_s[6].strip()])

    f.close()

    f = open(flights_filename, 'w')

    for flight in flights:
        f.write(','.join(flight) + '\n')

    f.close()

def main():
    generate_airports()
    run()
    
main()
