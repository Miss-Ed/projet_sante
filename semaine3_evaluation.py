# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — EVALUATION : Partie Pratique + Debuugage
# ============================================================

# ============================================================
# PARTIE PRATIQUE — Systeme d'Alerte Campagne de Vaccination
# 6 zones | Classification OMS | Rapport complet
# ============================================================

# Constantes OMS (pas de valeurs hardcodees dans les conditions)
SEUIL_ZONE_CRITIQUE    = 50.0  # %
SEUIL_ZONE_A_RISQUE    = 80.0  # %
SEUIL_ZONE_INSUFFISANTE = 95.0  # %

# Donnees des 6 zones
z1_nom = 'Bacongo';    z1_taux = 91.0; z1_pop = 180000
z2_nom = 'Madingou';   z2_taux = 67.0; z2_pop = 45000
z3_nom = 'Kinkala';    z3_taux = 48.0; z3_pop = 62000
z4_nom = 'Ouesso';     z4_taux = 38.0; z4_pop = 28000
z5_nom = 'Impfondo';   z5_taux = 78.5; z5_pop = 15000
z6_nom = 'Dolisie';    z6_taux = 95.5; z6_pop = 95000

# --- Classification zone 1 : Bacongo ---
if z1_taux < SEUIL_ZONE_CRITIQUE:
    z1_statut = 'ZONE CRITIQUE'; z1_couleur = '[ROUGE]'
elif z1_taux < SEUIL_ZONE_A_RISQUE:
    z1_statut = 'ZONE A RISQUE'; z1_couleur = '[ORANGE]'
elif z1_taux < SEUIL_ZONE_INSUFFISANTE:
    z1_statut = 'ZONE INSUFFISANTE'; z1_couleur = '[JAUNE]'
else:
    z1_statut = 'ZONE CONFORME'; z1_couleur = '[VERT]'

# --- Classification zone 2 : Madingou ---
if z2_taux < SEUIL_ZONE_CRITIQUE:
    z2_statut = 'ZONE CRITIQUE'; z2_couleur = '[ROUGE]'
elif z2_taux < SEUIL_ZONE_A_RISQUE:
    z2_statut = 'ZONE A RISQUE'; z2_couleur = '[ORANGE]'
elif z2_taux < SEUIL_ZONE_INSUFFISANTE:
    z2_statut = 'ZONE INSUFFISANTE'; z2_couleur = '[JAUNE]'
else:
    z2_statut = 'ZONE CONFORME'; z2_couleur = '[VERT]'

# --- Classification zone 3 : Kinkala ---
if z3_taux < SEUIL_ZONE_CRITIQUE:
    z3_statut = 'ZONE CRITIQUE'; z3_couleur = '[ROUGE]'
elif z3_taux < SEUIL_ZONE_A_RISQUE:
    z3_statut = 'ZONE A RISQUE'; z3_couleur = '[ORANGE]'
elif z3_taux < SEUIL_ZONE_INSUFFISANTE:
    z3_statut = 'ZONE INSUFFISANTE'; z3_couleur = '[JAUNE]'
else:
    z3_statut = 'ZONE CONFORME'; z3_couleur = '[VERT]'

# --- Classification zone 4 : Ouesso ---
if z4_taux < SEUIL_ZONE_CRITIQUE:
    z4_statut = 'ZONE CRITIQUE'; z4_couleur = '[ROUGE]'
elif z4_taux < SEUIL_ZONE_A_RISQUE:
    z4_statut = 'ZONE A RISQUE'; z4_couleur = '[ORANGE]'
elif z4_taux < SEUIL_ZONE_INSUFFISANTE:
    z4_statut = 'ZONE INSUFFISANTE'; z4_couleur = '[JAUNE]'
else:
    z4_statut = 'ZONE CONFORME'; z4_couleur = '[VERT]'

# --- Classification zone 5 : Impfondo ---
if z5_taux < SEUIL_ZONE_CRITIQUE:
    z5_statut = 'ZONE CRITIQUE'; z5_couleur = '[ROUGE]'
elif z5_taux < SEUIL_ZONE_A_RISQUE:
    z5_statut = 'ZONE A RISQUE'; z5_couleur = '[ORANGE]'
elif z5_taux < SEUIL_ZONE_INSUFFISANTE:
    z5_statut = 'ZONE INSUFFISANTE'; z5_couleur = '[JAUNE]'
else:
    z5_statut = 'ZONE CONFORME'; z5_couleur = '[VERT]'

# --- Classification zone 6 : Dolisie ---
if z6_taux < SEUIL_ZONE_CRITIQUE:
    z6_statut = 'ZONE CRITIQUE'; z6_couleur = '[ROUGE]'
elif z6_taux < SEUIL_ZONE_A_RISQUE:
    z6_statut = 'ZONE A RISQUE'; z6_couleur = '[ORANGE]'
elif z6_taux < SEUIL_ZONE_INSUFFISANTE:
    z6_statut = 'ZONE INSUFFISANTE'; z6_couleur = '[JAUNE]'
else:
    z6_statut = 'ZONE CONFORME'; z6_couleur = '[VERT]'

