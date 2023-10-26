def main():
    # Definición del número total de curules a asignar
    CURULES = 18

    # Lista de partidos con sus respectivos votos
    PARTIDOS = [
        {'partido': '', 'votos': 0},
    ]

    # Función para calcular los votos divididos por un divisor 'i'
    def calcular_votos_divisor(partido, i):
        puesto = partido['votos'] / i
        return {
            'partido': partido['partido'],
            'votos': partido['votos'],
            'curul': i,
            'votosDivisor': int(puesto)
        }

    # Generar una lista de todos los partidos con sus votos divididos para cada curul
    partidosCurules = [calcular_votos_divisor(partido, i) for partido in PARTIDOS for i in range(1, CURULES + 1)]

    # Ordenar la lista de partidos por votosDivisor en orden descendente
    partidosCurules.sort(key=lambda x: x['votosDivisor'], reverse=True)

    # Seleccionar a los ganadores (los primeros CURULES partidos en la lista ordenada)
    ganadores = partidosCurules[:CURULES]

    # Imprimir la lista de partidos ganadores
    for ganador in ganadores:
        print(ganador)

    try:
        # Solicitar datos al usuario
        curul_deseada = int(input("Ingresa la curul deseada: "))
        votos_obtenidos = int(input("Ingresa los votos obtenidos: "))

        # Buscar la entrada correspondiente a la curul deseada en la lista de ganadores
        entrada_curul_deseada = ganadores[-1]

        if entrada_curul_deseada is not None:
            # Calcular los votos necesarios y faltantes para obtener la curul deseada
            votos_per_curul = int(votos_obtenidos / curul_deseada)
            votos_necesarios = entrada_curul_deseada['votosDivisor']
            votos_faltantes = (votos_necesarios - votos_per_curul) * curul_deseada

            if votos_faltantes > 0:
                print(f"Necesitas al menos {votos_faltantes} votos adicionales para obtener la curul {curul_deseada}.")
            elif votos_faltantes == 0:
                print("Ya tienes suficientes votos para obtener la curul.")
            else:
                print("Ya tienes más votos que los necesarios para obtener la curul.")
        else:
            print(f"No se encontró la curul {curul_deseada} en la lista de partidos ganadores.")
    except ValueError:
        print("Ingresa un valor numérico válido.")

if __name__ == '__main__':
    main()
