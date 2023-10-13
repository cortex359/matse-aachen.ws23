#!/usr/bin/env python

aufgabe_a = 0
aufgabe_b = 0
aufgabe_c = 0
insg = 0

def count_cars(w):
    bereiche = [0, 0, 0, 0]
    for car in w:
        bereiche[car-1] += 1
    return bereiche

for w_1 in range(1,5):
    for w_2 in range(1,5):
        for w_3 in range(1,5):
            for w_4 in range(1,5):
                for w_5 in range(1,5):
                    for w_6 in range(1,5):
                        for w_7 in range(1,5):
                            for w_8 in range(1,5):
                                for w_9 in range(1,5):
                                    for w_10 in range(1,5):
                                        bereiche = count_cars((w_1, w_2, w_3, w_4, w_5, w_6, w_7, w_8, w_9, w_10))
                                        if bereiche[0] == 0:
                                            aufgabe_a += 1
                                        if bereiche[0] == 2 and bereiche[1] == 2 and bereiche[2] == 3 and bereiche[3] == 3:
                                            aufgabe_b += 1
                                        if bereiche[0] >= 2 and bereiche[1] >= 2 and bereiche[2] >= 2 and bereiche[3] >= 2:
                                            aufgabe_c += 1
                                        insg += 1

print("Aufgabe a)", aufgabe_a)
print("Aufgabe b)", aufgabe_b)
print("Aufgabe c)", aufgabe_c)
print("von insg. ", insg, "Konfigurationen")