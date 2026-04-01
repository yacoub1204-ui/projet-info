import Alliage
import Figure
import Plaques


class Tole:

    def __init__(self, x, y, z, all : Alliage):
        self._x = x
        self._y = y
        self._z = z
        self._all = all

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y
    
    def get_z(self):
        return self._z

    def get_all(self):
        return self._all


#____________
#methode 1
#______________

	def decoupe_simple(self, plaques):
		"""commence avec une tole entière.quand on place une plaque on crée 2 nouvelles zones :une à droite une en haut. on repete"""
		toles_utilisees = 1
	# zones disponibles dans la tole actuelle
		zones = [(self._x, self._y)]
		liste_plaques = plaques.get_list_f()
		for i in range(len(liste_plaques)):
			plaque = liste_plaques[i]
			placee = False
			for j in range(len(zones)):
				zone_x, zone_y = zones[j]
				px = plaque.get_x()
				py = plaque.get_y()			
				# sans rotation
				if px <= zone_x and py <= zone_y:
					zones.pop(j)
					# découpe
					zones.append((zone_x - px, py))      # droite
					zones.append((zone_x, zone_y - py))  # haut
					placee = True
					break
				# avec rotation
				plaque.tourner()
				px = plaque.get_x()
				py = plaque.get_y()
				if px <= zone_x and py <= zone_y:
					zones.pop(j)
					zones.append((zone_x - px, py))
					zones.append((zone_x, zone_y - py))
					placee = True
					break
				#remetdroite
				plaque.tourner()
			# nouvelle tole
			if not placee:
				toles_utilisees += 1
				zones = [(self._x, self._y)]
				px = plaque.get_x()
				py = plaque.get_y()
				zone_x, zone_y = zones.pop()
				zones.append((zone_x - px, py))
				zones.append((zone_x, zone_y - py))
		return toles_utilisees
                    
