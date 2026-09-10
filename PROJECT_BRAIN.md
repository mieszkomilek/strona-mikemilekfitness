# PROJECT_BRAIN — MikeMilekFitness
## Cel i zakres
Migracja mikemilekfitness.com z Shopify do mieszkomilek/strona-mikemilekfitness. Pierwszy etap: samodzielna strona główna, oryginalne media, wspólny link PayPal, GitHub Pages i dokumentacja dla AI.
Użytkownik wskazał repo strona-ewamilek wyłącznie jako wzór organizacji i źródło istniejącego linku PayPal. Kod, treści i obrazy tego repo nie zostały przeniesione.

## Źródła i wygląd
Odczyt Shopify oraz publicznej strony: 2026-09-09. Czarne tło, biała typografia Archivo Narrow, logo, szerokie zdjęcie Mike’a, opis „Czym się wyróżniam ?”, siedem kart oferty, film i stopka.
Treść opisu i misji zaktualizowana w wersji 1.01 na polecenie użytkownika. Ceny oraz kolejność ofert odpowiadają źródłu z dnia odczytu; nie są synchronizowane na żywo.

## Struktura
`templates/index.html` — układ strony; `data/home.json` — treść; `data/catalog.json` — oferta; `site.config.json` — domeny, płatność, SEO; `styles.css`, `mobile-home.css`, `assets/js/core.js` — wygląd i menu.
`index.html` jest generowany, lecz przechowywany w repo dla łatwego podglądu. `scripts/site_build.py` składa stronę i `_site/`; `scripts/site_qa.py` kontroluje wynik. Repo ma tę samą zasadę rozdzielenia danych, kodu i dokumentacji co wzorzec, bez zbędnych modułów numerologii, paneli i podstron Ewy.

## Media
Shopify Files: 17 obrazów i 7 ExternalVideo; wszystkie obrazy pobrane. Dodatkowo miniatura produktu widoczna w HTML i 4 fonty WOFF2. Łącznie 22 pliki z sumami SHA-256, 11 067 190 bajtów. Oryginały zachowane, bez rekompresji. Plik OFL fontu znajduje się obok fontów.
Filmy są hostowane na YouTube: zapisano 7 odnośników z Shopify i 1 film strony głównej w data/external-videos.json. To nie są pobrane pliki wideo. Shopify nie zawierał plików Video ani GenericFile w zwróconej bibliotece. Nie archiwizowano aplikacji Digital Downloads ani prywatnych materiałów klientów.
`data/media-manifest.json` mapuje źródła na lokalne nazwy, rozmiary i SHA-256. `scripts/import_media.py` odtwarza tylko brakujące pliki i nie akceptuje zmienionych źródeł.

## Płatności
Zgodnie z poleceniem użytkownika wszystkie 21 odnośników sprzedażowych kieruje do https://www.paypal.com/ncp/payment/7JL9X24RW64Q8 — linku odczytanego z index.html repo strona-ewamilek.
Nie utworzono ani nie zmieniono zasobów PayPal. Nie sprawdzono transakcji ani zgodności kwoty i produktu w checkout. Wspólny link nie przekazuje wyboru produktu, wariantu ani ceny i nie zapewnia automatycznej dostawy e-booków. Przed uruchomieniem właściwej sprzedaży ustalić docelowe płatności per oferta.

## Hosting i SEO
Podgląd: https://mieszkomilek.github.io/strona-mikemilekfitness/. Produkcja pozostaje https://mikemilekfitness.com/ na Shopify. Brak CNAME i zmian DNS.
Podgląd ma noindex,follow i pustą sitemap, aby nie konkurować z działającym Shopify. Robots umożliwia odczyt noindex. Zmiana indeksowania i domeny wyłącznie w świadomym etapie przełączenia.
Workflow pages.yml uruchamia się przy push main lub ręcznie, importuje brakujące media według manifestu, zapisuje je w repo, buduje, sprawdza i publikuje wyłącznie _site/. Kolejne zwykłe wdrożenia korzystają już z lokalnych plików. Nie tworzyć jednorazowych workflowów.

## Różnice funkcjonalne względem Shopify
Nie przeniesiono koszyka, logowania klientów i wyszukiwarki sklepowej. Sprzedaż zastąpiono PayPal. Newsletter wymaga odrębnej usługi — nie publikujemy niedziałającego formularza. Nie przenosimy odliczania promocji WEGANSNOW, bo jego ważność i obsługa w PayPal nie zostały potwierdzone.
Kontakt, Partnerzy i polityki prowadzą tymczasowo do dotychczasowej domeny. Do przeniesienia w następnym etapie przed wyłączeniem Shopify.
Wersja 1.00 odtwarza podstawowy układ i treść; nie wykonano porównania piksel po pikselu ani testu płatności.

## Wersje i kolejne sesje
Wersje aktualizowane jawnie w version.txt i VERSION_HISTORY.md. Po zmianie generuj ponownie stronę. Raportuj numer i wynik kontroli. Nie importować historii wersji Ewy. Zapisuj każdą trwałą decyzję tutaj.

