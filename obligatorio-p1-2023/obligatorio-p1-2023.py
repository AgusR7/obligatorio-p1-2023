class Empleado:
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        self.id = id
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} ({self.id}) - {self.nacionalidad}"

class ParticipanteCarrera:
    def simular_carrera(self, score_mecanicos, score_auto, errores_pits, penalidades):
        pass

    def lesionar(self, piloto_reserva):
        pass

    def abandonar_carrera(self):
        pass

    def abandono_carrera(self):
        pass

    def resetear_lesiones(self):
        pass

class Piloto(Empleado, ParticipanteCarrera):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score, num_auto):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
        self.num_auto = num_auto
        self.score_final = 0
        self.lesionado = False
        self.equipo = None
        self.puntaje_campeonato = 0
        self.abandono = False
        self.pilotos_abandonan = []


    def __str__(self):
        return f"{super().__str__()} - Piloto - Auto {self.num_auto} - Score: {self.score}"

    def simular_carrera(self, score_mecanicos, score_auto, errores_pits, penalidades):
        if self.lesionado:
            self.score_final = 0
        elif self.abandono:
            self.score_final = 0
        else:
            # Verifica si el piloto abandona antes de calcular el score_final
            if self.num_auto in self.pilotos_abandonan:
                print(f"{self.nombre} ha abandonado la carrera.")
                self.abandono_carrera()
            else:
                if errores_pits:
                    self.score_final = self.score + score_mecanicos + score_auto - 5 * errores_pits[0] - 8 * sum(map(int, penalidades))
                else:
                    # Manejar el caso cuando la lista está vacía
                    self.score_final = self.score + score_mecanicos + score_auto - 8 * sum(map(int, penalidades))
                # Resta puntos por errores en pits
                if errores_pits:
                    self.score_final = self.score + score_mecanicos + score_auto - 5 * errores_pits[0] - 8 * sum(map(int, penalidades))
                else:
                    # Manejar el caso cuando la lista está vacía
                    self.score_final = self.score + score_mecanicos + score_auto - 8 * sum(map(int, penalidades))

        # Restablecer condición de no lesionado y no abandono después de la carrera
        self.lesionado = False
        self.abandono = False

    def lesionar(self, piloto_reserva):
        self.lesionado = True
        self.abandono = True 
        print(f"{self.nombre} está lesionado y no participará en la carrera.")
        piloto_reserva.ocupar_lugar(self)

    def abandonar_carrera(self):
        print(f"{self.nombre} ha abandonado la carrera.")
        self.abandono_carrera()

    def abandono_carrera(self):
        self.abandono = True
        self.score_final = 0
        self.pilotos_abandonan.append(self.num_auto)

    def resetear_lesiones(self):
        self.lesionado = False
        self.abandono = False 
      


class PilotoReserva(Empleado, ParticipanteCarrera):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score, num_auto, piloto_reemplazado=None):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
        self.num_auto = num_auto
        self.puntaje_campeonato = 0
        self.lesionado = False
        self.equipo = None
        self.piloto_reemplazado = piloto_reemplazado

    def __str__(self):
        return f"{super().__str__()} - Piloto Reserva - Auto {self.num_auto} - Score: {self.score}"

    def simular_carrera(self, score_mecanicos, score_auto, errores_pits, penalidades):
        # Utilizar el score del piloto de reserva
        if errores_pits:
            self.score_final = self.piloto_reemplazado.score + score_mecanicos + score_auto - 5 * errores_pits[0] - 8 * sum(map(int, penalidades))
        else:
            # Manejar el caso en que la lista errores_pits está vacía
            self.score_final = self.piloto_reemplazado.score + score_mecanicos + score_auto - 8 * sum(map(int, penalidades))

        # Actualizar el puntaje total del piloto reserva acumulando el puntaje final
        self.puntaje_campeonato += self.score_final


    def ocupar_lugar(self, piloto):
        print(f"{self.nombre} ocupa el lugar de {piloto.nombre}.")
        # Utilizar las estadísticas propias del piloto de reserva
        self.score = piloto.score
        self.num_auto = piloto.num_auto
        self.puntaje_campeonato = piloto.puntaje_campeonato
        self.lesionado = False


class Mecanico(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario, score):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.score = score
        self.equipo = None

    def __str__(self):
        return f"{super().__str__()} - Mecánico - Score: {self.score}"

class DirectorEquipo(Empleado):
    def __init__(self, id, nombre, fecha_nacimiento, nacionalidad, salario):
        super().__init__(id, nombre, fecha_nacimiento, nacionalidad, salario)
        self.equipo = None

    def __str__(self):
        return f"{super().__str__()} - Director de Equipo"

