#FUNCIONES ENVOLVENTES

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,128)
y=np.sin(x)
yy=np.cos(x)
fig,ax=plt.subplots(figsize=(3,3))
ax.set_title('Armonicas')
ax.plot(x,y, label="sen(x)", color='black')
ax.plot(x,yy, label="cos(x)", color="blue")
ax.legend()

plt.show()
