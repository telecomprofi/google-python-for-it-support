# Google Python Crash course Week3
# Wile loop inside a function
def attempts(n):
  x = 1
  while x <= n:
    
    print("Attempt.."+str(x))
    x += 1
  print("Done")
  
  
attempts(5)
