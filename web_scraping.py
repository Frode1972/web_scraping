import requests, os, bs4
from txt_files import save_dict_to_file, load_dict_from_file
from sort_lib import bubble_sort, quicksort, insertion_sort
from PIL import Image


def verify_select(select, top_index):
    '''Check if the entry from the user is valid  '''
    if select in [str(x) for x in range(1, top_index+1)]:  # Check if entry is in the range from 1 to 10.
        return True
    elif select == "-1":
        return True
    else:
        return False


def check_dict():
    '''Check if the dict.txt exist and if it has over 2300 lines.  '''
    cont_dict = os.path.isfile("./dict.txt")
    if cont_dict is True:
        with open("dict.txt", "r") as f:
            lines = f.readlines()
            if len(lines) < 2300:
                return False
            else:
                return True
    else:
        return False


def anim_gif(img_name):
    '''The function shows the animation .gif'''
    try:
        img = Image.open(img_name)
        img.seek(1)
        count = 0
        while count < 271:
            img.seek(img.tell() + 1)
            img.show()
            count += 1
    except Exception as exc:
        print(exc)


def clear():
    '''clear the terminal window'''
    os.system('clear')
    if os.name == "nt":
        os.system('cls')


url = 'https://xkcd.com'   # starting url
os.makedirs('xkcd', exist_ok=True)
top_10 = []
img_liste = []
liste_innhold = {}
count = 0

# Check if the dict.txt exist and if it has over 2300 lines,
# if it is false the program read the web page.
exist_dict = check_dict()
if exist_dict is False:
    while not url.endswith('#'):
        # Find the URL of the comic image.
        try:
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Could not find comic image.')
            else:
                comicUrl = 'https:' + comicElem[0].get('src')  # Add images url to variabel
                picture_page = comicElem[0].get('src')
                filename = picture_page.split('/')[-1]  # Extract the filename
                img_size = len(requests.get(comicUrl).content)  # Find the image size
                print(f"{count} Read file: '{filename}' and extracts metadata from the image.")
                liste_innhold = {"filename":filename, "size":img_size, "url":comicUrl}
                img_liste.append(liste_innhold)  # Make a image list with filename, size and url.
        except Exception as exc:
            print('There was a problem: %s' % (exc))

        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://xkcd.com' + prevLink.get('href')
        count = count+1
    save_dict_to_file(img_liste)  # Save the image list to file
    print('Done.')
else:
    # load from file if the dict.txt exist and store the data in img_liste,
    # so we don't need to start downloading again.
    img_liste = load_dict_from_file()

# Use quicksort for sorting the img_list, the most effective from plot.
sorting = quicksort(img_liste)

# Pick out the top ten sizes.
top_index = 10  # Make it easier if you want a top 5 or top 20 list.
top_x = sorting[:top_index]

# Makes Top 10 list which is printed on the screen
cont = True
while cont:
    clear()
    print(f"Top {top_index} results:\n")
    for x, img in enumerate(top_x, 1):
        print(f"Number {x:<6} with filename: {img['filename']:<35} and with size {img['size']:<10} byte")
    print(f"\nWrite '-1' to end the program")
    print("-----------------------------------------------------------------------------------------------")
    select = input("Select one of the numbers to open the image or write '-1' to end the program:")  # Select image
    # Verify the entry, if it is not valid you must make a new entry until it is valid.
    while not verify_select(select, top_index):
        print("Wrong entry, select correct number!")
        select = input("Select one of the numbers to open the image or write '-1' to end the program:")
    select = int(select)
    for index, content in enumerate(top_x, 1):
        if select == index:
            img_name = ("./xkcd/"+content['filename'])
            exist_img = os.path.isfile(img_name)
            # Check if image already exist in folder, then it will be opened.
            if exist_img is True:
                if ".gif" in img_name:  # Check if it is an gif file.
                    anim_gif(img_name)
                im = Image.open(img_name, mode='r')
                im.show()  # Show the image file
            # The image will be downloaded to /xkcd if it is not in folder.
            else:
                try:
                    url_img = (content['url'])
                    res = requests.get(url_img)
                    res.raise_for_status()
                    imageFile = open(os.path.join('xkcd', os.path.basename(url_img)), 'wb')
                    for chunk in res.iter_content(5000000):
                        imageFile.write(chunk)
                        imageFile.close()
                    if ".gif" in img_name:  # Check if it is an gif file.
                        anim_gif(img_name)
                    im = Image.open(img_name, mode='r')
                    im.show()  # Show the image file
                except Exception as exc:
                    print('There was a problem: %s' % (exc))
        elif select == -1:  # End the program
            cont = False
