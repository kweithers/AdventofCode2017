import itertools
f = open("day20.txt","r")
data = f.read().splitlines()
locations = {}
velocities = {}
accelerations = {}
distances = {}
for i in range(len(data)):
    j = list(map(int,data[i].translate(None,'pva=<>').split(',')))
    locations[i] = j[0:3]
    velocities[i] = j[3:6]
    accelerations[i] = j[6:9]
    distances[i] = abs(j[0]) + abs(j[1]) + abs(j[2])

unchanged_counter = 0
while unchanged_counter < 1000:
    particles_left = len(locations)
    
    for i in locations.keys():
        for j in range(3):
            velocities[i][j] += accelerations[i][j]
            locations[i][j] += velocities[i][j]
        distances[i] = abs(locations[i][0]) + abs(locations[i][1]) + abs(locations[i][2])
    to_remove = []
    for a,b in itertools.product(locations.keys(),locations.keys()):
        if a != b:
            try:
                if locations[a] == locations[b]:
                    to_remove.append(a)
                    to_remove.append(b)
            except KeyError:
                pass   
        
    for c in list(set(to_remove)):
        del(locations[c])
        
    new_particles_left = len(locations)
    if particles_left == new_particles_left:
        unchanged_counter += 1
    else:
        unchanged_counter = 0    

print len(locations)