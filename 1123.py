import heapq

nCidades, nEstradas, cidRotasServicos, cidConsertado = map(int, input().split())

while(nCidades!=0 and nEstradas!=0 and cidRotasServicos!=0 and cidConsertado!=0):
    custo = []
    n_out = [[] * nCidades for i in range(nCidades)] 
    infty = 1
    
    for i in range(nCidades):
        linha = []
        for j in range(nCidades):
            if i == j:
                linha.append(0)
            else:
                linha.append(-1)
        custo.append(linha)
    aux=[]
    for j in range(nEstradas):    
        u, v, p = map(int, input().split()) 
        n_out[u].append(v)         
        n_out[v].append(u)     
        infty = infty + p  
        if(u>=cidRotasServicos and v>=cidRotasServicos):
            custo[u][v]=p
            custo[v][u]=p
        
        if(u>=cidRotasServicos and v<cidRotasServicos):
            custo[u][v]=p

        if(u<cidRotasServicos and v>=cidRotasServicos):
            custo[v][u]=p
        
        if(u<cidRotasServicos and v<cidRotasServicos and abs(u-v)==1):
            custo[u][v]=p
            custo[v][u]=p
        else:
            if(u<cidRotasServicos and v<cidRotasServicos): 
                aux.append((u, v))
    for i in range(len(aux)):
        custo[aux[i][0]][aux[i][1]]=infty
        custo[aux[i][1]][aux[i][0]]=infty



    marca = nCidades*[0]
    L = nCidades*[infty]
    raiz = cidConsertado
    L[raiz] = 0                            
    D = [(0,raiz)]                        
    for w in range(0,nCidades):
        if w != raiz:
            heapq.heappush(D,(L[w],w))      
    pai = nCidades*[-1]


    while D != []:
        Lmin, v = heapq.heappop(D)
        marca[v] = 1
        for w in n_out[v]:
            if marca[w] == 0:
                if L[v] + custo[v][w] < L[w]:
                    for i in range(len(D)):
                        if D[i] == (L[w],w):
                            pos = i
                            break
                    L[w] = L[v] + custo[v][w]    
                    D[pos] = (L[w],w)
                    heapq._siftdown(D,0,pos)     
                    pai[w] = v
    
    print(L[cidRotasServicos-1])

    nCidades, nEstradas, cidRotasServicos, cidConsertado = map(int, input().split())

