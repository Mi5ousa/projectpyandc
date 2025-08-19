import ctypes

# carrega a biblioteca
lib = ctypes.CDLL("./libcalc.dylib")  # ou "./libcalc.so" no Linux

# define argumentos e retorno (opcional, mas recomendado)
lib.multiplica.argtypes = [ctypes.c_int, ctypes.c_int]
lib.multiplica.restype = ctypes.c_int

# usa a função C
resultado = lib.multiplica(5, 6)
print("Resultado:", resultado)
