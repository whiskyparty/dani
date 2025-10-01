//SALUDO PERSONALIZADO
conts nombreusuario = prompt("ingrese el nombre de usuario");
if (nombreusuario) {
    console.log("hola,${nombreusuario} bienvenido")
    else {
        console.log("hola invitado, bienvenido")
    }
}
   //COMPARADOR DE NUMEROS
let numero1 =prompt("ingrese el primer numero")
let numero2 =prompt("ingrese el segundo numero")
if (numero1>numero2){
    alert("una de las entradas no es un numero valido")
    }else{
    //estructura if else if else
    if (numero1>numero2){}
        alert("el primer numero (+numero1+)"es el mayor")
    }else if (numero2>numero1){
        alert("el segundo numero (+numero2+)"es el mayor")
    }else{
        alert("los numeros son iguales")
        
    }

    //DIA LABORAL O FIN DE SEMANA
    swith (nombredeldia){
        case "lunes":
        case "martes":
        case "miercoles":
        case "jueves":
        case "viernes":
        return "dia laboral":
        break;
        case "sabado":
        case "domingo":
        return "fin de semana":
        break;
        default:
        return "dia no valido;"
        break;

    }

    //CUENTA REGRESIVA
    numero_actual = 10
    while (numero_actual >= 1){
        console.log(numero_actual)
        numero_actual--
    }

 




