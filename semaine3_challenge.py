# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 3 — Challenge : Tableau de bord 5 hopitaux
# Notions S2 : variables, types, operateurs, f-strings
# Notions S3 : if/elif/else, conditions composees and/or
# ============================================================

# --- DONNEES HOPITAUX (S2 reutilise) ---
h1_nom        = 'CHU Brazzaville'
h1_lits_tot   = 320
h1_lits_occ   = 298
h1_medecins   = 47
h1_ruptures   = 2
h1_alertes    = 2

h2_nom        = 'Hopital Pointe-Noire'
h2_lits_tot   = 180
h2_lits_occ   = 143
h2_medecins   = 22
h2_ruptures   = 0
h2_alertes    = 1

h3_nom        = 'Hopital Dolisie'
h3_lits_tot   = 95
h3_lits_occ   = 91
h3_medecins   = 8
h3_ruptures   = 1
h3_alertes    = 2

h4_nom        = 'Hopital Owando'
h4_lits_tot   = 45
h4_lits_occ   = 32
h4_medecins   = 3
h4_ruptures   = 3
h4_alertes    = 0

h5_nom        = 'CMS Impfondo'
h5_lits_tot   = 20
h5_lits_occ   = 19
h5_medecins   = 1
h5_ruptures   = 2
h5_alertes    = 1


# CALCUL TAUX D'OCCUPATION + CLASSIFICATION


#  HOPITAL 1 : CHU Brazzaville 
h1_taux_occ = (h1_lits_occ / h1_lits_tot) * 100   # 93.1%

if h1_taux_occ > 95:
    h1_niv_occ   = 'ALERTE CRITIQUE'
    h1_label_occ = '[CRI]'
elif h1_taux_occ > 85:
    h1_niv_occ   = 'ALERTE ELEVEE'
    h1_label_occ = '[ALT]'
elif h1_taux_occ > 70:
    h1_niv_occ   = 'SITUATION OPTIMALE'
    h1_label_occ = '[OK ]'
else:
    h1_niv_occ   = 'SOUS-UTILISATION'
    h1_label_occ = '[SOU]'

# Niveau d'alerte global hopital 1
if h1_ruptures >= 2 or h1_taux_occ > 95:
    h1_alerte_global = 'CRITIQUE'
elif h1_ruptures >= 1 or h1_taux_occ > 85 or (h1_alertes >= 2 and h1_medecins < 5):
    h1_alerte_global = 'PREOCCUPANT'
else:
    h1_alerte_global = 'SATISFAISANT'

# HOPITAL 2 : Pointe-Noire 
h2_taux_occ = (h2_lits_occ / h2_lits_tot) * 100   # 79.4%

if h2_taux_occ > 95:
    h2_niv_occ   = 'ALERTE CRITIQUE'
    h2_label_occ = '[CRI]'
elif h2_taux_occ > 85:
    h2_niv_occ   = 'ALERTE ELEVEE'
    h2_label_occ = '[ALT]'
elif h2_taux_occ > 70:
    h2_niv_occ   = 'SITUATION OPTIMALE'
    h2_label_occ = '[OK ]'
else:
    h2_niv_occ   = 'SOUS-UTILISATION'
    h2_label_occ = '[SOU]'

if h2_ruptures >= 2 or h2_taux_occ > 95:
    h2_alerte_global = 'CRITIQUE'
elif h2_ruptures >= 1 or h2_taux_occ > 85 or (h2_alertes >= 2 and h2_medecins < 5):
    h2_alerte_global = 'PREOCCUPANT'
else:
    h2_alerte_global = 'SATISFAISANT'

# HOPITAL 3 : Dolisie 
h3_taux_occ = (h3_lits_occ / h3_lits_tot) * 100   # 95.8%

if h3_taux_occ > 95:
    h3_niv_occ   = 'ALERTE CRITIQUE'
    h3_label_occ = '[CRI]'
elif h3_taux_occ > 85:
    h3_niv_occ   = 'ALERTE ELEVEE'
    h3_label_occ = '[ALT]'
elif h3_taux_occ > 70:
    h3_niv_occ   = 'SITUATION OPTIMALE'
    h3_label_occ = '[OK ]'
else:
    h3_niv_occ   = 'SOUS-UTILISATION'
    h3_label_occ = '[SOU]'

if h3_ruptures >= 2 or h3_taux_occ > 95:
    h3_alerte_global = 'CRITIQUE'
elif h3_ruptures >= 1 or h3_taux_occ > 85 or (h3_alertes >= 2 and h3_medecins < 5):
    h3_alerte_global = 'PREOCCUPANT'
else:
    h3_alerte_global = 'SATISFAISANT'

