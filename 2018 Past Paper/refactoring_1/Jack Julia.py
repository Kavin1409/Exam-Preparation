from numpy import *
import matplotlib.pyplot as plt


def get_init_coord(dimension, scale, range, shift, zoom, stretch):
    return scale*(dimension-range/shift)/(zoom*stretch*range)


def update_matrix(t, sharpness, init_x, init_y, limit1, limit2, enhance1, enhance2, contrast, A, x, y):
    while t == True:
        if init_x * init_x + init_y * init_y >= limit1:
            t = False
        if sharpness <= limit2:
            t = False
        a = init_x * init_x - init_y * init_y - contrast
        init_y = enhance1 * init_x * init_y + enhance2
        init_x = a
        sharpness = sharpness - 1
    A[y][x] = sharpness


def plot_julia():
    xrange=500
    yrange=500
    xscale =1.5
    yscale = 1.5
    xshift=2
    yshift=2
    xzoom=0.5
    yzoom=0.5
    xstretch=1
    ystretch=1
    initial_sharpness=300
    limit1=4
    limit2=1
    contrast=0.7
    enhance1=2
    enhance2=0.27015
    A = zeros([yrange, xrange])
    for x in range(xrange):
        for y in range(yrange):
            init_x = get_init_coord(x, xscale, xrange, xshift, xzoom, xstretch)
            init_y = get_init_coord(y, yscale, yrange, yshift, yzoom, ystretch)
            sharpness = initial_sharpness
            t=True
            update_matrix(t, sharpness, init_x, init_y, limit1, limit2, enhance1, enhance2, contrast, A, x, y)
    plt.imshow(A)
    plt.savefig("julia_image.png")

plot_julia()