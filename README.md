# ft_linear_regression
This is the 42 school introduction project to machine learning.<br />
This project is about creating a program that predicts the price of a car by using a linear function train with a gradient descent algorithm.<br />
./subject/ft_linear_regression.pdf for more details.<br />
## Usage

### First step
Train the model with the program trainer.py :
```
python3 trainer.py
```
You can also use options :
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
The first step will generate the file result.csv that will be used in the segond step
### Second step

Type :
```
python3 resolver.py
```
Then follow instructions.
