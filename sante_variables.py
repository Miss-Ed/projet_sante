# ============================================================ 
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy 
# Ce fichier centralise toutes les constantes et variables metier 
# Il sera enrichi chaque semaine jusqu'a S24 
# ============================================================ 
 
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ======== 
TAUX_EUR_FCFA = 655.957 
TAUX_USD_FCFA = 600.0 
SEUIL_OMS_DENSITE_MEDICALE = 2.3    # medecins pour 1000 habitants 
SEUIL_OMS_COUVERTURE_VACCIN = 95.0  # pourcentage minimum OMS 
SEUIL_MORTALITE_ALERTE = 2.0        # % deces / hospitalisations 
SEUIL_RUPTURE_STOCK_JOURS = 30      # jours minimum de stock 
DEPARTEMENTS_CONGO = [              # 12 departements officiels 
    'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette', 
    'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala', 
    'Niari', 'Plateaux', 'Pool', 'Sangha' 
] 
SEUIL_OMS_COUVERTURE_VACCIN    = 95.0   # % objectif OMS
SEUIL_OMS_ZONE_A_RISQUE        = 80.0   # %
SEUIL_OMS_ZONE_CRITIQUE        = 50.0   # %
SEUIL_OCCUPATION_CRITIQUE      = 95.0   # % saturation lits
SEUIL_OCCUPATION_ELEVE         = 85.0   # %
SEUIL_OCCUPATION_OPTIMAL       = 70.0   # %
COUT_COMMANDE_EXPRESS_FCFA     = 450000 # FCFA par commande urgente

# === SECTION B : VARIABLES DES 5 HOPITAUX =================== 

# Hopital 1 — CHU de Brazzaville 
h1_nom              = 'CHU de Brazzaville' 
h1_ville            = 'Brazzaville' 
h1_departement      = 'Brazzaville' 
h1_type             = 'CHU' 
h1_nb_lits          = 320 
h1_nb_lits_occupes  = 284 
h1_nb_medecins      = 47 
h1_nb_infirmiers    = 123 
h1_population_zone  = 1_800_000 

h2_nom              = 'Hopital General Pointe-Noire' 
h2_ville            = 'Pointe-Noire' 
h2_departement      = 'Pointe-Noire' 
h2_type             = '' 
h2_nb_lits          = 180 
h2_nb_lits_occupes  = 143 
h2_nb_medecins      = 22
h2_nb_infirmiers    = 0
h2_population_zone  = 0

h3_nom              = 'Hopital de Dolisie' 
h3_ville            = 'Dolisie' 
h3_departement      = 'Niari' 
h3_type             = '' 
h3_nb_lits          = 95 
h3_nb_lits_occupes  = 91
h3_nb_medecins      = 8
h3_nb_infirmiers    = 0 
h3_population_zone  = 0

h4_nom              = 'Hopital de district Owando' 
h4_ville            = 'Owando' 
h4_departement      = '' 
h4_type             = '' 
h4_nb_lits          = 45 
h4_nb_lits_occupes  = 32
h4_nb_medecins      = 3
h4_nb_infirmiers    = 0 
h4_population_zone  = 0

h5_nom              = 'Centre de sante de Impfondo' 
h5_ville            = 'Impfondo' 
h5_departement      = '' 
h5_type             = '' 
h5_nb_lits          = 20 
h5_nb_lits_occupes  = 19
h5_nb_medecins      = 1
h5_nb_infirmiers    = 0 
h5_population_zone  = 0

 
# TODO : Declarer les 5 medicaments essentiels 
m1_nom='artemether-lumefantrine'
m1_qte_dispo=0
m1_seuil_rupture=0
m1_cout_unitaire=0

m2_nom='amoxicilline'
m2_qte_dispo=0
m2_seuil_rupture=0
m2_cout_unitaire=0

m3_nom='paracetamol'
m3_qte_dispo=0
m3_seuil_rupture=0
m3_cout_unitaire=0

m4_nom='SRO'
m4_qte_dispo=0
m4_seuil_rupture=0
m4_cout_unitaire=0

m5_nom='vaccin_antipaludeen'
m5_qte_dispo=0
m5_seuil_rupture=0
m5_cout_unitaire=0

