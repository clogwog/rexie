'''
Create a header file with byte arrays representing 16x16 RGB images.
'''

import os
import cv2
import glob
from pathlib import Path


allbmpfiles = sorted(glob.glob("./*.bmp"))


out_name = "icons"


def run():

	target_size = (32,32)
	res_imgs = [ cv2.imread(f) for f in allbmpfiles ]

	out_file = "./generated/"+out_name+".h"
	header = "/* \n" \
			 " * Assets header: "+out_name+"\n" \
			 " * Automatically generated from image files: \n * "+"\n * ".join(allbmpfiles)+"\n" \
			 " */\n\n"


	with open(out_file, "w") as f:
		f.write(header)
		f.write("#define %s_frames %d\n" % (out_name, len(res_imgs)))
		f.write("#define %s_width %d\n" % (out_name, target_size[0]))
		f.write("#define %s_height %d\n" % (out_name, target_size[1]))
		f.write("\nconst uint8_t animation_icons[][]  = {\n")

		index = 0
		for img in res_imgs:
			spaceevery3 = 1
			crevery32 =1
			f.write("\n{ \n" )
			for v in img[:,:,::-1].reshape(-1).tolist():

				f.write("%s," % hex(v))
				if spaceevery3 == 3:
					spaceevery3=0
					f.write(" ")
				spaceevery3 = spaceevery3 + 1
				if crevery32 == ( 3* 32) :
					crevery32 = 0
					f.write("\n")
				crevery32 = crevery32 + 1

			f.write("\n")
			f.write("} ,\n")
			index = index + 1
		f.write("};\n")




if __name__ == '__main__':
	run()
