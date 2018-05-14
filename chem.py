import qrcode
import xlrd
import textwrap
from pybel import *
from PIL import Image, ImageFont, ImageDraw
from subprocess import call

def print_label(input, index):
	#size = 1200, 560
	size = 300, 300

	template = Image.open("template.png")

	m_in = readstring("smi", "-:%s" % input[0])
	#m_in.draw(filename="molecule.png")
	call(["obabel", ("-:=%s" % input[0]), "-O", "molecule.png"])
	mol = Image.open("molecule.png")
	call(["rm", "molecule.png"])

	label = "%s\n%s g/mol\n%s" % (input[1], input[2], input[0])
	qr_img = qrcode.make(label)

	qr_img = qr_img.resize((300, 300), Image.ANTIALIAS)
	mol = mol.resize((500, 500), Image.ANTIALIAS)
	template.paste(mol, (00, 60))
	template.paste(qr_img, (525, 50))


	d = ImageDraw.Draw(template)
	fnt = ImageFont.truetype('/usr/share/fonts/true/type/ubuntu-font-family/UbuntuMono-R.ttf', 60)
	fnt25 = ImageFont.truetype('/usr/share/fonts/true/type/ubuntu-font-family/UbuntuMono-R.ttf', 25)
	fnt15 = ImageFont.truetype('/usr/share/fonts/true/type/ubuntu-font-family/UbuntuMono-R.ttf', 15)
	w, h = d.textsize(("%s" % input[1]), font=fnt)
	d.text(((500-w)/2, 35), ("%s" % input[1]), font=fnt, fill=(0,0,0))

	fnt = ImageFont.truetype('/usr/share/fonts/true/type/ubuntu-font-family/UbuntuMono-R.ttf', 40)
	w, h = d.textsize(("MW: %.2f" % m_in.molwt), font=fnt)
	d.text(((1350-w)/2,430), ("MW: %.2f" % m_in.molwt), font=fnt, fill=(0,0,0))
	w, h = d.textsize(("%s" % m_in.formula), font=fnt)
	d.text(((1350-w)/2,380), ("%s" % m_in.formula), font=fnt, fill=(0,0,0))
	w, h = d.textsize(("Created: %s" % input[3]), font=fnt25)
	d.text(((1350-w)/2,480), ("Created: %s" % input[3]), font=fnt25, fill=(0,0,0))

	offset = 380
	for line in textwrap.wrap(("%s" % input[4]), width=23):
	    d.text((810, offset), line, font=fnt15, fill=(0,0,0))
	    offset += fnt15.getsize(line)[1]

	template.save("label_%d.png" % index)

def chem_main(filename):
	book = xlrd.open_workbook(filename)
	sheet = book.sheet_by_index(0)
	label_num = 0
	for row in range(sheet.nrows):
		l = []
		for column in range(sheet.ncols):
			l.append(sheet.cell(row,column).value)
		print_label(l, label_num)
		label_num += 1

if __name__ == "__main__": main()
