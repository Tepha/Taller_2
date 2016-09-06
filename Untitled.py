
# coding: utf-8

# In[15]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# $f(x) = \frac{e^x-e^-x}{e^x +e^-x}$

# In[16]:

x = np.linspace(-5, 5)
e = np.e
def f(x, e):
    return ((e ** x)-(e ** -x))/((e ** x)+(e ** -x))


# In[17]:

plt.plot(x, f(x, e), 'o')
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.grid(True)


# In[18]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


# $f(x)=\begin{cases} c & \text{si}& x\geq 0\\c & \text{si}& x<0\end{cases}$

# In[43]:

x = np.linspace(-5,5)
y = np.linspace(0,5)

def escalon(x, y):
    return np.piecewise(x, [x <= 0, x > 0], [0,1])
plt.plot(x, escalon(x,y))
plt.axis([x[0], x[-1], -0.1, 1.5])
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.grid(True)


# In[45]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt


#  $\digamma_k (x) =x$

# In[48]:

x = np.linspace(-5,5)

def linealmixta(x):
    return (x)
plt.plot(x, linealmixta(x), 'y')
plt.xlabel("Valor x")
plt.ylabel("Funcion f(x)")
plt.title('Funcion lineal')
plt.grid(True)


# In[ ]:




# In[ ]:



