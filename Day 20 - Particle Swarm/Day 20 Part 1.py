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
    closest = min(distances,key=distances.get)
    print closest
    for i in range(1000):
        for j in range(3):
            velocities[i][j] += accelerations[i][j]
            locations[i][j] += velocities[i][j]
        distances[i] = abs(locations[i][0]) + abs(locations[i][1]) + abs(locations[i][2])
    new_closest = min(distances,key=distances.get)
    if closest == new_closest:
        unchanged_counter += 1
    else:
        unchanged_counter = 0
    print new_closest
    