import numpy as np
import cv2
import play
from random import randint
from time import sleep
cap = cv2.VideoCapture(0)
ASPECT_RATIO = (500,500)
pts2 = np.float32([[0,0],[ASPECT_RATIO[1],0],[0,ASPECT_RATIO[0]],[ASPECT_RATIO[1],ASPECT_RATIO[0]]])


def canto_proximo(y1,x1,y2,x2,y3,x3,y4,x4,h,w,kind):
	if kind == "TL":
		yc, xc = 0, 0
	if kind == "TR":
		yc, xc = 0, w
	if kind == "BL":
		yc, xc = h, 0
	if kind == "BR":
		yc, xc = h, w

	d1 = np.sqrt(np.power(y1-yc,2)+ np.power(x1-xc,2))
	d2 = np.sqrt(np.power(y2-yc,2)+ np.power(x2-xc,2))
	d3 = np.sqrt(np.power(y3-yc,2)+ np.power(x3-xc,2))
	d4 = np.sqrt(np.power(y4-yc,2)+ np.power(x4-xc,2))
	d = [d1,d2,d3,d4]

	if min(d) == d1:
		return 0
	if min(d) == d2:
		return 1
	if min(d) == d3:
		return 2
	if min(d) == d4:
		return 3



def ordenar_pontos(aprox,shape):
	ordenados = np.copy(approx)
	h,w = shape

	y1,x1 = approx[0][0][0],approx[0][0][1]
	y2,x2 = approx[1][0][0],approx[1][0][1]
	y3,x3 = approx[2][0][0],approx[2][0][1]
	y4,x4 = approx[3][0][0],approx[3][0][1]

	TL = canto_proximo(y1,x1,y2,x2,y3,x3,y4,x4,h,w,"TL")
	TR = canto_proximo(y1,x1,y2,x2,y3,x3,y4,x4,h,w,"TR")
	BL = canto_proximo(y1,x1,y2,x2,y3,x3,y4,x4,h,w,"BL")
	BR = canto_proximo(y1,x1,y2,x2,y3,x3,y4,x4,h,w,"BR")

	ordenados[1] = approx[TL]
	ordenados[3] = approx[TR]
	ordenados[0] = approx[BL]
	ordenados[2] = approx[BR]

	return ordenados


tabuleiro = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
tabuleiro2 = [False, False, False, False, False, False, False, False, False]
escolhas = []

