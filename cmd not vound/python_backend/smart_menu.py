from collections import Counter
import os
import rgb_fox as rgbf
import pandas as pd
from PIL import Image
from kash import kash
import json

"""
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:,*********`:,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:`*************,:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:*****:,**:*****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:****`:,**:,****:`:,:`:,:`:,:`:,:`***`:,:`:,:`:,
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:`:,:`:,:`:,:`:,:`:,:`***`********:,
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,:`:,:`:,:`:,:`:,:`:,:`*************,
`:,:***:`:,:`:,:`:,:`:,:`********:,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`*********,:`:,:`:,:`:,:`:,:`:,:`**************
`:,:***:`:,:`:,:`:,:`:,:`:**********`:,:`:,:`:,:`:,:`:,:`*****,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,***********,:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`**********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,********:`:,:`:,:`:,:`:,:`****:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:****`:,**:,:****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:*****:,**:,*****`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:***************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`**************:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:************,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,**********:,:`:,:`:,:`:,:`:,:`***`:,:`:,****
`:,:***:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:*****:`:,:`:,:`:,:`:,:`:,:`:,**:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
*******:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
******,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,
`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,:`:,'
"""
from pri import nt

print = nt

import pytesseract as pt


@kash("identify_pure")
def identify_pure(i):
    return pt.image_to_string(Image.open(i).rotate(180, expand=True), lang="spa")


class SmartMenu:
    def __init__(s, image_paths):
        s.color_counter = Counter()
        s.image_paths = image_paths
        s.body = dict()
        # print(f'PYTESSSERACT: VERS..{pt.get_tesseract_version()}')

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def __serialize__(self):
        # Convert the object to a dictionary that can be serialized
        return {"image_paths": self.image_paths}

    @classmethod
    def __deserialize__(cls, data):
        # Create an instance of the class using the deserialized data
        return cls(**data)

    def identify(s, im):
        print("analyzing language data")
        content = identify_pure(im)
        # print('analyzing image boxes')
        # oh = pt.image_to_boxes(Image.open(im).rotate(180, expand=True), lang="spa")
        # for o in oh.split('\n'):
        #     print(o)
        # print('analyzing image data')
        # oh = pt.image_to_data(Image.open(im).rotate(180, expand=True), lang="spa")
        # for o in oh[1:]:
        #     print(o)
        # pdoh = pd.DataFrame(oh[1:], columns=oh[0].split("\t"))
        # print(pdoh)
        # print(dir(o))
        # print(type(o))
        print("storing up")
        s.body.update({im.split("/")[-1]: content})

    def get_html_body(s):
        for im in s.image_paths:
            s.identify(im)
        return s.body

    def pprint(s):
        print(*[f"{k}:{v}" for k, v in s.body.items()])

    def associate_prices_to_text(s):
        if not getattr(s, "body"):
            s.get_html_body()
        file_price_text = {}
        for arquivo, text in s.body.items():
            in_chunk = False
            chunk = ""

            # print("RAW" * 99)
            # for te in text.split("\n"):
            #     print(te)
            # print("RAW" * 99)

            chunkz = []
            for te in text.split("\n"):
                if te == "" and not in_chunk:
                    in_chunk = True
                elif te == "" and in_chunk:
                    chunkz += [chunk]
                    chunk = ""
                    in_chunk = False
                if in_chunk and te != "\n":
                    chunk += te + "\n"
            valid_chunk = lambda ch: any(
                [
                    len(list(filter(lambda x: x.isnumeric() or x in ".,", ch_l)))
                    for ch_l in ch.split("\n")
                ]
            )

            def get_value(_ch):
                """
                todo error if multiple vals, or prompt all possible"""
                val = 0
                for _ch_l in _ch.split("\n"):
                    if x := list(
                        filter(
                            lambda y: any(yy.isnumeric() for yy in y),
                            filter(lambda x: x.isnumeric() or x in ".,", _ch_l),
                        )
                    ):
                        return float("".join(x))
                # print( ValueError("invalid chunk" + str(_ch)))
                return val

            price_text = {}
            for c in filter(valid_chunk, chunkz):
                val = get_value(c)
                item = (
                    "".join([cc for cc in c if cc not in map(str, range(10))])
                    .replace("$", "")
                    .replace(".", "")
                )
                price_text.update({val: item})

            file_price_text[arquivo] = price_text

        return s.ex("fpt", file_price_text,)

    def ex(s, e, x):
        setattr(s, e, x)
        return x


def premain(roo: str):
    # Provide the path to the menu image
    x = os.listdir(roo)
    ips = ["/".join((os.getcwd(), roo, y,)) for y in x]
    return ips


def main(*a, **k):
    ips = premain("examples/sabor-catracha")
    sm = SmartMenu(ips)
    fpt = sm.associate_prices_to_text()

    for _fpt in sm.fpt.items():
        f, pt = _fpt
        print('FILE',f)
        for _pt in pt.items():
            p, t = _pt
            print('price',p)
            print('item; "',' '.join(t.split('\n')),'"')


if __name__ == "__main__":
    main()
