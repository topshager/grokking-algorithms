states_needed = set(["mt","wa","or","id","nv","ut","ca","az"]) # this is the states

stations = {}

#-Radio stations-
stations["kone"] = set(["id","nv","ut"])
stations["ktwo"] = set(["wa","id","mt"])
stations["kthree"] = set(["or","nv","ca"])
stations["kfour"] = set(["nv","ut"])
stations["kfive"] = set(["ca","az"])

final_stations = set() # creating a set for final station's

best_station = None
states_covered = set() #list of already processed  item's

for station, states_for_station in stations.items(): # assingnes station to key in station hash and states_for_station is assigned to  value for key
    covered = states_needed & states_for_station # intersection between  states_needed and states_for_station
    if len(covered) > len(states_covered):
        best_station = station
        states_covered  = covered
        final_stations.add(best_station)
        states_needed -= states_covered

    while states_needed:
        best_station = Nonestate_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station  = station
                states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
    print(final_stations)
