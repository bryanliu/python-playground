# coding=utf-8
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])


final_state = set()

def stations_needed():
    state_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    selected_station = []

    while state_needed:

        best_station_needed_covered = set()
        best_station = None

        for station, state_covered in stations.items():
            station_needed_covered = state_needed & state_covered
            if len(station_needed_covered) > len(best_station_needed_covered):
                best_station = station
                best_station_needed_covered = station_needed_covered

        state_neded -= best_station_needed_covered
        final_state.add(best_station)

stations_needed()
print final_state

'''
set 初始化是 set(), 而不是 () , () 是元组的初始化方式
集合的交集 & ，并集 |，差集 使用要注意
set 是 add  不是 append
'''