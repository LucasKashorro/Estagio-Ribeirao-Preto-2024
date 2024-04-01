inp = int(input("Insira a quantidade de termos da sequência: "))
if inp == 1:
    sequencia = [0]
else:
    sequencia = [0,1]

for i in range(inp - 2):
    termo = sequencia[-1] + sequencia[-2]
    sequencia.append(termo)
    
print(sequencia)