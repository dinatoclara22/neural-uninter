import numpy as np

# Definindo entradas
entradas = np.array([[4150760]])
saidas_esperadas = np.array([1])

# Inicializando pesos e bias aleatoriamente
pesos = np.random.uniform(-1, 1, size=1)
bias = np.random.uniform(-1, 1)
taxa_aprendizado = 0.1

def func_ativacao(soma):
    """
    Função de ativação que retorna 1 se a soma for maior ou igual a 0, caso contrário retorna 0.
    """
    return 1 if soma >= 0 else 0

def calcular_saida(entradas, pesos, bias):
    """
    Calcula a saída do neurônio com base nas entradas, pesos e bias.
    """
    soma_ponderada = np.dot(entradas, pesos) + bias
    return func_ativacao(soma_ponderada)

def treinar_neuronio(entradas, saidas_esperadas, pesos, bias, taxa_aprendizado, epocas):
    """
    Treina o neurônio usando a regra Delta.
    """
    for epoca in range(epocas):
        erro_total = 0

        for i in range(len(entradas)):
            saida = calcular_saida(entradas[i], pesos, bias)
            erro = saidas_esperadas[i] - saida
            pesos = pesos + taxa_aprendizado * erro * entradas[i]
            bias = bias + taxa_aprendizado * erro
            erro_total += abs(erro)

        if erro_total == 0:
            print(f"Treinamento finalizado após {epoca+1} épocas.")
            break

    return pesos, bias

def main():
    epocas = 10000
    pesos_finais, bias_final = treinar_neuronio(entradas, saidas_esperadas, pesos, bias, taxa_aprendizado, epocas)

    # Resultado final
    print("Pesos finais:", pesos_finais)
    print("Bias final:", bias_final)

if __name__ == "__main__":
    main()