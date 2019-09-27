import numpy

def pearson (x, y):
    if (len(x) != len(y)):
        # if the two data sets are not of equal length, then Pearson's Correlation Coefficient 
        # cannot be calculated so the function will end
        print("Error: length of set X is not equal to length of set Y.")
        return
    
    setLen = len(x)         # assigns the length of x and y to a variable
    
    stdX = numpy.std(x)     # calculates the standard deviation of the set X
    stdY = numpy.std(y)     # calculates the standard deviation of the set Y
    avgX = numpy.mean(x)    # calculates the mean of the set X
    avgY = numpy.mean(y)    # calculates the mean of the set X

    sum = 0                 # sum is a variable used to calculate the numberator of Pearson's Correlation Coefficient
    
    
    for i in range(setLen):
        sum = sum + ((x[i] - avgX) * (y[i] - avgY))
    
    num = sum / setLen      # num is the numerator of Pearson's Correlation Coefficient
    den = stdX * stdY       # den is the denominator of Pearson's Correlation Coefficient
    return num / den

# for listX and listY, each value in the array listX makes a pair with the corresponding value
# in the array listY   Example: listX[0] and listY[0] make (14, 2)
listX = [14, 16, 27, 42, 39, 50, 83]    # listX is the set of X values
listY = [2, 5, 7, 9, 10, 13, 20]        # listY is the set of Y values

print(pearson(listX, listY))            # executes the function pearson() using listX and listY and prints the result