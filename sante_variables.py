# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — challenge Entreprise
# Votre nom : ____MARIMPORI MANDAKA Edouarda_________________
# Date      : ____24/06/2026_________________________________
# ============================================================ 


# ============================================================
# HOPITAL 1 : HOPITAL DISTRICT KINKALA
# ============================================================

h1_nom = "Hôpital District Kinkala"
h1_budget = 12_500_000.0
h1_consultations = 1847
h1_hospitalisations = 312
h1_deces = 8
h1_lits_total = 45
h1_lits_occupes = 41
h1_medecins = 3
h1_population = 85000


# ============================================================
# HOPITAL 2 : CMS DE VINDZA
# ============================================================

h2_nom = "CMS de Vindza"
h2_budget = 6_800_000.0
h2_consultations = 923
h2_hospitalisations = 87
h2_deces = 2
h2_lits_total = 20
h2_lits_occupes = 14
h2_medecins = 1
h2_population = 42000


# HOPITAL 3 : HOPITAL DE KINDAMBA

h3_nom = "Hôpital de Kindamba"
h3_budget = 9_200_000.0
h3_consultations = 1234
h3_hospitalisations = 201
h3_deces = 11
h3_lits_total = 35
h3_lits_occupes = 33
h3_medecins = 2
h3_population = 67000


# CALCULS HOPITAL 1

h1_cout_moyen = round(h1_budget / h1_consultations, 2)
h1_taux_occupation = round((h1_lits_occupes / h1_lits_total) * 100, 2)
h1_densite = round((h1_medecins / h1_population) * 1000, 2)
h1_taux_mortalite = round((h1_deces / h1_hospitalisations) * 100, 2)


# CALCULS HOPITAL 2

h2_cout_moyen = round(h2_budget / h2_consultations, 2)
h2_taux_occupation = round((h2_lits_occupes / h2_lits_total) * 100, 2)
h2_densite = round((h2_medecins / h2_population) * 1000, 2)
h2_taux_mortalite = round((h2_deces / h2_hospitalisations) * 100, 2)


# CALCULS HOPITAL 3

h3_cout_moyen = round(h3_budget / h3_consultations, 2)
h3_taux_occupation = round((h3_lits_occupes / h3_lits_total) * 100, 2)
h3_densite = round((h3_medecins / h3_population) * 1000, 2)
h3_taux_mortalite = round((h3_deces / h3_hospitalisations) * 100, 2)


# DETERMINATION DU STATUT

if h1_taux_mortalite > 2 or h1_densite < 0.05:
    h1_statut = "CRITIQUE"
else:
    h1_statut = "NORMAL"

if h2_taux_mortalite > 2 or h2_densite < 0.05:
    h2_statut = "CRITIQUE"
else:
    h2_statut = "NORMAL"

if h3_taux_mortalite > 2 or h3_densite < 0.05:
    h3_statut = "CRITIQUE"
else:
    h3_statut = "NORMAL"


# ============================================================
# RAPPORT
# ============================================================

print("=" * 70)
print("RAPPORT COMPARATIF DES HOPITAUX DU DEPARTEMENT DU POOL")
print("=" * 70)

print()

print(f"HOPITAL : {h1_nom}")
print(f"Budget trimestriel     : {h1_budget:,.0f} FCFA".replace(",", " "))
print(f"Consultations          : {h1_consultations}")
print(f"Hospitalisations       : {h1_hospitalisations}")
print(f"Décès                  : {h1_deces}")
print(f"Coût moyen/patient     : {h1_cout_moyen:.2f} FCFA")
print(f"Taux occupation        : {h1_taux_occupation}%")
print(f"Densité médicale       : {h1_densite} médecin(s)/1000 hab")
print(f"Taux mortalité         : {h1_taux_mortalite}%")
print(f"STATUT                 : {h1_statut}")

print("-" * 70)

print(f"HOPITAL : {h2_nom}")
print(f"Budget trimestriel     : {h2_budget:,.0f} FCFA".replace(",", " "))
print(f"Consultations          : {h2_consultations}")
print(f"Hospitalisations       : {h2_hospitalisations}")
print(f"Décès                  : {h2_deces}")
print(f"Coût moyen/patient     : {h2_cout_moyen:.2f} FCFA")
print(f"Taux occupation        : {h2_taux_occupation}%")
print(f"Densité médicale       : {h2_densite} médecin(s)/1000 hab")
print(f"Taux mortalité         : {h2_taux_mortalite}%")
print(f"STATUT                 : {h2_statut}")

print("-" * 70)

print(f"HOPITAL : {h3_nom}")
print(f"Budget trimestriel     : {h3_budget:,.0f} FCFA".replace(",", " "))
print(f"Consultations          : {h3_consultations}")
print(f"Hospitalisations       : {h3_hospitalisations}")
print(f"Décès                  : {h3_deces}")
print(f"Coût moyen/patient     : {h3_cout_moyen:.2f} FCFA")
print(f"Taux occupation        : {h3_taux_occupation}%")
print(f"Densité médicale       : {h3_densite} médecin(s)/1000 hab")
print(f"Taux mortalité         : {h3_taux_mortalite}%")
print(f"STATUT                 : {h3_statut}")

print("=" * 70)

# BONUS

budget_total = h1_budget + h2_budget + h3_budget

cout_medecin = 1_200_000

medecins_actuels = h1_medecins + h2_medecins + h3_medecins
medecins_souhaites = 5 * 3

medecins_a_recruter = medecins_souhaites - medecins_actuels

cout_recrutement = medecins_a_recruter * cout_medecin

print()
print("BONUS")
print("-" * 70)

print(f"Budget total disponible : {budget_total:,.0f} FCFA".replace(",", " "))
print(f"Médecins actuels        : {medecins_actuels}")
print(f"Médecins souhaités      : {medecins_souhaites}")
print(f"Médecins à recruter     : {medecins_a_recruter}")
print(f"Coût recrutement        : {cout_recrutement:,.0f} FCFA".replace(",", " "))

if budget_total >= cout_recrutement:
    print("RESULTAT : Le budget est suffisant pour recruter les médecins.")
else:
    print("RESULTAT : Le budget est insuffisant pour recruter les médecins.")

print("=" * 70)