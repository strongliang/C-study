def update(mean1, var1, mean2, var2):
            new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
            new_var = 1/ (1/ var1 + 1/ var2)
            return [new_mean, new_var]


def predict (mean1, var1, mean2, var2):
                    new_mean = mean1 + mean2
                    new_var = var1 + var2
                    return [new_mean, new_var]
                    
measurements = [5., 6., 7., 9., 10.]
motion = [5., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 1.
mu = 1.
sig = 1.

for n in range(len(measurements)):
#    [mu, sig] = update(mu, sig, measurements[n], measurement_sig)
#    print 'update: ', [mu, sig]
    [mu, sig] = predict(mu, sig, motion[n], motion_sig)
    print 'predict: ', [mu, sig]