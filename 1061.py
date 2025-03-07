#estipulamos os valores de entrada para o horário inicial
palavra_dia, Sdi = input().split()
shi, smi, ssi = input().split(":")

# Convertemos as strings para inteiros
diai = int(Sdi)
hi = int(shi)
mi = int(smi)
si = int(ssi)

# Calculamos o tempo em segundos para o horário inicial
segi = hi * 3600 + mi * 60 + si

#estipulamos os valores de entrada para o horário final
palavra_dia_fim, Sdf = input().split()
shf, smf, ssf = input().split(":")

#Convertemos as strings para inteiros
diaf = int(Sdf)
hf = int(shf)
mf = int(smf)
sf = int(ssf)

# Calculamos o tempo em segundos para o horário final
segf = hf * 3600 + mf * 60 + sf

# Calculamos a diferença de tempo em segundos
Dh = segf - segi

# Verificamos se a diferença de tempo é negativa (significando que o horário final é no dia seguinte)
if Dh >= 0:
    dd = diaf - diai
else:
    dd = diaf - diai - 1
    Dh = 24 * 3600 - segi + segf

# Calculamos as horas, minutos e segundos
h = Dh // 3600
ms = Dh % 3600
m = ms // 60
s = ms % 60

# Imprime o resultado
print('{0:d} dia(s)'.format(dd))
print('{0:d} hora(s)'.format(h))
print('{0:d} minuto(s)'.format(m))
print('{0:d} segundo(s)'.format(s))
