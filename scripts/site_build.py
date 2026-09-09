"""Generate the homepage and a public-only Pages artifact."""
from pathlib import Path
from html import escape
import json,shutil
R=Path(__file__).resolve().parents[1]
def build():
 c=json.loads((R/'site.config.json').read_text());h=json.loads((R/'data/home.json').read_text());catalog=json.loads((R/'data/catalog.json').read_text());v=(R/'version.txt').read_text().strip();cards=[]
 for p in catalog:
  t=escape(p['title']);u=escape(c['paypalUrl']);price=('Od ' if p['priceFrom'] else '')+f"{float(p['price']):.2f}".replace('.',',')+' zł PLN'
  cards.append(f'<article class="product-card"><a class="product-image" data-sales-link href="{u}" aria-label="{t} — płatność PayPal"><img src="{escape(p["image"])}" width="600" height="600" loading="lazy" alt="{t}"></a><h3><a data-sales-link href="{u}">{t}</a></h3><p class="price">{price}</p><a class="buy" data-sales-link href="{u}" aria-label="{t} — przejdź do PayPal">Przejdź do PayPal</a></article>')
 values={'BASE_URL':c['baseUrl'],'EMAIL':c['email'],'VERSION':v,'ROBOTS':'index,follow' if c['indexingEnabled'] else 'noindex,follow','TITLE':h['title'],'SUBTITLE':h['subtitle'],'INTRO_HEADING':h['introHeading'],'OFFERS_HEADING':h['offersHeading'],'MISSION':h['mission'],'VIDEO_URL':h['videoUrl']}
 page=(R/'templates/index.html').read_text()
 for k,val in values.items():page=page.replace('{{'+k+'}}',escape(val,quote=True))
 page=page.replace('{{INTRO_HTML}}',h['introHtml']).replace('{{PRODUCTS}}','\n'.join(cards));assert '{{' not in page
 (R/'index.html').write_text(page)
 (R/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+c['baseUrl']+'sitemap.xml\n')
 urls='<url><loc>'+escape(c['baseUrl'])+'</loc></url>' if c['indexingEnabled'] else ''
 (R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>\n')
 (R/'version.js').write_text('window.SITE_VERSION = '+json.dumps(v)+';\n')
 dest=R/'_site'
 if dest.exists():shutil.rmtree(dest)
 dest.mkdir()
 for name in ['index.html','styles.css','mobile-home.css','robots.txt','sitemap.xml','manifest.webmanifest','version.txt','.nojekyll']:shutil.copy2(R/name,dest/name)
 shutil.copytree(R/'assets',dest/'assets')
 print(f'Built version {v}: {len(catalog)} offers')
if __name__=='__main__':build()
