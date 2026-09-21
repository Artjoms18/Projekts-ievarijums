receptes_numurs=int(input("Ievadiets receptes numuru:\n1) 1 kg ābolu = 300 gr. cukura\n2) 1 kg ābolu = 500 gr.cukura\n"))

cukura_cena= float(input("Ievadi cukura cenu:"))
aboli_kg= float(input("Ievadi, cik ābolu tev ir(kg): "))
if receptes_numurs==1:
    izmaksa= cukurs_uz_kg*0.3
else:
    izmaksa= cukurs_uz_kg*0.5


print(f"Par cukuru tu samaksāsi {cukura_cena*aboli_kg*0.7} eiro ")
