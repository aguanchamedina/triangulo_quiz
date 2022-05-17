#Determinar si un triangulo es equilatero, isoceles o escaleno 

a=int(input("ingrese lado a: "))
b=int(input("ingrese lado b: "))
c=int(input("ingrese lado c: "))

if a==b and b==c:
  print("el triangulo es equilatero")
elif a==c or b == c or c==a or a==b:
  print("el triangulo es isoceles")
else:
  print("el triangulo escaleno")