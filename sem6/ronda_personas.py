import config


cuenta = int(0) # tipado estático
persona = 0 # tipado dinámico

giro = "horario"


if (config.LIMITE_CUENTA >= config.PERSONAS):
    # for ciclo in range(config.LIMITE_CUENTA):
    while (cuenta < config.LIMITE_CUENTA):
        cuenta = cuenta + 1 # se aumenta en 1 contador general

        if (giro == "horario"):
            if (persona == config.PERSONAS):
                persona = 0
            persona = persona + 1 # se suma 1 a contador de persona
        else:
            if (persona == 1):
                persona = config.PERSONAS + 1
            persona = persona - 1 # se resta 1 a contador de persona
        
        print(persona, cuenta)
        
        if (cuenta % 8 == 0): # cuenta es perfectamente divisible por 8
            if (giro == "horario"):
                giro = "antihorario"
            else:
                giro = "horario"

        if (cuenta % 11 == 0): # cuenta es perfectamente divisible por 11
            if (giro == "horario"):
                persona = persona + 1
            else:
                persona = persona - 1
else:
    print("Límite de cuenta menor a la cantidad de personas en la ronda")
