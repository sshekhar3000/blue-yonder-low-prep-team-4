import csv
from classes import Demand

def store_demands(demands_file):
    demands = []
    with open(demands_file) as file:
        keys = ["WH", "Demand ID", "Item", "Day", "X", "Y", "Z", "DeliveryFrom", "DeliveryTo", "DeliveryFailure"]
        csvrf = csv.DictReader(file, keys)
        
        next(csvrf, None)
        for row in csvrf:
            demand = Demand()
            # demand.demand_id, demand.WH_id, demand.item_id, demand.day, demand.x, demand.y, demand.z, demand.del_start, demand.del_end = int(row["Demand ID"][-1]), int(row["WH"][-1]),  int(row["Item"][-1]), row["Day"], row["X"], row["Y"], row["Z"], row["DeliveryFrom"], row["DeliveryTo"]
            did = row["Demand ID"]
            did = did[did.index("D")+1:]
            did = int(did)
            demand.demand_id = did
            whid = row["WH"]
            whid = whid[whid.index("H")+1:]
            whid = int(whid)
            demand.WH_id = whid
            iid = row["Item"]
            iid = iid[iid.index("-")+1:]
            iid = int(iid)
            demand.item_id = iid
            day = row["Day"]
            day = day[day.index(" ")+1:]
            day = int(day)
            demand.day = day
            demand.x = row["X"]
            demand.y = row["Y"]
            demand.z = row["Z"]
            demand.del_start = row["DeliveryFrom"]
            demand.del_end = row["DeliveryTo"]
            demands.append(demand)
        
    return demands

