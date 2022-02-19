#Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείτε “καπάκια”.
#Έχετε στην κατοχή σας 27 “καπάκια”, 9 για κάθε μέγεθος (μικρό, μεσαίο, μεγάλο).
#Μια τριάδα που τερματίζει το παιχίνδι γίνεται οριζόντια, κάθετα ή διαγώνια.
#Η τριάδα αποτελείται από καπάκια είτε του ίδιου μεγέθους είτε από το μικρό προς το μεγαλύτερο.
#Επειδή έχετε καπάκια, ένα καπάκι μπορεί να μπει σε οποιοδήποτε τετράγωνο, αρκεί να είναι ελεύθερο ή να υπάρχει εκεί μικρότερο καπάκι.
#Γράψτε ένα πρόγραμμα το οποίο παίζει τυχαία το παιχνίδι 100 φορές και επιστρέφει το μέσο όρο των βημάτων για να λήξει το παιχνίδι.


import random
import math
am='p21105'

list=[]

vhma=0.0
for u in range(100):
    vhma+=1
    
    for i in range(3):
        list2=[[0,0,0],[0,0,0],[0,0,0]]
        vhma+=1
        b=False
        j=0
        while(j<3):
            vhma+=1
            list3=[]
            h=0
            while(h<3):
                vhma+=1
                 
                r=random.randint(0,10)
                
                kapaki=2*math.pi*r
               
                while kapaki not in list3:
                    list3.append(kapaki)
                    h+=1
            for a in range(3):
                if list3[a] not in list2[j-1]:
                    if list3[a] not in list2[j-2]:
                        b=True
                    else:
                        b=False
                        break
                else:
                    b=False
                    break
                
            if b == True :
                sorted(list3)
                list2.insert(j,list3)
                j+=1

            

        sorted(list2)
        
        list.append(list2)
        
    sorted(list)

    
mo=vhma/(100*27)
        
for k in range(100):
    
    print ('Game',k+1,': \n')
    
    for l in range(3):
        
        print ('\t Line',l+1,list[k][l],'\n')
        
print("O mesos oros twn vhmatwn einai :",mo)
