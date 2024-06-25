#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:30:13 2021

@author: avinash
"""

import numpy as np

################################
def leakyrelu(input, deriv=False):
    if deriv:
        return np.where(input > 0, 1.0, 0.01)
    return np.where(input > 0, input, input * 0.01)

def sigmoid(input, deriv=False):
    output = 1 / (1 + np.exp(-input)) 
    if deriv:
        return output * (1 - output)
    return output

def cross_entropy(output, target):
    m = target.shape[0]
    epsilon = 1e-5
    return -(1 / m) * np.sum(target * np.log(output + epsilon) + (1 - target) * np.log(1 - output + epsilon))

################################

# Random Initialization
iarray = np.random.rand(1, 5)
weight1 = np.random.rand(5, 2)
bias1 = np.random.rand(1, 2)
weight2 = np.random.rand(2, 1)  # Adjusted to match output layer size
bias2 = np.random.rand(1, 1)  # Adjusted to match output layer size

print('The Input array is:', iarray)

# The target matrix we need is
target = np.array([[0.12]])

print('The Target array is:', target)

learning_rate = 0.5

for i in range(3000000):
    
    # Forward propagation
    hidden = leakyrelu(np.dot(iarray, weight1) + bias1)
    output = sigmoid(np.dot(hidden, weight2) + bias2)
    
    # Calculate error
    error = cross_entropy(output, target)
    
    if i % 100000 == 0:  # Print error occasionally to see progress
        print(f'Iteration {i}, Error: {error}')
    
    # Backward propagation
    output_delta = output - target
    hidden_delta = output_delta.dot(weight2.T) * leakyrelu(hidden, deriv=True)
    input_delta = hidden_delta.dot(weight1.T)
    
    # Update weights and biases
    weight2 -= learning_rate * hidden.T.dot(output_delta)
    weight1 -= learning_rate * iarray.T.dot(input_delta)
    bias2 -= learning_rate * np.sum(output_delta, axis=0, keepdims=True)
    bias1 -= learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

print('The output after training is:', output)
print('The final error is:', error)
