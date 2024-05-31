import matplotlib.pyplot as plt
import numpy as np

# Example data: replace these with your actual data
house_points = [133, 129, 125, 121, 108, 104, 98, 94, 93]  # X values
house_price_limits = [820.42,794.31,768.27, 742.21, 657.45, 631.40, 592.31, 566.21, 559.71]  # Y values
house_energy_labels = ['A++', 'A+', 'A', 'B', 'C', 'D', 'E', 'F', 'G']  # Labels for the points

# Calculate the linear fit
slope, intercept = np.polyfit(house_points, house_price_limits, 1)

# Create the linear fit line
fit_line = np.polyval([slope, intercept], house_points)

# Create the plot
plt.figure(figsize=(10, 8))  # Increased height to add text below

# Plot the house price limits
plt.plot(house_points, house_price_limits, marker='o', linestyle='-', color='b', label='House Price Limits')

# Plot the linear fit line
plt.plot(house_points, fit_line, linestyle='--', color='r', label=f'Linear Fit: y={slope:.2f}x+{intercept:.2f}')

# Annotate each data point with the corresponding energy label
for i, label in enumerate(house_energy_labels):
    plt.annotate(label, (house_points[i], house_price_limits[i]), textcoords="offset points", xytext=(0, 10), ha='center')

# Add titles and labels
plt.title('House Price Limits vs House Points')
plt.xlabel('House Points')
plt.ylabel('House Price Limits')
plt.legend()

# Add a finer grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add details of the measurements below the plot
measurement_details = (
    "Measurements details:\n"
    "House Points: Represents the energy efficiency points of houses.\n"
    "House Price Limits: Represents the price limits for houses in thousands.\n"
    "Energy Labels: Correspond to the energy efficiency rating of houses (A++ to G)."
)
plt.figtext(0.1, -0.1, measurement_details, wrap=True, horizontalalignment='left', fontsize=10)

# Adjust layout to make room for the text
plt.tight_layout(rect=[0, 0.05, 1, 1])

# Show the plot
plt.show()
