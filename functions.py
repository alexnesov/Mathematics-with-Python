import pandas as pd
import plotly.graph_objects as go
import numpy as np
import math
x = np.arange(-5,6)



# Very useful resource https://www.python-course.eu/polynomial_class_in_python.php
def ownpow(a, b):
    """
    """
    if a > 0:
        return a**b
    if a < 0:
        temp = abs(a)**b
        return -1*temp
    if a==0:
        return 0


# even function
fig = go.Figure(data=go.Scatter(x=x, y=x**2))
fig.update_layout(title="even function")
fig.show()


# quadratic parabola
# x² - 4
y = [x**2+2*x+3 for x in x]
fig = go.Figure(data=go.Scatter(x=x, y=y))
fig.update_layout(title="quadratic parabola")
fig.show()


# odd function
fig = go.Figure(data=go.Scatter(x=x, y=2*x**3-1))
fig.update_layout(title="odd function")
fig.show()

# parabola (quadratic)
fig = go.Figure(data=go.Scatter(x=x, y=(6*x)**2+5*x-1))
fig.update_layout(title="quadratic parabola")
fig.show()


