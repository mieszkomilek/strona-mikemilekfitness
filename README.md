# Wegański Trener — Mike Miłek Fitness
Statyczna wersja strony głównej mikemilekfitness.com, przygotowana dla GitHub Pages.

## Start pracy z AI
1. AGENTS.md — instrukcje pracy.
2. PROJECT_BRAIN.md — cel, decyzje, ograniczenia i stan projektu.
3. WEBSITE_STANDARD.md — struktura i standard techniczny.
4. MIGRATION_PLAN.md — ukończone oraz następne etapy.
5. version.txt i VERSION_HISTORY.md — wersja i historia zmian.

## Lokalnie
Wymagany Python 3.9 lub nowszy. Brak zależności zewnętrznych.
```sh
python3 scripts/import_media.py
python3 scripts/site_build.py
python3 scripts/site_qa.py
python3 -m http.server 8080 --directory _site
```
Otwórz http://localhost:8080/.

## Publikacja
Settings → Pages → Source: GitHub Actions.
Jeden workflow `.github/workflows/pages.yml` weryfikuje media, buduje, sprawdza i publikuje `_site/`.
Podgląd: https://mieszkomilek.github.io/strona-mikemilekfitness/
Domena mikemilekfitness.com pozostaje na Shopify. Nie dodajemy CNAME.
