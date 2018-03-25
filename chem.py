import qrcode
import xlrd
from pybel import *
from PIL import Image, ImageFont, ImageDraw
from subprocess import call

def print_label(input, index):
	size = 600, 280

	template = Image.open("template.png")

	call(["obabel", ("-:%s" % input[0]), "-O", "molecule.png"])
	mol = Image.open("molecule.png")
	call(["rm", "molecule.png"])

	label = "%s\n%s g/mol\n%s" % (input[1], input[2], input[0])
	qr_img = qrcode.make(label)

	qr_img.thumbnail(size, Image.ANTIALIAS)
	template.paste(mol, (0, 30))
	template.paste(qr_img, (300, 30))


	d = ImageDraw.Draw(template)
	fnt = ImageFont.truetype('/usr/share/fonts/true/type/ubuntu-font-family/UbuntuMono-R.ttf', 25)
	w, h = d.textsize(("%s\t\t%s g/mol" % (input[1], input[2])), font=fnt)
	d.text(((600-w)/2, 20), ("%s\t\t%s g/mol" % (input[1], input[2])), font=fnt, fill=(0,0,0))

	template.save("label_%d.png" % index)

def main():
	book = xlrd.open_workbook("input.xls")
	sheet = book.sheet_by_index(0)
	label_num = 0
	for row in range(sheet.nrows):
		l = []
		for column in range(sheet.ncols):
			l.append(sheet.cell(row,column).value)
		print_label(l, label_num)
		label_num += 1

if __name__ == "__main__": main()
