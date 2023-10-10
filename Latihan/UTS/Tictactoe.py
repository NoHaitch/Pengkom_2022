tictactoe = [["" for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        valid = False
        while valid == False:
            inp = input(f"Masukkan tictactoe posisi [{i+1}][{j+1}]: ")
            if(inp == "O" or inp == "X" or inp == ""):    
                valid = True
                if(inp != ""):
                    tictactoe[i][j] = inp
                else:
                    tictactoe[i][j] = "E"
            else:
                print("Input harus diantara 'X', 'O' atau kosong ''. ")
for baris in tictactoe:
    for kolom in baris:
        print(kolom,end=" ")
    print()
# menang baris
for i in range(3):
    if(tictactoe[i][0] != "E"):
        if(tictactoe[i][0] == tictactoe[i][1] == tictactoe[i][2]):
            if(tictactoe[i][0] == "X"):
                print("Pemenang : X")
            else:
                print("Pemenang : O")
            exit()
# menang kolom
for i in range(3):
    if(tictactoe[0][i] != "E"):
        if(tictactoe[0][i] == tictactoe[1][i] == tictactoe[2][i]):
            if(tictactoe[0][i] == "X"):
                print("Pemenang : X")
            else:
                print("Pemenang : O")
            exit()   
# menang diagonal
if(tictactoe[0][0] != "E"):
    if(tictactoe[0][0] == tictactoe[1][1] == tictactoe[2][2]):
        if(tictactoe[0][0] == "X"):
            print("Pemenang : X")
        else:
            print("Pemenang : O")
        exit()
if(tictactoe[0][2] != "E"):
    if(tictactoe[0][2] == tictactoe[1][1] == tictactoe[2][0]):
        if(tictactoe[0][2] == "X"):
            print("Pemenang : X")
        else:
            print("Pemenang : O")
        exit()
print("Tidak ada pemenang : Z")
