#jogo da adivinhacao
import random
aleatorio=random.randrange(0, 100)
tentativas=0
venceu=False
print("Bem vindo ao jogo da forca")
print("Você deve adivinhar um número entre 0 e 100")

def compara(palpite,aleatorio):
	if(palpite>aleatorio):
		print("Menos!")
	if(palpite<aleatorio):
		print("Mais!")
	if(palpite==aleatorio):
		global venceu
		venceu=True
        

while(venceu==False):
    palpite=int(input("Digite seu palpite:"))
    compara(palpite,aleatorio)
    tentativas=tentativas+1

print(f"Você acertou em {tentativas} tentativas")


