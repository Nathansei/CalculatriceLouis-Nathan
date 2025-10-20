import math
class Calculettefactice():
    def __init__(self):
        pass
    def exposant(self,nb,expo):
        """
        calcule n^expo
        """
    def multiplication(self,nb1,nb2):
        """
        multpilication entiere
        """
    def division(self,quotient, diviseur):
        """
        calcule quotient/diviseur et reste
        """
    def factorielle(self,nb):
        """
        Calcule nb!
        """
    def fibonnacci(self,nb):
        """
        fonction fibonacci
        """
    def exp_e(self, x):
        """
        Approxime e^x à 0.001 pres
        """
    def multiplication_flottant(self, nb1, nb2):
        """
        Vraie fonction multiplication réutilisant la multiplicaiton entière
        """
    def division_precise(self, nb1, nb2, precision_chiffres=4):
        """
        Approximation division à precision chiffres apres la virgule
        """


class Calculs(Calculettefactice):
    def __init__(self):
        pass
    def multiplication(self,nb1,nb2):
        if nb1 == 0 or nb2 == 0:
            return 0
        signe_negatif = (nb1 < 0) ^ (nb2 < 0)
        a = abs(nb1)
        b = abs(nb2)
        if a > b:
            a, b = b, a
        resultat = 0
        for _ in range(b):
            resultat += a
        if signe_negatif:
            return -resultat
        else:
            return resultat
    def division(self,dividende, diviseur):
        if diviseur==0:
            return "Error"
        test=(dividende < 0) ^ (diviseur < 0)
        dividende_abs = abs(dividende)
        diviseur_abs = abs(diviseur)

        quotient = 0
        while dividende_abs >= diviseur_abs:
            dividende_abs -= diviseur_abs
            quotient += 1
        reste = dividende_abs
        if dividende < 0 and reste != 0:
            reste = dividende_abs + diviseur_abs
            if (dividende < 0) and (diviseur > 0):
                reste = diviseur - reste
            elif (dividende < 0) and (diviseur < 0):
                reste = -reste
        if test:
            return (-quotient,reste)
        else:
            return(quotient,reste)
    def factorielle(self,nb):
        if nb<0:
            raise ValueError("factorielle: nb doit etre >=0")
        res=1
        for i in range(1,nb+1):
            res=Calculs.multiplication(self,res,i)
        return res
    def fibo(self,n):
        if n <= 1:
            return n
        return Calculs.fibo(self,n - 1) + Calculs.fibo(self,n - 2)
    def exposant(self,nb,expo):
        if not isinstance(expo,int):
            raise ValueError("exposant: un exposant doit etre un entier")
        if expo < 0:
            return Calculs.division_precise(self,1,Calculs.exposant(self,nb,-expo))
        res = 1
        for _ in range(expo):
            res = res * nb
        return res
    def exp_e(self, x):
        if x==0:
            return 1
        n = 0
        terme = 1.0
        somme = 0.0
        while abs(terme) >= 0.001:
            somme += terme
            n += 1
            terme = Calculs.division_precise(self,Calculs.exposant(self,x, int(n)), Calculs.factorielle(self,n))
        return round(somme, 3)
    def multiplication_flottant(self, nb1, nb2):
        if nb1==0 or nb2==0:
            return 0
        test_signe = (nb1 < 0) ^ (nb2 < 0)

        str_nb1 = str(abs(nb1))
        str_nb2 = str(abs(nb2))

        if '.' in str_nb1:
            part_ent_1, part_dec_1 = str_nb1.split('.')
            nb_dec_1 = len(part_dec_1)
        else:
            part_ent_1 = str_nb1
            part_dec_1 = ""
            nb_dec_1 = 0
        if '.' in str_nb2:
            part_ent_2, part_dec_2 = str_nb2.split('.')
            nb_dec_2 = len(part_dec_2)
        else:
            part_ent_2 = str_nb2
            part_dec_2 = ""
            nb_dec_2 = 0
        total_dec = nb_dec_1 + nb_dec_2

        entier_1 = int(part_ent_1 + part_dec_1)
        entier_2 = int(part_ent_2 + part_dec_2)

        res_entier = Calculs.multiplication(self,entier_1, entier_2)

        res_str = str(res_entier)

        while len(res_str) <= total_dec:
            res_str = "0" + res_str

        if total_dec > 0:
            pos_virgule = len(res_str) - total_dec
            res_final_str = res_str[:pos_virgule] + '.' + res_str[pos_virgule:]
        else:
            res_final_str = res_str

        res_float = float(res_final_str)

        if test_signe:
            return -res_float
        else:
            return res_float
    def division_precise(self, nb1, nb2, precision_chiffres=4):
        if nb2 == 0:
            raise ValueError("Error: Division par zéro")
        test_signe = (nb1 < 0) ^ (nb2 < 0)

        nb1_abs = abs(nb1)
        nb2_abs = abs(nb2)

        str_nb1 = str(nb1_abs)
        str_nb2 = str(nb2_abs)

        if '.' in str_nb1:
            part_ent_1, part_dec_1 = str_nb1.split('.')
            nb_dec_1 = len(part_dec_1)
        else:
            part_ent_1 = str_nb1
            part_dec_1 = ""
            nb_dec_1 = 0

        if '.' in str_nb2:
            part_ent_2, part_dec_2 = str_nb2.split('.')
            nb_dec_2 = len(part_dec_2)
        else:
            part_ent_2 = str_nb2
            part_dec_2 = ""
            nb_dec_2 = 0

        entier_1 = int(part_ent_1 + part_dec_1)
        entier_2 = int(part_ent_2 + part_dec_2)

        diff_dec = nb_dec_1 - nb_dec_2

        if diff_dec > 0:
            puissance_dix = self.exposant(10, diff_dec)
            dividende_entier = entier_1
            diviseur_entier = self.multiplication(entier_2, puissance_dix)
        elif diff_dec < 0:
            puissance_dix = self.exposant(10, abs(diff_dec))
            dividende_entier = self.multiplication(entier_1, puissance_dix)
            diviseur_entier = entier_2
        else:
            dividende_entier = entier_1
            diviseur_entier = entier_2

        part_ent_res, reste = self.division(dividende_entier, diviseur_entier)

        part_dec_res = ""

        for _ in range(precision_chiffres):
            reste_x_10 = self.multiplication(reste, 10)

            chiffre_dec, reste_nouveau = self.division(reste_x_10, diviseur_entier)

            part_dec_res += str(chiffre_dec)
            reste = reste_nouveau

            if reste == 0:
                part_dec_res += "0" * (precision_chiffres - len(part_dec_res))
                break

        res_str = str(part_ent_res) + "." + part_dec_res
        res_final = float(res_str)

        if test_signe:
            return -res_final
        else:
            return res_final

