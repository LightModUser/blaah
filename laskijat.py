from typing import List, Union


class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.

    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, *args: Union[int, float]) -> Union[int, float]:
        """Palauttaa annettujen lukujen summan.

        :param args: summan luvut
        :type args: Union[int, float]
        :return: lukujen summa
        :rtype: Union[int, float]
        """
        return sum(args)

    def kerro(self, *args: Union[int, float]) -> Union[int, float]:
        """Palauttaa annettujen lukujen tulon.

        :param args: tulon luvut
        :type args: Union[int, float]
        :return: lukujen tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in args:
            tulo *= luku
        return tulo


class MonenLaskija(Laskija):
    """Luokka, joka toteuttaa monen luvun summan ja tulon.

    Perii luokan Laskija.

    Julkiset metodit:
        summaa(*Union[int, float])
        kerro(*Union[int, float])
    """

    pass


def argumenttien_tulostaja(**kwargs):
    """Tulostaa annetut avainsana-argumentit.

    :param kwargs: tulostettavat avainsana-argumentit
    :type kwargs: dict
    """
    for k, n in kwargs.items():
        print(f'Argumentin "{k}" arvo on {n}.')


### Seuraavat rivit tekevät tarkistustulostukset. Älä koske niihin.

laskija = Laskija()
monenlaskija = MonenLaskija()

print(laskija.summaa(11, 31))
print(laskija.kerro(3, 12))
print()
print(monenlaskija.summaa(1, 2, 3, 4, 5))
print(monenlaskija.kerro(1, 2, 3, 4, 5))
print()
print(monenlaskija.summaa(1, 2, 3, 4, 5, 6, 7))
print(monenlaskija.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')