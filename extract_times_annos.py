from bs4 import BeautifulSoup as bs

def get_bs_content(file_name):

    with open(file_name, "r") as f:
        content = f.readlines()
    content = "".join(content)
    bs_content = bs(content, features="xml")
    return bs_content


def populate_times(root):

    found_time = False
    time_dict = dict()
    children = root.children

    for child in children:

        # stop looking after we found time specs
        if found_time:
            break

        if child == "\n":
            pass
        else:
            try:
                l_content = len(child.contents)
                for i in range(l_content):
                    if child.contents[i] == "\n":
                        pass
                    else:
                        try:
                            k = child.contents[i]["TIME_SLOT_ID"]
                            v = child.contents[i]["TIME_VALUE"]
                            time_dict[k] = v
                            if not found_time:
                                found_time = True
                        except KeyError:
                            pass

            except TypeError:
                pass

    print(f"Number of time segments found = {len(time_dict.keys())}")
    return time_dict


def populate_annos(root):
    pass


if __name__ == "__main__":

    elan_file_name = "data/Cactus 4_8_22_Satya_V3.eaf"
    bs_content = get_bs_content(elan_file_name)
    root = next(bs_content.children)

    time_dict = populate_times(root)
    anno_dict = populate_annos(root)
