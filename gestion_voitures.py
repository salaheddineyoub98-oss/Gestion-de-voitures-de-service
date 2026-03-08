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
   