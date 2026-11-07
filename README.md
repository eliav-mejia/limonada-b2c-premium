# Limonada Premium · limonada-b2c-premium

Sastrería ejecutiva **para mujer** en la Ciudad de México: traje sastre con **blusas a la medida** (cuello, largo de manga,
puño), piezas **Esenciales** por talla y uniformes ejecutivos para equipos de mujeres. Línea B2C premium de Limonada (desde 1997).

- Repositorio: <https://github.com/eliav-mejia/limonada-b2c-premium> · rama `main` = producción
- Publicado en: <https://eliav-mejia.github.io/limonada-b2c-premium/> (GitHub Pages por GitHub Actions)
- **Variante B · Portafolio editorial** (como casasiego.com), ruta **TypeScript** de `builds/sites/_plataforma/variantes/`,
  con estilos en **Tailwind CSS v4** (paleta terracota)
- Versión: **1.0.1** · fase interna (v1.x en github.io, `noindex`; el dominio propio se decide en v2.0.0)

## Probar en local

El sitio es **estático y ya compilado**: `index.html` se puede abrir directo desde disco. Solo hace falta compilar al
cambiar textos, estilos o TypeScript, y hay que versionar `css/sitio.css` y `js/main.js` junto con el cambio.

```bash
npm install                # .npmrc fija legacy-peer-deps (error de npm 10 con los peers opcionales de vitest)
npm run build              # tools/paginas.py → tsc → css/sitio.css (Tailwind CLI) → js/main.js (esbuild, IIFE)
npm test                   # vitest
npm run dev                # http://localhost:8231
```

## Estructura (paralela a casasiego.com)

```
index.html                       portada: héroe · Cap. I Tu colección · Cap. II Esenciales · láminas I–IV · la blusa ·
                                 Club + Para tu equipo · manifiesto                (≈ index.html de Casa Siego)
marcas/coleccion/                línea nº 1 · traje sastre con blusas a la medida, 3 pasos, formulario   (≈ brands/justo/)
marcas/esenciales/               línea nº 2 · 4 piezas por talla, pedido por WhatsApp              (≈ brands/justo/tienda/)
marcas/esenciales/guia-de-tallas/  tallas CH–XG y cómo medirse                     (≈ justo/tienda/guia-de-tallas/)
membresia/                       Club Limonada Premium · términos de clienta Priority               (≈ membresia/)
ayuda/ · ayuda/<slug>/           Centro de Ayuda, 12 artículos + FAQPage JSON-LD                     (≈ ayuda/)
terminos.html · privacidad/ · 404.html
tools/paginas.py                 FUENTE de todas las páginas (cabecera, pie, <head>, textos, LOOKS, ARTICULOS)
src/styles/sitio.css             FUENTE Tailwind → tokens.css (@theme, paleta) → layout.css → marca.css (@apply)
css/sitio.css                    COMPILADO (npm run css), lo que enlazan las páginas; no editar a mano
js/main.js                       COMPILADO (npm run js) desde src/main.ts
src/main.ts                      menú, aparición al desplazar, WhatsApp con referencia LP-XXXX, formulario por mailto
src/contacto.ts · marcas.ts · parallax.ts · proteger.ts
tests/                           vitest: contacto, parallax, hotlink del Worker
workers/imagenes/                Cloudflare Worker antihotlinking (se despliega aparte con wrangler; no lo publica Pages)
img/fotos/ · robots.txt · sitemap.xml · _headers (CSP; GitHub Pages lo ignora) · .well-known/tdmrep.json
.github/workflows/pages.yml      push a main → build → test → copia lo publicable a _site/ → GitHub Pages
_interno/                        LOCAL, fuera de Git: README, TIMELINE, deployed/, propuestas/
```

**Flujo de edición:** todo texto se cambia en `tools/paginas.py`, nunca en el HTML generado. Toda página nueva entra sola
al sitio y al sitemap. Toda URL es relativa: funciona en github.io y en un dominio propio.

## Paleta (Tailwind `@theme`, `src/styles/tokens.css`)

| Token | Hex | Uso |
|---|---|---|
| `crema` | #EFEBE4 | fondo base |
| `arena` | #E3D1BE | secciones alternas, marcos de foto (las fotos se funden con `mix-blend-multiply`) |
| `terracota-claro` | #CD8D77 | anillos de foco, acentos sobre fondo oscuro |
| `terracota` | #AD5C43 | numerales y adornos (≥ 24 px) |
| `terracota-profundo` | #8C432C | botones, enlaces, sección oscura |
| `taupe` | #A6927F | bordes, títulos del pie |
| `lana` | #8F7D71 | bordes y líneas |
| `tinta` | #2B211C | texto y pie (añadido: lana y taupe no llegan a 4.5:1 sobre crema) |

## Pendiente con la clienta
- Confirmar WhatsApp (`5215614800424`) y correo (`ventas@limonada.com.mx`), tomados de limonada.com.mx.
- Precios de Esenciales (hoy «por confirmar»), tabla de tallas contra el patrón de taller, nombres de las piezas.
- Fotografías propias: las cuatro láminas vienen del catálogo dama de limonada.com.mx (640×960).
- Aviso de privacidad: texto base, revisar con asesoría legal antes de la Etapa 2 (pagos).
- GTM/GA4: sin etiqueta en v1.0.0.
