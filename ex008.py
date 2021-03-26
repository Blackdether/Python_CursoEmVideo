distancia = float(input('Digite a distância em metros: '))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
centimetros = int(distancia * 100)
milimetros = int(centimetros * 10)
print('A distância percorrida: \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \nem metros é {}m; {}\n{:.0f}dm  \nem centímetros é {}cm; \nem milímetros é {}mm.'.format(km, hm, dam, distancia,'\033[31m', dm,  centimetros, milimetros))
