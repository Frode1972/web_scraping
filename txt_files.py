def load_unsort(): 
    L=[]   
    with open("unsorted.txt","r") as f:
        for line in f:
            line=int(line.strip())
            L.append(line)   
    return L  

def save_unsorted_list(L):
    try:
        f=open('unsorted.txt','w')
        for list in L:
            #f.write(f"{str(list)}\n")
            f.write(f"{int(list)}\n")
    except Exception as exc:
        print('There was a problem A: %s' % (exc))
    f.close()

def save_sorted_list(L):
    try:
        f=open('sorted.txt','w')
        for list in L:
            f.write(f"{str(list)}\n")
    except Exception as exc:
        print('There was a problem A: %s' % (exc))
    f.close()

def save_dict_to_file(dics):
    try:
        f = open('dict.txt','w')
        for x,y in enumerate(dics):
            #f.writelines(f"str{dic} \n")
            name=""
            count=0
            for a, b in y.items():
                name=str(a)+","+str(b)
                #print(f"{a} \t {b}")               
                f.write(f"{name}")
                if count<2 : f.write(",")
                count=count+1
            f.write(f"\n")             
    except Exception as exc:
        print('There was a problem A: %s' % (exc))
    f.close()
   
def load_dict_from_file():   
    img_list=[]
    f = open ("dict.txt","r")
    for line in f:
        data=line.split(",")         
        #dics.append(data)
        liste_inn={data[0]:data[1],data[2]:data[3],data[4]:data[5].strip()}
        img_list.append(liste_inn)
    f.close()
    return img_list