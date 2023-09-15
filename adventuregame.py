print('''
                                        _   __,----'~~~~~~~~~`-----.__
                                   .  .    `//====-              ____,-'~`
                   -.            \_|// .   /||\\  `~~~~`---.___./
             ______-==.       _-~o  `\/    |||  \\           _,'`
       __,--'   ,=='||\=_    ;_,_,/ _-'|-   |`\   \\        ,'
    _-'      ,='    | \\`.    '',/~7  /-   /  ||   `\.     /
  .'       ,'       |  \\  \_  "  /  /-   /   ||      \   /
 / _____  /         |     \\.`-_/  /|- _/   ,||       \ /
,-'     `-|--'~~`--_ \     `==-/  `| \'--===-'       _/`
          '         `-|      /|    )-'\~'      _,--"'
                      '-~^\_/ |    |   `\_   ,^             /\
                           /  \     \__   \/~               `\__
                       _,-' _/'\ ,-'~____-'`-/                 ``===\
                      ((->/'    \|||' `.     `\.  ,                _||
        ./                       \_     `\      `~---|__i__i__\--~'_/
       <_n_                     __-^-_    `)  \-.______________,-~'
        `B'\)                  ///,-'~`__--^-  |-------~~~~^'
        /^>                           ///,--~`-\
       `  `
''')
print("Bienvenido a la mazmorra del dragon rojo.")
print("tu mision es encontrar la guarida del dragón y tomar su botín") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
decision = input("Entras a la mazmorra y lo primero que ves son dos caminos divididos, uno esta completamente oscuro el otro tiene una luz naranja al fondo, cual eliges ? oscuro o naranja\n")
decision_min = decision.lower()

if decision_min == "oscuro":
    decision = input("Enciendes una antorcha y te diriges al fondo, cuando llegas al final te encuentras con un cofre: lo abres? Si o no\n")
    decision_min = decision.lower()
    if decision_min == "si":
        print("Era un cofre trampa y mueres, GAME OVER")
    elif decision_min == "no":
        print("Ignoras el cofre y continuas caminando de repente te emboscan 6 arañas gigantes las cuales te atacan sin piedad y mueres. GAME OVER")    
elif decision_min == "naranja":
    decision = input("Caminas al fondo y llegas a la luz naranja por sorpresa era un ciclope con antorcha, decide que hacer: LUCHAR O HUIR?\n ")
    decision_min = decision.lower()
    if decision_min == "luchar":
        decision = input("Fue un duro combate pero derrotaste al ciclope terminaste algo herido pero aun puedes seguir de pie asi que continuas hacia adelante en el camino, te encuentras 2 puertas una roja y otra azul cual abres?: roja o azul\n")
        decision_min = decision.lower()
        if decision_min == "roja":
            print("Felicidades encontraste el botín del dragón, has conquistado la mazmorra")
        elif decision_min == "azul":
            print("Abres la puerta y te encuentras cara a cara con el dragón, el dragón te escupe una llamarada y mueres al instante. GAME OVER!!")    
    elif decision_min == "huir":
        print("El ciclope te alcanza con su mano y te atrapa, te aplasta y mueres al instante. GAME OVER")
