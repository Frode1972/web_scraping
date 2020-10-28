import requests, os, bs4, image
from txt_files import load_unsort, save_unsorted_list, save_dict_to_file, load_dict_from_file, save_sorted_list
from sort_lib import bubble_sort, quicksort, insertion_sort
from PIL import Image

def top_ten_list (sorting, img_liste):
    #Make top ten dictionary and list with filename, url and size
    counter=0
    for number in sorting:
        for x, y in enumerate(img_liste):
                
            sjekk=(int(y["size"]))
            if sjekk == int(number):          
                if counter<10:
                    top_list={"filename":y['filename'],"size":y['size'],"url":y['url']}
                    top_10.append(top_list)              
                    counter +=1
def verify_select(select):      
    if select in [str(x) for x in range(1,11)]:
        return True   
    elif select == "99":
        return True
    else:
        return False
def check_dict():
    cont_dict=os.path.isfile("./dict.txt")
    if cont_dict is True:
        with open("dict.txt","r") as f:
            lines=f.readlines()
            if len(lines)<2300:
                return False
            else:
                return True
    else:
        return False

def anim_gif(img_name):
    img = Image.open(img_name) 
    img.seek(1)
    count=0
    try:
        while count<271:
            img.seek(img.tell() + 1)
            img.show()
            count +=1
    except Exception as exc:
        print(exc)

url = 'https://xkcd.com'   # starting url
os.makedirs('xkcd', exist_ok=True)
top_10=[]
img_liste=[]
L=[]
liste_innhold={}
count=0
exist_dict=check_dict()

if exist_dict == False:
    while not url.endswith('#'):              
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Find the URL of the comic image.
        try:
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Could not find comic image.')
            else:
                comicUrl = 'https:' + comicElem[0].get('src')
                picture_page=comicElem[0].get('src')                                     
                filename= picture_page.split('/')[-1]
                img_size = len(requests.get(comicUrl).content)              
                print(f"Download {count} {filename}")                
                liste_innhold={"filename":filename,"size":img_size,"url":comicUrl}
                img_liste.append(liste_innhold)
        except Exception as exc:
            print('There was a problem A: %s' % (exc))

        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')
        count=count+1
    save_dict_to_file(img_liste)
    print('Done.')
else:
       img_liste = load_dict_from_file() #load from file 

for x, y in enumerate(img_liste): #Catch the size from img_list and store it in L
    L.append(int(y["size"]))  

save_unsorted_list(L) #Saves an unsorted size list which is also used by plot.py
sorting=quicksort(L) #Sort the list by size
#sorting=insertion_sort(L) #Sort the list by size
top_ten_list (sorting, img_liste) # Make top 10 list

cont=True
while cont:
    #Makes Top 10 list which is printed on the screen
    os.system('cls')
    print("Top ten results:\n")
    for x, y in enumerate(top_10,1):
        print (f"Number {x:<6} with filename: {y['filename']:<35} and with size {y['size']:<10} byte" )
    print(f"\nWrite '99' to end the program")
    print("-----------------------------------------------------------------------------------------")
    
    select=input("Select one of the numbers to open the image or quit to end the program:")
    
    while not verify_select(select):
        print("Wrong entry, select correct number!")
        select=input("Select one of the numbers to open the image or quit to end the program:")
    select=int(select)
    for a, b in enumerate(top_10,1):       
        if select==a:
            url_img=(b['url'])
            img_name=("./xkcd/"+b['filename'])
            exist_img = os.path.isfile(img_name)
            if exist_img == True:
                if ".gif" in img_name:
                    anim_gif(img_name)                       
                im = Image.open(img_name,mode='r')
                im.show()
                              
            else:           
                res = requests.get(url_img)
                res.raise_for_status()
                imageFile = open(os.path.join('xkcd', os.path.basename(url_img)),'wb')
                for chunk in res.iter_content(5000000):
                    imageFile.write(chunk)
                    imageFile.close()
                if ".gif" in img_name:
                    anim_gif(img_name)
                im = Image.open(img_name,mode='r')
                im.show()             
                                   
        elif select == 99:
            cont=False
            
    


