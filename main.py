class Calculettefactice():
    def __init__(self):
        pass
    def exposant(self,nb,expo):
        """
        calcule n^expo
        """
    def multiplication(self,nb1,nb2):
        """
        calcule nb1*nb2
        """
    def division(self,quotient, diviseur):
        """
        calcule quotient/diviseur
        """
    def fibonnacci(self,nb):
        """
        fonction fibonacci
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
            return "Error"
        res=0
        for i in range(nb+1):
            res=Calculs.multiplication(res,i)
        return res