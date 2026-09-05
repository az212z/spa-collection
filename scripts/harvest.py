import urllib.request,re,json,concurrent.futures,pathlib
sources={
'ri':'ri-spa-ry-sb-riyadh-ri-spa-ry-sb-dy7imz1t',
'tarfah':'tarfah-spa-trfh-sb-jeddah-slwn-trfh-sb-helmi-koutbi-street-jeddah-23521-saudi-arabia-q1iznhzr',
'makrama':'slwn-hmm-mkrm-makrama-salon-spa-jeddah-slwn-hmm-mkrm-lnsyy-jd-elffpq1r',
'flaire':'flaire-spa-lryd-flaire-spa-hy-sj8nsilo',
'wthn':'wthn-spa-riyadh-wthn-spa-w2fxr8hg',
'basecoat':'base-coat-nail-spa-jeddah-3940-al-rawdhah-rbwufloi',
'glowday':'glow-day-riyadh-prince-turki-ibn-abdulaziz-al-awwal-rd-al-aqiq-riyadh-13515-hrvkwiub',
'bannanah':'bannanah-spa-bnn-sb-riyadh-prince-nasir-bin-saud-bin-farhan-al-saud-street-eyhb383g',
'cote':'cote-nail-spa-kwt-sb-riyadh-8782-uthman-ibn-affan-rd-yi93aygh'}
pathlib.Path('research/sources.json').write_text(json.dumps(sources,indent=2))
def fetch(p):
 n,s=p;url='https://www.fresha.com/a/'+s
 try:
  raw=urllib.request.urlopen(url,timeout=40).read().decode();pathlib.Path('research/'+n+'.html').write_text(raw)
  d=json.loads(re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',raw).group(1))['props']['pageProps']['data']['location']
  pathlib.Path('research/'+n+'.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
  return n,d['name'],d['contactNumber'],d['owner']['onlineLinks'],len(d['galleryModalDesktopLargeImages']),len(d['services'])
 except Exception as e:return n,str(e)
for r in concurrent.futures.ThreadPoolExecutor(max_workers=5).map(fetch,sources.items()): print(r)
