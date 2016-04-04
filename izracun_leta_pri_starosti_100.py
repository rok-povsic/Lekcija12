import datetime

ime = raw_input("Vpisi svoje ime: ")
starost = int(raw_input("Vpisi svojo starost: "))

cez_toliko_let_bom_star_100 = 100 - starost

trenutno_leto = datetime.datetime.now().year
leto_ko_bom_100 = trenutno_leto + cez_toliko_let_bom_star_100

print "Zivjo " + ime + ", leta " + str(leto_ko_bom_100) + " bos star 100 let."
