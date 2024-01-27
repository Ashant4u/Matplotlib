#############################

#Matplotlib Our First Plot


#############################

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_squared = [ x **2 for x in x_values]

plt.plot(x_values, x_squared)

plt.show()


plt.plot(x_values, x_squared)
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.show()

import pandas as pd

my_df = pd.DataFrame({"X": x_values, 
                      "Y": x_squared})
plt.plot(my_df["X"], my_df["Y"])
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.show()