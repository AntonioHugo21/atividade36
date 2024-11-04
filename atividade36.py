notas = []

for cont in range(0,4):
    notas.append(float(input('Digite sua nota: ')))
    
media = sum(notas) / len(notas)

print(f'Suas notas foram {notas}')
print(f'A sua média de notas é {media}')