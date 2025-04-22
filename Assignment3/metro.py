"""
7 stations
3 skips
wall_touches = 0
for i between 0 -> stations+1 #8 in this case
    array[i].append(char(97+a)) This will print the list of stations
    # [a, b, c, d, e, f, g]
now_station = 0 #which indexes in the array to 'a'

while wall_touches < 5:
    for j between 0 -> skips #3 in this case
        now_station += skips
    print(arrray[j])
"""
stations = 10
skips = 3
wall_touches = 1
stations_map = []
#direction is a variable indicating the direction of the metro, if 1 then to the right(+ in index), if -1 then to the left(- in index)
direction = 1

#Makes the stations map
for i in range(0, stations):
    stations_map.append(chr(97+i))
now_station = 0
print(stations_map)
default = 0
default_skip = skips

print("Now is stop: " + stations_map[now_station])
#The train keeps running
while wall_touches < 5:
    # now_station += 1 * direction -1
    if default == 0:
        skips = skips - 1
    #Runs for 1, 2, 3
    for i in range(0, skips):
        #Every iteration skip, it will move the station by 1 multiplied by 1 or -1 to indicate direction
        now_station += 1*direction
        #At every skip/stop, checks if the train is at an end and counts it
        #This is for the first end

        if now_station == 0:

            wall_touches += 1

            #If the now_station is 0 which is 'a', it will move to the right
            direction = 1
        #This is for the second end
        elif now_station == stations - 1:
            wall_touches += 1
            #Once it reaches the right end, it will move to the left with -1
            direction = -1

    default += 1
    skips = default_skip

    print(stations_map[now_station], end='')


