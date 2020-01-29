import datetime

def formato_horas(hora):
    formatoSalida = '%H:%M'
    hora = hora.replace('.', ':')
    if 'PM' in hora and ':' in hora:
        format = '%I:%M%p'
    elif 'PM' in hora:
        format = '%I%p'
    elif ':' in hora:
        format = '%H:%M'
    else:
        format = '%H'

    tempDate = datetime.datetime.strptime(hora, format)
    hora_con_formato = tempDate.strftime(formatoSalida)

    return hora_con_formato


horas = ['3PM', '18:30', '13', '4.10PM', '5']
horas_uniformes = []

for hora in horas:
    horas_uniformes.append(formato_horas(hora))

print(horas_uniformes)

