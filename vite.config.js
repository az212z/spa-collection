import {defineConfig} from 'vite';
import react from '@vitejs/plugin-react';
import {resolve} from 'node:path';
const ids=['ri','cote','wthn','flaire','tarfah','basecoat','glowday','bannanah','relax','nanis'];
export default defineConfig({base:"/spa-collection/",plugins:[react()],build:{rollupOptions:{input:Object.fromEntries(['index',...ids].map(id=>[id,resolve(id==='index'?'index.html':`${id}/index.html`)]))}}});
