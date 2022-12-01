import numpy, random, os
lr = 1 #learning rate
bias = 1 #value of bias
weights = [random.random(),random.random(),random.random()] #weights generated in a list (3 weights in total for 2 neurons and the bias)


##https://towardsdatascience.com/first-neural-network-for-beginners-explained-with-code-4cfd37e06eaf##


def Perceptron(input1, input2, output) :
    #print("goo")
    outputP = input1*weights[0]+input2*weights[1]+bias*weights[2]
    if outputP > 0 : #activation function (here Heaviside)
        outputP = 1
    else :
        outputP = 0
    error = output - outputP
    weights[0] += error * input1 * lr
    weights[1] += error * input2 * lr
    weights[2] += error * bias * lr


for i in range(50) :
    Perceptron(1,1,1) #True or true
    Perceptron(1,0,1) #True or false
    Perceptron(0,1,1) #False or true
    Perceptron(0,0,0) #False or false

x = int(input())
y = int(input())
outputP = x*weights[0] + y*weights[1] + bias*weights[2]
if outputP > 0 : #activation function
   outputP = 1
else :
   outputP = 0
print(x, "or", y, "is : ", outputP)

outputP = 1/(1+numpy.exp(-outputP)) #sigmoid function

print("Hello?")