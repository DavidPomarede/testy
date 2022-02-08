import json
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as FF
import plotly.graph_objs as go

import numpy as np
from google.colab import files
uploaded = files.upload()
//import pandas as pd

with open('036-CAR01.json') as json_file:
    data = json.load(json_file)
    vertices, triangles = np.array(data['vertices']), np.array(data['faces']) - 1
    
    x, y, z = vertices[:,0], vertices[:,2], -vertices[:,1]
    car_type = data['car_type']
    graph_data = plotly_trisurf(x,y,z, triangles, colormap=cm.RdBu, plot_edges=None)

    # with no axis
    noaxis=dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title='')
    
    # with axis
    axis = dict(
        showbackground=True,
        backgroundcolor="rgb(230, 230,230)",
        gridcolor="rgb(255, 255, 255)",
        zerolinecolor="rgb(255, 255, 255)",
    )
    
    layout = go.Layout(
         title=car_type + ' with noaxis',
         width=800, height=600,
         scene=dict(
             xaxis=dict(noaxis), yaxis=dict(noaxis), zaxis=dict(noaxis),
#              aspectratio=dict( x=1, y=2, z=0.5)
         )
    )

    fig = go.Figure(data= graph_data, layout=layout)
    
    
    fig.show()
    
    layout = go.Layout(
         title=car_type + ' with axis', 
         width=800, height=600,
         scene=dict(
             xaxis=dict(axis), yaxis=dict(axis), zaxis=dict(axis),
#              aspectratio=dict( x=1, y=2, z=0.5)
         )
    )

    fig = go.Figure(data= graph_data, layout=layout)
    fig.update_layout(scene_aspectmode="data")
    
    fig.show()
