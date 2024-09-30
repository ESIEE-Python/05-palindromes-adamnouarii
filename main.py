"""
Module verifiant si une chaine de caractères est un palindrome

"""
def ispalindrome(p):
    """
    Verifie si une chaine de caractères est un palindrome

    Args : une chaine de caractère p

    Returns : Booléen
    """
    p=p.replace(" ","").lower()
    if p == p[::-1]:
        return True
    return False
def main():
    """
    appel à la fonction secondaire ispalindrome
    """
    p = 'Adz'
    a = 'DED'
    print(ispalindrome(p))
    print(ispalindrome(a))
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
