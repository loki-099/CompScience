import matplotlib.pyplot as plt #* FOR GRAPH
import math #* FOR FINDING SQUARE ROOT FOR EUCLIDIAN DISTANCE

data_points = [
    ([2, 3], "A"),
    ([5, 4], "A"),
    ([3, 6], "A"),
    ([8, 7], "B"),
    ([7, 5], "B"),
    ([9, 6], "B"),
    ([4, 8], "C"),
    ([6, 9], "C"),
    ([5, 7], "C")
] #* EXAMPLE DATA POINTS

for point, label in data_points: #* PLOTTING THE DATA POINTS
    plt.subplot(1,1,1)
    if label == "A":
        plt.scatter(point[0], point[1], color="red")
    elif label == "B":
        plt.scatter(point[0], point[1], color="blue")
    elif label == "C":
        plt.scatter(point[0], point[1], color="yellow")

def dist(dist): #* SORTING KEY 
    return dist[0]

def calculateDistance(x,y): #* FUNCTION TO CALCULATE EUCLIDIAN DISTANCE FROM NEW POINT TO EXISTING POINTS
    distances = []
    for point, label in data_points:
        distance = math.sqrt((x - point[0]) ** 2  + (y - point[1]) ** 2)
        distances.append([distance, label])
    distances.sort(key=dist)
    return distances

def clusterfy(x, y, k=4): #* FUNCTION TO CLASSIFY NEW POINT, DEFAULT VALUE FOR K is 4
    distances = calculateDistance(x,y)
    labels = {'A': 0, 'B': 0, 'C': 0}
    for distance, label in distances[:4]:
        labels[label] += 1
    calculatedLabel = max(labels, key=labels.get) 

    print(f"NEW POINT({x},{y}) IS CALCULATED AS CLASS: {calculatedLabel}")
    print(labels)


plt.scatter(6,5, color="green")
clusterfy(6,5)
plt.title("KNN Graph")
plt.show()

