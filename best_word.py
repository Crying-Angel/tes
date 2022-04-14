# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 12:55:16 2022

@author: thoma
"""
L=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def base_convert(i, b):
    result = []
    while i > 0:
            result.insert(0, i % b)
            i = i // b
    return result
wr=open('ouverture_5.txt','w')
for fl in L:
    Res=[]
    l=5
    name=f'ms_{l}.txt'
    f=open(name)
    W=[]
    for ligne in f.readlines():
        ligne=ligne.strip()
        ligne=ligne.upper()
        if ligne[0]==fl:
            W.append(ligne)
    for h in range (len(W)):
        w=W[h]
        s=0
        n=0
        for k in range (4**(l-1)):
            name=f'm{l}m.txt'
            f=open(name)
            M=[]
            for ligne in f.readlines():
                ligne=ligne.strip()
                ligne=ligne.upper()
                if ligne[0]==fl:
                    M.append(ligne)
            comb=base_convert(k, 4)
            conc=[0 for g in range(l-1-len(comb))]
            comb=conc+comb
            Wt=[1 for i in range(l)]
            E=[1 for i in range(l)]
            Ae=[1 for i in range(l)]
            Abs=[]
            for j in range(1,l):
                cas=comb[j-1]
                if cas==0 :
                    Abs.append(w[j])
                elif cas==1 :
                    Ae[j]=w[j]
                elif cas==2 :
                    E[j]=w[j]
                elif cas==3:
                    Wt[j]=w[j]
            if len(Abs)>0:
                c=0
                while c<len(M):
                    m=M[c]
                    change=True
                    for i in range(len(Abs)):
                        if Abs[i] in m:
                            M.pop(c)
                            change=False
                            break
                    if change:
                        c+=1
            c=0        
            while c<len(M):
                m=M[c]
                change=True
                for i in range(len(Ae)):
                    if Ae[i]!=1:
                        if Ae[i]==m[i]:
                            M.pop(c)
                            change=False
                            break
                if change:
                    c+=1
            c=0        
            while c<len(M):
                m=M[c]
                change=True
                for i in range(len(E)):
                    if E[i]!=1:
                        if not(E[i] in m) or E[i]==m[i]:
                            M.pop(c)
                            change=False
                            break
                if change:
                    c+=1
            c=0        
            while c<len(M):
                m=M[c]
                change=True
                for i in range(len(Wt)):
                    if Wt[i]!=1:
                        if not(Wt[i]==m[i]):
                            M.pop(c)
                            change=False
                            break
                if change:
                    c+=1
            if len(M)>0:
                s+=len(M)
                n+=1
            f.close()
        Res.append([w,s/n])
        print([w,s/n])
    if len(Res)>0:
        m=Res[0][1]
        w=Res[0][0]
        for i in range (len(Res)): 
            if m>Res[i][1]:
                m=Res[i][1]
                w=Res[i][0]
        print(w)
        wr.write(w)
        wr.write('\n')
   
wr.close()
        
            
                
                
            
    
    
    
