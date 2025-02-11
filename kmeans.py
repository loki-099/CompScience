import math

def euclidianDistance(p1, p2): #* FUNCTION FOR FINDING THE EUCLIDIAN DISTANCE
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kmeans_clustering(dataPoints, initialCentroids, maxIterations=10):
    k = len(initialCentroids)
    centroids = [list(c) for c in initialCentroids]  #* COPY OF INITIAL CENTROIDS
    
    for iteration in range(1, maxIterations + 1):
        clusters = {i: [] for i in range(k)}
        
        #* ASSIGN EACH DATA POINT TO THE NEAREST CENTROID
        for point in dataPoints:
            distances = [euclidianDistance(point, centroid) for centroid in centroids]
            closestCluster = distances.index(min(distances))
            clusters[closestCluster].append(point)
        
        print(f"Iteration {iteration}:")
        for i in range(k):
            print(f"  Cluster {i+1}: {clusters[i]}")
        
        #* COMPUTE NEW CENTROIDS
        newCentroids = []
        for i in range(k):
            if clusters[i]:
                x_sum = sum(point[0] for point in clusters[i]) / len(clusters[i])
                y_sum = sum(point[1] for point in clusters[i]) / len(clusters[i])
                newCentroids.append([x_sum, y_sum])
            else:
                newCentroids.append(centroids[i])  #* RETAIN OLD CENTROID IF NO POINTS ASSIGNED
        
        print("  Centroid movement:")
        for i in range(k):
            print(f"    Old: {centroids[i]}, New: {newCentroids[i]}")
        
        #* CHECK FOR CONVERGENCE (IF CENTROIDS DON'T CHANGE)
        if newCentroids == centroids:
            print("Centroids have stabilized. Stopping iterations.")
            break
        
        centroids = newCentroids  #* UPDATE CENTROIDS
    
    #* FINAL CLUSTER ASSIGNMENT
    print("\nFinal Classification:")
    for i in range(k):
        print(f"  Cluster {i+1}: {clusters[i]}")
    print(f"  Final Centroids: {centroids}")

#* DATA POINTS AND INITIAL CENTROIDS
dataPoints = [[2,10], [2,5], [8,4], [5,8], [7,5], [6,4], [1,2], [4,9]]
initialCentroids = [[2,10], [5,8], [1,2]]

#* RUN K-MEANS CLUSTERING
kmeans_clustering(dataPoints, initialCentroids)