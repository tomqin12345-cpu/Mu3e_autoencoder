#importing essential stuff
import uproot 
import awkward as ak
import numpy as np 
#location of the file 
FILE="/home/tg26549/training test data/mu3e_sim_test.root"

#Reading the pixel hits and detector geometry
with open(FILE, "rb") as stream:
    with uproot.open(stream) as root:
        hits = root["mu3e"].arrays(
            ["frameId", "Nhit", "hit_pixelid", "hit_timestamp"],
            library="ak",
        )

        sensors = root["alignment/sensors"].arrays(
            [
                "id", "nrow", "ncol",
                "vx", "vy", "vz",
                "rowx", "rowy", "rowz",
                "colx", "coly", "colz",
            ],
            library="np",
        ) 
#maps a sensor's id to its row in the geometry arrays 
sensor_lookup = {
    int(sensor_id): index
    for index, sensor_id in enumerate(sensors["id"])
} 
#check every frame 
frames=[]
