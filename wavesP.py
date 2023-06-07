#TP  Waves : 

# Modules 
import numpy as np
import matplotlib.pyplot as plt

#  ---------------------------Figures Seperated -------------------------------------------------
# Wave with CC :
 
 
p = np.arange(3.5,10.6,0.1)    # Position for wave from 3.5 cm untile 10.5 cm  
A1 = np.array([4.33,7.27,8.51,8.13,7.28,6.35,5.96,4.90,3.68,2.54,1.88,1.03,0.75,2.75,0,0,0,0.37,0.75,1.23,2.64,3.58,3.30,2.25,1.13,0.65,0.83,1.23,1.13,0.83,0.37,0,0.375,0.938,1.41,1.88,2.45,2.83,2.83,2.64,1.98,1.31,1.03,0.65,0.37,0,0,0,0.75,2.08,3.76,4.33,3.68,2.83,2.25,1.69,1.88,2.35,2.35,2.08,1.41,0.75,0.27,0,0,0,0,0.3,0.75,0.69,3.49])

# show figure 1 as test  position and amplitude for first wave :
plt.figure()
plt.plot(p,A1, c= "blue", label="CC")
plt.xlabel("Position(cm)",fontweight = "bold")
plt.ylabel("Amplitude(mV)",fontweight= "bold")
plt.title("Court Circuit", fontweight= "bold")
plt.grid()
plt.legend()
#plt.set_size_inches(18.5, 10.5)
plt.savefig("figure1.png")
plt.show()



# Wave with CO:
#  The positions are the same but amplitude is not so 
A2 = np.array([0.27,0.0375,0.46,0.83,1.31,1.79,2.54,3.01,3.01,2.45,1.88,1.61,1.60,1.50,1.31,1.28,1.28,1.31,1.50,1.50,1.31,1.28,1.31,1.41,1.41,1.41,1.41,1.50,1.69,1.61,1.31,1.28,0.65,0.46,0.37,0.27,0.27,0.46,0.46,0.56,0.46,0.37,0.37,0.46,0.46,0.46,0.37,0.27,0,0.27,0.46,0.83,1.13,1.41,1.79,2.25,2.83,3.30,3.30,3.10,2.54,2.25,1.88,1.60,1.60,1.96,1.88,1.98,1.88,1.50,1.13])

# Plot Figure containe Wave with CO
plt.figure()
plt.plot(p,A2,c= "orange", label= "CO")
plt.xlabel("Position(cm)", fontweight= "bold")
plt.ylabel("Amplitude(mV)", fontweight= "bold")
plt.title("Court Overt", fontweight="bold")
plt.grid()
plt.legend()
plt.savefig("figure2.png")
plt.show() # show the Figure of CO 


# Wave with Charge : 
A3 = np.array([0,0.37,0.56,0.83,1.31,1.69,1.88,1.88,1.69,1.13,0.56,0.46,0.37,0.27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.46,0.56,0.65,0.75,1.03,1.28,1.50,1.31,1.13,1.65,1.46,0,0,0,0,0,0,0,0,0,0.27,0.37,0.37,0.37,0.46,0.46,0.56,0.56,0.46,0.30,0.27,0.27,0,0,0.27,0.27,0.27,0.27,0.27,0,0])

# Plot Figure containe Wave with Charge:

plt.figure()
plt.plot(p,A3, c= "green", label= "CH adatée")
plt.xlabel("Position(cm)", fontweight="bold")
plt.ylabel("Amplitude(mV)", fontweight="bold")
plt.title("Charge Adaptée ", fontweight="bold")
plt.legend()
plt.grid()
plt.savefig("figure3.png")
plt.show()  # show figure of 



# show all figures together seperated with subplot :
plt.figure()
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1) #adjust some space so we can see axes and no interaction btw it and the Titles 
plt.subplot(3,1,1)
plt.plot(p,A1, c="blue", label="CC")
plt.xlabel("Position(cm)", fontweight="bold")
plt.ylabel("Amplitude(mV)", fontweight="bold")
plt.title("Court Circuit", fontweight="bold")
plt.legend()
plt.grid()


plt.subplot(3,1,2)
plt.plot(p,A2, c="orange", label="CO")
plt.xlabel("Position(cm)", fontweight="bold")
plt.ylabel("Amplitude(mV)", fontweight="bold")
plt.title("Court Overt ", fontweight="bold")
plt.legend()
plt.grid()


plt.subplot(3,1,3)
plt.plot(p,A3, c="green", label="CH")
plt.xlabel("Position(cm)",fontweight="bold")
plt.ylabel("Amplitude (mV)",fontweight="bold")
plt.title("Charge Adaptée",fontweight="bold")
plt.legend()
plt.grid()
plt.savefig("figure4.png")

plt.show()# show the graph 



# show all graphes in just one figure and one and one plot :

plt.figure()

plt.plot(p,A1, c="blue", label="CC") # wave with CC

plt.plot(p,A2, c="orange", label="CO")  # wave with CO

plt.plot(p,A3, c="green", label="CH adaptée")  # wave with CH

plt.xlabel("Position (cm)",fontweight="bold")
plt.ylabel("Amplitude(mV)",fontweight="bold")
plt.title("Court Circuit,Overt, Charge Adaptée",fontweight="bold")
plt.legend()
plt.grid()
plt.savefig("figure5.png")

plt.show()# show the graph 

