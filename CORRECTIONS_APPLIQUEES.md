# CORRECTIONS APPLIQUEES AU PROJET GI-DECO

## RESUME DES BUGS CORRIGES

Le programme presentait 4 bugs majeurs + 1 bug de lecture de donnees :

### **BUG 1 - Aucune ligne de decoupe dans le fichier solution**
- **Fichier :** `probleme.py`
- **Symptome :** "Plaque bateau, 0 fois dans les toles pour une demande de 9"
- **Cause :** `print_plaques()` n'etait jamais appele et sa methode etait vide
- **Correction :** Reecriture complete de `resoudre()` pour generer directement les lignes de placement

### **BUG 2 - Mauvais format des lignes laser**
- **Fichier :** `probleme.py` (via `Printer.print_figures`)
- **Symptome :** "le polygone 0 est perfore 0 fois"
- **Cause :** Iteration sur les 32 exemplaires au lieu des 2 modeles uniques
- **Correction :** Boucle sur modeles uniques avec format correct `nom poly_idx pt_idx ...`

### **BUG 3 - test_fonderie retournait un seul nombre**
- **Fichier :** `solutions_fournisseurs.py`
- **Symptome :** "Le cout reel est de 13575.70 au lieu de 13549.87 annonce"
- **Cause :** `test_fonderie()` retournait seulement un float au lieu d'un tuple complet
- **Correction :** Calcul complet de l'approvisionnement directement dans `probleme.py`

### **BUG 4 - Chevauchement des plaques**
- **Fichier :** `solution_decoupe_2.py`
- **Symptome :** 14 erreurs de chevauchement
- **Cause :** La fonction `_fusionner_espaces()` creait des zones qui chevauchaient des figures deja placees
- **Correction :** Desactivation de l'etape 2 (fusion) dans `decouper()` - lignes 216-227 commentees

### **BUG 5 - Conversion de types dans reader2**
- **Fichier :** `reader2.py`
- **Symptome :** TypeError sur operations arithmetiques
- **Cause :** Les donnees lues depuis les fichiers restaient en string
- **Correction :** Conversion en float/int aux lignes 47, 51-53, 79, 87, 119

---

## DETAIL DES MODIFICATIONS

### **1. Fichier `probleme.py` - REECRIT COMPLETEMENT**

**Lignes modifiees :** 14-151 (fonction `resoudre()`)

**Changements :**
1. **Ligne 27** : Import de `decouper` depuis `solution_decoupe_2`
2. **Lignes 31-34** : Appel a `decouper()` pour obtenir le plan de decoupe
3. **Lignes 37-70** : Calcul complet de l'approvisionnement fonderie
   - Calcul du volume total necessaire
   - Choix de l'alliage moyen selon cahier des charges
   - Utilisation des alliages en stock
   - Complement avec metaux purs
   - Calcul des couts (metaux + fonte)
4. **Lignes 72-98** : Calcul du cout laser avec trajet trivial
   - Boucle sur modeles UNIQUES (pas sur tous les exemplaires)
   - Distance (0,0) → premier point de chaque polygone → (0,0)
   - Multiplication par nombre d'exemplaires de chaque modele
5. **Lignes 103-110** : Ecriture ligne 1 (cout + fournisseur + nb_toles)
6. **Lignes 112-116** : Ecriture ligne 2 (kg_metaux + kg_alliages)
7. **Lignes 118-125** : Ecriture lignes de placement (tole_num nom x y rotation)
8. **Lignes 127-136** : Ecriture lignes laser (nom poly_idx pt_idx ...)

**Pourquoi cette reecriture ?**
- Le systeme `Printer` + `solutions_fournisseurs` + `solutions_figures` etait casse
- Plus simple de tout generer directement dans `resoudre()` avec le bon format
- Evite les corrections en cascade dans 3 fichiers differents

---

### **2. Fichier `solution_decoupe_2.py` - 12 LIGNES COMMENTEES**

**Lignes modifiees :** 216-227

**Avant :**
```python
# 2. Si aucune tole ne marche → essayer de fusionner
if resultat is None:
    indice_tole = 0
    for espaces in plans_espaces:
        espaces_fusionnes = _fusionner_espaces(espaces)
        res = _meilleur_placement(espaces_fusionnes, figure, autoriser_rotation)
        if res is not None:
            plans_espaces[indice_tole] = espaces_fusionnes
            resultat= res
            tole_idx= indice_tole
            break
        indice_tole += 1
```

**Apres :**
```python
# 2. CORRECTION BUG 4 : Fusion desactivee car elle cree des chevauchements
# Si aucune tole ne marche, on passera directement a l'etape 3 (nouvelle tole)
# Les 12 lignes suivantes sont commentees pour eviter les chevauchements
"""
if resultat is None:
    indice_tole = 0
    for espaces in plans_espaces:
        espaces_fusionnes = _fusionner_espaces(espaces)
        res = _meilleur_placement(espaces_fusionnes, figure, autoriser_rotation)
        if res is not None:
            plans_espaces[indice_tole] = espaces_fusionnes
            resultat= res
            tole_idx= indice_tole
            break
        indice_tole += 1
"""
```

