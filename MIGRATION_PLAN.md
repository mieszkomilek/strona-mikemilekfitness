# Plan migracji
## Etap 1 — fundament i pierwsza strona
- [x] Odczyt struktury repo wzorcowego, bez kopiowania jego kodu i treści.
- [x] Inwentaryzacja Shopify Files oraz obrazów i fontów strony głównej.
- [x] Pobranie 22 plików i zapis źródeł, rozmiarów oraz SHA-256.
- [x] Zapis odnośników do 8 filmów YouTube.
- [x] Osobne dane treści i siedmiu ofert, szablon, CSS i menu mobilne.
- [x] Wszystkie CTA oferty zastąpione wskazanym wspólnym linkiem PayPal.
- [x] Dokumentacja AI, wersjonowanie, build i QA.
- [x] Workflow GitHub Pages; ustawienie Source: GitHub Actions użytkownik potwierdził.
- [x] Przywrócony dostęp do zapisu GitHub; przygotowany import plików.
- [ ] Potwierdzenie pierwszego zdalnego deploymentu i dostępności adresu Pages.

## Etap 2 — dopracowanie strony głównej
1. Porównać wygląd z Shopify na telefonie i komputerze: kadrowanie hero, odstępy, font, karty, stopka.
2. Zweryfikować aktualność opisów, cen i nagłówka „Najczęściej kupowane w tym tygodniu” (to zachowany tekst, nie raport analityczny).
3. Dodać zoptymalizowane warianty obrazów i srcset, zachowując wszystkie oryginały.
4. Ustalić usługę newslettera i ewentualną prawdziwą promocję.

## Etap 3 — pełne odejście od Shopify
1. Przenieść Kontakt, Partnerzy, polityki i ewentualne szczegóły ofert.
2. Zastąpić wspólny link PayPal płatnościami dopasowanymi do oferty, wariantów i dostawy produktów cyfrowych, jeśli użytkownik to zleci.
3. Sprawdzić proces sprzedaży; płatny zakup testowy wymaga osobnego polecenia.
4. Przygotować mapę przekierowań starych URL (GitHub Pages nie obsługuje dowolnych przekierowań serwerowych).
5. Po akceptacji przełączyć domenę, canonical, sitemap i indeksowanie; zweryfikować HTTPS.
6. Shopify wyłączyć dopiero po sprawdzeniu treści, sprzedaży i przekierowań.
