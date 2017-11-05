import numpy as np
import sklearn
from scipy import stats
from sklearn.datasets.samples_generator import make_regression
import pylab




def batch_gradient_descent(x, y, num_iter, step_size):
	num_samples = x.shape[0]
	theta = np.ones(2)
	x_transpose = x.transpose()

	for iter in range(0, num_iter):
		hypothesis = np.dot(x, theta)
		loss = hypothesis - y

		#calc cost function
		cost_func = np.sum(loss ** 2) / (2 * num_samples)
		print "iter %s | cost_func: %.3f" % (iter, cost_func)

		#calc gradient 
		gradient = np.dot(x_transpose, loss) / num_samples

		#update theta
		theta = theta - step_size * gradient
	return theta



#############################################################
##################      MAIN        #########################
#############################################################

X, Y = make_regression(n_samples=100, n_features=1, n_informative=1,
						random_state=0, noise=35)

num_samples, n = np.shape(X)

#insert column
X = np.c_[np.ones(num_samples), X]
step_size = 0.05

theta = batch_gradient_descent(X, Y, 10, step_size)

#plot
for i in range(X.shape[1]):
	y_predicted = theta[0] + theta[1]*X

pylab.plot(X[:,1], Y, 'o')
pylab.plot(X, y_predicted, 'k-')
pylab.show()
