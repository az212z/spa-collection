import json,pathlib,urllib.request,concurrent.futures,shutil
root=pathlib.Path('public/assets'); root.mkdir(parents=True,exist_ok=True)
manifest=[];tasks=[]
for n in json.load(open('research/sources.json')):
 l=json.load(open('research/'+n+'.json')); (root/n).mkdir(exist_ok=True)
 for i,p in enumerate(l['galleryModalDesktopLargeImages']):tasks.append((n,i,p['url'],p.get('longDescription','')))
 pg=l.get('portfolioGallery')
 if pg: pathlib.Path('research/'+n+'-portfolio.json').write_text(json.dumps(pg,ensure_ascii=False,indent=2))
def fetch(t):
 n,i,url,alt=t; out=root/n/(str(i)+'.jpg')
 try:
  if not out.exists():out.write_bytes(urllib.request.urlopen(url,timeout=35).read())
  return {'brand':n,'path':str(out),'url':url,'description':alt,'source':'https://www.fresha.com/a/'+json.load(open('research/sources.json'))[n]}
 except Exception as e:return {'error':str(e),'brand':n}
manifest=list(concurrent.futures.ThreadPoolExecutor(max_workers=8).map(fetch,tasks))
ig='/var/folders/pj/3shsgp0933x7vw544rf6l7qh0000gn/T/browser-use/assets/5e5970ef-21ab-48f5-aa35-d541c2dc395f/'
(root/'nanis').mkdir(exist_ok=True)
shutil.copy(ig+'manifest.json','research/nanis-instagram-manifest.json')
for i,f in enumerate(['bece998117ea87d2','71e1f17105a25893','aebd78202130a2b7','32d7e4d6df1a47f0','a39ab0cd4c09f96e','d37a5cc87f46e75c']):
 out=root/'nanis'/(str(i)+'.jpg');shutil.copy(ig+f+'.jpg',out);manifest.append({'brand':'nanis','path':str(out),'source':'https://www.instagram.com/nanis.spa.sa/','assetId':f})
shutil.copy(ig+'936c785a1a44801b.jpg',root/'nanis/logo.jpg')
shutil.copy('research/nanis-prices',root/'nanis/menu.pdf')
pathlib.Path('research/asset-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('assets:',len(manifest),'errors:',[m for m in manifest if 'error'in m])
