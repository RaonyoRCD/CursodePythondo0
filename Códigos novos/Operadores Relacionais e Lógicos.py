# Neste código estou usando apenas o operador relacional ==, mas eu poderia usar qualquer outro operador relacional que eu quiser (==; !=; >; <; >= ou <=) Claro que com a troca deste operador, os resultados também serão modificados.

# Também estou utilizando os operadores lógicos AND; OR e NOT.

A=5
B=10
C=10
print("Minhas variáveis são: A=5, B=10 e C=10.")

print("")

print("Estes são os de sinal == com o operador lógico AND:")
print(A==B and B==A)# Operador Relacional de igualdade + o and (E)
print(A==C and C==A)# Operador Relacional de igualdade + o and (E)
print(B==C and C==A)# Operador Relacional de igualdade + o and (E)
print(A==A and A==A)# Operador Relacional de igualdade + o and (E)

print("")

print("Estes são os de sinal == com o operador lógico or:")
print(A==B or B==A)# Operador Relacional de igualdade + o or (E)
print(A==C or C==A)# Operador Relacional de igualdade + o or (E)
print(B==C or C==A)# Operador Relacional de igualdade + o or (E)
print(A==A or A==A)# Operador Relacional de igualdade + o or (E)

print("")

print("Estes são os de sinal == com o operador lógico not:")
print(not (B==A and A==B))# Operador Lógico de negação NOT.
print(not B==A or A==C)# Operador Lógico de negação NOT.
print(not (B==A or B==C))# Operador Lógico de negação NOT.
print(not C==A)# Operador Lógico de negação NOT.
print(not A==A)# Operador Lógico de negação NOT.