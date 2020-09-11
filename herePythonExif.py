from PIL import Image
from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS
import sys
#                    Has GPSInfo?
# stratInsanity.JPG [√]   'GPSInfo': {1: 'N', 2: (36.0, 7.0, 28.05), 3: 'W', 4: (115.0, 10.0, 6.97), 5: b'\x00', 6: 629.3669064748201, 7: (9.0, 37.0, 28.0), 12: 'K', 13: 0.0, 16: 'M', 17: 222.91115311909263, 23: 'M', 24: 222.91115311909263, 29: '2018:06:21', 31: 66.15432098765432}
    # Acceptable Google Format: (36 7 28.05 N 115 10 6.97 W)
# emelyArcade.JPG [√]    'GPSInfo': {1: 'N', 2: (36.0, 8.0, 18.57), 3: 'W', 4: (115.0, 9.0, 58.51), 5: b'\x00', 6: 633.5058823529412, 7: (23.0, 5.0, 9.79), 12: 'K', 13: 0.23, 16: 'M', 17: 350.5717821782178, 23: 'M', 24: 350.5717821782178, 29: '2018:06:20', 31: 10.0}
    # Acceptable Google Format: (36 8 18.57 N 115 9 58.51 W)

# 4thJuly.JPG[√]         'GPSInfo': {1: 'N', 2: (34.0, 1.0, 49.51), 3: 'W', 4: (118.0, 19.0, 11.15), 5: b'\x00', 6: 46.989311218613224, 7: (4.0, 13.0, 34.99), 12: 'K', 13: 0.0, 16: 'M', 17: 72.46701811300352, 23: 'M', 24: 72.46701811300352, 29: '2019:04:14', 31: 10.0}
# groundCamME.JPG [√]    'GPSInfo': {1: 'N', 2: (34.0, 2.0, 44.9), 3: 'W', 4: (118.0, 20.0, 18.41), 5: b'\x00', 6: 43.623719032932044, 12: 'K', 13: 0.9014801973596479, 16: 'M', 17: 129.3024750118991, 23: 'M', 24: 129.3024750118991, 29: '2020:09:11', 31: 64.11955403087478}
# zhuCam.JPG [~]   'SubjectLocation': (2510, 1371, 1004, 998)
# poptartCam.JPG [~] 'SubjectLocation': (2009, 1509, 2318, 1390)

# famLawrys.JPG [-]
# shrimpSS.PNG [-]
# smileyDL.PNG [-]
# trashCam.HEIC [Incompatible File Type]
# yellowtintCam.HEIC [Incompatible File Type]

# Change name to whichever photo you want to use
# and the path, I stored mine in the same folder/location as the .py file was stored
filename = '4thJuly.JPG'

img_file = filename
image = Image.open(img_file)
exifD ={}

for tag, value in image._getexif().items():
 if tag in TAGS:
  exifD[TAGS[tag]] = value

if 'GPSInfo' not in exifD:
 print('Your file does not have GPSInfo')
 sys.exit()



def get_exif(filename):
	image = Image.open(filename)
	image.verify()
	return image._getexif()

exif = get_exif(filename)

# Turns number tags into word tags. 34853 -> GPSInfo
def get_labeled_exif(exif):
	labeled = {}
	for (key,val) in exif.items():
		labeled[TAGS.get(key)] = val

	return labeled

exif = get_exif(filename)
labeled = get_labeled_exif(exif)
# print(labeled)

def get_geotagging(exif):
	if not exif:
		print("No EXIF metadata found")
		# quit()

	geotagging = {}
	for (idx, tag) in TAGS.items():
		if tag == 'GPSInfo':
			if idx not in exif:
				print("No EXIF geotagging found")
				# quit()

			for (key, val) in GPSTAGS.items():
				if key in exif[idx]:
					geotagging[val] = exif[idx][key]

	return geotagging

exif = get_exif(filename)
geotags = get_geotagging(exif)
print(geotags)






