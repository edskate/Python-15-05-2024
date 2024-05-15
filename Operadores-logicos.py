idade = 15
altura = 1.75

resultado = (idade >= 18) and (altura >= 1.70)
msg = 'pode participar do evento ' + str(resultado)
print(msg)

# programa de disparo de alarme

porta = 'f'
janela = 'a'

alarme = (porta == 'a') or (janela =='a')
masg = 'Alarme disparado ' + str(alarme)
print(masg)

tem_dinheiro = True
tem_dinheiro = not tem_dinheiro
masg = 'tem dinheiro ' + str(tem_dinheiro)
print(masg)