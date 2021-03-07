final_station = set()

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


def stations_needed():
    state_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    while state_needed:
        print "New round of check, state needed:", state_needed
        best_station = None
        best_state_covered = set()

        for station, state_for_station in stations.items():
            covered = state_needed & state_for_station
            print "Find best station for this round"
            print "current station", station, state_for_station, "covered", covered
            if len(covered) > len(best_state_covered):
                best_station = station
                best_state_covered = covered
        print "Best station: ", best_station
        state_needed -= best_state_covered
            # stations.remove(best_station)
        final_station.add(best_station)

stations_needed()
print final_station
