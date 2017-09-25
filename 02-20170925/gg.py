a,b,c = 2,4,8
def func():
    global a,c
    a,b,c = 3,6,9
    def func_x():
         nonlocal b
         global c
         a,b,c = 5,10,15
         print("func_x:{},{},{}".format(a,b,c))
    func_x()
    print("func:{},{},{}".format(a,b,c))
print("before func:{},{},{}".format(a,b,c))
func()
print("after func:{},{},{}".format(a,b,c))
