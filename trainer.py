import csv
import numpy as np
import matplotlib.pyplot as plt
import math
import sys


def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

##creation of the model  F=X.theta
def model(X, theta):
    return X.dot(theta)

## definition of the cost function
def cost_function(X, y, theta, m):
    m = len(y)
    return 1/(2*m) * np.sum((model(X, theta) - y)**2)

## definition of gradian decent
def gradient_decent(X, y, theta, m_ ,arg_):
    learning_rate = arg_[3]
    n_iteration = arg_[4]
    cost_history = np.zeros(n_iteration)
    m = len(y)
    for i in range(0, n_iteration):
        tmp =learning_rate * 1/m * (X.T.dot(model(X, theta) - y))
        theta = theta -  tmp
        cost_history[i]= cost_function(X, y, theta, m)
        if (arg_[5] != 0):
            print(i + 1 ,"iteration done from ",n_iteration ,"the cost is now :",cost_history[i], end="\r")
    if (arg_[5] != 0):
        print("\n")
    return theta,cost_history

def output_data(teta0,teta1, ymin, ymax):
    with open('result.csv', mode='w') as employee_file:
        result_writer = csv.writer(employee_file, delimiter=',', quotechar='"')
        result_writer.writerow(['teta0', 'teta1', 'xmin', 'xmax'])
        result_writer.writerow([teta0[0], teta1[0], ymin, ymax])

def Normalise_value(MinSource, MaxSource, MinTarget, MaxTarget, Val):
    return ((Val - MinSource) / (MaxSource - MinSource)) * ((MaxTarget - MinTarget) + MinTarget)

def normalise_tab(tab, MinSource = 0, MaxSource=0, MinTarget = 0, MaxTarget = 1):
    TabLen = len(tab)
    NormTab = np.zeros((TabLen,1))
    for i in range(0, TabLen):
        NormTab[i] = Normalise_value(MinSource, MaxSource, MinTarget, MaxTarget, tab[i])
    return NormTab

def ParsingArgs(ar, arg_):
    fs = "data.csv"
    if (len(ar) > 1):
        if (ar.count("-h") >1 or ar.count("-pc") >1 or ar.count("-pt") >1):
            print("Bad arguments")
            sys.exit()
        if (ar.count("-f") >1 or ar.count("-lr") >1 or ar.count("-it") >1 or ar.count("-v") >1):
            print("Bad arguments")
            sys.exit()
        if ("-h" in ar):
            print("-h  print this help message")
            print("-pc Plot the cost history graph ")
            print("-pt Plot the final prediction line")
            print("-f  specify a file name for the dataset")
            print("-lr specify a learning rate that is by default set to 0.9")
            print("-it specify number of iterations that is by default set to 1000")
            print("-v  verbose mode, print each step of the traning procesus")
            sys.exit()
        if ("-pc" in ar):
            arg_[0] = 1
        if ("-pt" in ar):
            arg_[1] = 1
        if ("-f" in ar):
            if (len(ar) <= ar.index("-f") + 1):
                print("Bad arguments")
                sys.exit()
            fs = (ar[ar.index("-f") + 1])
        if ("-lr" in ar):
            if ((len(ar) <= ar.index("-lr") + 1) or not isfloat(ar[ar.index("-lr") + 1])):
                print("Bad arguments")
                sys.exit()
            if (float(ar[ar.index("-lr") + 1]) <= 0):
                print("Bad arguments")
                sys.exit()
            arg_[3] = float(ar[ar.index("-lr") + 1])
        if ("-it" in ar):
            if ((len(ar) <= ar.index("-it") + 1) or not(ar[ar.index("-it") + 1].isnumeric())):
                print("Bad arguments")
                sys.exit()
            if (int(ar[ar.index("-it") + 1]) <= 0):
                print("Bad arguments")
                sys.exit()
            arg_[4] = int(ar[ar.index("-it") + 1])
        if ("-v" in ar):
            arg_[5] = 1
    return fs,arg_

def PlotCH(ran, cost_history):
    plt.plot(ran,cost_history)
    plt.title('Cost history')
    plt.xlabel('Number of iterations')
    plt.ylabel('Cost value')
    plt.show()

def PlotPL(X, theta ,x ,y):
    prediction = model(X, theta)
    plt.scatter(x, y)
    plt.title('Prediction line with trained theta')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.plot(x, prediction)
    plt.show()

arg_ = [0, 0, 0, 0.9, 1000, 0]
FileName, arg_ = ParsingArgs(sys.argv, arg_)
##initialising of x and y array according to the dataset size with taking care
##of ignoring the first line that is in general the name of the colomn
if (arg_[5] != 0):
    print("Extracting  data from ", FileName)

dataset = np.genfromtxt(FileName, delimiter=',')
dataset = dataset[1:,:]
x = dataset[:,0]
y = dataset[:,1]
m =len(y)

x = np.reshape(x, (len(x),1))
y = np.reshape(y, (len(y),1))


if (arg_[5] != 0):
    print("Normalising data")
Scaled_x = normalise_tab(x, np.min(x), np.max(x), 0, 1)
##creating the X martice
if (arg_[5] != 0):
    print("Creating the X martice")

X = np.hstack((np.ones(x.shape),x))
Scaled_X = np.hstack((np.ones(x.shape), Scaled_x))
##creation and inisialisation of theta
if (arg_[5] != 0):
    print("Creation and inisialisation of theta")
theta =  np.random.randn(2,1)
if (arg_[5] != 0):
    print("Gradian decent is starting now")
final_theta, cost_history = gradient_decent(Scaled_X, y, theta, m, arg_)
if (arg_[0] == 1):
    PlotCH(range(arg_[4]), cost_history)
if (arg_[1] == 1):
    PlotPL(Scaled_X, final_theta ,x ,y)
output_data(final_theta[0], final_theta[1], np.min(x), np.max(x))
print("Parameters have been stored in result.csv")
print("you can now run the resolver script named resolver.py")
