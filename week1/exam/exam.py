from utils import unzip_with_7z
import string
from itertools import product

zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

#Déclaration de l'alphabet parce que flemme
alphabet = list(string.ascii_lowercase)

def testCode(leCodeDeuxLettres):
    secret_password = leCodeDeuxLettres + 'bcmpda'
    unzip_with_7z(zip_file_path, dest_path, secret_password)
    return


def brutForceCode():
    for lettre in product(alphabet, repeat=2):
        combinaison = ''.join(lettre) + 'bcmpda'
        if unzip_with_7z(zip_file_path, dest_path, combinaison):
            print(f"✔ Succès avec le mot de passe : {combinaison}bcmpda")
            return    

brutForceCode()