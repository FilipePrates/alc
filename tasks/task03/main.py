# // Técnica Numérica = Quadratura numérica “cobrir com
# // quadrados” (uso diferente daquele empregado em
# // integração de equações diferenciais parciais).
# // Obs.: ordenadas e pesos para a Quadratura de Gauss podem ser acessados, por
# // exemplo, em https://pomax.github.io/bezierinfo/legendre-gauss.html

# // Dividir em retângulos, calcular a área de cada um:
# // Base x Altura => 
# //  Base/"largura" = deltaX ; (fim - início) / N (Número de Pontos de Integração/Retângulos)
# //  Altura = (f(x)+f(x+1))/2 ; média de cada lado do retângulo
# // Soma todos as Áreas dos retângulos e obtém aproximação final.

# // Objetivo -> Obter aproximação acurada com menor N possível (+ barato computacionalmente)
