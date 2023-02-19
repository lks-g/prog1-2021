import random

# vrati dvojprvkovy zoznam dosky
def gen_chessboard(n):  
    coordinate_list = []
    s = [' ']
    temporary_list = []

    for k in range(n):
        s.append(k % 10)
    coordinate_list.append(s)
    
    for i in range(n):
        temporary_list.append(i % 10)
        for j in range(n):
            if (i > (n//2 + 1) or i < (n//2 - 1))\
                    and (j > (n//2 + 1) or j < (n//2 - 1)):
                temporary_list.append(' ')
                
            elif i == n//2 and j == n//2:
                temporary_list.append('X')

            elif (i == n//2 and j != 0 and j != (n - 1) and j != n//2)\
                    or (j == n//2 and i != 0 and i != (n - 1) and i != n//2):
                temporary_list.append('D')

            else:
                temporary_list.append('*')

        coordinate_list.append(temporary_list)
        temporary_list = []

    return coordinate_list

 # vykresli pomocou 2D zoznamu hraciu dosku
def chessboard_print(chess):   
    for elem in chess:
        for item in elem:
            print(item, end='  ')
        print()

def movement_simulation(n):
    board = gen_chessboard(n)
    y_a, x_a = 1, n//2 + 2                          # suradnica panacika a
    y_b, x_b = n, n // 2                            # suradnica panacika b
    x_home_a, y_home_a = n//2 + 1, n//2             # suradnice domceka a
    x_home_b, y_home_b = n // 2 + 1, n // 2 + 2     # suradnice domceka b

    num_rounds = 0              # pocet kol
    end = True                  # koniec hry

    exist_a, exist_b = False, False                                                 # nachadza sa panacik a,b na doske
    num_a_piece, num_b_piece = n // 2 - 1, n // 2 - 1                               # pocet panacikov a,b v zalohe
    path_a, path_b = ((n * 4) - ((13 - n) // 2)) - 1, ((n * 4) - ((13 - n) // 2)) - 1  # pocet policok do ciela pre a, b
    kill_count = 0

    while end:
        for k in range(2):      # k0 tah A, k1 tah B
            if (not exist_a and k == 0) or (not exist_b and k == 1):
                for _ in range(3):                       # ked hrac nema panacika na doske 3 krat hadze,
                    throw = random.randint(1, 6)         # a ak hodi 6, tak postavi si ho na hraciu plochu
                    if k == 0:
                        print("Startovaci hod hraca A: => " + str(throw))

                    else:
                        print("Startovaci hod hraca B: => " + str(throw))

                    if throw == 6:
                        if k == 0:
                            board[1][n//2 + 2] = "A"
                            num_a_piece -= 1
                            exist_a = True
                            break

                        else:
                            board[n][n // 2] = "B"
                            num_b_piece -= 1
                            exist_b = True
                            break

            if (exist_a and k == 0) or (exist_b and k == 1):    # ak hrac ma panacika na ploche,
                throw = random.randint(1, 6)                    # tak hadze kockou a posuva sa o dany pocet
                throw_6 = throw

                while throw == 6:                               # ak hodi hrac 6 tak hadze este raz a hody sa scitaju
                    throw = random.randint(1, 6)
                    throw_6 += throw
                throw = throw_6

                if k == 0:
                    print("Hrac A hodil kockou spolu => " + str(throw))

                else:
                    print("Hrac B hodil kockou spolu => " + str(throw))

                if k == 0:
                    print("Ciel je: (" + str(path_a - throw) + "," + str((path_a - num_a_piece) - throw) + ')')
                    if throw > path_a:                               # ak hodil viac nez je cesta do domceka straca tah
                        print("Moc velke cislo, stracas tah A")
                        continue

                    elif (path_a - num_a_piece) <= throw <= path_a:   # ak hodil presne do domceka tak sa postavi
                        board[y_a][x_a] = '*'                               # na poslednu poziciu a konci kolo
                        board[y_home_a][x_home_a] = 'A'                     # nabuduci tah bude znova 3 krat hadzat
                        y_home_a -= 1                                       # aby dalsiu figurku dostal na hraci plan
                        path_a = ((n * 4) - ((13 - n) // 2) - ((n//2 - 1) - num_a_piece)) - 1
                        y_a = 1
                        x_a = n // 2 + 2
                        exist_a = False
                        print("hrac A je v domceku")
                        continue
                else:
                    print("ciel je: (" + str(path_b - throw) + "," + str((path_b - num_b_piece) - throw) + ')')
                    if throw > path_b:
                        print("moc velke cislo, stracas tah hrac B")
                        continue

                    elif (path_b - num_b_piece) <= throw <= path_b:
                        board[y_b][x_b] = '*'
                        board[y_home_b][x_home_b] = 'B'
                        y_home_b += 1
                        path_b = ((n * 4) - ((13 - n) // 2) - ((n//2 - 1) - num_b_piece)) - 1
                        y_b = n
                        x_b = n // 2
                        exist_b = False
                        print("hrac B je v domceku")
                        continue

                previous_x_a, previous_y_a = x_a, y_a
                previous_x_b, previous_y_b = x_b, y_b

                for i in range(throw):
                    if k == 0:
                        if x_a == n // 2 + 1 and y_a == 1:  # pohyb nad domcekom
                            y_a += 1
                            path_a -= 1

                        elif (x_a == (n//2 + 2)) and (0 < y_a < n//2 or n > y_a > (n//2 + 1))\
                                or ((y_a == n//2 or y_a == n//2 + 1) and x_a == n):         # Down
                            y_a += 1
                            path_a -= 1

                        elif (x_a == (n//2)) and (1 < y_a < (n//2 + 1) or (n + 1) > y_a > (n//2 + 2))\
                                or ((y_a == n//2 + 2 or y_a == n//2 + 1) and x_a == 1):   # Up
                            y_a -= 1
                            path_a -= 1

                        elif (y_a == (n//2) and (0 < x_a < (n//2) or n > x_a > (n//2 + 1)))\
                                or (y_a == 1 and (x_a == n//2 + 1 or x_a == n//2)):         # Right
                            x_a += 1
                            path_a -= 1

                        elif (y_a == (n//2 + 2) and (1 < x_a < (n//2 + 1) or (n + 1) > x_a > (n//2 + 2)))\
                                or (y_a == n and x_a == n//2+2):         # Left
                            x_a -= 1
                            path_a -= 1

                        elif x_a == n//2 + 1 and y_a == n:               # vyhnutie sa domceku hraca B
                            x_a -= 1
                            y_a -= 1
                            path_a -= 1
                    else:
                        if x_b == n//2 + 1 and y_b == n:     # pohyb nad domcekom
                            y_b -= 1
                            path_b -= 1

                        elif (x_b == (n//2 + 2)) and (0 < y_b < n//2 or n > y_b > (n//2 + 1))\
                                or ((y_b == n//2 or y_b == n//2 + 1) and x_b == n):         # Down
                            y_b += 1
                            path_b -= 1

                        elif (x_b == (n//2)) and (1 < y_b < (n//2 + 1) or (n + 1) > y_b > (n//2 + 2))\
                                or ((y_b == n//2 + 2 or y_b == n//2 + 1) and x_b == 1):   # Up
                            y_b -= 1
                            path_b -= 1

                        elif (y_b == (n//2) and (0 < x_b < (n//2) or n > x_b > (n//2 + 1)))\
                                or (y_b == 1 and x_b == n//2):         # Right
                            x_b += 1
                            path_b -= 1

                        elif (y_b == (n//2 + 2) and (1 < x_b < (n//2 + 1) or (n + 1) > x_b > (n//2 + 2)))\
                                or (y_b == n and (x_b == n//2 + 1 or x_b == n//2+2)):         # Left
                            x_b -= 1
                            path_b -= 1

                        elif x_b == n//2 + 1 and y_b == 1:               # vyhnutie sa domceku hraca B
                            x_b += 1
                            y_b += 1
                            path_b -= 1

                board[previous_y_a][previous_x_a] = '*'
                board[previous_y_b][previous_x_b] = '*'

                if k == 0 and y_b == y_a and x_a == x_b and exist_b and exist_a:   # vyhadzovanie ked je na tahu hrac A
                    y_b = n
                    x_b = n//2
                    exist_b = False
                    num_b_piece += 1
                    path_b = ((n * 4) - ((13 - n) // 2) - ((n//2 - 1) - num_b_piece)) - 1
                    print("Hracovi B bol vyhodeny panacik")
                    board[y_a][x_a] = 'A'
                    kill_count += 1

                if k == 1 and y_b == y_a and x_a == x_b and exist_b and exist_a:   # vyhadzovanie ked je na tahu hrac B
                    y_a = 1
                    x_a = n//2 + 2
                    exist_a = False
                    num_a_piece += 1
                    path_a = ((n * 4) - ((13 - n) // 2) - ((n//2 - 1) - num_a_piece)) - 1
                    print("Hracovi A bol vyhodeny panacik")
                    board[y_b][x_b] = 'B'
                    kill_count += 1

                else:
                    if exist_b:
                        board[y_b][x_b] = 'B'
                    if exist_a:
                        board[y_a][x_a] = 'A'

        chessboard_print(board)
        num_rounds += 1

        print("Kolo cislo: " + str(num_rounds))
        print()

        if (num_a_piece == 0 and not exist_a) or (num_b_piece == 0 and not exist_b):    # ukoncenie hry
            if num_a_piece == 0 and not exist_a:
                print("Vyhral hrac A!")
            else:
                print("Vyhral hrac B!")
            print("Hraci sa povyhadzovali: " + str(kill_count) + "-krát")
            end = False

movement_simulation(9)