# HOPITAL 4 : Owando 
h4_taux_occ = (h4_lits_occ / h4_lits_tot) * 100   # 71.1%

if h4_taux_occ > 95:
    h4_niv_occ   = 'ALERTE CRITIQUE'
    h4_label_occ = '[CRI]'
elif h4_taux_occ > 85:
    h4_niv_occ   = 'ALERTE ELEVEE'
    h4_label_occ = '[ALT]'
elif h4_taux_occ > 70:
    h4_niv_occ   = 'SITUATION OPTIMALE'
    h4_label_occ = '[OK ]'
else:
    h4_niv_occ   = 'SOUS-UTILISATION'
    h4_label_occ = '[SOU]'

if h4_ruptures >= 2 or h4_taux_occ > 95:
    h4_alerte_global = 'CRITIQUE'
elif h4_ruptures >= 1 or h4_taux_occ > 85 or (h4_alertes >= 2 and h4_medecins < 5):
    h4_alerte_global = 'PREOCCUPANT'
else:
    h4_alerte_global = 'SATISFAISANT'

#  HOPITAL 5 : CMS Impfondo 
h5_taux_occ = (h5_lits_occ / h5_lits_tot) * 100   # 95.0%

if h5_taux_occ > 95:
    h5_niv_occ   = 'ALERTE CRITIQUE'
    h5_label_occ = '[CRI]'
elif h5_taux_occ > 85:
    h5_niv_occ   = 'ALERTE ELEVEE'
    h5_label_occ = '[ALT]'
elif h5_taux_occ > 70:
    h5_niv_occ   = 'SITUATION OPTIMALE'
    h5_label_occ = '[OK ]'
else:
    h5_niv_occ   = 'SOUS-UTILISATION'
    h5_label_occ = '[SOU]'

if h5_ruptures >= 2 or h5_taux_occ > 95:
    h5_alerte_global = 'CRITIQUE'
elif h5_ruptures >= 1 or h5_taux_occ > 85 or (h5_alertes >= 2 and h5_medecins < 5):
    h5_alerte_global = 'PREOCCUPANT'
else:
    h5_alerte_global = 'SATISFAISANT'

# BILAN NATIONAL

nb_critiques = 0
if h1_alerte_global == 'CRITIQUE':
    nb_critiques = nb_critiques + 1
if h2_alerte_global == 'CRITIQUE':
    nb_critiques = nb_critiques + 1
if h3_alerte_global == 'CRITIQUE':
    nb_critiques = nb_critiques + 1
if h4_alerte_global == 'CRITIQUE':
    nb_critiques = nb_critiques + 1
if h5_alerte_global == 'CRITIQUE':
    nb_critiques = nb_critiques + 1

total_ruptures = h1_ruptures + h2_ruptures + h3_ruptures + h4_ruptures + h5_ruptures

# BONUS : cout estime des commandes urgentes
COUT_COMMANDE_EXPRESS = 450000  # FCFA
cout_total_fcfa = total_ruptures * COUT_COMMANDE_EXPRESS


# AFFICHAGE TABLEAU DE BORD

print('=' * 70)
print('  TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE')
print('  Date : 16 janvier 2026 | Pour le Conseil des Ministres')
print('=' * 70)
print(f'  {"HOPITAL":<25} {"OCCUPATION":<14} {"ALERTES":<12} {"NIVEAU GLOBAL"}')
print('-' * 70)
print(f'  {h1_nom:<25} {h1_taux_occ:.1f}% {h1_label_occ}  {h1_ruptures}R + {h1_alertes}A      [{h1_alerte_global}]')
print(f'  {h2_nom:<25} {h2_taux_occ:.1f}% {h2_label_occ}  {h2_ruptures}R + {h2_alertes}A      [{h2_alerte_global}]')
print(f'  {h3_nom:<25} {h3_taux_occ:.1f}% {h3_label_occ}  {h3_ruptures}R + {h3_alertes}A      [{h3_alerte_global}]')
print(f'  {h4_nom:<25} {h4_taux_occ:.1f}% {h4_label_occ}  {h4_ruptures}R + {h4_alertes}A      [{h4_alerte_global}]')
print(f'  {h5_nom:<25} {h5_taux_occ:.1f}% {h5_label_occ}  {h5_ruptures}R + {h5_alertes}A      [{h5_alerte_global}]')
print('-' * 70)
print(f'  {nb_critiques} hopital(s) sur 5 en situation CRITIQUE')
print(f'  {total_ruptures} ruptures de stock identifiees a l\'echelle nationale')
print(f'  BONUS : Cout estime commandes urgentes : {cout_total_fcfa:,} FCFA'.replace(',', ' '))
if nb_critiques >= 3:
    print('  RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA')
print('=' * 70)
