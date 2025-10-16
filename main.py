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
    def division(self,quotient, dividende):
        """
        calcule quotient/dividende
        """
    def fibonnacci(self,nb):
        """
        fonction fibonacci
        """


class Calculs(Calculettefactice):
    def __init__(self):
        pass
    def multiplication(self,nb1,nb2):
        res=0
        test=True
        if (nb1>0 and nb2<0) or (nb1<0 and nb2>0):
            test=False
        if nb1<0:
            nb1=-nb1
        if nb2<0:
            nb2=-nb2
        for i in range(nb1):
            res+=nb2
        if test==False:
            res=-res
        return res

