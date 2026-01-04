from kalkulator import oldal_ellenorzes

def test_github_online():
    # A 200-as kód jelenti, hogy az oldal él és virul
    assert oldal_ellenorzes("https://github.com") == 200

def test_hibas_oldal():
    # Egy nem létező oldalra None-t vagy hibát kell kapnunk
    assert oldal_ellenorzes("https://ez-az-oldal-biztosan-nem-letezik.hu") is None
