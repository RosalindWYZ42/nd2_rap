import nd2
import os
import datetime
import json


nd2file = "Z:\IHC_Coloc\images\Slide.22.10x.nd2"
metadata = nd2.metadata(nd2file)

ndfile="Z:\IHC_Coloc\images\Slide78\"+"100x SR.nd2"
with nd2.ND2File(r"Z:\IHC_Coloc\images\Slide78\100x SR.nd2") as ndfile:
    metadata = ndfile.metadata

f = nd2.ND2File(r"Z:\IHC_Coloc\images\Slide78\100x SR.nd2")
all = f.unstructured_metadata()
all = print('s')

with open("sample.json", "w") as outfile: 
    json.dump(all, outfile, sort_keys=True,
    indent=4,
    separators=(',', ': '))