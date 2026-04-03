import os

def fct_test1(x):
    x += 1
    return x

def fct_test2(x):
    x -= 1
    return x

class Test:
    def __init__(self, x):
        self._x = x

    def test_x(self, fonction):
        return fonction(self._x)
    
##test

objet = Test(2)
print(objet.test_x(fct_test2))
print(os.listdir("/Users/Samuel/documents/Cours/Projet Informatique/instances"))

