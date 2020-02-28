#almacenar resultados de futbol para sacar estadisticas y probabilidades 
#de futuros partidos 

equipos = {
    1:{
        'equipo': 'real madrid',
        'goles' : 6,
        'recibidos' : 5,
        'victorias' : 1,
        'derrotas' : 0,
        'empates' : 2
    },

    2:{
        'equipo': 'barcelona',
        'goles' : 7,
        'recibidos' : 5,
        'victorias' : 1,
        'derrotas' : 1,
        'empates' : 1
    },

  3:{
        'equipo': 'atletico de madrid',
        'goles' : 5,
        'recibidos' : 2,
        'victorias' : 3,
        'derrotas' : 0,
        'empates' : 0
    }
}

def prediccionPartido(equipo_1, equipo_2):
    equipo_local = equipo_1['equipo']
    equipo_visitante = equipo_2['equipo']
    local = 0
    visitante = 0
    empate = 0
    if equipo_1['goles'] > equipo_2['goles']:
        local += 1
    elif equipo_1['goles'] < equipo_2['goles']:
        visitante += 1
    else:
        empate +=1 

    if equipo_1['recibidos'] < equipo_2['recibidos']:
        local += 1
    elif equipo_1['recibidos'] > equipo_2['recibidos']:
        visitante += 1
    else:
        empate +=1 

    if equipo_1['victorias'] > equipo_2['victorias']:
        local += 1
    elif equipo_1['victorias'] < equipo_2['victorias']:
        visitante += 1
    else:
        empate +=1 

    if equipo_1['derrotas'] < equipo_2['derrotas']:
        local += 1
    elif equipo_1['derrotas'] > equipo_2['derrotas']:
        visitante += 1
    else:
        empate +=1 

    if equipo_1['empates'] < equipo_2['empates']:
        local += 1
    elif equipo_1['empates'] > equipo_2['empates']:
        visitante += 1
    else:
        empate +=1 

    print('local : '+str(local))
    print('visitante : '+str(visitante))
    print('empate : '+str(empate))

    if empate > local and visitante:
        print('las probabilidades de empate son altas')
    elif local > visitante:
        print(f'{equipo_local} tiene mas probabilidades de ganar')
    elif local < visitante:
        print(f'{equipo_visitante} tiene mas probabilidades de ganar')
    

equipo_local= {}
equipo_visitante= {}
local = input('ingrese el equipo local: ')
visitante = input('ingrese equipo visitante: ')
for equipo in equipos:
    if local in  equipos[equipo]['equipo']:
        equipo_local = equipos[equipo]
        print(equipo_local)
    
    if visitante in equipos[equipo]['equipo']:
        equipo_visitante = equipos[equipo]
        print(equipo_visitante)
    

if equipo_local == {}  and equipo_visitante == {} :
    print('seleccionar dos equipos para realizar la prediccion')    
else: 
    prediccionPartido(equipo_local, equipo_visitante)  
     





