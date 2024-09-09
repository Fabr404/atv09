# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).
km = float(input("kms percoridos : "))
consumo = float(input("consumo : "))
total = (km/consumo)
print(f"o total foi de {total}  km por litro ")