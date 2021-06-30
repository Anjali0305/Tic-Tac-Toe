print("TIC TAC GAME created by ANJALI :)")
a = """
_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9  
"""
print(a)
g = [1,2,3,4,5,6,7,8,9]
x = []
y = []
c = 0

def gameover(g):
    if (g[0]=="0" and g[1] == "0" and g[2] == "0") or \
       (g[3]=="0" and g[4] == "0" and g[5] == "0") or \
       (g[6]=="0" and g[7] == "0" and g[8] == "0") or \
       (g[0]=="X" and g[1] == "X" and g[2] == "X")  or \
       (g[3]=="X" and g[4] == "X" and g[5] == "X") or \
       (g[6]=="X" and g[7] == "X" and g[8] == "X"):
       return True

    elif (g[0]=="0" and g[3] == "0" and g[6] == "0")  or \
         (g[1]=="0" and g[4] == "0" and g[7] == "0") or \
         (g[2]=="0" and g[5] == "0" and g[8] == "0") or \
         (g[0]=="X" and g[3] == "X" and g[6] == "X")  or \
         (g[1]=="X" and g[4] == "X" and g[7] == "X") or \
         (g[2]=="X" and g[5] == "X" and g[8] == "X"):
       return True  

    elif (g[0]=="0" and g[4] == "0" and g[8] == "0")  or \
         (g[2]=="0" and g[4] == "0" and g[6] == "0") or \
         (g[0]=="X" and g[4] == "X" and g[8] == "X")  or \
         (g[2]=="X" and g[4] == "X" and g[6] == "X"):
       return True      

for i in range (0,5):
    
    x.append(int(input("Enter choice player 1(0): [Dont enter already filled spaces] -->")))
    g[x[i]-1] = "0"
    m = """ 
    _{}_|_{}_|_{}_
    _{}_|_{}_|_{}_
     {} | {} | {}  
    """.format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8])
    print(m)

    if gameover(g):
        print("Player 1(0) has Won!! \\_(*.*)__")
        break
    else:
        c += 1
        pass

    if c == 9:
        print("ITS A DRAW! \\_('O')_/")  
    else:    
        y.append(int(input("Enter choice player 2(X): [Dont enter already filled spaces] -->")))
        g[y[i]-1] = "X"
        m = """ 
        _{}_|_{}_|_{}_
        _{}_|_{}_|_{}_
         {} | {} | {}  
        """.format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8])
        print(m)

        if gameover(g):
            print("Player 2(X) has Won! __(*.*)_/")
            break
        else:
            c += 1
            pass  







