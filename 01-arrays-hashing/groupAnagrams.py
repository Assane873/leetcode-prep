from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultat = []
        groupes = {}
        for mot in strs:
            # sorted mot renvoie en réalité une liste de la forme : ['lettre1', 'lettre2', 'lettre3']
            cle = "".join(sorted(mot)) # donc on utilise join pour coller les lettres entre elle et former un mot, le séparateur est "" car on ne veut pas d'espace entre les lettres.
            if cle in groupes:
                groupes[cle].append(mot) # si le mot est deja une clé de groupes, on met le mot en tant que valeur (donc dans la liste qui constitue la valeur de chaque clé)
            else:
                groupes[cle] = [] # sinon on crée une liste vide qui sera la valeur de la nouvelle clé
                groupes[cle].append(mot) # on y ajoute ensuite le mot
        resultat = groupes.values() # on veut une list comme type de retour et ".values" renvoie toutes les valeurs d'un dictionnaire   
        return resultat
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))       

