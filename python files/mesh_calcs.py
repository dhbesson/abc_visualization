import requests, sys, os, time
server="https://cloudrf.com"
format = "kmz" # kmz, shp, tiff, url, html

def calc_mesh(dir,net):
    # dir = "networks/mesh_1W_2m"
    if not os.path.exists(dir):
        os.makedirs(dir)

    def mesh(uid,net):
        r = requests.get(server+"/API/mesh/mesh.php?uid="+str(uid)+"&network="+net)
        print(r.text)
        result = r.text.split("/")
        fname = result[len(result)-1].split(".")[0]
        return fname

    def archiveDL(uid,key,fname,format):
        dlargs={'uid': uid, 'key': key, 'file': fname, 'fmt': format}
        r = requests.get(server+"/API/archive/data.php", params=dlargs)
        print(r.content)
        file = open(dir + os.sep + fname + "."+format,"wb")
        file.write(r.content)
        file.close()
        print("Wrote %d bytes to %s.%s" % (len(r.text),fname,format))


    uid = 'YOUR CLOUDRF UID HERE'
    key = 'YOUR CLOUDRF KEY HERE'
    # net = 'ABC_1W_2m'


    fname = mesh(uid,net)
    archiveDL(uid,key,fname,format)
