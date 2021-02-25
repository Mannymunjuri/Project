class Animal: 

    def __init__(self,species,kingdom,phylum,subphylum,order,family):
        self.species = species
        self.kingdom = kingdom
        self.phylum = phylum 
        self.subphylum = subphylum
        self.order = order
        self.family = family
    def getSpecies(self):
        return self.species
    def getKingdom(self):
         return self.kingdom 
    def getPhylum(self):
        return self.phylum
    def getSubphylum(self):
        return self.subphylum
    def getOrder(self):
        return self.order 
    def getFamily(self):
        return self.family
       
animal1= Animal ("Rabbit","Animalia","Chordata","Mammalia","Vertabrata","Leporidae")
animal1.getSpecies()
animal1.getKingdom()
animal1.getPhylum()
animal1.getSubphylum()
animal1.getFamily()
print(animal1.getSpecies())
print(animal1.getKingdom())
print(animal1.getPhylum())
print(animal1.getSubphylum())
print(animal1.getOrder())
print(animal1.getFamily())


