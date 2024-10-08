## Definição dos dados de entrada e saída
O código utiliza uma entrada única fornecida (4150760) e define a saída esperada como 1 para fins de classificação binária.

## Inicialização dos Pesos e Bias
Os pesos e o bias são inicializados de forma aleatória para iniciar o treinamento do neurônio, conforme explicado na seção sobre treinamento de perceptrons.

## Função de Ativação
Foi usada a função de ativação de degrau, retornando 1 se a soma ponderada das entradas for maior ou igual a 0 e 0 caso contrário. O propósito é simples e eficaz para classificações binárias.

## Características

- Função de ativação: A função degrau foi escolhida pela simplicidade e eficiência em problemas de classificação binária.
- Taxa de aprendizado: O valor de 0.1 foi utilizado para garantir que o ajuste dos pesos ocorresse gradualmente, evitando oscilações bruscas.
- Número de épocas: O treinamento foi programado para rodar até 10.000 iterações ou até que o erro total fosse zero, garantindo a convergência.
