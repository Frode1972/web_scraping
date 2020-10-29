
def save_dict_to_file(dics):
    '''Save meta data filename, size and url to dict.txt.
    As filename,fall_back.png,size,100332,url,https://imgs.xkcd.com/comics/fall_back.png'''
    try:
        f = open('dict.txt', 'w')
        for i, data in enumerate(dics):
            name = ""
            count = 0
            for key, info in data.items():
                name = str(key)+", "+str(info)
                f.write(f"{name}")
                if count < 2:
                    f.write(",")
                count = count+1
            f.write(f"\n")
    except Exception as exc:
        print('There was a problem A: %s' % (exc))
    f.close()


def load_dict_from_file():
    '''Load info form dict.txt and put the data in list and dictonary [{}]'''
    img_list = []
    f = open("dict.txt", "r")
    for line in f:
        data = line.split(",")
        liste_inn = {data[0]: data[1], data[2]: int(data[3]), data[4]: data[5].strip()}
        img_list.append(liste_inn)
    f.close()
    return img_list
