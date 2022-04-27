# b.py that could be run stand-alone or as imported module from a
print("Hello World from %s!" % (__name__)) #this part runs when b.py is run stand-alone


def fff():
    if __name__=='__main__':
         print ("Hello World from %s!"  %(__name__))



