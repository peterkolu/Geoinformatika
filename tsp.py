import csv, random
import matplotlib.pyplot as plt

#input_file="C:\\Users\\lucip\\Desktop\\fleska\\mgr_1_zimni\\geoinformatika\\tsp\\zeleznice.txt"
input_file="C:\\Users\\lucip\\Desktop\\fleska\\mgr_1_zimni\\geoinformatika\\tsp\\mesta.txt"

coord = []

with open(input_file) as file:
    reader = csv.reader(file)
    for row in reader:
        coord.append([float(row[0]), float(row[1])])


def nearest_neighbor(coordinates):
    '''The algorithm starts by randomly selecting a starting city from a list of cities. 
    It then goes through the remaining cities, always adding the closest city to the current path.'''

    # choose a random city as the first city of the trip
    start = random.choice(coordinates)
  
    # create a list of visited cities
    path = [start]
    total_distance = 0.0
  
    # browse the remaining cities and add the nearest city
    for i in range(1, len(coordinates)):
        #setting infinity
        nearest_city = None
        nearest_distance = float("inf")
        for j in range(len(coordinates)):
            coord = coordinates[j]
            #if the coord element has not been visited yet, find the distance between it and the last element visited
            if coord not in path:
                d = ((coord[0] - path[-1][0]) ** 2 + (coord[1] - path[-1][1]) ** 2) ** 0.5
                if d < nearest_distance:
                    nearest_city = coord
                    nearest_distance = d
        path.append(nearest_city)
        total_distance += nearest_distance
  
    # add the distance from the last visited city to the starting point
    path.append(start)
    total_distance += ((path[-1][0] - path[0][0]) ** 2 + (path[-1][1] - path[0][1]) ** 2) ** 0.5

    # graph
    x = [coord[0] for coord in coordinates]
    y = [coord[1] for coord in coordinates]
    path_x = [coord[0] for coord in path]
    path_y = [coord[1] for coord in path]
    plt.scatter(x, y, color="red")
    plt.plot(path_x, path_y, color="blue")
    plt.title('Nearest Neighbor')
    plt.show()
  
    return total_distance

def distance_between(point1, point2):
    '''returns the distance between two points'''

    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def best_insertion(coordinates):
    '''The algorithm starts by randomly selecting two cities as the start 
    and end of a trip. It then traverses the remaining cities and selects the 
    best place to insert them into the path to minimize the total distance '''

   # choose a random city as the first city of the trip
    start = random.choice(coordinates)
    path = [start]

    # choose a second city at random from the remaining cities
    second = random.choice([point for point in coordinates if point != start])
    path.append(second)
    distance = distance_between(start, second)

    # for each city outside the first
    for i in range(len(coordinates)):
        if coordinates[i] == start:
            continue
        # choose the best place to insert this city
        best_distance = float("inf")
        best_index = 0
        for j in range(1, len(path)):
            # check if inserting a city at this location causes the smallest total distance
            new_distance = distance + distance_between(coordinates[i], path[j-1]) + distance_between(coordinates[i], path[j]) - distance_between(path[j-1], path[j])
            if new_distance < best_distance:
                best_distance = new_distance
                best_index = j

        # put the city in the best place and update the total distance
        path.insert(best_index, coordinates[i])
        distance = best_distance

    # add the city where the journey started to the end of the journey
    path.append(start)
    distance += distance_between(path[-1], path[-2])

    # list of x- and y-coordinates for each city
    x = [point[0] for point in coordinates]
    y = [point[1] for point in coordinates]

    # list of x- and y-coordinates for a route between cities
    path_x = [point[0] for point in path]
    path_y = [point[1] for point in path]

    # graph
    plt.scatter(x, y, color="red")
    plt.plot(path_x, path_y, color="blue")
    plt.title('Best Insertion')
    plt.show()
    
    return distance

print("Nearest Neighbor total distance: ",round(nearest_neighbor(coord), 3), "m")
print("Best Insertion total distance: ",round(best_insertion(coord), 3), "m")

