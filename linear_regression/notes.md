## Objective
Understand supervised learning for regression by deriving linear regression from first principles, both from an optimization and a probabilistic perspective.

## Problem formulation
Basically, we are given a training set of m examples (m rows in a table for example).

(x^{i} , y^{i}) where i = 1,2,...,m

x are the inputs and y are the outputs.

This is a supervised learning problem since we have labels y. The objective here is to learn a function that maps inputs x to outputs y with minimal error on the training set.

## Model / Hypothesis
We choose a linear hypothesis:

h(x) = THETA^T * x where THETA is in R^n and x are the features such as x = (x_0,x_1,..). Particularity : x_0 = 1.

This choice leads to a convex cost function (so, a convex optimization problem)

## Cost function
Here is the cost function (using least squares cost function):

J(theta) = 1/2 * sum (from i = 1 to m) (h(x)^{i} - y^{i})^2

Advantages : differentiable everywhere, convex wrt theta, strongly penalizes large errors 

The objective is to minimize J(theta) wrt theta.
## Optimization
To optmize J(theta), we will use Gradient Descent algorithm.

The gradient of J(theta) is:

dJ/dtheta_j = sum (from i = 1 to m) (h(x)^{i} - y^{i}) * x_j

How do we update that. It's simple:

theta_j := theta_j - alpha * dJ/dtheta_j where alpha is the Learning Rate.

All parameters are updated simultaneouly.

Another thing, because J(theta) is convex, the Gradient Descent Algorithm will converge to the global minimum.

## Mathematical derivations
We define:

- X as the Design Matrix. X is a m*n matrix (m is the number of training examples and n the number of features)
- y as the target vector which is R^m vector.

Thanks to that, the cost function J(theta) can be written as follows:

J(theta) = 1/2 (X*THETA - y)^T(X*THETA - y) 

And:

Gradient wrt theta of J(theta) = X^T(X*THETA - y)

By setting the gradient of J(theta) to 0, we get:

THETA = (X^TX)^-1X^Ty (if X is invertible)

This is the 'Normal equation'. Doesn't need alpha (learning rate), it is a closed-form solution but its computational cost is high (O(n^3)). So it is not usable when n is large.

## Observations
- Linear regression is a convex optimization problem
- Gradient descent scales better with large datasets
- The normal equation provides intuition but is rarely used in practice for high-dimensional data
- This framework generalizes directly to logistic regression and neural networks

Linear regression is the foundation of most machine learning models: loss definition, gradient computation, and parameter updates follow the same structure.