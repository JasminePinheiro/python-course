idade = 22
nome = "Jasmine"
if idade > 18:
    print(f"{nome} pode dirigir")
    
# Operador and



# Operador not
numero = 4

if (numero > 2) and (numero < 5):
    print(numero)
else:
    print("O número não atende as restrições")    

# Operador or
if (numero > 2) or (numero % 2 == 0):
    print(numero)
else:
    print("O número não atende as restrições")    
    
# Operador not
# o not invalida a regra
if not(numero > 5) and (numero % 2 == 0):
    print("Isso será impresso se as duas condições são verdadeiras")
else:
    print("Falso")
    
disciplina = 'Data Science'
nota_final = 90
semestre = 2
if disciplina == 'Data Science' and nota_final >= 80 and semestre != 1:
    print("Você está aprovado em %s com a nota final %s" %(disciplina, nota_final))
else:
    print("Você não está aprovado em %r com a nota final %r" %(disciplina, nota_final))
    
# Saída: Você não está aprovado em Matemática com a nota final 7.5 usando o %s ('amigavel' ao usuario)
# Saída: Você não está aprovado em 'Matemática' com a nota final 7.5 usando o %r (não tão 'amigavel')