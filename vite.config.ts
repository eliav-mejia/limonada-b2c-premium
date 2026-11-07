import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';
import { readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const raiz = fileURLToPath(new URL('.', import.meta.url));
const FUERA = new Set(['node_modules', 'dist', 'public', 'src', 'tests', 'tools', 'workers', '_interno', '.git', '.github']);

// Una entrada por página HTML (portada, marcas/<id>/, ayuda/<slug>/…): lo que genere tools/paginas.py entra solo.
function paginas(dir = raiz, salida: Record<string, string> = {}): Record<string, string> {
  for (const n of readdirSync(dir)) {
    const ruta = join(dir, n);
    if (statSync(ruta).isDirectory()) { if (!FUERA.has(n) && !n.startsWith('.')) paginas(ruta, salida); }
    else if (n.endsWith('.html')) salida[relative(raiz, ruta).replace(/\.html$/, '').replace(/[\\/]/g, '-')] = ruta;
  }
  return salida;
}

export default defineConfig({
  base: './', // rutas relativas: sirve igual en github.io/limonada-b2c-premium/ y en un dominio propio
  plugins: [tailwindcss()],
  build: { rollupOptions: { input: paginas() } },
});
