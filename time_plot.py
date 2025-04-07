# Import the numpy library which makes manipulating numbers easier
import numpy as np # Imported as np to make the code shorter and more efficient

# Import the matplotlib Library which is used to plot charts and graphs 
import matplotlib.pyplot as plt # Imported as plt in order to make the code more efficient


# Create values for the x axis using the arange module form the numpy library
times = np.arange(0, 100, 1) # start from 0 excluding 100 stepping by 1
# Generate 100 random numbers and get their cumulative sum using the cumsum module form the numpy library
values = np.cumsum(np.random.randn(100))

# Plot the graph
plt.plot(times, values) # times on the x axis and values on the y axis
# Display the graph
plt.show()
