'''
HttpRequest     -> Objecto que recibe peticiones desde el cliente.
HttResponse     -> Objecto que envia respuestas al cliente desde el servidor.
'''
from django.http import HttpResponse
from datetime import datetime

def inicio(request):
    respuesta = '''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>Inicio</title>
            </head>
            <body>
                <h1>Bienvenido a la página de inicio...</h1>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)

def imc(request, peso, altura):
    titulo = 'Calculadora IMC'
    calculo_imc = float(peso) / pow(float(altura), 2)
    encabezado = f'El Incice de Masa Corporal es {calculo_imc:.2f}'
    fecha = datetime.now().strftime('%d-%m-%Y - %I:%M:%S %p')
    
    if calculo_imc < 18.5:
        status = 'peso bajo'
    elif calculo_imc >= 18.5 and calculo_imc < 24.9:
        status = 'peso normal'
    elif calculo_imc >= 24.9 and calculo_imc < 29.9:
        status = 'sobrepeso'
    else:
        status = 'obesidad' 

    respuesta = f'''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>{titulo}</title>
            </head>
            <body>
                <h1>{encabezado}</h1>
                <h2>{status.upper()}</h2>
                <hr>
                <h3>Fecha: {fecha}</h3>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)

def cine(request, edad):
    if edad <= 10 or edad >= 60:
        entrada = 'exonerado'
    else:
        entrada = 'pagar entrada'
        
    respuesta = f'''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>Cine</title>
            </head>
            <body>
                <h1>Entrada al cine:</h1>
                <h2>{entrada.upper()}</h2>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)
    
def empleado(request):
    datos = [
        'Empleado',
        'Datos del empleado',
        'Manuel',
        'Lopez',
        26,
        455.0,
        False
    ]
    
    respuesta = f'''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>{datos[0]}</title>
            </head>
            <body>
                <h1>{datos[1]}</h1>
                <hr>
                <h2>Nombre: {datos[2]}</h2>
                <h2>Apellido: {datos[3]}</h2>
                <h2>Edad: {datos[4]}</h2>
                <h2>Sueldo: {datos[5]}</h2>
                <h2>Casado: {'Si' if datos[6] else 'No'}</h2>
                <hr>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)

def producto(request):
    datos = {
        'titulo': 'Producto',
        'encabezado': 'Datos del producto'
    }
    
    producto = {
        'nombre': 'Jabón liquido',
        'existencia': 100,
        'precio': 2
    }
    
    respuesta = f'''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <title>{datos["titulo"]}</title>
            </head>
            <body>
                <h1>{datos["encabezado"]}</h1>
                <hr>
                <h2>Nombre: {producto["nombre"]}</h2>
                <h2>Existencia: {producto["existencia"]} litros</h2>
                <h2>Precio por litro: {producto["precio"]} {'Dolar' if producto["precio"] == 1 else 'Dolares'}</h2>
                <hr>
            </body>
        </html>
    '''
    
    return HttpResponse(respuesta)