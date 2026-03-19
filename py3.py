#Ejercio 1
nombre = input("Ingrese el nombre del cliente: ")
while not nombre.isalpha() or nombre == "":
    print("Error: El nombre debe contener solo letras y no puede estar vacío.")
    nombre = input("Ingrese el nombre del cliente: ")

cant_input = input("¿Cuantos productos desea comprar?: ")
while not cant_input.isdigit() or int(cant_input) <= 0:
    print("Error: Ingrese un numero entero positivo mayor a 0.")
    cant_input = input("¿Cuantos productos desea comprar?: ")

cantidad_productos = int(cant_input)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad_productos + 1):
    print(f"\n--- Producto {i} ---")
    
    precio_in = input(f"Precio del producto {i}: ")
    while not precio_in.isdigit():
        print("Error: El precio debe ser un numero entero.")
        precio_in = input(f"Precio del producto {i}: ")
    
    precio = int(precio_in)
    total_sin_descuento += precio
    
    tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    while tiene_desc not in ['s', 'n']:
        print("Error: Ingrese 'S' para si o 'N' para no.")
        tiene_desc = input("¿Tiene descuento? (S/N): ").lower()
    
    if tiene_desc == 's':
        precio_final = precio * 0.90 
    else:
        precio_final = precio
        
    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos

print("-" * 30)
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
 
 #Ejercicio 2

USUARIO_REAL = "alumno"
CLAVE_REAL = "python123"
intentos_max = 3
acceso_concedido = False

for i in range(1, intentos_max + 1):
    print(f"Intento {i}/{intentos_max}")
    user_input = input("Usuario: ")
    pass_input = input("Clave: ")

    if user_input == USUARIO_REAL and pass_input == CLAVE_REAL:
        print("Acceso concedido.")
        acceso_concedido = True
        break
    else:
        if i < intentos_max:
            print("Error: credenciales invalidas.\n")
        else:
            print("Cuenta bloqueada.")

while acceso_concedido:
    print("\n--- Menu de Campus ---")
    print("1) Ver estado de inscripcion")
    print("2) Cambiar clave")
    print("3) Mostrar mensaje motivacional")
    print("4) Salir")
    
    opcion = input("Opcion: ")

    if not opcion.isdigit():
        print("Error: ingrese un numero valido.")
        continue
    
    opcion = int(opcion)

    if opcion == 1:
        print("Estado: Inscripto")
    
    elif opcion == 2:
        nueva_clave = input("Nueva clave: ")
        if len(nueva_clave) < 6:
            print("Error: minimo 6 caracteres.")
        else:
            confirmacion = input("Confirme su nueva clave: ")
            if nueva_clave == confirmacion:
                CLAVE_REAL = nueva_clave
                print("Clave cambiada con exito.")
            else:
                print("Error: Las claves no coinciden.")
                
    elif opcion == 3:
        print("Frase del dia: 'El exito es la suma de pequeños esfuerzos repetidos dia tras dia.'")
    
    elif opcion == 4:
        print("Saliendo del sistema... ¡Hasta luego!")
        break
    
    else:
        print("Error: opcion fuera de rango.")

       
 #Ejercicio 3
       
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador: ")
while not operador.isalpha():
    operador = input("Nombre invalido. Ingrese solo letras: ")

print(f"\n--- Bienvenid@ {operador} al Sistema de Turnos ---")

