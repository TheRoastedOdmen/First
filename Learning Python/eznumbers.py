import time # тут библиотека времени
import math # а вот это считает корни и прочий матан
 
with open('outfile.txt', 'w') as out: # ясно же, что с файлом работать будем
    out.write('Первый нах посчитал от 1 and 10 000\n-----\n А чего добился ты ?\n')
    start = time.clock()
    print("2\n3\n5\n7\n11\n13\n17\n19\n23\n")
    out.write( "2\n3\n5\n7\n11\n13\n17\n19\n23\n") ## Это выкидывает перечисленные числа сразу, это круто, экономит нам 0.04 секунды при расчёте до 1000000
    for i in range(29, 1000000, 2):
        if ( 
            i % 2 ==  0 or # |(                                                         )
            i % 3 ==  0 or # |(                                                         )
            i % 5 ==  0 or # |(                                                         )
            i % 7 ==  0 or # |(   быстренько проверим на первые простые,                )
            i % 11 == 0 or # |(   массив можно продолжать до усрачки                    )
            i % 13 == 0 or # |(                                                         )
            i % 17 == 0 or # |(                                                         )
            i % 19 == 0 or # |(                                                         )
            i % 23 == 0    # |(                                                         )
	):
            continue
	# если реально похоже на простое, подозрительно щуримся и проверяем его решетом ->	
        else:
            for j in range(29, int(math.sqrt(i) + 1), 2): # нафиг все чётные, да и считать можно с 29
                if i % j == 0:
                    break
                else:
                    print(i)
                    out.write(str(i) + "\n")
 
    finish = time.clock()
    print(finish - start)
    out.write('Program work at ' + str(finish - start) + ' second') # тут запишем время выполнения