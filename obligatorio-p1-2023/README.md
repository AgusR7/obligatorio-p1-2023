Simulador de Carreras de Fórmula 1
Este es un simulador de carreras de Fórmula 1 desarrollado en Python. Permite gestionar empleados, autos, equipos y simular carreras, proporcionando resultados y consultas relacionadas con el campeonato.

Contenido del Código
Clases Principales
Empleado: Representa a un empleado genérico, con atributos como ID, nombre, fecha de nacimiento, nacionalidad y salario.

ParticipanteCarrera: Clase abstracta que define métodos para simular carreras y gestionar eventos como lesiones y abandonos.

Piloto: Subclase de Empleado y ParticipanteCarrera, modela a un piloto de Fórmula 1. Incluye métodos específicos para simular carreras y eventos relacionados.

PilotoReserva: Subclase de Empleado y ParticipanteCarrera, representa a un piloto de reserva con la capacidad de ocupar el lugar de un piloto titular.

Mecanico: Subclase de Empleado, representa a un mecánico con un puntaje asociado.

DirectorEquipo: Subclase de Empleado, modela a un director de equipo.

Auto: Representa un automóvil con modelo, año y un puntaje asociado.

Equipo: Representa un equipo de Fórmula 1 con nombre, modelo de auto, pilotos titulares, pilotos de reserva y mecánicos.

SimuladorF1
SimuladorF1: Clase principal que contiene métodos para gestionar empleados, autos, equipos y realizar simulaciones de carreras. Proporciona opciones para realizar consultas sobre el campeonato.

Ejecución
Requisitos:

Python 3.x instalado.
Ejecución (2 métodos):

Método 1. Ejecuta el código en un interprete compatible con Python

Método 2. Copia y pega el código en un archivo Python (por ejemplo, obligatorio-p1-2023.py).
Ejecuta el archivo Python haciendo doble click o llamandolo en CMD/Bash de la forma: python obligatorio-p1-2023.py (en caso de haber nombrado de esa manera al archivo).

Uso del Programa:
El programa presenta un menú interactivo con opciones para dar de alta empleados, autos y equipos, simular carreras y realizar consultas sobre el campeonato.

Notas Adicionales
Asegúrate de proporcionar la información solicitada de manera adecuada durante la ejecución del programa para obtener resultados precisos en la simulación de carreras y consultas.
El programa fue diseñado de tal manera que requiere una linealidad de decisiones, donde para poder ejecutar satisfactoriamente la simulación de carreras o realizar consultas; se deba previamente concretar la correspondiente alta de empleados, autos y equipos.
Los resultados de la simulación de carreras y las consultas se mostrarán en la consola.

Agustín Rivera, Jonathan Mazzoli - Universidad de Montevideo, 2023.

