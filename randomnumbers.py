#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
	 
#Write the rest of your code below this line 👇
lanzamiento = random.randint(0 , 1)

if lanzamiento == 1:
    print("Heads")
elif lanzamiento == 0:
    print("Tails")