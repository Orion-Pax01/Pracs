from xmlrpc.server import SimpleXMLRPCServer

# Function to add two numbers
def add(x, y):
    return x + y

# Function to find factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Create the server
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server is running on port 8000...")

# Register the functions
server.register_function(add, "add")
server.register_function(factorial, "factorial")

# Run the server
server.serve_forever()
