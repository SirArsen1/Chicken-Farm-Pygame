Nest_Surfaces = [ # occupied is a check whether the surface is taken by chicken sprite
    {"surface":None, "occupied":False, "object":None, "visibility":False, "hp_pos":(114,79)},
    {"surface":None, "occupied":False, "object":None, "visibility":False, "hp_pos":(336,79)},
    {"surface":None, "occupied":False, "object":None, "visibility":False, "hp_pos":(558,79)}
]

def get_nest_surface_data():
    return [
        {k: d[k] for k in ("occupied", "object", "visibility")}
        for d in Nest_Surfaces
    ]

get_nest_surface_data()
print(get_nest_surface_data())