# --- Personnes non vaccinees par zone ---
z1_non_vaccines = int(z1_pop * (1 - z1_taux / 100))
z2_non_vaccines = int(z2_pop * (1 - z2_taux / 100))
z3_non_vaccines = int(z3_pop * (1 - z3_taux / 100))
z4_non_vaccines = int(z4_pop * (1 - z4_taux / 100))
z5_non_vaccines = int(z5_pop * (1 - z5_taux / 100))
z6_non_vaccines = int(z6_pop * (1 - z6_taux / 100))

total_non_vaccines = (z1_non_vaccines + z2_non_vaccines + z3_non_vaccines
                      + z4_non_vaccines + z5_non_vaccines + z6_non_vaccines)

# --- Compteurs par categorie ---
nb_rouge  = 0
nb_orange = 0
nb_jaune  = 0
nb_vert   = 0

for statut in [z1_statut, z2_statut, z3_statut, z4_statut, z5_statut, z6_statut]:
    if statut == 'ZONE CRITIQUE':
        nb_rouge = nb_rouge + 1
    elif statut == 'ZONE A RISQUE':
        nb_orange = nb_orange + 1
    elif statut == 'ZONE INSUFFISANTE':
        nb_jaune = nb_jaune + 1
    else:
        nb_vert = nb_vert + 1

# --- Affichage rapport ---
print('=' * 62)
print('  RAPPORT CAMPAGNE VACCINATION — DSS CONGO')
print('  Date : 15 janvier 2026')
print('=' * 62)
print(f'  {z1_couleur} {z1_nom:<12} {z1_taux}% | Non vaccines : {z1_non_vaccines:,} => {z1_statut}')
print(f'  {z2_couleur} {z2_nom:<12} {z2_taux}% | Non vaccines : {z2_non_vaccines:,} => {z2_statut}')
print(f'  {z3_couleur} {z3_nom:<12} {z3_taux}% | Non vaccines : {z3_non_vaccines:,} => {z3_statut}')
print(f'  {z4_couleur} {z4_nom:<12} {z4_taux}% | Non vaccines : {z4_non_vaccines:,} => {z4_statut}')
print(f'  {z5_couleur} {z5_nom:<12} {z5_taux}% | Non vaccines : {z5_non_vaccines:,} => {z5_statut}')
print(f'  {z6_couleur} {z6_nom:<12} {z6_taux}% | Non vaccines : {z6_non_vaccines:,} => {z6_statut}')
print('-' * 62)
print(f'  Total personnes non vaccinees : {total_non_vaccines:,}')
print(f'  ROUGE [CRITIQUE]    : {nb_rouge} zone(s)')
print(f'  ORANGE [A RISQUE]   : {nb_orange} zone(s)')
print(f'  JAUNE [INSUFFISANT] : {nb_jaune} zone(s)')
print(f'  VERT [CONFORME]     : {nb_vert} zone(s)')
print('-' * 62)

# Recommandation finale si nb_rouge > 1
if nb_rouge > 1:
    print(f'  !! RECOMMANDATION : {nb_rouge} zones CRITIQUES detectees')
    print('  => Campagne d\'urgence nationale obligatoire — intervention DSS')
print('=' * 62)


# ============================================================
# PARTIE DEBUUGAGE — 4 erreurs identifiees et corrigees
# ============================================================
print()
print('=' * 62)
print('  PARTIE DEBUUGAGE — Code triage corrige')
print('=' * 62)

# Code original avec 4 erreurs :
# ERREUR 1 (ligne if niveau 1) : 'and' au lieu de 'or'
#   => and exige que les 3 conditions soient VRAIES simultanement
#   => Correction : utiliser 'or' (une seule suffit)
#
# ERREUR 2 (elif niveau 3) : copie exacte du elif ORANGE
#   => JAUNE ne sera jamais atteint
#   => Correction : elif temperature > 37.5 or douleur > 6
#
# ERREUR 3 (cas defaut) : 'elif:' n'existe pas en Python
#   => SyntaxError : elif requiert une condition
#   => Correction : 'else:'
#
# ERREUR 4 (print) : '{Niveau}' — N majuscule => NameError
#   => Python est sensible a la casse : 'niveau' != 'Niveau'
#   => Correction : '{niveau}'

# Code corrige :
temperature_test = 38.0
spo2_test = 96.0
tension_test = 145
douleur_test = 4

# ERREUR 1 corrigee : or au lieu de and
if temperature_test > 39.5 or spo2_test < 90 or tension_test > 180:
    niveau = 'ROUGE'
# ERREUR 2 corrigee : conditions JAUNE differentes de ORANGE
elif temperature_test > 38.5 or spo2_test < 94 or tension_test > 140:
    niveau = 'ORANGE'
elif temperature_test > 37.5 or douleur_test > 6:
    niveau = 'JAUNE'
# ERREUR 3 corrigee : else au lieu de elif:
else:
    niveau = 'VERT'

# ERREUR 4 corrigee : {niveau} minuscule
print(f'  Test tension=145 mmHg => Niveau de triage : {niveau}')
print('  (Attendu : ORANGE — tension > 140 avec or)')
print('=' * 62)
