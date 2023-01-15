### mini sistema de notas

sistema={
    'nombreDeInstitucion':"Colegio N",
    'cursos':["python","javascript","java","php"],
    'profesores':["profesor1","profesor2"],
    'alumnos':{
        "7753":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python"],
                "notas":{}
                },
        "7754":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["python","java"],
                "notas":{}
                },
        "7755":{"nombre":"juan",
                "apellido":"rodriguez",
                "cursos":["php"],
                "notas":{}
                },
    },
    "cursoProfesor":{
        "python":[],
        "javascript":[],
        "java":[],
        "php":[]
    }
}

##asignar profesor curso
profesoresActuales=sistema['profesores']
profesorPorAsignar=input("que profesor es: ")
if profesorPorAsignar in profesoresActuales:
    print("existe el profesor")
    print(sistema["cursos"])
    cursoPorAsignar=input("Que curso va asignar a este profesor:")
    if cursoPorAsignar in sistema['cursos']:
            cursoTemp=sistema["cursoProfesor"][cursoPorAsignar]
            cursoTemp.append(profesorPorAsignar)
            sistema['cursoProfesor'][cursoPorAsignar]=cursoTemp
    else:
        print('no existe el curso')    
else:
    print("no existe profesor,desea agregarlo")
    print(profesorPorAsignar,sistema['profesores'])
    profesorTemp=sistema['profesores']
    profesorTemp.append(profesorPorAsignar)
    sistema['profesores']=profesorTemp
    print(sistema)

## asignar nota a alumno
codAlumno=input("ingrese el codigo del alumno")
listaAlumnos=list(sistema["alumnos"].keys())
if codAlumno in listaAlumnos:
    print("alumno existe")
    cursosDelAlumno=sistema["alumnos"][codAlumno]["cursos"]
    notas=sistema["alumnos"][codAlumno]["notas"]
    notaPorIngresar=int(input("ingrese la nota por asignar"))
    sistema["alumnos"][codAlumno]["notas"]={'python':[notaPorIngresar]}
    print(sistema)
else:
    print("alumno no existe")



