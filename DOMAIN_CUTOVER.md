# Przełączenie domeny — stan 2026-09-10

## Aktualny operator DNS

Panel zarządzania domeną `mikemilekfitness.com` znajduje się w Shopify (Sklep „Wegański Trener” → Domeny → Ustawienia DNS). Shopify nadal zarządza strefą DNS i serwerami nazw, mimo że rekordy strony zostały przełączone na GitHub Pages. Rekordy pocztowe pozostają w tej samej strefie Shopify.

## Stan odczytany z DNS

- NS: ns-cloud-c1/c2/c3/c4.googledomains.com (infrastruktura widoczna przy zarządzaniu przez Shopify).
- A @: 185.199.108.153 (ustawione w Shopify; pozostałe adresy A GitHub Pages mogą być dodane zgodnie z polityką operatora).
- AAAA @: brak na zrzucie po zmianie (nie dodawano bez potwierdzenia formularza Shopify).
- CNAME www: mieszkomilek.github.io (ustawione w Shopify).
- MX @: 1 mx.mikemilekfitness.com.cust.b.hostedemail.com.
- TXT SPF @: v=spf1 include:_spf.hostedemail.com ~all.

To odczyt rekordów, nie pełny eksport strefy. Przed zapisem zrobić eksport z panelu, w tym DKIM, DMARC, weryfikacje i pozostałe subdomeny. Nie zmieniać NS ani rekordów pocztowych.

## Docelowe rekordy

| Typ | Nazwa | Wartość |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |
| CNAME | www | mieszkomilek.github.io |

Zastępujemy wyłącznie dotychczasowe A/AAAA @ i CNAME www. Nie wpisywać nazwy repozytorium do CNAME.

## Kolejność wykonania

1. Dostęp do panelu DNS i zalogowanego GitHub Settings → Pages. Konektor GitHub udostępnia zapis kodu, ale nie ma narzędzia ustawiania custom domain.
2. Zabezpieczyć eksport strefy i dane/materiały potrzebne z Shopify; publiczne kopie źródeł w data/ nie są kopią klientów, zamówień, aplikacji ani płatnych plików.
3. Zweryfikować domenę w ustawieniach konta GitHub, publikując podany przez GitHub rekord TXT. Wartości TXT nie zgadywać.
4. Ustawić Custom domain na mikemilekfitness.com w repo strona-mikemilekfitness, przed zmianą A/AAAA/CNAME.
5. Przełączyć wskazane rekordy DNS, zachowując pocztę.
6. Ustawić baseUrl=https://mikemilekfitness.com/ oraz indexingEnabled=true w site.config.json; wygenerować, sprawdzić i opublikować.
7. Po wystawieniu certyfikatu włączyć Enforce HTTPS. Sprawdzić domenę główną, www, certyfikat, stare adresy produktów/polityk i kontakt.
8. W Google Search Console dodać/zweryfikować domenę i zgłosić https://mikemilekfitness.com/sitemap.xml. Potrzebna zalogowana sesja właściciela.
9. Shopify wygaszać dopiero po testach oraz zabezpieczeniu domeny/poczty i wymaganych prywatnych danych; PayPal jest osobnym późniejszym etapem.

## Zachowanie starych adresów

Generator tworzy fizyczne strony pod starymi ścieżkami z natychmiastowym meta refresh, linkiem i canonical do nowego adresu. To nie jest przekierowanie HTTP 301; GitHub Pages nie zapewnia własnych reguł 301 dla dowolnych ścieżek. Mapa znajduje się w data/redirect-map.json. Pełne 301 wymagają dodatkowej warstwy obsługi HTTP — DNS A/CNAME nie przekierowuje ścieżek URL.

## Powrót w razie problemu

Przywrócić zapisane A/AAAA/CNAME, usunąć custom domain z Pages i przywrócić konfigurację podglądu baseUrl + noindex. Zachować działający sklep do czasu weryfikacji przełączenia.

Źródło rekordów i kolejności: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site (odczyt 2026-09-10).
Przy publikacji z GitHub Actions plik CNAME w repo nie ustawia custom domain — wymagane są ustawienia Pages.
