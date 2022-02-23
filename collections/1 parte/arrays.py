numeros = [2.23, 3.33]

# Arrays no python
from array import array as pyArr
python_array = pyArr("d", numeros)
print(python_array)

# Arrays no numPy
from numpy import array as npArr
numpy_array = npArr(numeros)
print(numpy_array)