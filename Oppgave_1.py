# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:18:48 2024

@author: Petter

Exercise 1

Annual fees for owning an electric car vs a petrol car

Kilometer pr år ?? km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

"""
km_pr_aar               = 500
Forsikring_Elbil        = 5000
Forsikring_Bensinbil    = 7500
Trafikkforsikringsavg   = 8.38*365
Forbruk_Elbil           = 0.2*2
Forbruk_Bensinbil       = 1
Bomavgift_Elbil         = 0.1
Bomavgift_Bensinbil     = 0.3
Aarlig_kost_Bensinbil   = km_pr_aar*Forbruk_Bensinbil + km_pr_aar*Bomavgift_Bensinbil + Trafikkforsikringsavg + Forsikring_Bensinbil
Aarlig_kost_Elbil       = km_pr_aar*Forbruk_Elbil + km_pr_aar*Bomavgift_Elbil + Trafikkforsikringsavg + Forsikring_Elbil

print("Aarlig kostnad Bensinbil kr.", km_pr_aar*Forbruk_Bensinbil + km_pr_aar*Bomavgift_Bensinbil + Trafikkforsikringsavg + Forsikring_Bensinbil )

print("Aarlig kostnad Elbil     kr.", km_pr_aar*Forbruk_Elbil + km_pr_aar*Bomavgift_Elbil + Trafikkforsikringsavg + Forsikring_Elbil )

print("Aarlig besbarelse ved å eie elbil kontra bensinbil er kr.", Aarlig_kost_Bensinbil - Aarlig_kost_Elbil )

