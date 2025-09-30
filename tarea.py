#CALCULADORA DE PROPINA📱

costo_comida = float(input("cual es el costo de la comida?"))
propina = int(input("cual es elporcentaje que deseas dejar de propina? 20, 30,?"))
propina_decimal = propina / 100
total_propina = costo_comida * propina_decimal
total_cuenta = costo_comida + total_propina
print(f"la propina es de ${total_propina} y el total de la cuenta es de &{total_cuenta}")


#VERIFICADOR DE EDAD🔞

edad = int(input("ingrese su edad:"))
if edad >= 18:
    print("eres mayor de edad, puedes votar.👌🏽👌🏽")
else:
    print("eres menor de edad, no puedes votar😔😔")

#ADIVINA EL NUMERO SECRETO🪄

print("bienvenido al juego de adivina el numero secreto🔍")
print("estoy pensando en un numero del 1 al 10 🤐")
print("tienes 2 intentos para adivinar")
try:
    numero_secreto = 7
    intento_1 = int(input("cual es tu primer intento?"))
    if intento_1 == numero_secreto:
        print("felicidades, adivinaste en el ptimer intentooo")
    else:
        print("intento incorrecto tienes una opotunidad mas")
        intento_2 = int(input("cual es tu segundo intento"))
        if intento_2 == numero_secreto:
            print("feliidades, adivinaste en el segundo intento")
        else:
            print("lo siento, no adivinaste, el numero secreto era 7")
        except ValueError:
            print("por favor ingresa otro numero")
        

#CONTADOR DE VOCALES 🔠

texto = input("ingresa un texto para contar las vocales:")
conteo_vocales = 0
vocales = "aeiouAEIUO"
conteo_vocales = += 1 for letra in texto if letra in vocales
print(f"el numero de vocales en un texto es: {conteo_vocales}")