while(cap.isOpened() and (not play.won(tabuleiro))):
	ret, im = cap.read()

	if ret==True:
		imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
		ret2,thresh = cv2.threshold(imgray,170,255,0)
		image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		for i in range(len(contours)):
			area = cv2.contourArea(contours[i])
			approx = cv2.approxPolyDP(contours[i],0.02*cv2.arcLength(contours[i],True),True)
			if area > 10000 and len(approx) == 4:

				approx = ordenar_pontos(approx,im.shape[:2])
				pts1 = np.float32([\
					[approx[0][0][0],approx[0][0][1]],\
					[approx[1][0][0],approx[1][0][1]],\
					[approx[2][0][0],approx[2][0][1]],\
					[approx[3][0][0],approx[3][0][1]] ])

				M = cv2.getPerspectiveTransform(pts1,pts2)

				dst = cv2.warpPerspective(im,M,(ASPECT_RATIO[1],ASPECT_RATIO[0]))
				template = cv2.imread('x.png', 0)
				template = cv2.resize(template, dsize=(im.shape[0] // 4, im.shape[1] // 4))
				w, h = template.shape[::-1]
				im_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
				res = cv2.matchTemplate(im_gray, template, cv2.TM_CCOEFF_NORMED)
				threshold = 0.4
				loc = np.where(res >= threshold)


				for pt in zip(*loc[::-1]):
					#cv2.rectangle(dst, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
					#cv2.circle(dst, (pt[0] + w //2 , pt[1] + h // 2), 5, (255, 0, 0), -1)

					if im.shape[0]//6 - 50 < pt[0] +w/2 < im.shape[0]//6 + 50 and im.shape[1]//8 - 50 < pt[1]+h/2 < im.shape[1]//8 + 50 and tabuleiro2[0] == False:
						play.move(tabuleiro, 0, 1)
						aux = randint(0,8)
						tabuleiro2[0] = True
						while(tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif im.shape[0]//6 -50 < pt[0]+w/2 < im.shape[0]//6 + 50 and 3*im.shape[1]//8 - 50 < pt[1]+h/2< 3*im.shape[1]//8 +50 and tabuleiro2[3] == False:
						play.move(tabuleiro, 3, 1)
						aux = randint(0,8)
						tabuleiro2[3] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif im.shape[0]//6 - 50 < pt[0] +w/2< im.shape[0]//6 + 50 and 5*im.shape[1]//8 - 50 < pt[1]+h/2< 5*im.shape[1]//8 +50 and tabuleiro2[6] == False:
						play.move(tabuleiro, 6, 1)
						aux = randint(0, 8)
						tabuleiro2[6] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif 3*im.shape[0]//6 - 50 < pt[0] +w/2< 3*im.shape[0]//6 + 50 and im.shape[1]//8 - 50< pt[1] +h/2<im.shape[1]//8 +50 and tabuleiro2[1] == False:
						play.move(tabuleiro, 1, 1)
						aux = randint(0, 8)
						tabuleiro2[1] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif 3*im.shape[0]//6 - 50 < pt[0] +w/2< 3 * im.shape[0]// 6 +50 and 3*im.shape[1]//8 - 50 < pt[1] +h/2< 3* im.shape[1]//8 +50 and tabuleiro2[4] == False:
						play.move(tabuleiro, 4, 1)
						aux = randint(0, 8)
						tabuleiro2[4] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif 3*im.shape[0]//6 - 50 < pt[0] +w/2<3*im.shape[0]//6  +50 and 5*im.shape[1]// 8 - 50 < pt[1] +h/2< 5*im.shape[1]//8 +50 and tabuleiro2[7] == False:
						play.move(tabuleiro, 7, 1)
						aux = randint(0, 8)
						tabuleiro2[7] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif 5*im.shape[0]//6 - 50 < pt[0] +w/2< 5*im.shape[0]//6 +50 and im.shape[1]//8 - 50 < pt[1] +h/2< im.shape[1]//8 +50 and tabuleiro2[2] == False:
						play.move(tabuleiro, 2, 1)
						aux = randint(0, 8)
						tabuleiro2[2] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif 5*im.shape[0]//6 - 50 < pt[0] +w/2< 5*im.shape[0]//6 +50 and 3*im.shape[1]//8 - 50 < pt[1] +h/2< 3*im.shape[1]//8 + 50 and tabuleiro2[5] == False:
						play.move(tabuleiro, 5, 1)
						aux = randint(0, 8)
						tabuleiro2[5] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					elif 5*im.shape[0]//6 - 50 < pt[0] +w/2< 5*im.shape[0]//6 +50 and 5* im.shape[1]//8 - 50 < pt[1] +h/2< 5*im.shape[1]//8 +50 and tabuleiro2[8] == False:
						play.move(tabuleiro, 8, 1)
						aux = randint(0, 8)
						tabuleiro2[8] = True
						while (tabuleiro2[aux] != False):
							aux = randint(0, 8)
						escolhas.append(aux)
					print(tabuleiro)



				for escolha in escolhas:
					if escolha == 0:
						cv2.circle(dst, (im.shape[0] // 6, im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[0] = True
					elif escolha == 3:
						cv2.circle(dst, (im.shape[0] // 6, 3 * im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[3] = True
					elif escolha == 6:
						cv2.circle(dst, (im.shape[0] // 6, 5 * im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[6] = True
					elif escolha == 1:
						cv2.circle(dst, (3 * im.shape[0] // 6, im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[1] = True
					elif escolha == 4:
						cv2.circle(dst, (3 * im.shape[0] // 6, 3 * im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[4] = True
					elif escolha == 7:
						cv2.circle(dst, (3 * im.shape[0] // 6, 5 * im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[7] = True
					elif escolha == 2:
						cv2.circle(dst, (5 * im.shape[0] // 6, im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[2] = True
					elif escolha == 5:
						cv2.circle(dst, (5 * im.shape[0] // 6, 3 * im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[5] = True
					elif escolha == 8:
						cv2.circle(dst, (5 * im.shape[0] // 6, 5 * im.shape[1] // 8), 50, (0, 0, 255), 4)
						play.move(tabuleiro, escolha, 0)
						tabuleiro2[8] = True

				cv2.imshow("output", dst)
				print(dst.shape)

			im = cv2.drawContours(im, contours, i, (0,255,0), 3)


		cv2.imshow('frame',im)
	if cv2.waitKey(1) == 32:
		break

sleep(2)
cv2.imshow('frame', im)
