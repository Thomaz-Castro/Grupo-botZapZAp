import pyautogui
from time import sleep

# https://api.whatsapp.com/send?phone=XXXXXXXXXXX    Comando api whatsapp
# Point(x=933, y=53)  barra de pesquisa
# Point(x=688, y=357) iniciar conversa
# Point(x=702, y=426) usar o web
# Point(x=925, y=701) clica para digitar a mensagem

sleep(3)


print('================ BOT ZAP ZAP ================\n')
print('                    online                   ')
numlista = [12996395090,12981952413,24999033643,12991888048,35992431957,12981730285,12981270088,12996459416,1298115232355,12997310050,12988783974,12988232059,12997337493,12992575747,12996574350,12981559699,12988129082,12996172298,12997978432,11964768349,12996572202,12996087292,12991595563,12996671788,85999801478,12991276579,12981544723,12996563132,12982768155
                    ]
lelis = len(numlista)

msg = """slvvv, é o thomaz entra ai no grupo da sala
https://chat.whatsapp.com/IA75eKS0MxO7rsS7U3erZe"""

for l in range (0,(lelis+1)):
    processado = str(numlista[l])
    
    if processado.isnumeric() == True and len(processado) == 11:

        print('\nNúmero em Processo: '+ processado)

        #Entro no link do whatsapp
        pyautogui.moveTo(933,53,duration=0.5)
        pyautogui.click()
        pyautogui.press("backspace")
        sleep(1)

        link = str("https://api.whatsapp.com/send?phone=55"+processado)

        pyautogui.write(link)
        sleep(1)
        pyautogui.press("enter")

        #Clico para inciar uma conversa
        pyautogui.moveTo(688,357,duration=0.5)
        sleep(3)
        pyautogui.click()

        #Clicou para utilizar o whatsapp web
        pyautogui.moveTo(702,426,duration=0.5)
        sleep(2)
        pyautogui.click()


        #clica para digitar a mensagem
        pyautogui.moveTo(925,701,duration=0.5)
        sleep(10)
        pyautogui.write(msg)
        pyautogui.click("enter")
        print('Número ({}) processado, mensagem enviada com sucesso'.format(processado))
        print('-='*20)
        print('')
        sleep(3)
        

    else:
        print('\nNumero erronio: '+ processado)
        print('É número?: '+ str(processado.isnumeric()))
        print('Número de digitos: '+ len(processado))
        print('-='*20)
        print('')
        sleep(2)

print('\nProcesso finalizado\n')
print('================ BOT ZAP ZAP ================\n')
print('                  offline                    ')