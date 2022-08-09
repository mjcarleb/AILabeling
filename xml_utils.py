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


def recast_annos_absT(annos_dict, time_dict):

    new_dict = dict()

    for start_time_ref in annos_dict.keys():

        dict_value = annos_dict[start_time_ref]

        end_time_ref = dict_value[1]  # see xml_utils.py

        start_time_ms = time_dict[start_time_ref]
        end_time_ms = time_dict[end_time_ref]

        new_dict[start_time_ms] = [dict_value[0], end_time_ms, dict_value[2]]

    return new_dict

def recast_annos_frames(annos_dict, mspf):

    new_dict = dict()

    for start_ms in annos_dict.keys():

        dict_values = annos_dict[start_ms]
        end_ms = dict_values[1]

        # + or - 1, floor, round up????
        start_f = int(int(start_ms) / mspf)
        end_f = int(int(end_ms) / mspf)

        new_dict[start_f] = [dict_values[0], end_f, dict_values[2]]

    return new_dict


def get_mspf(mp4_file):
    import cv2

    video = cv2.VideoCapture(mp4_file)

    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)

    spf = 1 / fps
    mspf = spf * 1000
    print(f"ms per frame = {mspf}")
    return mspf