## Stan przekazania
Dostęp do zapisu GitHub został przywrócony. Wersja 1.00 przygotowana do pierwszego wdrożenia; lokalny build i QA przeszły poprawnie. Użytkownik potwierdził ustawienie GitHub Actions w Pages.

## Decyzje wersji 1.04
Newsletter został usunięty z zakresu. Kontakt odbywa się wyłącznie przez `mieszkomilek@gmail.com`; nie migrujemy formularza kontaktowego. Wszystkie linki płatności nadal kierują do PayPal. Strony `kontakt.html` i `partnerzy.html` zostały dodane jako kolejny etap migracji, przed dalszymi podstronami ofertowymi. Decyzje te są częścią Second Brain i muszą pozostać aktualne przy kolejnych zmianach.

## Decyzje wersji 1.05
Dodano lokalne `warunki.html` i `zwroty.html`; stopka nie prowadzi już do Shopify. Treść jest roboczym przeniesieniem zasad odczytanych z Shopify i wymaga sprawdzenia prawnego przed uruchomieniem docelowej sprzedaży. Kontakt pozostaje wyłącznie mailowy, a płatności pozostają w PayPal.

## Branding od wersji 1.01
Główna marka to MikeMilekFitness, zamiast Wegański Trener. Nowy tekstowy logotyp i favicon M; oryginalne pliki mediów pozostają zachowane. Weganizm przedstawiamy jako wyrazistą ciekawostkę osobistą w limonkowym bloku pod hero. Użytkownik podał: 40 lat, wegetarianizm od 2017, weganizm od 2018 i nadal świetna forma. Wiek jest deklaracją na dzień 2026-09-09, nie obliczamy daty urodzenia ani nie aktualizujemy go automatycznie. Opisy produktów roślinnych i oryginalne okładki pozostają zgodne z ich zawartością. Wszystkie płatności pozostają bez zmian. Wersja 1.00 została pomyślnie opublikowana na Pages.

## Decyzje wersji 1.06
Kontakt: WhatsApp +48 606 708 185, e-mail, Instagram i Facebook. Formularza nie ma. Dodano oferta.html z PayPal.

## Decyzje wersji 1.07
Link Kontakt w nagłówku prowadzi do `kontakt.html`. Dodano lokalne `prywatnosc.html` i `wysylka.html`; kontakt i płatności pozostają bez zmian.

## Decyzje wersji 1.08
Każda z siedmiu ofert ma własną podstronę opartą na handle produktu. Karty na stronie głównej prowadzą do szczegółów, a osobny przycisk prowadzi do wspólnego PayPal. Opisy są celowo ogólne do czasu potwierdzenia pełnych treści i dostawy cyfrowej.

## Decyzje i audyt wersji 1.09 — 2026-09-10
- Przed SEO technicznym wykonano ponowny odczyt siedmiu produktów przez Shopify search_products/get_product. Źródło: data/offer-source-2026-09-10.json, bez danych klientów i stanów magazynowych.
- Wersja 1.08 nie była pełną migracją opisów: zawierała identyczny tekst zastępczy i niepotwierdzone „Wariant ustalany indywidualnie”. Usunięto oba; przywrócono pełne opisy i 29 wariantów z cenami. Ceny początkowe były zgodne.
- Treść opisów pozostaje identyczna po usunięciu znaczników edytora i normalizacji odstępów; jedyna zmiana słowna w opisach: Wegański Trener → MikeMilekFitness w karcie prezentowej, zgodnie z dyspozycją użytkownika. Nazwy i ceny wariantów zachowane, również nietypowe 35 zł dla treningu ciężary + cardio. Nie korygować ich na podstawie domysłów.
- FAQ i indywidualne metadane SEO są redakcyjnymi skrótami potwierdzonych opisów i wariantów; nie dodano terminów realizacji, gwarancji wyników ani automatycznej dostawy. Materiały ebook/video to opisy sprzedawanych produktów; prywatnych plików nie publikujemy.
- Główna: opis i misję skrócono do faktów z oryginału; osobista historia wieku i weganizmu pochodzi od użytkownika. Nagłówek ofert „Najczęściej kupowane w tym tygodniu” zastąpiono neutralnym, ponieważ statyczny katalog nie korzysta z tygodniowych statystyk.
- Ikony SVG Instagram/Facebook/e-mail w nagłówku i stopce są osadzone lokalnie, z tekstem dostępnym dla czytników. Kontakt w stopce prowadzi do kontakt.html; osobny e-mail pozostaje mailto.
- Wspólny PayPal pozostaje bez zmian. Strony jawnie wyjaśniają brak przekazywania wariantu/kwoty i odsyłają do kontaktu przed płatnością.
- oferta.html jest generowana jako pełny katalog i trafia do _site, co naprawia niedziałający link z ofert.
- Podgląd nadal noindex; bez zmiany domeny, DNS, mapy indeksowania i bez rozpoczęcia punktu 3. Testy weryfikują wszystkie lokalne linki i zgodność opisów ze snapshotem.
- Raport porównawczy: CONTENT_AUDIT.md. Audyt treści w tym etapie dotyczy strony głównej i siedmiu ofert, nie potwierdza zgodności stron prawnych ani Partnerów.