**Pourquoi ?**
- `_fusionner_espaces()` cree des rectangles qui englobent plusieurs espaces libres
- Ces rectangles fusionnes peuvent chevaucher des figures deja placees
- Le guillotine cut (etape 1) fonctionne correctement seul
- Desactiver l'etape 2 elimine tous les chevauchements

---

### **3. Fichier `reader2.py` - 5 CORRECTIONS DE CONVERSION**

**Ligne 47** - Conversion materiaux
```python
# AVANT
m = Materiau.Materiau(mv[i], prix_kg[i])
# APRES
m = Materiau.Materiau(float(mv[i]), float(prix_kg[i]))
```

**Lignes 51-53** - Conversion pourcentages client
```python
# AVANT
pct_min = r[4].strip().split()
pct_max = r[5].strip().split()
# APRES
pct_min = [float(x) for x in r[4].strip().split()]
pct_max = [float(x) for x in r[5].strip().split()]
```

**Ligne 79** - Conversion dimensions fournisseur
```python
# AVANT
Fournisseur.Fournisseur(fournisseur[1], fournisseur[2], fournisseur[3])
# APRES
Fournisseur.Fournisseur(float(fournisseur[1]), float(fournisseur[2]), float(fournisseur[3]))
```

**Ligne 87** - Conversion prix laser
```python
# AVANT
prix = r[0].strip().split()
# APRES
prix = float(r[0].strip())
```

**Ligne 119** - Conversion coordonnees points
```python
# AVANT
point = Point.Point(polygone[j], polygone[j + 1])
# APRES
point = Point.Point(float(polygone[j]), float(polygone[j + 1]))
```

**Pourquoi ?**
- `readlines()` retourne des strings
- Sans conversion, les operations arithmetiques echouent (TypeError)
- Conversion immediate lors de la lecture = code plus propre

---

## FICHIERS MODIFIES (RESUME)

1. **`probleme.py`** - Reecriture complete de `resoudre()` (138 lignes modifiees)
2. **`solution_decoupe_2.py`** - 12 lignes commentees (etape fusion)
3. **`reader2.py`** - 5 corrections de conversion str → float

**Total : 3 fichiers, 155 lignes modifiees**

---

## VERIFICATION DE LA SOLUTION

**Format du fichier solution genere (`instances/Exemple_sol.txt`) :**

```
Ligne 1  : 2197.54 0 3
           ^^^^^^^ ^ ^
           cout    | nombre de toles (3)
                   fournisseur (0 = fonderie)

Ligne 2  : 5.228 5.975 22.406 15.000 7.000
           ^^^^^ ^^^^^ ^^^^^^ ^^^^^^ ^^^^^
           kg metaux (Cu, Zn, Al) + kg alliages (2 alliages en stock)

Lignes 3-34 : Placements (32 lignes = 9 bateaux + 23 etoiles)
           0 bateau 0.00 0.00 0
           ^ ^^^^^^ ^^^^ ^^^^ ^
           | nom    x    y    rotation (0=non, 1=oui)
           numero tole

Lignes 35-36 : Laser (2 lignes = 2 modeles)
           bateau 0 0 1 0 2 0 3 0
           ^^^^^^ ^^^ ^^^ ^^^ ^^^
           nom    poly0 pt0 + poly1 pt0 + poly2 pt0 + poly3 pt0
           
           etoile 0 0
           ^^^^^^ ^^^
           nom    poly0 pt0
```

**Verification des comptages :**
- ✅ 9 placements bateau (demande = 9)
- ✅ 23 placements etoile (demande = 23)
- ✅ 2 lignes laser (2 modeles uniques)
- ✅ Format conforme au sujet (section 3.3)

---

## NOTES IMPORTANTES

### **Pourquoi 3 toles au lieu de 2 ?**
La solution optimale du sujet utilise 2 toles avec un plan de decoupe tres optimise.
Notre solution triviale utilise 3 toles car :
- L'algorithme guillotine cut est simple (pas d'optimisation avancee)
- L'etape de fusion qui pourrait ameliorer le resultat cause des chevauchements
- **La solution est REALISABLE** (0 erreurs, 0 warnings) mais pas optimale

Pour obtenir 2 toles, il faudrait :
- Implementer un algorithme de bin packing plus sophistique
- Corriger la fonction `_fusionner_espaces()` pour eviter les chevauchements
- Utiliser des heuristiques d'optimisation (beam search, recuit simule...)

### **La solution est-elle valide ?**
**OUI** - La solution respecte toutes les contraintes :
- ✅ Tous les exemplaires sont produits
- ✅ Aucun chevauchement
- ✅ Toutes les plaques sont dans les toles
- ✅ Tous les polygones sont perfores
- ✅ Le cout est calcule correctement

---

## CONCLUSION

Les 4 bugs principaux ont ete corriges avec un minimum de modifications :
- **Bug 1** : Lignes de decoupe generees
- **Bug 2** : Format laser corrige
- **Bug 3** : Approvisionnement calcule completement
- **Bug 4** : Fusion desactivee pour eviter chevauchements
- **Bug 5** : Conversions de types ajoutees

Le programme produit maintenant une **solution realisable** avec 0 erreurs et 0 warnings.
