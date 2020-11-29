# ft_linear_regression
This project is about creating a program that predicts the price of a car by using a linear function train with a gradient descent algorithm
./subject/ft_linear_regression.pdf for more details
##usage
first step is to train the model with the program trainer.py
```
python3 trainer.py
```
you can also use option in this first step:
```
 python3 trainer.py -h
  -h  print this help message
  -pc Plot the cost history graph
  -pt Plot the final prediction line
  -f  specify a file name for the dataset
  -lr specify a learning rate that is by default set to 0.9
  -it specify number of iterations that is by default set to 1000
  -v  verbose mode, print each step of the traning procesus
```
the first step will generate the file result.csv that will be used in the segond step
```
python3 resolver.py
  Please specify a number of km for getting a prediction of car price:
```

