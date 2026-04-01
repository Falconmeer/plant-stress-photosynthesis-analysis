import pandas as pd
import matplotlib.pyplot as plt
# Example dataset including photosynthetic efficiency
data = {
    "Chlorophyll": [35, 40, 38, 42],
    "Temperature": [28, 30, 32, 31],
    "FvFm": [0.78, 0.75, 0.72, 0.74]  # Photosynthetic efficiency
}
df = pd.DataFrame(data)
# Summary statistics
print(df.describe())
# Scatter plot: Chlorophyll vs Photosynthetic Efficiency
df.plot(kind='scatter', x='Chlorophyll', y='FvFm')
plt.show()
