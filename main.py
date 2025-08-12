import csv
import os

class DatabazeTelat:
    # cesta k souboru, nastavení hlavičky souboru telata.csv
    def __init__(self, cesta_k_souboru="telata.csv"):
        self.cesta_k_souboru = cesta_k_souboru
        self.hlavicky = ["číslo", "datum_narozeni", "pohlaví", "plemeno", "číslo_matky", "hmotnost"]
        self.data = self.nacti_data()

    # Načte data ze souboru telata.csv, pokud neexistuje tak ho vytvoří
    def nacti_data(self):
        zaznamy = {}
        if not os.path.exists(self.cesta_k_souboru):
            with open(self.cesta_k_souboru, 'w', newline='', encoding='utf-8') as soubor:
                csv.DictWriter(soubor, fieldnames=self.hlavicky).writeheader()
            return zaznamy
        with open(self.cesta_k_souboru, newline='', encoding='utf-8') as soubor:
            for radek in csv.DictReader(soubor):
                zaznamy[radek["číslo"]] = radek
        return zaznamy
    
    # Uloží data do souboru
    def uloz_data(self):
        with open(self.cesta_k_souboru, 'w', newline='', encoding='utf-8') as soubor:
            zapisovac = csv.DictWriter(soubor, fieldnames=self.hlavicky)
            zapisovac.writeheader()
            zapisovac.writerows(self.data.values())

    # přidání nového telete
    def pridej_tele(self):
        cislo = input("Zadejte číslo telete: ")
        if cislo in self.data:
            print("Záznam s tímto číslem již existuje!")
            return      
    # udaje o teleti
        nove_tele = {
            "číslo": cislo,
            "datum_narozeni": input("Datum narození: "),
            "pohlaví": input("Pohlaví: "),
            "plemeno": input("Plemeno: "),
            "číslo_matky": input("Číslo matky: "),
            "hmotnost": input("Hmotnost: ")
        }

        self.data[cislo] = nove_tele
        self.uloz_data()
        os.system("cls")
        print("Záznam přidán.")

    # Upraví záznam o teleti
    def uprav_zaznam(self):
        cislo = input("Zadejte číslo zvířete k úpravě: ")
        if cislo not in self.data:
            print("Záznam nenalezen!")
            return
        print("Ponechte prázdné pro nezměněné hodnoty.")
        for polozka in self.hlavicky[1:]:
            nova_hodnota = input(f"{polozka} ({self.data[cislo][polozka]}): ")
            if nova_hodnota:
                self.data[cislo][polozka] = nova_hodnota

        self.uloz_data()
        os.system("cls")
        print("Záznam aktualizován.")

    # Smazání telete
    def smaz_zaznam(self):
        cislo = input("Zadejte číslo zvířete k odstranění: ")
        if cislo in self.data:
            del self.data[cislo]
            self.uloz_data()
            os.system("cls")
            print("Záznam odstraněn.")
        else:
            print("Záznam nenalezen!")

    # Vypíše celý soubor
    def zobraz_vse(self):
        """Vypíše všechny záznamy."""
        os.system("cls")
        if not self.data:
            print("Databáze je prázdná.")
            return
        
        print(f"{'Číslo':<15}{'Datum narození':<20}{'Pohlaví':<15}{'Plemeno':<20}{'Číslo matky':<15}{'Hmotnost':<10}")
        print("=" * 92)
        for zaznam in self.data.values():
            print(f"{zaznam['číslo']:<15}{zaznam['datum_narozeni']:<20}{zaznam['pohlaví']:<15}{zaznam['plemeno']:<20}{zaznam['číslo_matky']:<15}{zaznam['hmotnost']:<10}")
            print("-" * 92)

    # Detailní výpis telete
    def zobraz_detail(self):
        cislo = input("Zadejte číslo zvířete k zobrazení: ")
        os.system("cls")
        if cislo in self.data:
            zaznam = self.data[cislo]
            # Obrázek kravičky
            print(f'''
            Detailní informace o zvířeti:   
           
            {"=" * 30}        _ (.".) _ 
            {'Číslo':<15}\t{zaznam['číslo']}           '-'/. .\\'-'
            {"-" * 30}         /_   _\     _...._
            {'Datum narození':<15}\t{zaznam['datum_narozeni']}        (` o o `)---`      '.
            {"-" * 30}        /"---"`             \\
            {'Pohlaví':<12}\t{zaznam['pohlaví']}               |            /     ;|
            {"-" * 30}        |           |      ||
            {'Plemeno':<12}\t{zaznam['plemeno']}             \\    \  \  \     /\\\\
            {"-" * 30}          \`;-'| |-.-'-,  \ |)
            {'Číslo matky':<15}\t{zaznam['číslo_matky']}               ( | ( | `-uu ( |
            {"-" * 30}            ||  ||    || ||
            {'Hmotnost':<12}\t{zaznam['hmotnost']} kg                /_( /_(   /_(/_(
            ''')
        else:
            print("Záznam nenalezen!")

# Hlavní smyčka programu
databaze = DatabazeTelat()
while True:
    print("Databáze telat")
    print("1. Přidat nové tele")
    print("2. Upravit záznam")
    print("3. Odebrat záznam")
    print("4. Zobrazit detail záznamu")
    print("5. Zobrazit všechny záznamy")
    print("6. Ukončit")

    volba = input("Vyberte možnost: ")

    if volba == "1":
        databaze.pridej_tele()
    elif volba == "2":
        databaze.uprav_zaznam()
    elif volba == "3":
        databaze.smaz_zaznam()
    elif volba == "4":
        databaze.zobraz_detail()
    elif volba == "5":
        databaze.zobraz_vse()
    elif volba == "6":
        os.system("cls")
        print("Program ukončen. Změny byly uloženy.")
        break
    else:

        print("Neplatná volba, zkuste to znovu.")
