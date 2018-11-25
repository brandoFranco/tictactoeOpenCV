#
# Jogo da Velha utilizando Visao Computacional e Realidade aumentada.
#

import numpy as np
import cv2
import play
from random import randint
from time import sleep


cap = cv2.VideoCapture(0)
tamanho = (500, 500)
pts2 = np.float32([[0,0], [tamanho[1], 0], [0, tamanho[0]], [tamanho[1], tamanho[0]]])


tabuleiro = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
tabuleiro2 = [False, False, False, False, False, False, False, False, False]
escolhas = []

while(cap.isOpened() and play.won(tabuleiro) == 0):
	ret, img = cap.read()

	if ret==True:
		imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ret2,thresh = cv2.threshold(imgray,170,255,0)
		image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		for i in range(len(contours)):
			area = cv2.contourArea(contours[i])
			aprox = cv2.approxPolyDP(contours[i], 0.02 * cv2.arcLength(contours[i], True), True)
			if area > 10000 and len(aprox) == 4:

				aprox = play.ordena(aprox, img.shape[:2])
				pts1 = np.float32([\
					[aprox[0][0][0], aprox[0][0][1]],\
					[aprox[1][0][0], aprox[1][0][1]],\
					[aprox[2][0][0], aprox[2][0][1]],\
					[aprox[3][0][0], aprox[3][0][1]] ])

				M = cv2.getPerspectiveTransform(pts1,pts2)

				dst = cv2.warpPerspective(img, M, (tamanho[1], tamanho[0]))
				template = cv2.imread('x.png', 0)
				template = cv2.resize(template, dsize=(img.shape[0] // 4, img.shape[1] // 4))
				w, h = template.shape[::-1]
				im_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
				res = cv2.matchTemplate(im_gray, template, cv2.TM_CCOEFF_NORMED)
				threshold = 0.5
				loc = np.where(res >= threshold)

				for pt in zip(*loc[::-1]):
					cv2.rectangle(dst, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 0)
					if img.shape[0]//6 - 50 < pt[0] +w/2 < img.shape[0]//6 + 50 and img.shape[1]//8 - 50 < pt[1]+h/2 < img.shape[1]//8 + 50 and tabuleiro2[0] == False:
						play.move(tabuleiro, 0, 1)
						tabuleiro2[0] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif img.shape[0]//6 -50 < pt[0]+w/2 < img.shape[0]//6 + 50 and 3*img.shape[1]//8 - 50 < pt[1]+h/2< 3*img.shape[1]//8 +50 and tabuleiro2[3] == False:
						play.move(tabuleiro, 3, 1)
						tabuleiro2[3] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif img.shape[0]//6 - 50 < pt[0] +w/2< img.shape[0]//6 + 50 and 5*img.shape[1]//8 - 50 < pt[1]+h/2< 5*img.shape[1]//8 +50 and tabuleiro2[6] == False:
						play.move(tabuleiro, 6, 1)
						tabuleiro2[6] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif 3*img.shape[0]//6 - 50 < pt[0] +w/2< 3*img.shape[0]//6 + 50 and img.shape[1]//8 - 50< pt[1] +h/2<img.shape[1]//8 +50 and tabuleiro2[1] == False:
						play.move(tabuleiro, 1, 1)
						tabuleiro2[1] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif 3*img.shape[0]//6 - 50 < pt[0] +w/2< 3 * img.shape[0]// 6 +50 and 3*img.shape[1]//8 - 50 < pt[1] +h/2< 3* img.shape[1]//8 +50 and tabuleiro2[4] == False:
						play.move(tabuleiro, 4, 1)
						tabuleiro2[4] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif 3*img.shape[0]//6 - 50 < pt[0] +w/2<3*img.shape[0]//6  +50 and 5*img.shape[1]// 8 - 50 < pt[1] +h/2< 5*img.shape[1]//8 +50 and tabuleiro2[7] == False:
						play.move(tabuleiro, 7, 1)
						tabuleiro2[7] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif 5*img.shape[0]//6 - 50 < pt[0] +w/2< 5*img.shape[0]//6 +50 and img.shape[1]//8 - 50 < pt[1] +h/2< img.shape[1]//8 +50 and tabuleiro2[2] == False:
						play.move(tabuleiro, 2, 1)
						tabuleiro2[2] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif 5*img.shape[0]//6 - 50 < pt[0] +w/2< 5*img.shape[0]//6 +50 and 3*img.shape[1]//8 - 50 < pt[1] +h/2< 3*img.shape[1]//8 + 50 and tabuleiro2[5] == False:
						play.move(tabuleiro, 5, 1)
						tabuleiro2[5] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)
					elif 5*img.shape[0]//6 - 50 < pt[0] +w/2< 5*img.shape[0]//6 +50 and 5* img.shape[1]//8 - 50 < pt[1] +h/2< 5*img.shape[1]//8 +50 and tabuleiro2[8] == False:
						play.move(tabuleiro, 8, 1)
						tabuleiro2[8] = True
						if play.won(tabuleiro) == 0:
							aux = randint(0,8)
							while(tabuleiro2[aux] != False):
								aux = randint(0, 8)
							escolhas.append(aux)

				for escolha in escolhas:
					if escolha == 0:
						cv2.circle(dst, (img.shape[0] // 6, img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[0] = True
					elif escolha == 3:
						cv2.circle(dst, (img.shape[0] // 6, 3 * img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[3] = True
					elif escolha == 6:
						cv2.circle(dst, (img.shape[0] // 6, 5 * img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[6] = True
					elif escolha == 1:
						cv2.circle(dst, (3 * img.shape[0] // 6, img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[1] = True
					elif escolha == 4:
						cv2.circle(dst, (3 * img.shape[0] // 6, 3 * img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[4] = True
					elif escolha == 7:
						cv2.circle(dst, (3 * img.shape[0] // 6, 5 * img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[7] = True
					elif escolha == 2:
						cv2.circle(dst, (5 * img.shape[0] // 6, img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[2] = True
					elif escolha == 5:
						cv2.circle(dst, (5 * img.shape[0] // 6, 3 * img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[5] = True
					elif escolha == 8:
						cv2.circle(dst, (5 * img.shape[0] // 6, 5 * img.shape[1] // 8), 50, (255, 0, 0), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[8] = True
				fonte = cv2.FONT_HERSHEY_SIMPLEX
				if play.won(tabuleiro) == 1:
					cv2.putText(dst, 'Voce perdeu!!!', (125, 250), fonte, 1, (0, 0, 0), 2, cv2.LINE_AA)
				elif play.won(tabuleiro) == 2:
					cv2.putText(dst, 'Voce ganhou!!!', (125, 250), fonte, 1, (0, 0, 0), 2, cv2.LINE_AA)
				elif play.won(tabuleiro) == 3:
					cv2.putText(dst, 'Deu Velha!!!', (125, 250), fonte, 1, (0, 0, 0), 2, cv2.LINE_AA)
				cv2.imshow("output", dst)


			img = cv2.drawContours(img, contours, i, (0, 255, 0), 3)


		cv2.imshow('frame', img)
	if cv2.waitKey(1) == 32:
		break
sleep(3)
cv2.imshow('frame', img)