# TODO : Calculer les KPIs globaux initiaux 
h1_taux_occ = round((h1_nb_lits_occupes / h1_nb_lits) * 100, 1)
h2_taux_occ = round((h2_nb_lits_occupes / h2_nb_lits) * 100, 1)
h3_taux_occ = round((h3_nb_lits_occupes / h3_nb_lits) * 100, 1)
h4_taux_occ = round((h4_nb_lits_occupes / h4_nb_lits) * 100, 1)
h5_taux_occ = round((h5_nb_lits_occupes / h5_nb_lits) * 100, 1)
total_lits     = h1_nb_lits + h2_nb_lits + h3_nb_lits + h4_nb_lits + h5_nb_lits
total_occupes  = h1_nb_lits_occupes + h2_nb_lits_occupes + h3_nb_lits_occupes + h4_nb_lits_occupes + h5_nb_lits_occupes
taux_national  = round((total_occupes / total_lits) * 100, 1)


# TODO : Afficher le rapport initial du systeme de sante
print('=' * 60)
print('  RAPPORT INITIAL — MODULE SANTE_VARIABLES')
print('  Semaine 2 — Variables & KPIs')
print('=' * 60)
print(f'  Total lits national : {total_lits}')
print(f'  Lits occupes        : {total_occupes}')
print(f'  Taux d\'occupation   : {taux_national}%')
print('=' * 60)

# Classification statut stocks (S3 NOUVEAU)
# Regle PNA Congo : du plus restrictif au plus large

# Medicament 1
if m1_qte_dispo <= m1_seuil_rupture:
    m1_statut = 'RUPTURE CRITIQUE'; m1_couleur = '[ROUGE]'
elif m1_qte_dispo <= m1_seuil_rupture * 1.5:
    m1_statut = 'ALERTE STOCK'; m1_couleur = '[ORANGE]'
elif m1_qte_dispo <= m1_seuil_rupture * 2.0:
    m1_statut = 'STOCK LIMITE'; m1_couleur = '[JAUNE]'
else:
    m1_statut = 'STOCK NORMAL'; m1_couleur = '[VERT]'

# Medicament 2
if m2_qte_dispo <= m2_seuil_rupture:
    m2_statut = 'RUPTURE CRITIQUE'; m2_couleur = '[ROUGE]'
elif m2_qte_dispo <= m2_seuil_rupture * 1.5:
    m2_statut = 'ALERTE STOCK'; m2_couleur = '[ORANGE]'
elif m2_qte_dispo <= m2_seuil_rupture * 2.0:
    m2_statut = 'STOCK LIMITE'; m2_couleur = '[JAUNE]'
else:
    m2_statut = 'STOCK NORMAL'; m2_couleur = '[VERT]'

# Medicament 3
if m3_qte_dispo <= m3_seuil_rupture:
    m3_statut = 'RUPTURE CRITIQUE'; m3_couleur = '[ROUGE]'
elif m3_qte_dispo <= m3_seuil_rupture * 1.5:
    m3_statut = 'ALERTE STOCK'; m3_couleur = '[ORANGE]'
elif m3_qte_dispo <= m3_seuil_rupture * 2.0:
    m3_statut = 'STOCK LIMITE'; m3_couleur = '[JAUNE]'
else:
    m3_statut = 'STOCK NORMAL'; m3_couleur = '[VERT]'

# Medicament 4
if m4_qte_dispo <= m4_seuil_rupture:
    m4_statut = 'RUPTURE CRITIQUE'; m4_couleur = '[ROUGE]'
elif m4_qte_dispo <= m4_seuil_rupture * 1.5:
    m4_statut = 'ALERTE STOCK'; m4_couleur = '[ORANGE]'
elif m4_qte_dispo <= m4_seuil_rupture * 2.0:
    m4_statut = 'STOCK LIMITE'; m4_couleur = '[JAUNE]'
else:
    m4_statut = 'STOCK NORMAL'; m4_couleur = '[VERT]'

# Medicament 5
if m5_qte_dispo <= m5_seuil_rupture:
    m5_statut = 'RUPTURE CRITIQUE'; m5_couleur = '[ROUGE]'
elif m5_qte_dispo <= m5_seuil_rupture * 1.5:
    m5_statut = 'ALERTE STOCK'; m5_couleur = '[ORANGE]'
elif m5_qte_dispo <= m5_seuil_rupture * 2.0:
    m5_statut = 'STOCK LIMITE'; m5_couleur = '[JAUNE]'
