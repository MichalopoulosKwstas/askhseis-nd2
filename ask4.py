import random
am='p21105'
wfp1=0#wins for player 1
wfp2=0#wins for player 2
draw=0

for h in range(100):
    print('Game :',h+1)
    print('\t\t*','*'*30)
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        
        for karta in xartia:
            
            if karta[0] == 10 or karta[0] in figures:
                
                player1.append(karta)
                xartia.remove(karta)
                break
            

        # print (player1)
        for card in player1:
            
            
            if card[0] in figures:
                
                sum1=sum1+10
            else:
                
                sum1=sum1+card[0]
        if sum1<=9:
            print('\t\t*',sum1,' '*26,'*')
        else:
            print('\t\t*',sum1,' '*25,'*')
    if sum1>21:
        print('\t\t*',"P2 wins!",' '*19,'*')
        print('\t\t*','*'*30)
        wfp2+=1
    else:

        print('\t\t*',"\tP2 joins the game",' '*4,'*',"\n",' '*14,'*',' '*28,'*') #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            for karta in xartia:
            
                if karta[0] != 10 or karta[0] not in figures:
                    
                    player2.append(karta)
                    xartia.remove(karta)
                    break
            
              
            #print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            if sum2<=9:
                print('\t\t*',sum2,' '*26,'*')
            else:
                print('\t\t*',sum2,' '*25,'*')
        if sum2>21:
            sum2=0
        if sum1>sum2:
            print('\t\t*',"P1 wins!",' '*19,'*')
            print('\t\t*','*'*30)
            wfp1+=1
        elif sum2>sum1:
            print('\t\t*',"P2 wins!",' '*19,'*')
            print('\t\t*','*'*30)
            wfp2+=1
        else:
            print('\t\t*',"draw!",' '*22,'*')
            print('\t\t*','*'*30,'\n')
            draw+=1
    
p1=100*wfp1/100
p2=100*wfp2/100
p3=100*draw/100
print ("O player 1 kairdise to :",p1,"% twn paixnidiwn\nO player 2 kairdise to :",p2,"% twn paixnidiwn\nTo pososto twn isopaliwn einai :",p3,"%")
