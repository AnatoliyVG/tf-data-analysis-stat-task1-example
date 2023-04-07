import pandas as pd
import numpy as np

chat_id = 1399245853 


def estimate_acceleration(path_measurements):
    median = np.median(path_measurements) # оценка медианы
    acceleration = 2 * median / 49 # формула для коэффициента ускорения
    return acceleration

    
     

path_measurements = np.array([10, 12, 9, 11, 10.5])
acceleration = estimate_acceleration(path_measurements)
print(acceleration)
