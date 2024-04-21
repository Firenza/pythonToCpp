import ctypes

# Load the shared library
example = ctypes.CDLL('./test.so')

# Specify the argument types and return type
example.multiply.argtypes = [ctypes.c_int, ctypes.c_double]
example.multiply.restype = ctypes.c_double

# Call the function
result = example.multiply(5, 2.5)

# Print the result
print(result)