import json
from pathlib import Path
p=Path('src/data.json');b=json.loads(p.read_text())
copy={
'ri':('وقت للعناية، على راحتكِ.','من الحمام المغربي إلى العناية بالشعر والأظافر؛ اختاري ما يناسب زيارتكِ.','خدمات ري','اختاري موعد زيارتكِ','نلتقي في الملقا'),
'cote':('تفاصيل أظافركِ، بذوقكِ.','مانيكير وبديكير، جل ورموش. اختاري تفاصيل إطلالتكِ من قائمة كوت.','قائمة كوت','موعدكِ في كوت','كوت في النرجس'),
'wthn':('إطلالتكِ، كما تحبينها.','قصّ ولون وعناية بالشعر، مع خدمات الأظافر والرموش في وذن.','اختياراتكِ في وذن','رتّبي زيارتكِ لوذن','عنوان وذن'),
'flaire':('لمسة فلير.','لون جديد لأظافركِ أو جلسة مساج؛ مساحة صغيرة للعناية في يومكِ.','خدمات فلير وأسعارها','احجزي وقتًا لكِ','زورينا في الصحافة'),
'tarfah':('أهلًا بكِ في ترفه.','حمام مغربي وعناية بالشعر والأظافر. تفاصيل الزيارة تبدأ باختياركِ.','قائمة العناية','زيارتكِ القادمة إلى ترفه','ترفه، جدة'),
'basecoat':('لونكِ المفضّل يبدأ هنا.','عناية بالأظافر وطلاء وفن أظافر، في بيس كوت بالروضة.','قائمة الأظافر','اختاري لونكِ وموعدكِ','بيس كوت، الروضة'),
'glowday':('وقفة هادئة في يومكِ.','مساج وحمام مغربي، وعناية بالشعر والبشرة في قلو داي.','العناية في قلو داي','موعد للعناية والراحة','قلو داي في العقيق'),
'bannanah':('عناية قريبة من ذوقكِ.','شعر وأظافر ومساج. اختاري خدمات زيارتكِ من قائمة بنانة.','خدمات بنانة','نرتّب موعدكِ؟','عنوان بنانة'),
'relax':('خذي وقتكِ للراحة.','جلسات مساج للجسم والقدمين، وعناية للسيدات في قرطبة.','جلسات ريلاكس فوت','اختاري جلستكِ','ريلاكس فوت، قرطبة'),
'nanis':('تفاصيل تحبينها في إطلالتكِ.','عناية بالشعر والأظافر وحمام نانيس؛ تصفّحي الخدمات وصور الأعمال.','قائمة نانيس','زيارتكِ إلى نانيس','نانيس في الربيع')}
for x in b:
 x['headline'],x['subhead'],x['servicesTitle'],x['bookingTitle'],x['visitTitle']=copy[x['id']]
p.write_text(json.dumps(b,ensure_ascii=False,indent=2))
p=Path('src/main.jsx');s=p.read_text()
s=s.replace("import brands from './data.json';","import rawBrands from './data.json';\nconst base=import.meta.env.BASE_URL;\nconst local=p=>base+p.replace(/^\\//,'');\nconst brands=rawBrands.map(b=>({...b,images:b.images.map(local),logo:b.logo?local(b.logo):null}));")
s=s.replace("location.pathname.split('/').filter(Boolean)[0]","location.pathname.slice(base.length).split('/').filter(Boolean)[0]")
s=s.replace('href={`/${b.id}/`}','href={local(`${b.id}/`)}').replace('href="/"','href={base}').replace('href="/research.html"','href={local("research.html")}')
s=s.replace('src="/assets/cote/3.jpg"','src={local("assets/cote/3.jpg")}').replace('src="/assets/tarfah/4.jpg"','src={local("assets/tarfah/4.jpg")}').replace("?'/assets/nanis/menu.pdf'","?local('assets/nanis/menu.pdf')")
s=s.replace('لكل مزاج،<br className="mobile-only"/> طقسٌ يناسبه.','{b.servicesTitle}').replace('<h2>موعدكِ مع نفسكِ.</h2>','<h2>{b.bookingTitle}</h2>').replace('<h2>ننتظركِ هنا.</h2>','<h2>{b.visitTitle}</h2>')
s=s.replace('<span className="invite-en" dir="ltr" lang="en">A moment, just for you.</span>','<span className="invite-en" dir="ltr" lang="en">{b.en}</span>')
s=s.replace('تصفّحي الخدمات، اختاري ما تحبين، ثم رتّبي زيارتكِ.','الخدمات والأسعار المنشورة، لتختاري قبل الزيارة.')
s=s.replace('اختاري خدماتكِ ووقتكِ المفضل،<br/>واتركي بقية التفاصيل للمركز.','حددي الخدمات والوقت المناسب لكِ.<br/>المركز يؤكد لكِ التفاصيل والتوفر.')
p.write_text(s)
p=Path('vite.config.js');s=p.read_text().replace('defineConfig({plugins','defineConfig({base:"/spa-collection/",plugins');p.write_text(s)
