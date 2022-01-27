import matplotlib.cm as cm
def tri_indices(simplices):
    return ([triplet[c] for triplet in simplices] for c in range(3))

def plotly_trisurf(x, y, z, simplices, colormap=cm.RdBu, plot_edges=None):

    points3D=np.vstack((x,y,z)).T
    tri_vertices=map(lambda index: points3D[index], simplices)
    zmean=[np.mean(tri[:,2]) for tri in tri_vertices ]
    min_zmean=np.min(zmean)
    max_zmean=np.max(zmean)
    facecolor=[map_z2color(zz,  colormap, min_zmean, max_zmean) for zz in zmean]
    I,J,K=tri_indices(simplices)

    triangles=go.Mesh3d(x=x, y=y, z=z,
                     facecolor=facecolor,
                     i=I, j=J, k=K,
                     name='')

    if plot_edges is None: return [triangles]
    else:
        lists_coord=[[[T[k%3][c] for k in range(4)]+[ None]   for T in tri_vertices]  for c in range(3)]
        Xe, Ye, Ze=[reduce(lambda x,y: x+y, lists_coord[k]) for k in range(3)]

        lines=go.Scatter3d(x=Xe, y=Ye, z=Ze,
                        mode='lines',
                        line=dict(color= 'rgb(50,50,50)', width=1.5))
        return [triangles, lines]
    
def map_z2color(zval, colormap, vmin, vmax):
    if vmin>vmax: raise ValueError('incorrect relation between vmin and vmax')
    t=(zval-vmin)/float((vmax-vmin))#normalize val
    R, G, B, alpha=colormap(t)
    return 'rgb('+'{:d}'.format(int(R*255+0.5))+','+'{:d}'.format(int(G*255+0.5))+\
           ','+'{:d}'.format(int(B*255+0.5))+')'
