
from matplotlib.pyplot import cm
import matplotlib.pyplot as plt
import random
import numpy as np
import time

f = 0
X_SIZE = 1000
Y_SIZE = 1000

def calculate_New_C(clusters, c, k):
    
    sum_cx = []
    sum_cy = []
    for i in range(0,k):
        temp = 0
        temp2 = 0
    
        for j in range(0,len(clusters[i])):
            temp = temp + clusters[i][j][0]
            temp2 = temp2 + clusters[i][j][1]
        sum_cx.append(int(temp/len(clusters[i])))
        sum_cy.append(int(temp2/len(clusters[i])))
    
    new_c = [sum_cx,sum_cy]

    for i in range(0,k):
        c[i][0] = new_c[0][i]
        c[i][1] = new_c[1][i]
    
def distance_between_two_points(p1,p2):
    return ((((p2[0] - p1[0] )**2) + ((p2[1]-p1[1])**2) )**0.5)

def plot_samples(points, c, K):
    global f
    plt.figure(f)
    plt.scatter(points[0], points[1], c='black')
    plt.scatter(c[0:K,0], c[0:K,1], c='red')
    f += 1
    
def plot_clusters(clusters,c,k):
    global f
    color = cm.rainbow(np.linspace(0,1,k))
    # colormap = np.array(['r', 'g', 'b'])
    plt.figure(f)
    for i in range(0,k):
        for j in range(0,len(clusters[i])):
            plt.scatter(clusters[i][j][0],clusters[i][j][1],c=color[i].reshape(1,-1))

    plt.scatter(c[0:k,0], c[0:k,1], c='black')

    f += 1
    
def k_means(points, c, k,clusters):
    l1 = len(points[1])
    min_d = 10000

    for i in range(0, l1):
        min_d = 10000
        p = []
        pst = -1
        p = [points[0][i],points[1][i]]
        p = np.asarray(p)
        for j in range(0,k):
            dist = 0.0
            dist = distance_between_two_points(c[j],p)
            print(dist,end=" ")
            if dist < min_d:
                min_d = dist
                pst = j
        print()
        print(pst,min_d,p,end="")
        
        clusters[pst].append(p.tolist())
        print()

    print()
    
    for i in range(0,k):
        print("Cluster %d" % (i+1))
        print(clusters[i])
        print("Size of %d cluster : %d" % (i , len(clusters[i])) )
        print()
    
def main():
    global f
    # Number of Clusters
    K = 4

    X = np.random.randint(300, size = X_SIZE)
    Y = np.random.randint(300, size = Y_SIZE)

    points = np.array([X,Y])
    
    c = []
    clusters = []

    for i in range(0,K):
        new = []
        clusters.append(new)
    
    for i in range(0, K):
        new = []
        new  = [random.choice(points[0]),random.choice(points[1])]
        c.append(new)
    
    c = np.asarray(c)
    
    plot_samples(points, c , K)

    k_means(points, c, K,clusters)

    plot_clusters(clusters,c,K)
    calculate_New_C(clusters, c, K)
    print()
    
    # how many times the algorithm gonna run... Printing more Plots (n+2)
    for _ in range(1):
        for i in range(0,K):
            clusters[i] = []
    
        print()
        k_means(points, c, K,clusters)
        calculate_New_C(clusters, c, K)
        plot_clusters(clusters,c,K)
        print("Centers :")
        print(c) 
        time.sleep(0.2)

    plt.show()

if __name__ == "__main__":
    
    main()