opcion = ""
while opcion != "5":
    print("\nMENu DE OPCIONES:")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        if dia == "1" or dia == "2":
            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                paciente = input("Invalido. Ingrese nombre (solo letras): ")

            if dia == "1":
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: El paciente ya tiene un turno este dia.")
                elif lunes1 == "": lunes1 = paciente
                elif lunes2 == "": lunes2 = paciente
                elif lunes3 == "": lunes3 = paciente
                elif lunes4 == "": lunes4 = paciente
                else: print("Sin cupos para el Lunes.")
            
            else:
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: El paciente ya tiene un turno este dia.")
                elif martes1 == "": martes1 = paciente
                elif martes2 == "": martes2 = paciente
                elif martes3 == "": martes3 = paciente
                else: print("Sin cupos para el Martes.")
        else:
            print("Dia incorrecto.")                                                                                                                                                      
    elif opcion == "2":
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente a cancelar: ")
        
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""
            elif lunes2 == paciente: lunes2 = ""
            elif lunes3 == paciente: lunes3 = ""
            elif lunes4 == paciente: lunes4 = ""
            else: print("Paciente no encontrado.")
        elif dia == "2":
            if martes1 == paciente: martes1 = ""
            elif martes2 == paciente: martes2 = ""
            elif martes3 == paciente: martes3 = ""
            else: print("Paciente no encontrado.")

    elif opcion == "3":
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"\nAgenda Lunes:\n1. {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"2. {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"3. {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"4. {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print(f"\nAgenda Martes:\n1. {martes1 if martes1 != '' else '(libre)'}")
            print(f"2. {martes2 if martes2 != '' else '(libre)'}")
            print(f"3. {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4":
        occ_lunes = 0
        if lunes1 != "": occ_lunes += 1
        if lunes2 != "": occ_lunes += 1
        if lunes3 != "": occ_lunes += 1
        if lunes4 != "": occ_lunes += 1
        
        occ_martes = 0
        if martes1 != "": occ_martes += 1
        if martes2 != "": occ_martes += 1
        if martes3 != "": occ_martes += 1

        print("\n--- RESUMEN ---")
        print(f"Lunes: {occ_lunes} ocupados, {4 - occ_lunes} disponibles.")
        print(f"Martes: {occ_martes} ocupados, {3 - occ_martes} disponibles.")

        if occ_lunes > occ_martes:
            print("Dia con mas turnos: Lunes")
        elif occ_martes > occ_lunes:
            print("Dia con mas turnos: Martes")
        else:
            print("Empate en cantidad de turnos.")

print(f"\nSistema cerrado. ¡Hasta luego, {operador}!")

#Ejercio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzadas_seguidas = 0 

nombre_agente = input("Ingrese su nombre de agente: ")
while not nombre_agente.isalpha():
    print("Error: El nombre solo debe contener letras.")
    nombre_agente = input("Ingrese su nombre de agente: ")

print(f"\nBienvenido, Agente {nombre_agente}. La mision comienza ahora.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO! La alarma activo el cierre de emergencia.")
        break

    print("-" * 30)
    print(f"ESTADO: Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVA' if alarma else 'Apagada'} | Codigo: [{codigo_parcial}]")
    print("-" * 30)

    print("1. Forzar cerradura (-20 energia, -2 tiempo)")
    print("2. Hackear panel (-10 energia, -3 tiempo)")
    print("3. Descansar (+15 energiia, -1 tiempo)")
    
    opcion = input("Seleccione una accion: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        opcion = input("Opcion invalida. Elija 1, 2 o 3: ")

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        forzadas_seguidas += 1

        if forzadas_seguidas == 3:
            alarma = True
            print("¡AVISO! Intentaste forzar demasiadas veces seguidas. La cerradura se trabo y la ALARMA se activo.")
        else:
            if energia < 40:
                print("¡ADVERTENCIA! Poca eneria, riesgo de activar alarma.")
                num = input("Elija un numero del 1 al 3: ")
                while not num.isdigit() or num not in ["1", "2", "3"]:
                    num = input("Debe elegir 1, 2 o 3: ")
                
                if num == "3":
                    alarma = True
                    print("¡Mala suerte! Activaste la alarma al forzar.")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con exito!")

    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        forzadas_seguidas = 0 

        print("Hackeando...")
        for i in range(1, 5):
            print(f"Progreso: {i * 25}%...")
            codigo_parcial += "A"
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Codigo completo! Una cerradura se abrio automaticamente.")

    elif opcion == "3":
        forzadas_seguidas = 0
        recuperacion = 15
        if alarma:
            recuperacion -= 10
            print("Es dificil descansar con la sirena sonando...")
        
        energia += recuperacion
        if energia > 100: energia = 100
        
        tiempo -= 1
        print(f"Descanso finalizado. Energia actual: {energia}")

print("\n" + "="*30)
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El Agente {nombre_agente} ha abierto la boveda.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueo por la alarma.")
elif energia <= 0:
    print("DERROTA: Te quedaste sin energia.")
elif tiempo <= 0:
    print("DERROTA: Se termino el tiempo.")
print("="*30)

#Ejercico 5
nombre = ""
while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")

hp_gladiador = 100      
hp_enemigo = 100       
pociones = 3              
danio_pesado = 15         
danio_enemigo = 12    
juego_activo = True       

print("\n=== INICIO DEL COMBATE ===")

while hp_gladiador > 0 and hp_enemigo > 0:
    print("-" * 30)
    print(f"{nombre} (HP: {hp_gladiador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz (Uso de for)")
    print("3. Curar")
    
    opcion = ""
    while True:
        opcion = input("Opcion: ")
        if opcion.isdigit():
            if opcion in ["1", "2", "3"]:
                break
            else:
                print("Error: Elige 1, 2 o 3.")
        else:
            print("Error: Ingrese un numero valido.")
    
    if opcion == "1":
        if hp_enemigo < 20:
            critico = float(danio_pesado * 1.5)
            hp_enemigo -= int(critico)
            print(f"¡GOLPE CRiTICO! Atacaste al enemigo por {critico} puntos de daño.")
        else:
            hp_enemigo -= danio_pesado
            print(f"¡Atacaste al enemigo por {danio_pesado} puntos de daño!")

    elif opcion == "2":
        print(">> ¡Inicias una rafaga de golpes!")
        for i in range(3):
            hp_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            hp_gladiador += 30
            pociones -= 1
            print(f"¡Usaste una pocion! Recuperas 30 HP. (Te quedan {pociones})")
        else:
            print("¡No quedan pociones! Pierdes el turno intentando buscar una.")

    if hp_enemigo > 0:
        hp_gladiador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")
    
    print("=== NUEVO TURNO ===")

print("\n" + "="*30)
if hp_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caido en combate.")
print("="*30)