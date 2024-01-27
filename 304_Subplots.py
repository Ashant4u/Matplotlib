#############################

#Matplotlib   SubPlots 


#############################


import matplotlib.pyplot as plt

x_values = [0, 1, 2 , 3 , 4, 5, 6, 7, 8, 9 , 10]
x_squared = [ x ** 2 for x in x_values]
x_cubed  =  [x ** 3 for x in x_values]

plt.subplot(2, 1, 1)
plt.plot(x_values, x_squared, label = "X Squared")
plt.title("X Squared")
plt.xlabel("X")
plt.ylabel("X Squared")


plt.subplot(2, 1, 2) # Number of rows of plot 
plt.bar(x_values, x_cubed, label = "X Cubed")
plt.title("X Cubed")
plt.xlabel("X")
plt.ylabel("X Cubed")
plt.tight_layout()
plt.show()


####### 2 sub plots in column
plt.subplot(1, 2, 1)
plt.plot(x_values, x_squared, label = "X Squared")
plt.title("X Squared")
plt.xlabel("X")
plt.ylabel("X Squared")
plt.subplot(1, 2, 2) # Number of rows of plot 
plt.bar(x_values, x_cubed, label = "X Cubed")
plt.title("X Cubed")
plt.xlabel("X")
plt.ylabel("X Cubed")
plt.tight_layout()
plt.show()





plt.subplot(2, 2, 1)
plt.plot(x_values, x_squared, label = "X Squared")
plt.title("X Squared")
plt.xlabel("X")
plt.ylabel("X Squared")
plt.subplot(2, 2, 2) # Number of rows of plot 
plt.bar(x_values, x_cubed, label = "X Cubed")
plt.title("X Cubed")
plt.xlabel("X")
plt.ylabel("X Cubed")
plt.subplot(2, 2, 3)
plt.plot(x_values, x_squared, label = "X Squared")
plt.title("X Squared")
plt.xlabel("X")
plt.ylabel("X Squared")
plt.subplot(2, 2, 4) # Number of rows of plot 
plt.bar(x_values, x_cubed, label = "X Cubed")
plt.title("X Cubed")
plt.xlabel("X")
plt.ylabel("X Cubed")
plt.tight_layout()
plt.show()
plt.tight_layout()
plt.show()