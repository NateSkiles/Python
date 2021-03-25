
# Parent Class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = 'Sequence A'
    origin = 'Unknown'
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\n".format(self.name, self.species, self.legs, self.arms)
        return msg



if __name__ == "__main__":

