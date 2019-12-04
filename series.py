def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

print(fibonacci(10))

def lucas(n): 
  
    a = 2
    b = 1
      
    if (n == 0) : 
        return a 
   
    # generating number 
    for i in range(2, n + 1) : 
        c = a + b 
        a = b 
        b = c 

    return b
print(lucas(8))

def sum_series(n, a, b):

  for i in range(0, n):
      temp = a
      a = b
      b = temp + b
  return a

print(sum_series(8, 2, 1))

