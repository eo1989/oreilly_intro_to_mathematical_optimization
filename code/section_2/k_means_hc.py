import pandas as pd
import numpy as np
import random


# Cluster points using k-means algorithm using hill climbing
# Desmos graph: https://www.desmos.com/calculator/pb4ewmqdvy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "{0},{1}".format(self.x, self.y)


def distance_between(point1, point2):
    return ((point2.x - point1.x)**2 + (point2.y - point1.y)**2) ** .5


k = 4
points = [(Point(row.x, row.y)) for index, row in pd.read_csv("https://tinyurl.com/y25lvxug").iterrows()]
centroids = [Point(0, 0) for _ in range(k)]

best_loss = 1_000_000_000.0

for _ in range(100_000):
    random_centroid = random.choice(centroids)

    random_x_adjust = np.random.standard_normal()
    random_y_adjust = np.random.standard_normal()

    random_centroid.x += random_x_adjust
    random_centroid.y += random_y_adjust

    new_loss = 0.0

    for p in points:
        new_loss += min(distance_between(p, c) for c in centroids)**2

    if new_loss < best_loss:
        best_loss = new_loss
    else:
        random_centroid.x -= random_x_adjust
        random_centroid.y -= random_y_adjust

for c in centroids:
    print("CENTROID: {0}".format(c))

    for p in points:
        if distance_between(p, c) == min(
            distance_between(p, c2) for c2 in centroids
        ):
            print("    {0}".format(p))
