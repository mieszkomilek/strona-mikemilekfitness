# Audyt treści — 2026-09-10

Porównano wersję GitHub 1.08 (b42d9eba60dac18f7c8c4ab6dceb170640f01b56) z bieżącymi opisami siedmiu produktów pobranymi przez Shopify get_product oraz stroną główną https://mikemilekfitness.com/.
Źródłowy snapshot produktów: data/offer-source-2026-09-10.json. Żaden zapis w Shopify nie został wykonany.

## Wynik przed poprawką

Wszystkie siedem podstron zawierało nieźródłowy tekst „Oferta dopasowana do Twojego celu i poziomu” oraz „Wariant ustalany indywidualnie”. Nie były wierną migracją. Wszystkie ceny początkowe były zgodne z Shopify.

| Oferta | Braki w 1.08 uzupełnione w 1.09 | Warianty |
| --- | --- | --- |
| Wegańskie przepisy | Cały opis: ponad 30 przepisów, około 400 kcal na posiłek, makroskładniki, wskazówki | 1: 35 zł |
| Plan diety | Miesiąc, ponad 30 posiłków do wyboru, kontakt po zamówieniu i lista potrzebnych informacji | 2: po 125 zł |
| Karta prezentowa | Ważność 6 miesięcy | 6: 10, 25, 50, 100, 200, 400 zł |
| Konsultacje i prowadzenie online | Dieta, trening, monitorowanie postępów i zakres konsultacji telefonicznej | 4: 440, 620, 80, 125 zł |
| Autorskie ćwiczenia | Ponad 100 stron na partię, 4 zdjęcia, opis, QR do wideo, dostawa e-mailem | 8: wszystkie 135 zł, pojedyncza partia 35 zł |
| Trening personalny | Oryginalny opis jest jedynie nazwą produktu; lokalizacja i czas wynikają z wariantów | 4: 1 h za 125 zł lub 5 × 1 h za 530 zł, kobiety/mężczyźni, Poznań |
| Plan treningowy | Miesiąc, 4 zdjęcia ćwiczenia z ciężarami, fachowy opis i QR do wideo | 4: trzy po 125 zł, ciężary + cardio 35 zł |

## Zasady zgodności

- Pełne opisy renderowane automatycznie ze snapshotu; usunięte tylko znaczniki edytora, bez dopisywania oferty.
- Zmiana marki Wegański Trener → MikeMilekFitness w tytule i opisie karty to świadoma dyspozycja użytkownika.
- E-book z jednym domyślnym wariantem ma czytelną etykietę „E-book” zamiast technicznego „Default Title”.
- Nazwy, kolejność i ceny pozostałych wariantów są zachowane. Nietypowa cena 35 zł w planie treningowym istnieje w źródle — nie poprawiamy jej samodzielnie.
- Każdy produkt ma jedno zdjęcie w odpowiedzi get_product; wszystkie siedem zdjęć już znajduje się lokalnie. Wideo opisane jako zawartość produktu nie jest publicznym plikiem do przeniesienia.
- FAQ i metadane są skrótami faktów z opisów i wariantów. Nie stanowią tekstu identycznego słowo w słowo z Shopify.
- Strona główna: doświadczenie ponad 10 lat, dieta roślinna, trening i współpraca online/bezpośrednio są w oryginale. Nowa marka oraz 40 lat / 2017 / 2018 pochodzą z dyspozycji użytkownika. Usunięto niezweryfikowaną sugestię bieżącego rankingu tygodniowego.
- PayPal, brak newslettera, kontakt e-mail/WhatsApp i brak koszyka są zatwierdzonymi różnicami funkcjonalnymi.
- Wspólny PayPal nie przenosi produktu, wariantu ani kwoty. Nie wprowadzono automatycznej dostawy ani nowej integracji płatności.

## Walidacja i granice

scripts/offer_qa.py porównuje pełne teksty opisów ze snapshotem po normalizacji białych znaków i dopuszczonej zmianie marki, sprawdza warianty, metadane, lokalne linki i ikony.
To potwierdza zgodność z odczytem z 2026-09-10, a nie stałą synchronizację z Shopify.
Punkt 3 (SEO techniczne, przełączenie indeksowania) nie został rozpoczęty. Podgląd pozostaje noindex.
Strony prawne i Partnerzy nie były przedmiotem tego audytu. Ich wcześniejsze robocze treści wymagają osobnego porównania przed uznaniem całej migracji za zakończoną.
