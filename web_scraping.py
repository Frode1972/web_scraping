import requests, os, bs4, image, sys
from txt_files import save_dict_to_file, load_dict_from_file
from sort_lib import bubble_sort, quicksort, insertion_sort
from PIL import Image


def verify_select(select):
    '''Check if the entry from the user is valid  '''
    if select in [str(x) for x in range(1, 11)]:  # Check if entry is in the range from 1 to 10.
        return True
    elif select == "99":
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
    img = Image.open(img_name)
    img.seek(1)
    count = 0
    try:
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

exist_dict = check_dict()
# Check if the dict.txt exist and if it has over 2300 lines,
# if it is fase the program read the web page.
if exist_dict is False:
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
                comicUrl = 'https:' + comicElem[0].get('src')  # Add images url to variabel
                picture_page = comicElem[0].get('src')
                filename = picture_page.split('/')[-1]  # Extract the filename
                img_size = len(requests.get(comicUrl).content)  # Find the image size
                print(f"Read file number {count} and extract data from {filename}.")
                liste_innhold = {"filename": filename, "size": img_size, "url": comicUrl}
                img_liste.append(liste_innhold)  # Make a image list with filename, size and url.
        except Exception as exc:
            print('There was a problem A: %s' % (exc))

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

# Use quicksort for sorting the img_list
sorting = quicksort(img_liste)

# Pick out the top ten sizes.
top_10 = sorting[:10]

# Makes Top 10 list which is printed on the screen
cont = True
while cont:
    clear()
    print("Top ten results:\n")
    for x, y in enumerate(top_10, 1):
        print(f"Number {x:<6} with filename: {y['filename']:<35} and with size {y['size']:<10} byte")
    print(f"\nWrite '99' to end the program")
    print("-----------------------------------------------------------------------------------------------")
    select = input("Select one of the numbers to open the image or write 99 to end the program:")  # Select image
    # Verify the entry, if it is not valid you must make a new entry until it is valid.
    while not verify_select(select):
        print("Wrong entry, select correct number!")
        select = input("Select one of the numbers to open the image or write 99 to end the program:")
    select = int(select)
    for index, content in enumerate(top_10, 1):
        if select == index:
            url_img = (content['url'])
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
        elif select == 99:  # End the program
            cont = False
