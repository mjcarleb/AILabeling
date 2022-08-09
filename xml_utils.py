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

    found_annos = False
    annos_dict = dict()
    children = root.children

    for child in children:

        # stop looking after we found time specs
        if found_annos:
            break

        if child == "\n":
            pass
        else:
            try:
                l_contents = len(child.contents)
                if child.contents == "\n":
                    pass
                else:
                    for i in range(l_contents):
                        if child.contents[i] == "\n":
                            pass
                        elif child.contents[i].name == "ANNOTATION":
                            annotation_id = child.contents[i].contents[1].attrs["ANNOTATION_ID"]
                            time_slot_ref1 = child.contents[i].contents[1].attrs["TIME_SLOT_REF1"]
                            time_slot_ref2 = child.contents[i].contents[1].attrs["TIME_SLOT_REF2"]
                            annotation_label = child.contents[i].contents[1].contents[1].contents[0]

                            # annos dict will be keyed off of start time
                            # annos dict will contain list anno_id, ending time slot and label
                            annos_dict[time_slot_ref1] = [annotation_id, time_slot_ref2, annotation_label]
                            found_annos = True

            except TypeError:
                pass

    print(f"Number of annos found = {len(annos_dict.keys())}")
    return annos_dict
