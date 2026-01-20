
# creando mi excepcion personalizada
class Miexcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante te equivocaste: {err}")

# manejandola
try:
    # lanzando mi propia excepcion
    raise Miexcepcion("Eres una persona poco culta")
except:
    print("como cometiste ese error?")


    