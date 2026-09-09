"""Restore missing originals from the reviewed, checksum-pinned manifest."""
from pathlib import Path
import hashlib,json,urllib.request,urllib.parse
R=Path(__file__).resolve().parents[1]
def sync():
 assets=json.loads((R/'data/media-manifest.json').read_text())['assets'];restored=0
 for a in assets:
  target=(R/a['path']).resolve();assert target.is_relative_to(R/'assets')
  if target.exists():
   assert hashlib.sha256(target.read_bytes()).hexdigest()==a['sha256'],f'Changed asset: {a["path"]}'
   continue
  url=a['source'];p=urllib.parse.urlsplit(url)
  assert p.scheme=='https' and p.hostname in {'cdn.shopify.com','mikemilekfitness.com'}
  with urllib.request.urlopen(url,timeout=60) as response:data=response.read()
  assert len(data)==a['bytes'] and hashlib.sha256(data).hexdigest()==a['sha256'],f'Source changed: {a["path"]}'
  target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);restored+=1
 print(f'Media verified: {len(assets)}, restored: {restored}')
if __name__=='__main__':sync()
