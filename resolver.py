import csv
import numpy as np
import matplotlib.pyplot as plt


def Get_teta(CsvFileName):
    x = 0
    y = 0
    with open(CsvFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            a, b, xmin, xmax = row
            #escaping the first line that is in general the name of the colomn
            if (line_count > 0):
                a = float(a)
                b = float(b)
                xmin = float(xmin)
                xmax = float(xmax)
            line_count = line_count + 1
        return a,b, xmin, xmax

def parsing(theta):
    try:
        theta[0],theta[1], xmin, xmax = Get_teta("result.csv")

    except:
        print("plese train the IA befor executing the resolver")
        print("theta[0] = ",theta[0])
        print("theta[1] = ",theta[1])

        return 0, 0, 0, 1
    x = input("Please specify a number of km for getting a prediction of car price: ")
    try:
        x = float(x)
    except:
        print("please specify an avalable number of km")
        return 0, 0, 0, 1
    return x, xmin, xmax, 0

def Normalise_value(MinSource, MaxSource, MinTarget, MaxTarget, Val):
    return ((Val - MinSource) / (MaxSource - MinSource)) * ((MaxTarget - MinTarget) + MinTarget)


def model(x, theta):
    return theta[0] + theta[1] * x

theta = np.zeros((2,1))
err = 0;
x, xmin, xmax, err = parsing(theta)
if (x < 0):
    print("i am not sure that a negative mileage is possible !")
    err = 1;

if err == 0:
    x = Normalise_value(xmin, xmax, 0.0, 1.0, x)
    y = model(x, theta)
    if (y > 0):
        print("the price of the car is about : ",y)
    else :
        print("this car is too old ! i can't give a negative price !")
