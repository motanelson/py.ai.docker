import matplotlib.pyplot as plt
from scipy import stats


# Dados
x = list(range(20))
y = [float(v) * 1.25 for v in x]
xx = list(range(40))
yy = [float(v) * 1.25 for v in xx]
# Regressão linear
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

print(yy)

def predicts(froms,intos):
    for n in range(froms,intos):
        print(myfunc(n), end=", ")
predicts(0,40)
print("")