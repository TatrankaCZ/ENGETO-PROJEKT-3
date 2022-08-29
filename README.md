# Engeto projekt 3

# Třetí projekt pro online kurz ENGETO

## Popis

Extrahování výsledků z voleb v roce 2017. odkaz k prohlédnutí [zde](https://volby.cz/pls/ps2017nss/ps?xjazyk=CZ).

## Instalace knihoven

Knihovny, které jsou použity v kódu jsou v `requirements.txt`.

Doporučují použít virtuální prostředí a instalovat knihovny následovně:

`$ pip install -r requirements.txt # instaluje knihovny`

## Spuštění projektu

`python3 "jméno skriptu.py" "<url na stránku>" "<Jméno výstupového souboru>"`

## Ukázka projektu

# Výsledky hlasování pro okres Benešov:

1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101`
2. argument: `vysledky_benesov.csv`

## Spuštění programu:

`python3 "jméno skriptu.py" "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" "vysledky_benesov.csv"`

# Průběh stahování:

```
Working...  

DONE
```

# Částečný výstup:

```
code,location,registered,envelopes,valid...
529303, Benešov, 13104, 8485, 8437, 1052, 10,...
532568, Bernartice, 191, 148, 148, 4, 0,...
...
```
