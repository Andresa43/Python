from tkinter import END


altura = float(input('Digite a altura da parede: '))

largura = float(input('Digite a largura da parede: '))

area = altura * largura 

litro = area / 2

print('Sua parede tem dimensão {}x{} e sua área é de {}m². Você precisará de {} litros de tinta para pintar a sua parede '.format(altura, largura, area, litro))