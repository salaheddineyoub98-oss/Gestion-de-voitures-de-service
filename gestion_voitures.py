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
    def affecterVoiture(self, voiture):
        if self.voitureService is None and voiture.chauffeur is None:
        self.voitureService = voiture
        voiture.chauffeur = self
    else:
        print("Impossible d'affecter la voiture")
    def retirerVoiture(self):
        if self.voitureService is not None:
        self.voitureService.chauffeur = None
        self.voitureService = None
class Voiture:
    def __init__(self,matricule,annee,marque,kilomtrage):
        self.matricule=matricule
        self.annee=annee
        self.marque=marque
        self.kilomtrage=kilomtrage
        self.chauffeur=None
    def affichierInformation(self):
        print('matricule : ',self.matricule)
        print('annee : ',self.annee)
        print('marque : ',self.marque)
        print('kiloetrage : ',self.kilomtrage)
        if self.chauffeur is None:
            print('pas de chauffeur ')
        else:
            print('chaffeure ',self.chauffeur.nom)
e1 = Employe("S111", "salaheddine", "youb")
e2 = Employe("S112", "Manar", "Derar")

v1 = Voiture("M7111", 2026, "Toyota", 1500)
v2 = Voiture("M123", 2026, "Honda", 3000)