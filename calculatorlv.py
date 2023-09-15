print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


#cuenta cuantas veces las letras L O V E aparecen en cada uno de los nombres 
#cuenta cuantas veces las letras L O V E aparecen en cada uno de los nombres 
counter1 = 0
counter2 = 0
name1_lower = name1.lower()
name2_lower = name2.lower()


#in es un operador conocido como operador de pertenencia  que verifica si cierto elemento aparece en una secuencia 
if ("l") in name1_lower:
    counter1 = name1_lower.count("l")#aqui la funcion count esta devolviendo un valor numerico el cual se esta almacenando en una variable llamada counter la cual ira aumentando si las condiciones se cumplen
if ("l") in name2_lower:
         counter2 = name2_lower.count("l")
if ("o") in name1_lower:
      counter1 += name1_lower.count("o")
if ("o") in name2_lower:
        counter2 += name2_lower.count("o")
if ("v") in name1_lower:
      counter1 += name1_lower.count("v")
if ("v") in name2_lower:
         counter2 += name2_lower.count("v")
if ("e") in name1_lower:
      counter1 += name1_lower.count("e")
if ("e") in name2_lower:
       counter2 += name2_lower.count("e")
         
total_counters1 = counter1 + counter2

counter1 = 0
counter2 = 0
if ("t") in name1_lower:
    counter1 = name1_lower.count("t")#aqui la funcion count esta devolviendo un valor numerico el cual se esta almacenando en una variable llamada counter la cual ira aumentando si las condiciones se cumplen
if ("t") in name2_lower:
         counter2 = name2_lower.count("t")
if ("r") in name1_lower:
      counter1 += name1_lower.count("r")
if ("r") in name2_lower:
        counter2 += name2_lower.count("r")
if ("u") in name1_lower:
      counter1 += name1_lower.count("u")
if ("u") in name2_lower:
         counter2 += name2_lower.count("u")
if ("e") in name1_lower:
      counter1 += name1_lower.count("e")
if ("e") in name2_lower:
       counter2 += name2_lower.count("e")
      
total_counters2 = counter1 + counter2      
counters = str(total_counters2)+str(total_counters1)
#print(total_counters1)
#print (total_counters2)
#print(counters)
counters_numer = int(counters)

if counters_numer < 10 or counters_numer > 90:
       print(f"Your score is {counters_numer}, you go together like coke and mentos.")
elif counters_numer >= 40 and counters_numer <=50:
       print(f"Your score is {counters_numer}, you are alright together.")
else:
       print(f"Your score is {counters_numer}")
#hacer 4 contadores que verificaran las letras por ej. true --> name1 y name 2 cada uno
#con sus contadores para que al final de haga la suma, luego otras 2 para la palabra love --> name1 y name2
#counter1, counter2, counter3, counter4