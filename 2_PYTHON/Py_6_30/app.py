from clases.Institucion import Institucion
from clases.Alumno import Alumno

codo = Institucion("Codo a Codo")
codo.agregarAlumno(Alumno('Sofia G.', '33554566'))
codo.agregarAlumno(Alumno('Ezequiel R..', '44556688'))
codo.agregarAlumno(Alumno('Mora R.', '23454332'))
codo.agregarAlumno(Alumno('Pamela G.', '220098765'))
codo.agregarAlumno(Alumno('Luciano G.', '2221111135'))
eylin = Alumno('Eylin R.', '28282828')
codo.agregarAlumno(eylin)

print()
codo.mostrarAlumnos()

codo.buscarPersonaPorDni('28282828')