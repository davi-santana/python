''' Faça um algoritmo que leia a duração de um
evento em uma fábrica, expresso em segun-
dos, e mostre-o em horas, minutos e segun-
dos. '''

segundos = int(input("Digite a duração do evento em segundos: "))
horas = int(segundos / 3600)
segundos = (segundos % 3600)
minutos = int(segundos / 60)
segundos = int(segundos % 60)
print("A duração do evento e de {} horas {} minutos e {} segundos" .format(horas, minutos, segundos))
