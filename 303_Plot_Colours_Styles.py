#############################

#Matplotlib   Plot Colours And Style


#############################

import matplotlib.pyplot as plt

x_values = [0, 1, 2 , 3 , 4, 5, 6, 7, 8, 9 , 10]
x_squared = [ x ** 2 for x in x_values]
x_cubed  =  [x ** 3 for x in x_values]

plt.plot(x_values, x_squared, label = "X Squared")
plt.plot(x_values, x_cubed, label = "X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()

###Adding color

plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink")
plt.plot(x_values, x_cubed, label = "X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()

###Adding Color RGB Value

plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink")
plt.plot(x_values, x_cubed, label = "X Cubed", color = [1.0,0.5,0.25])
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()

###Adding Color Hex Value

plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink")
plt.plot(x_values, x_cubed, label = "X Cubed", color = "#0000FF")
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()

###Adding Line Width

plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink", linewidth = 3)
plt.plot(x_values, x_cubed, label = "X Cubed", color = "#0000FF", linewidth = 0.5)
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()


########## Adding line style
plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink", linewidth = 2, linestyle ="--")
plt.plot(x_values, x_cubed, label = "X Cubed", color = "#0000FF", linewidth = 2,linestyle =":")
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()

###Adding Markers
plt.plot(x_values, x_squared, label = "X Squared", color = "deeppink", linewidth = 2, marker =".")
plt.plot(x_values, x_cubed, label = "X Cubed", color = "#0000FF", linewidth = 2,marker ="o", markersize = 10, markerfacecolor = "red", markeredgecolor = "green")
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()


##Check style type available

plt.style.available
plt.style.use('seaborn-v0_8-dark-palette')

plt.plot(x_values, x_squared, label = "X Squared")
plt.plot(x_values, x_cubed, label = "X Cubed")
plt.title("Exponential Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of Y")
plt.legend()
plt.show()