def test():
    print("🚀 Lancement de la batterie de tests pour la classe Calculs 🚀")

    # --- Test 1: multiplication (par additions) ---
    print("\n" + "="*30)
    print("1. Tests pour 'multiplication'")
    print(f"   5 * 3   = {c.multiplication(5, 3)}   (Attendu: 15)")
    print(f"   5 * -3  = {c.multiplication(5, -3)}  (Attendu: -15)")
    print(f"  -5 * 3   = {c.multiplication(-5, 3)}  (Attendu: -15)")
    print(f"  -5 * -3  = {c.multiplication(-5, -3)} (Attendu: 15)")
    print(f"   5 * 0   = {c.multiplication(5, 0)}   (Attendu: 0)")
    print(f"   0 * 5   = {c.multiplication(0, 5)}   (Attendu: 0)")
    print(f"   1 * 5   = {c.multiplication(1, 5)}   (Attendu: 5)")
    print(f"   5 * 1   = {c.multiplication(5, 1)}   (Attendu: 5)")

    # --- Test 2: division (entière) ---
    print("\n" + "="*30)
    print("2. Tests pour 'division' (quotient, reste)")
    print(f"   10 / 3   = {c.division(10, 3)}   (Attendu: (3, 1))")
    print(f"   10 / 2   = {c.division(10, 2)}   (Attendu: (5, 0))")
    print(f"  -10 / 3   = {c.division(-10, 3)}  (Attendu (selon ta logique): (-3, -1))")
    print(f"   10 / -3  = {c.division(10, -3)}  (Attendu (selon ta logique): (-3, 1))")
    print(f"  -10 / -3  = {c.division(-10, -3)} (Attendu (selon ta logique): (3, -1))")
    print(f"    7 / 8   = {c.division(7, 8)}   (Attendu: (0, 7))")
    print(f"   10 / 0   = {c.division(10, 0)} (Attendu: 'Error: Division par zéro')")

    # --- Test 3: factorielle ---
    print("\n" + "="*30)
    print("3. Tests pour 'factorielle'")
    print(f"   5! = {c.factorielle(5)} (Attendu: 120)")
    print(f"   0! = {c.factorielle(0)} (Attendu: 1)")
    print(f"   1! = {c.factorielle(1)} (Attendu: 1)")
    try:
        c.factorielle(-5)
    except ValueError as e:
        print(f"  -5! = {e} (Attendu: ValueError)")

    # --- Test 4: fibo ---
    print("\n" + "="*30)
    print("4. Tests pour 'fibo'")
    print(f"   fibo(0) = {c.fibo(0)} (Attendu: 0)")
    print(f"   fibo(1) = {c.fibo(1)} (Attendu: 1)")
    print(f"   fibo(2) = {c.fibo(2)} (Attendu: 1)")
    print(f"   fibo(7) = {c.fibo(7)} (Attendu: 13)")
    print(f"  fibo(10) = {c.fibo(10)} (Attendu: 55)")
    try:
        c.fibo(-1)
    except ValueError as e:
        print(f"  fibo(-1) = {e} (Attendu: ValueError)")

    # --- Test 5: exposant ---
    print("\n" + "="*30)
    print("5. Tests pour 'exposant'")
    print(f"   2^3  = {c.exposant(2, 3)}  (Attendu: 8)")
    print(f"   5^0  = {c.exposant(5, 0)}  (Attendu: 1)")
    print(f"   0^5  = {c.exposant(0, 5)}  (Attendu: 0)")
    print(f"   1^5  = {c.exposant(1, 5)}  (Attendu: 1)")
    print(f"   5^1  = {c.exposant(5, 1)}  (Attendu: 5)")
    print(f"  -2^3  = {c.exposant(-2, 3)} (Attendu: -8)")
    print(f"  -2^2  = {c.exposant(-2, 2)} (Attendu: 4)")
    try:
        c.exposant(2, -1)
    except ValueError as e:
        print(f"  2^-1  = {e} (Attendu: ValueError)")

    # --- Test 6: exp_e ---
    print("\n" + "="*30)
    print("6. Tests pour 'exp_e' (Approximation)")
    print(f"   e^0 = {c.exp_e(0)} (Vérification math.exp(0): {math.exp(0)})")
    print(f"   e^1 = {c.exp_e(1)} (Vérification math.exp(1): {math.exp(1)})")
    print(f"   e^2 = {c.exp_e(2)} (Vérification math.exp(2): {math.exp(2)})")
    print(f"  e^-1 = {c.exp_e(-1)} (Vérification math.exp(-1): {math.exp(-1)})")

    # --- Test 7: multiplication_flottant ---
    print("\n" + "="*30)
    print("7. Tests pour 'multiplication_flottant'")
    print(f"   1.23 * 4.5  = {c.multiplication_flottant(1.23, 4.5)} (Attendu: 5.535)")
    print(f"   0.1 * 0.1   = {c.multiplication_flottant(0.1, 0.1)} (Attendu: 0.01)")
    print(f"   -2.5 * 10.0 = {c.multiplication_flottant(-2.5, 10.0)} (Attendu: -25.0)")
    print(f"   10.0 * -2.5 = {c.multiplication_flottant(10.0, -2.5)} (Attendu: -25.0)")
    print(f"   -2.5 * -2.5 = {c.multiplication_flottant(-2.5, -2.5)} (Attendu: 6.25)")
    print(f"   10 * 0.5    = {c.multiplication_flottant(10, 0.5)} (Attendu: 5.0)")
    print(f"   1.23 * 0    = {c.multiplication_flottant(1.23, 0)} (Attendu: 0.0)")

    # --- Test 8: division_precise ---
    print("\n" + "="*30)
    print("8. Tests pour 'division_precise' (précision 4)")
    print(f"   10 / 3      = {c.division_precise(10, 3)}      (Vérification: ~3.3333)")
    print(f"   1 / 8       = {c.division_precise(1, 8)}       (Attendu: 0.1250)")
    print(f"   -7 / 4      = {c.division_precise(-7, 4)}      (Attendu: -1.7500)")
    print(f"   7 / -4      = {c.division_precise(7, -4)}      (Attendu: -1.7500)")
    print(f"   -7 / -4     = {c.division_precise(-7, -4)}     (Attendu: 1.7500)")
    print(f"   1.23 / 4.5  = {c.division_precise(1.23, 4.5)}  (Vérification: ~0.2733)")
    print(f"   5 / 2.5     = {c.division_precise(5, 2.5)}     (Attendu: 2.0000)")
    print(f"   1 / 1000    = {c.division_precise(1, 1000)}    (Attendu: 0.0010)")

    print("\n" + "="*30)
    print("🏁 Tests terminés. 🏁")


c = Calculs()
test()