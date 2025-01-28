import matplotlib.pyplot as plt

# Given Data
weights = [140, 155, 159, 179, 192, 200, 212] # variable X
heights = [60, 62, 67, 70, 71, 72, 75] # variable Y

# Get the Slope and Intercept from Given Data
def getSlopeAndIntercept(weights, heights):
    n = len(weights)
    sumOfX = sum(weights)
    sumOfY = sum(heights)
    sumOfXY = sum(list(map(lambda x, y: x * y, weights, heights)))
    sumOfXSquared = sum(list(map(lambda x: x * x, weights)))
    sumOfXThenSquared = sumOfX * sumOfX

    slope = ((n * sumOfXY) - (sumOfX * sumOfY)) / ((n * sumOfXSquared) - sumOfXThenSquared) # Formula for Slope
    intercept = (sumOfY - (slope * sumOfX)) / n # Formula for Intercept

    print(f"Slope: {slope} \nIntercept: {intercept}")
    return slope, intercept


slope, intercept = getSlopeAndIntercept(weights, heights)


# Return list of y values from our linear function
def linearFunction(weights):
    y = []
    for x in weights:
        y.append(intercept + slope * x) # Formula for Linear Regression
    return y

# Plotting the Graph
plt.title("Linear Regression")
plt.plot(weights, linearFunction(weights), label="Regression Line")
plt.scatter(weights, heights, c="red", label="Actual Given Data")
plt.xlabel("Weights(lbs)")
plt.ylabel("Heights(inches)")
plt.legend(loc='best')
plt.show()