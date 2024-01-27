#############################

#Matplotlib Additional  Plot Features


#############################

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x_squared = [ x **2 for x in x_values]

x_cubed = [ x **3 for x in x_values]


plt.plot(x_values,x_squared)
plt.plot(x_values,x_cubed)
plt.title("Exponential  Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of y")
plt.show()

############ Adding Labels

plt.plot(x_values,x_squared, label =" X Sqaured")
plt.plot(x_values,x_cubed, label =" X Cubed")
plt.title("Exponential  Growth")
plt.xlabel("The Value of X")
plt.ylabel("The Value of y")
plt.legend()
plt.show()

############## Changing limit on axis

plt.plot(x_values,x_squared, label =" X Sqaured")
plt.plot(x_values,x_cubed, label =" X Cubed")
plt.title("Exponential  Growth")
plt.xlabel("The Value of X")
plt.xlim(2,8)
plt.ylabel("The Value of y")
plt.ylim(-100,800)
plt.legend()
plt.show()

############## Addding grid

plt.plot(x_values,x_squared, label =" X Sqaured")
plt.plot(x_values,x_cubed, label =" X Cubed")
plt.title("Exponential  Growth")
plt.xlabel("The Value of X")
plt.xlim(2,8)
plt.ylabel("The Value of y")
plt.ylim(-100,800)
plt.grid(True)
plt.legend()
plt.show()

######### Adding our own x/y values


plt.plot(x_values,x_squared, label =" X Sqaured")
plt.plot(x_values,x_cubed, label =" X Cubed")
plt.title("Exponential  Growth")
plt.xlabel("The Value of X")
plt.xticks(range(11))
plt.ylabel("The Value of y")

plt.legend()
plt.show()

###Empty axis values
plt.plot(x_values,x_squared, label =" X Sqaured")
plt.plot(x_values,x_cubed, label =" X Cubed")
plt.title("Exponential  Growth")
plt.xlabel("The Value of X")
plt.xticks([])
plt.ylabel("The Value of y")
plt.yticks([])
plt.legend()
plt.show()


