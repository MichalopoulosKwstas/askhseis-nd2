#Έστω μία σκακίερα στην οποία τοποθετούμε πάνω της,
#σε τυχαίες θέσεις, έναν λευκό πύργο και αξιωματικό και μια μαύρη βασίλισσα.
#Ο κάθε παίκτης παίρνει ως δυο βαθμούς σε κάθε γύρο ανάλογα με το αν τρώει κομμάτι του αντιπάλου.
#Έτσι, ο λευκός μπορεί να πάρει 2 βαθμούς αν ο πύργος τρώει τη βασίλισσα και το ίδιο κάνει και ο αξιωματικός του.
#Αν μόνο ένα από τα κομμάτια του τρώει τη βασίλισσα τότε παίρνει ένα βαθμό.
#Αντίστοιχα, ο μαύρος παίρνει δύο βαθμούς αν η βασίλισσά του μπορεί να φάει και τα δύο κομμάτια του λευκού ή ένα αν μπορεί να φάει μόνο ένα. Μετά από 100 παιχνίδια,
#εμφανίστε τους βαθμούς των δύο παικτών.
import random
am='p21105'
aspra=0
maura=0

chess=[['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0']]



purgos='pyrgos aspro'
vas='vassilisa mauro'
aksiom='aksiomatikos aspro'
    
#prosthetw ta pionia
pos=random.randint(0,7)
chess[pos].pop()
chess[pos].insert(pos,purgos)
  

pos=random.randint(0,7)
chess[pos].pop()
chess[pos].insert(pos,vas)
    

pos=random.randint(0,7)
chess[pos].pop()
chess[pos].insert(pos,aksiom)



for s in  range(100):
    random.shuffle(chess)#anakatema
    for a in range(2):#h seira twn paixtwn
        for j in range(0,7):   
            for i in range(0,7):
                if a == 0:#seira twn asprwn
        
                    if chess[j][i]==purgos:
                        vhma=random.randint(0,2)
                        pos=random.randint(0,7)
                        chess[j].pop(i)
                        
                        if vhma==0:
                            chess[j].insert(pos,purgos)
                            if  chess[j][pos+1]== vas :
                                aspra+=2
                                chess[j].remove(vas)
                                
                                  
                        else:
                            chess[pos].insert(i,purgos)
                            chess[j].append(0)
                            if  chess[pos][i+1]== vas :
                                aspra+=2
                                chess[pos].remove(vas)
                                
                             
                
                                
                    if chess[j][i]==aksiom:
                        pos=random.randint(0,7)
                        chess[j].pop(i)
                        chess[j].append(0)
                        chess[pos].insert(i+1,aksiom)
                        if  chess[pos][i+2]== vas :
                            aspra+=2
                            chess[pos].remove(vas)
                            chess[pos].append(0)
                            
                            
              
                else:#seira twn maurwn

                    
                    if chess[j][i]==vas:
                        pos=random.randint(0,7)
                        chess[j].pop(i)
                        chess[j].append(0)
                        chess[pos].insert(pos,vas)
                        
                        if  chess[pos][pos+1]== purgos :
                            maura+=1
                            chess[pos].remove(purgos)
                
                           
                               
                        if  chess[pos][pos+1]== aksiom :
                            maura+=1
                            chess[pos].remove(aksiom)
        
                          
                           

                                    
print ('\tO paixths me ta maura pionia eixe sunolika:',maura,'vathmous\n\tkai o paixths me ta aspra eixe sunolika :',aspra,'vathmous')
if aspra>maura:
    print('O paixths me ta aspra pionia nikaei!')
elif maura>aspra:
    print('O paixths me ta maura pionia nikaei!')
else:
    print('\n\tIsopalia!!!')
