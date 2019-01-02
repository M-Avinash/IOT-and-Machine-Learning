import numpy as np
import random
import time


################################
def sigmoid(input, deriv=False):
    if deriv == True:
        return input*(1-input)
    return 1/(1+np.exp(-input)) 

def leakyrelu(input, alpha = 0.01):
    output = 1. * (input>0)
    output[output ==0] = alpha
    return output

def cross_entropy(output, target, deriv = False):
    m=target.shape[0]
    if deriv == True:
        return (np.subtract(output,target))/m
    return -(1/m)*(np.sum(np.dot(np.log(output),target.T) + np.dot(np.log(1-output),(1-target).T)))
################################
    
#Random Initializaion
iarray  = np.random.rand(1,5) #Randomly Initalized Input Array
weight1 = np.random.rand(5,2) #Randomly Initalized weights for input neurons
bias1   = np.random.rand(1,2) #Randomly Initalized bias for input neurons
weight2 = np.random.rand(2,5) #Randomly Initalized wights for hidden neurons
bias2   = np.random.rand(1,5) #Randomly Initalized bias for hidden neurons

#The target matrix we need is
target =np.array([[1,0,0,1,1]])

for i in range (15000):
    
    #Begin forward propagation steps    
    #Multiply Input and Weight1 vectors, apply leakyrelu function
    hidden = leakyrelu(np.dot(iarray, weight1) +bias1)
                          
    #Muiltiply Hidden and Weight 2 vectors, apply sigmoid function
    output = sigmoid(np.dot(hidden,weight2) +bias2, deriv = False)
    
    #Calculate the total error using cross entropy log loss
    error = cross_entropy(output, target)
#   print(' The cross entropy loss or total error is   :', str(error)) <<- Uncomment this line to visualize error reduction at every iteration  
    
    # Implement backward propagation for gradient descent     
    
    #derivative of logistic classification with cross entropy [Target --> Output]
    #https://peterroelants.github.io/posts/cross-entropy-logistic/
    output_delta = cross_entropy(output, target, deriv=True)
    
    #derivative of sigmoid function on the output layer [Output --> Hidden]
    #http://www.ai.mit.edu/courses/6.892/lecture8-html/sld015.htm
    hidden_delta = sigmoid(output_delta, deriv=True)
    
    #derivative of the leakyrelu function on the hidden layer [Hidden --> Input]
    #leakyrelu(x) = max(0, x)
    input_delta =  np.array(leakyrelu(hidden_delta))

    #Update weights with a learning rate of "0.5"
    weight2  = (weight2 - 0.9*hidden_delta)
    weight1  = (weight1 - 0.9*input_delta.T)
    
    #time.sleep(0.3)

print(output)

