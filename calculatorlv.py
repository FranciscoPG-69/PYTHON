print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


#cuenta cuantas veces las letras L O V E aparecen en cada uno de los nombres 
counter1 = 0
counter2 = 0
name1_lower = name1.lower()
name2_lower = name2.lower()


#in es un operador conocido como operador de pertenencia  que verifica si cierto elemento aparece en una secuencia 
if ("l") in name1_lower:
    counter1 = name1_lower.count("l")#aqui la funcion count esta devolviendo un valor numerico el cual se esta almacenando en una variable llamada counter la cual ira aumentando si las condiciones se cumplen
   
if ("o") in name1_lower:
      counter1 += name1_lower.count("o")

if ("v") in name1_lower:
      counter1 += name1_lower.count("v")

if ("e") in name1_lower:
      counter1 += name1_lower.count("e")

if ("t") in name1_lower:
      counter1 += name1_lower.count("t")

if ("r") in name1_lower:
      counter1 += name1_lower.count("r")

if ("u") in name1_lower:
      counter1 += name1_lower.count("u")

if ("e") in name1_lower:
      counter1 += name1_lower.count("e")
#verificando el nombre2 
if ("l") in name2_lower:
       counter2 += name2_lower.count("l")
if ("o") in name2_lower:
       counter2 += name2_lower.count("o")
if ("v") in name2_lower:
       counter2 += name2_lower.count("v")
if ("e") in name2_lower:
        counter2 += name2_lower.count("e")
if ("t") in name2_lower:
        counter2 += name2_lower.count("t")
if ("r") in name2_lower:
        counter2 += name2_lower.count("r")
if ("u") in name2_lower:
        counter2 += name2_lower.count("u")
if ("e") in name2_lower:
        counter2 += name2_lower.count("e")
        

counters = str(counter1)+str(counter2)
print(counter1)
print (counter2)
print(counters)
counters_numer = int(counters)

if counters_numer < 10 or counters_numer > 90:
       print(f"Your score is {counters_numer}, you go together like coke and mentos.")
elif counters_numer >= 40 and counters_numer <=50:
       print(f"Your score is {counters_numer}, you are alright together.")
else:
       print(f"Your score is {counters_numer}")