else:
    m5_statut = 'STOCK NORMAL'; m5_couleur = '[VERT]'

# Comptage alertes medicaments
nb_ruptures = 0
nb_alertes_stock = 0
for statut in [m1_statut, m2_statut, m3_statut, m4_statut, m5_statut]:
    if statut == 'RUPTURE CRITIQUE':
        nb_ruptures = nb_ruptures + 1
    elif statut == 'ALERTE STOCK':
        nb_alertes_stock = nb_alertes_stock + 1


# Classification occupation hopitaux (S3 NOUVEAU)
# Regle DSS : taux d'occupation par niveau


# Hopital 1
if h1_taux_occ > SEUIL_OCCUPATION_CRITIQUE:
    h1_niv_occ = 'ALERTE CRITIQUE'; h1_label = '[CRI]'
elif h1_taux_occ > SEUIL_OCCUPATION_ELEVE:
    h1_niv_occ = 'ALERTE ELEVEE'; h1_label = '[ALT]'
elif h1_taux_occ > SEUIL_OCCUPATION_OPTIMAL:
    h1_niv_occ = 'SITUATION OPTIMALE'; h1_label = '[OK ]'
else:
    h1_niv_occ = 'SOUS-UTILISATION'; h1_label = '[SOU]'

# Hopital 2
if h2_taux_occ > SEUIL_OCCUPATION_CRITIQUE:
    h2_niv_occ = 'ALERTE CRITIQUE'; h2_label = '[CRI]'
elif h2_taux_occ > SEUIL_OCCUPATION_ELEVE:
    h2_niv_occ = 'ALERTE ELEVEE'; h2_label = '[ALT]'
elif h2_taux_occ > SEUIL_OCCUPATION_OPTIMAL:
    h2_niv_occ = 'SITUATION OPTIMALE'; h2_label = '[OK ]'
else:
    h2_niv_occ = 'SOUS-UTILISATION'; h2_label = '[SOU]'

# Hopital 3
if h3_taux_occ > SEUIL_OCCUPATION_CRITIQUE:
    h3_niv_occ = 'ALERTE CRITIQUE'; h3_label = '[CRI]'
elif h3_taux_occ > SEUIL_OCCUPATION_ELEVE:
    h3_niv_occ = 'ALERTE ELEVEE'; h3_label = '[ALT]'
elif h3_taux_occ > SEUIL_OCCUPATION_OPTIMAL:
    h3_niv_occ = 'SITUATION OPTIMALE'; h3_label = '[OK ]'
else:
    h3_niv_occ = 'SOUS-UTILISATION'; h3_label = '[SOU]'

# Hopital 4
if h4_taux_occ > SEUIL_OCCUPATION_CRITIQUE:
    h4_niv_occ = 'ALERTE CRITIQUE'; h4_label = '[CRI]'
elif h4_taux_occ > SEUIL_OCCUPATION_ELEVE:
    h4_niv_occ = 'ALERTE ELEVEE'; h4_label = '[ALT]'
elif h4_taux_occ > SEUIL_OCCUPATION_OPTIMAL:
    h4_niv_occ = 'SITUATION OPTIMALE'; h4_label = '[OK ]'
else:
    h4_niv_occ = 'SOUS-UTILISATION'; h4_label = '[SOU]'

# Hopital 5
if h5_taux_occ > SEUIL_OCCUPATION_CRITIQUE:
    h5_niv_occ = 'ALERTE CRITIQUE'; h5_label = '[CRI]'
elif h5_taux_occ > SEUIL_OCCUPATION_ELEVE:
    h5_niv_occ = 'ALERTE ELEVEE'; h5_label = '[ALT]'
elif h5_taux_occ > SEUIL_OCCUPATION_OPTIMAL:
    h5_niv_occ = 'SITUATION OPTIMALE'; h5_label = '[OK ]'
else:
    h5_niv_occ = 'SOUS-UTILISATION'; h5_label = '[SOU]'

# Comptage hopitaux en saturation
nb_hopitaux_saturation = 0
for niv in [h1_niv_occ, h2_niv_occ, h3_niv_occ, h4_niv_occ, h5_niv_occ]:
    if niv == 'ALERTE CRITIQUE':
        nb_hopitaux_saturation = nb_hopitaux_saturation + 1
        