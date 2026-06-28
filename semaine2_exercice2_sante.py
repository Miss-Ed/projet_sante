# ============================================================ 
# AKIENI ACADEMY — Projet Sante Publique 
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS 
# ============================================================ 
 
# --- DONNEES BRUTES --- 
budget_fcfa = 87_450_000   # underscore pour lisibilite des grands nombres 
nb_consultations_ext = 4823
nb_hospitalisations = 1247
nb_deces = 18
nb_lits_total = 180
nb_lits_occupes = 143
nb_medecins = 22
nb_infirmiers = 58
population_dept = 128_000
taux_eur_fcfa = 655.957
taux_usd_fcfa = 600.0
 
# --- A COMPLETER --- 
# 1. Conversions devises 
budget_eur = round(budget_fcfa / taux_eur_fcfa, 2)
budget_usd = round(budget_fcfa / taux_usd_fcfa, 2)
 
# 2. Indicateurs OMS 
densite_medicale = round((nb_medecins / population_dept) * 1000, 2)
taux_mortalite = round((nb_deces / nb_hospitalisations) * 100, 2)
taux_occupation = round((nb_lits_occupes / nb_lits_total) * 100, 2)

# 3. Division entiere et modulo 
budget_medicaments = int(budget_fcfa * 0.35)
cout_journalier_meds = 450_000 
jours_stock = budget_medicaments // cout_journalier_meds   # division entiere // 
jours_restants = budget_medicaments % cout_journalier_meds  # modulo % 
 
# 4. Puissance pour projection 
budget_n_plus_2 = round(budget_fcfa * (1.08 ** 2), 2)
 
# --- AFFICHAGE RAPPORT --- 
print(f'=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===') 
print()
print("BUDGET")
print(f"  Dépenses Q4        : {budget_fcfa:,.0f} FCFA".replace(",", " "))
print(f"  En euros           : {budget_eur:,.2f} EUR".replace(",", " "))
print(f"  En dollars         : {budget_usd:,.2f} USD".replace(",", " "))

print()

print("INDICATEURS OMS")
print(f"  Densité médicale   : {densite_medicale} médecins / 1000 hab")
print(f"  Taux mortalité     : {taux_mortalite}%")
print(f"  Taux occupation    : {taux_occupation}%")

print()

print("ANALYSE PHARMACIE")
print(f"  Budget médicaments : {budget_medicaments:,.0f} FCFA".replace(",", " "))
print(f"  Jours de stock     : {jours_stock} jours")
print(f"  Jours dépassement  : {jours_restants} jours")

print()

print("ANALYSE CONSULTATIONS")

if nb_consultations_ext % 2 == 0:
    print("  Nombre de consultations : PAIR")
else:
    print("  Nombre de consultations : IMPAIR")

print()

print("PROJECTION")
print(f"  Budget N+2 (8%/an) : {budget_n_plus_2:,.2f} FCFA".replace(",", " "))

print()
# ... completez l'affichage

# ANALYSE OMS
if densite_medicale >= 2.3:
    print("ALERTE : Densité médicale conforme aux normes OMS.")
else:
    print(f"ALERTE : Densité médicale CRITIQUE ({densite_medicale} pour 1000 hab — norme OMS : 2.3)")

if taux_mortalite > 2:
    print("ALERTE : Taux de mortalité élevé.")
else:
    print("Taux de mortalité acceptable.")

if 70 <= taux_occupation <= 85:
    print("Taux d'occupation optimal.")
else:
    print("Taux d'occupation hors norme.")

print("=" * 65)