class Auto:
    def __init__(self, modelo, año, score):
        self.modelo = modelo
        self.año = año
        self.score = score

    def __str__(self):
        return f"Auto {self.modelo} ({self.año}) - Score: {self.score}"

class Equipo:
    def __init__(self, nombre, modelo_auto, pilotos_titulares, pilotos_reserva, mecanicos):
        self.nombre = nombre
        self.modelo_auto = modelo_auto
        self.pilotos_titulares = pilotos_titulares
        self.pilotos_reserva = pilotos_reserva
        self.mecanicos = mecanicos
        self.pilotos = pilotos_titulares

    def __str__(self):
        return f"Equipo: {self.nombre}, Modelo de Auto: {self.modelo_auto}, Pilotos Titulares: {', '.join(str(p) for p in self.pilotos_titulares)}, Pilotos Reserva: {', '.join(str(p) for p in self.pilotos_reserva)}, Mecánicos: {', '.join(str(m) for m in self.mecanicos)}"

    def obtener_score_mecanicos(self):
        return sum(mecanico.score for mecanico in self.mecanicos)

    def obtener_pilotos(self):
        return self.pilotos_titulares + self.pilotos_reserva



class SimuladorF1:
    def __init__(self):
        self.empleados = []
        self.autos = []
        self.equipos = []

    def alta_empleado(self):
        try:
            id = int(input("Ingrese cedula: "))
            nombre = input("Ingrese nombre: ")
            fecha_nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
            nacionalidad = input("Ingrese nacionalidad: ")
            salario = float(input("Ingrese salario: "))

            print("Ingrese cargo:")
            print("1. Piloto")
            print("2. Piloto Reserva")
            print("3. Mecánico")
            print("4. Jefe de equipo")

            tipo_empleado = int(input("Seleccione el tipo de empleado: "))

            if tipo_empleado == 1:
                score = int(input("Ingrese score del piloto (entre 1 y 99): "))
                num_auto = int(input("Ingrese número de auto del piloto: "))
                piloto = Piloto(id, nombre, fecha_nacimiento, nacionalidad, salario, score, num_auto)
                self.empleados.append(piloto)

            elif tipo_empleado == 2:
                score = int(input("Ingrese score del piloto reserva (entre 1 y 99): "))
                num_auto = int(input("Ingrese número de auto del piloto reserva: "))
                piloto_reserva = PilotoReserva(id, nombre, fecha_nacimiento, nacionalidad, salario, score, num_auto)
                self.empleados.append(piloto_reserva)

            elif tipo_empleado == 3:
                score = int(input("Ingrese score del mecánico (entre 1 y 99): "))
                mecanico = Mecanico(id, nombre, fecha_nacimiento, nacionalidad, salario, score)
                self.empleados.append(mecanico)

            elif tipo_empleado == 4:
                jefe_equipo = DirectorEquipo(id, nombre, fecha_nacimiento, nacionalidad, salario)
                self.empleados.append(jefe_equipo)

            else:
                print("Tipo de empleado no válido.")

        except ValueError as e:
            print(f"Error: {e}")

    def alta_auto(self):
        try:
            # Dar de alta el auto
            modelo = input("Ingrese modelo: ")
            año = int(input("Ingrese año: "))
            score = int(input("Ingrese score: "))

            auto = Auto(modelo, año, score)
            self.autos.append(auto)
            print(f"Auto {modelo} ({año}) agregado exitosamente.")
        except ValueError as e:
            print(f"Error: {e}")

    def alta_equipo(self):
        try:
            nombre_equipo = input("Ingrese nombre del equipo: ")

            # Muestra los pilotos titulares existentes para seleccionar
            pilotos_titulares = [emp for emp in self.empleados if isinstance(emp, Piloto) and not emp.lesionado]
            print("\nPilotos titulares disponibles:")
            for i, piloto in enumerate(pilotos_titulares):
                print(f"{i + 1}. {piloto.nombre} - Equipo Actual: {piloto.equipo.nombre if piloto.equipo else 'Ninguno'}")

            # Selecciona pilotos titulares para el equipo
            titulares_seleccionados = []
            for _ in range(2):  # Seleccionar 2 titulares
                indice_titular = int(input("Seleccione el número del piloto titular: ")) - 1
                if 0 <= indice_titular < len(pilotos_titulares):
                    piloto_seleccionado = pilotos_titulares[indice_titular]
                    titulares_seleccionados.append(piloto_seleccionado)
                else:
                    print("Número de piloto no válido. Intente nuevamente.")
                    return  # Salir si hay un error

            # Selecciona pilotos reserva para el equipo
            pilotos_reserva_seleccionados = []
            for _ in range(1): 
                print("\nSeleccione piloto reserva para el equipo:")
                for i, piloto in enumerate(self.empleados):
                    if isinstance(piloto, PilotoReserva) and piloto not in pilotos_reserva_seleccionados:
                        print(f"{i + 1}. {piloto.nombre} - Equipo Actual: {piloto.equipo.nombre if piloto.equipo else 'Ninguno'}")

                indice_reserva = int(input("Seleccione el número del piloto reserva: ")) - 1
                if 0 <= indice_reserva < len(self.empleados):
                    piloto_reserva_seleccionado = self.empleados[indice_reserva]
                    
                    # Agregar el piloto reserva con la información adicional
                    piloto_reserva = PilotoReserva(
                        id=piloto_reserva_seleccionado.id,
                        nombre=piloto_reserva_seleccionado.nombre,
                        fecha_nacimiento=piloto_reserva_seleccionado.fecha_nacimiento,
                        nacionalidad=piloto_reserva_seleccionado.nacionalidad,
                        salario=piloto_reserva_seleccionado.salario,
                        score=piloto_reserva_seleccionado.score,
                        num_auto=piloto_reserva_seleccionado.num_auto,
                        piloto_reemplazado=piloto_reserva_seleccionado
                    )
                    
                    pilotos_reserva_seleccionados.append(piloto_reserva)
                else:
                    print("Número de piloto reserva no válido. Intente nuevamente.")
                    return  # Salir si hay un error

            # Muestra los mecánicos disponibles para seleccionar
            mecanicos_disponibles = [emp for emp in self.empleados if isinstance(emp, Mecanico)]
            print("\nMecánicos disponibles:")
            for i, mecanico in enumerate(mecanicos_disponibles):
                print(f"{i + 1}. {mecanico.nombre} - Equipo Actual: {mecanico.equipo.nombre if mecanico.equipo else 'Ninguno'}")

            # Selecciona mecánicos para el equipo
            mecanicos_seleccionados = []
            for _ in range(8):  # Seleccionar 8 mecánicos
                indice_mecanico = int(input("Seleccione el número del mecánico: ")) - 1
                if 0 <= indice_mecanico < len(mecanicos_disponibles):
                    mecanico_seleccionado = mecanicos_disponibles[indice_mecanico]
                    mecanicos_seleccionados.append(mecanico_seleccionado)
                else:
                    print("Número de mecánico no válido. Intente nuevamente.")
                    return  # Salir si no funciona

            # Muestra el auto disponible para seleccionar
            autos_disponibles = [auto for auto in self.autos]
            print("\nAutos disponibles:")
            for i, auto in enumerate(autos_disponibles):
                print(f"{i + 1}. {auto.modelo} - Año: {auto.año}")

            # Selecciona el auto para el equipo
            indice_auto = int(input("Seleccione el número del auto: ")) - 1
            if 0 <= indice_auto < len(autos_disponibles):
                auto_seleccionado = autos_disponibles[indice_auto]
            else:
                print("Número de auto no válido. Intente nuevamente.")
                return  # Salir si algo es invalido

            # Muestra los jefes de equipo disponibles para seleccionar
            jefes_equipo_disponibles = [emp for emp in self.empleados if isinstance(emp, DirectorEquipo) and emp.equipo is None]
            print("\nJefes de equipo disponibles:")
            for i, jefe_equipo in enumerate(jefes_equipo_disponibles):
                print(f"{i + 1}. {jefe_equipo.nombre}")

            # Selecciona el jefe de equipo para el equipo
            indice_jefe_equipo = int(input("Seleccione el número del jefe de equipo: ")) - 1
            if 0 <= indice_jefe_equipo < len(jefes_equipo_disponibles):
                jefe_equipo_seleccionado = jefes_equipo_disponibles[indice_jefe_equipo]
            else:
                print("Número de jefe de equipo no válido. Intente nuevamente.")
                return  # Salir si hay algo invalido

            # Crea el equipo y asigna empleados y auto
            equipo = Equipo(nombre_equipo, auto_seleccionado, titulares_seleccionados, pilotos_reserva_seleccionados, mecanicos_seleccionados)
            self.equipos.append(equipo)

            # Asigna el equipo a los empleados seleccionados
            for emp in titulares_seleccionados + pilotos_reserva_seleccionados + mecanicos_seleccionados + [jefe_equipo_seleccionado]:
                emp.equipo = equipo

            print(f"Equipo {nombre_equipo} agregado exitosamente.")
        except ValueError as e:
            print(f"Error: {e}")

