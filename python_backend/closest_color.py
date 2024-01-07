from webcolors import rgb_to_name, hex_to_rgb, rgb_to_hex, CSS3_HEX_TO_NAMES

CSS3_HEX_TO_INT = {k: int(k.replace("#", ""), 16) for k, v in CSS3_HEX_TO_NAMES.items()}

print(CSS3_HEX_TO_NAMES)


def closest_color(rgb):
    rgb_int = int(rgb_to_hex(x).replace("#", ""), 16)
    if (name := CSS3_HEX_TO_NAMES.get(rgb_to_hex(x))) :
        return name
    # tuples of hex_int, sorted by int
    cors = sorted(CSS3_HEX_TO_INT.items(), key=lambda hex_int: hex_int[1])
    print("COOOR@", rgb_int)
    for ix, hex_i_int_i in enumerate(cors[:-1]):
        hex_i, int_i = hex_i_int_i
        print("inter-color", hex_i_int_i)
        # iterate hex_ints.
        # if rgb_int is between int values, return CSS3_HEX_TO_NAMES.get(hex)
        if (sky_limit := cors[ix + 1][1]) > rgb_int:
            print(
                "Sky limit, ", sky_limit,
            )
            return CSS3_HEX_TO_NAMES.get(hex_i)
    return CSS3_HEX_TO_NAMES[cors[-1][0]]
