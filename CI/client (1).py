import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Addition
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
result_add = proxy.add(x, y)
print("Addition result: ", result_add)

# Factorial
n = int(input("Enter a number for factorial: "))
result_factorial = proxy.factorial(n)
print("Factorial: ", result_factorial)
