"""Render offers from a dated, read-only source snapshot, with explicit branding edits."""
from html import escape
from html.parser import HTMLParser
from decimal import Decimal
import json

class Description(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in {'p', 'ul', 'ol', 'li', 'strong', 'em', 'br'}:
            self.parts.append('<' + tag + '>')
    def handle_endtag(self, tag):
        if tag in {'p', 'ul', 'ol', 'li', 'strong', 'em'}:
            self.parts.append('</' + tag + '>')
    def handle_data(self, data):
        self.parts.append(escape(data))

def description_html(raw):
    parser = Description()
    parser.feed(raw)
    return ''.join(parser.parts).replace('Wegański Trener', 'MikeMilekFitness')

def money(value):
    return f'{Decimal(value):.2f}'.replace('.', ',') + ' zł'

def render_offers(root, config, catalog, version, cards):
    source = json.loads((root/'data/offer-source-2026-09-10.json').read_text())
    original = {p['id']: p for p in source['products']}
    editorial = json.loads((root/'data/offer-editorial.json').read_text())
    template = (root/'templates/offer.html').read_text()
    for p in catalog:
        s = original[p['id']]
        e = editorial[p['handle']]
        variants = ''.join('<tr><th scope="row">' + escape(v['title'] if v['title'] != 'Default Title' else 'E-book') + '</th><td>' + money(v['price']) + '</td></tr>' for v in s['variants'])
        related = ''.join('<li><a href="' + escape(handle) + '.html">' + escape(next(x['title'] for x in catalog if x['handle'] == handle)) + '</a></li>' for handle in e['related'])
        faq = ''.join('<details><summary>' + escape(q) + '</summary><p>' + escape(a) + '</p></details>' for q, a in e['faq'])
        values = {
            'TITLE': p['title'], 'SEO_TITLE': e['title'] + ' | MikeMilekFitness',
            'DESCRIPTION': e['description'], 'URL': config['baseUrl'] + p['handle'] + '.html',
            'ROBOTS': 'index,follow' if config['indexingEnabled'] else 'noindex,follow',
            'IMAGE': p['image'], 'OG_IMAGE': config['baseUrl'] + p['image'], 'VERSION': version,
            'PRICE': ('Od ' if p['priceFrom'] else '') + money(p['price']),
            'PAYPAL': config['paypalUrl']
        }
        page = template
        for key, value in values.items():
            page = page.replace('{{'+key+'}}', escape(value, quote=True))
        for key, value in {'BODY': description_html(s['descriptionHtml']), 'VARIANTS': variants, 'FAQ': faq, 'RELATED': related}.items():
            page = page.replace('{{'+key+'}}', value)
        assert '{{' not in page
        (root/(p['handle']+'.html')).write_text(page)
    listing = template.split('<body>')[0].replace('{{SEO_TITLE}}', 'Oferta | MikeMilekFitness').replace('{{DESCRIPTION}}', 'Plany diety i treningu, e-booki, konsultacje online, trening personalny i karta prezentowa MikeMilekFitness.').replace('{{URL}}', config['baseUrl']+'oferta.html').replace('{{OG_IMAGE}}', config['baseUrl']+catalog[0]['image']).replace('{{ROBOTS}}', 'index,follow' if config['indexingEnabled'] else 'noindex,follow').replace('{{VERSION}}', version)
    listing += '<body><main class="page-width simple-page"><nav aria-label="Nawigacja"><a href="./">MikeMilekFitness</a> · <a href="kontakt.html">Kontakt</a></nav><h1>Oferta MikeMilekFitness</h1><div class="product-grid">' + '\n'.join(cards) + '</div></main></body></html>'
    (root/'oferta.html').write_text(listing)
