import numpy as np

Pwr1_replaceable = float(100)
Pwr1_replace = np.around((10 * np.log10(Pwr1_replaceable * 1000)), decimals=1)

print(Pwr1_replace)