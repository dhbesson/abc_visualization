import requests, csv, sys, os, time, json, codecs

server = "https://cloudrf.com"

# dir = "calculations/antennas_1W_2m"


# Open CSV file
import codecs
# csvfile = csv.reader(codecs.open('antennas.csv', 'rU', 'utf-16'))

uid = 'YOUR CLOUDRF UID HERE'
key = 'YOUR CLOUDRF KEY HERE'


def calc_area(dir,csvfile_loc):
    n = 0
    csvfile = csv.DictReader(open(csvfile_loc))
    if not os.path.exists(dir):
        os.makedirs(dir)
    for row in csvfile:
        # Pause script. Important otherwise server will ban you.
        time.sleep(1)
        start_time = time.time()  # Stopwatch start
        # print row
        r = requests.post(server + "/API/area", data=row)
        print(r.text)
        # try:
        j = json.loads(r.text)

        r = requests.get(j['kmz'])
        fn = dir + os.sep + str(row['nam']) + ".kmz"
        file = open(fn, "wb")
        file.write(r.content)
        file.close()
        print("Saved to %s" % fn)


        elapsed = round(time.time() - start_time, 1)  # Stopwatch
        print("Elapsed: " + str(elapsed) + "s")
        n = n + 1