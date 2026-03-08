class Employe:
    def __init__(self,numeropermis,nom,prenom):
        self.numeropermis=numeropermis
        self.nom=nom
        self.prenom=prenom
        self.voitureService=None
    def afichierInformation(self):
        print('permis : ',self.numeropermis)
        print('nom : ',self.nom)
        print('prenome : ',self.prenom)
        if self.voitureService is None:
            print(' pas de voiture on service')
        else:
            print('voiture : ',self.voitureService)
class Voiture:
    def __init__(self,matricule,annee,marque,kilomtrage):
        self.matricule=matricule
        self.annee=annee
        self.marque=marque
        self.kilomtrage=kilomtrage
        self,chauffeur=None
    