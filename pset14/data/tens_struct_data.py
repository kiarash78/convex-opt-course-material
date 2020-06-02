import numpy as np
import matplotlib.pyplot as plt

n = 20

N = 85

A = np.asarray(np.mat("""[0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 -1 0 0 0 0 0 0 0 ;
0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ;
0 -1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ;
0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 -1 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 1 0 ;
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 -1 ;
0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 -1 0 0 0 0 -1 0 0 0 0 ;
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 1 0 0 0 ;
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 -1 0 -1 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 1 ;
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 1 0 1 1 0 -1 0 0 -1 0 0 0 -1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 ;
0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 1 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 1 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 ;
0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 -1 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ;
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 -1 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 ;
0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 -1 0 0 -1 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 -1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -1 0 0 0 0 0 ;
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 ;
0 0 -1 0 0 0 0 -1 0 1 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 -1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 ;
0 0 0 0 -1 0 0 0 0 0 -1 -1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 ;
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 -1 0 0 1 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 1 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ;
0 0 1 -1 0 -1 0 0 0 0 0 0 -1 0 0 -1 0 0 0 0 0 -1 1 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 1 0 0 0 0 -1 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 ;
0 0 0 0 0 1 0 0 0 0 1 0 0 0 -1 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0 -1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -1 0 -1 1 0 0 0 0 0 -1 0 ;
-1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 -1 0 0 0 0 1 0 0 0 0 0 -1 0 0 0 0 0 0 0 0 0 0 0 0 1 -1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 -1 0 1 0 0 0 0 0 0 0 0 0 0 0 -1 0 0 0 0 0 0
]"""))

p = 5;

g = 9.800;

x_fixed = np.asarray(np.mat("""[0.726
0.148
0.106
0.785
0.707
]"""))[0,:]


y_fixed =  np.asarray(np.mat("""[0.339
0.837
0.407
0.120
0.972
]"""))[0,:]

m =  np.asarray(np.mat("""[0.265
0.633
0.187
0.456
0.689
0.814
0.204
0.264
0.380
0.614
0.515
0.941
0.758
0.930
0.650
0.638
0.151
0.010
0.745
0.238
]"""))[0,:]

k_tot = 200;

# Mass x-coordinates for uniform stiffness allocation.
x_unif =  np.asarray(np.mat("""[0.726
0.148
0.106
0.785
0.707
0.530
0.436
0.456
0.459
0.507
0.533
0.411
0.510
0.515
0.418
0.508
0.529
0.464
0.570
0.485
]"""))[0,:]

# Mass y-coordinates for uniform stiffness allocation.
y_unif =  np.asarray(np.mat("""[0.339
0.837
0.407
0.120
0.972
-0.949
-0.351
-0.180
-0.465
-0.400
-0.165
-0.607
-0.815
-0.594
-0.714
-0.374
-0.501
-0.223
-0.628
-0.551
]"""))[0,:]

##################################################3
# Plotting code.

# The following code plots the tensile structure with evenly distributed
# stiffness.

k_unif = (k_tot/N)*np.ones(N);
ind_ex = np.where(k_unif < 1e-2); #do not show springs with k < 1e-2
def unif_plot():
    Aadj = A[:,np.setdiff1d(np.arange(N),ind_ex)];
    Aadj2 = np.dot(Aadj,Aadj.T)-np.diag(np.diag(Aadj@Aadj.T)) != 0;

    for i in range(n):
            for j in range(i):
                    if Aadj2[i,j]:
                            plt.plot([x_unif[i],x_unif[j]],[y_unif[i],y_unif[j]],"bo-")
    plt.plot(x_fixed,y_fixed,'ro');
    plt.xlabel('x') ; plt.ylabel('y')
    #plt.show()

# Use the following code to plot your optimized structure.
# Here k_opt is the optimum stiffness profile and x_opt, y_opt the
# corresponding mass coordinates

#ind_ex = np.where(k_opt < 1e-2); #do not show springs with k < 1e-2
#Aadj = A[:,np.setdiff1d(np.arange(N),ind_ex)];
#Aadj2 = np.dot(Aadj,Aadj.T)-np.diag(np.diag(Aadj@Aadj.T)) != 0;
#
#for i in range(n):
#	for j in range(i):
#		if Aadj2[i,j]:
#			plt.plot([x_opt[i],x_opt[j]],[y_opt[i],y_opt[j]],"bo-")
#plt.plot(x_fixed,y_fixed,'ro');
#plt.show()
