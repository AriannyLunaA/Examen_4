l_usuarios=[]

def ingresarUsuario():
    usuarioNombre=input("Ingrese Nombre de usuario: ")
    sexo=input("Ingrese sexo (F o M): ")
    contraseña=input("Ingrese contraseña:")

    l_usuarios.append([usuarioNombre])
    l_usuarios.append([sexo])
    l_usuarios.append([contraseña])
    return
def validar(contraseña):
        if len(contraseña) <=8 and " " not in contraseña:
            print("Usuario Ingresado con exito")
        else:
            print("No cumple lo solicidado")


print (l_usuarios)

def validar_sexo(sexo):
    print("")
 

 #Validacion de contraseña


   
def buscar(usuarioNombre):
    for item in l_usuarios:
        print (usuarioNombre)
 

#opcion=0

while True:
    
    print("menú de usuario: ")
    print("1.Ingresar usuario ")
    print("2.Buscar usuario: ")
    print("3.Eliminar usuario: ")
    print("4.Salir")
    
    opt=int(input("Ingrese opción: "))
    match opt:
        case 1:
            ingresarUsuario()
            print("Ingresar Usuario")
            print() 

        case 2:
            buscar()
        
        case 3:
             print() 
        case 4:
             print("Terminando programa...")
             break
        case _:
            print("Ingrese opcion valida.") 

    