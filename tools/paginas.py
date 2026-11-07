#!/usr/bin/env python3
"""Genera todas las páginas HTML de Limonada Premium (cabecera, pie y <head> comunes) y sitemap.xml.

    python3 tools/paginas.py        # desde la raíz; npm run build lo llama y compila css/ y js/

Arquitectura (Variante B · Portafolio editorial, como casasiego.com):
    index.html                         portada: Cap. I Tu colección · Cap. II Esenciales · láminas · Club · equipos
    marcas/coleccion/                  línea nº 1 · Tu colección ejecutiva (traje sastre + blusa a la medida)
    marcas/esenciales/                 línea nº 2 · Esenciales (piezas listas por talla) + guia-de-tallas/
    membresia/                         Club Limonada Premium · clienta Priority (términos)
    ayuda/ + ayuda/<slug>/             Centro de Ayuda (ARTICULOS)
    terminos.html · privacidad/ · 404.html

Todas las rutas son relativas: el sitio funciona en eliav-mejia.github.io/limonada-b2c-premium/ y en un dominio propio.
"""
import html, json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[1]
URL = "https://eliav-mejia.github.io/limonada-b2c-premium/"
VERSION = "1.0.1"
WA = "5215614800424"          # WhatsApp de Limonada (confirmar con la clienta antes de v2.0.0)
CORREO = "ventas@limonada.com.mx"
KEYWORDS = ("trajes sastre para mujer, ropa ejecutiva para mujer, blusas a la medida, sastrería para dama, "
            "uniformes ejecutivos para mujer, trajes a la medida, Ciudad de México")
ROBOTS = "noindex, follow, noai, noimageai"   # v1.x: fase interna sin dominio propio (ver README)

LOOKS = [
    dict(id="directora", n="I", nombre="La Directora", foto="05-directora.jpg",
         alt="Saco entallado sin solapa de un botón en textura café y pantalón recto café",
         piezas="Saco y pantalón recto", tela="Textura café", corte="Entallado, sin solapa, un botón",
         ocasion="Dirección · oficina", tallas="CH · M · G · XG"),
    dict(id="junta", n="II", nombre="La Junta", foto="06-junta.jpg",
         alt="Saco entallado de tres botones en cuadro gris y falda lápiz negra con abertura",
         piezas="Saco y falda lápiz", tela="Cuadro gris, falda negra", corte="Entallado, tres botones",
         ocasion="Juntas · atención a clientes", tallas="CH · M · G · XG"),
    dict(id="funda", n="III", nombre="La Funda", foto="07-funda.jpg",
         alt="Vestido funda gris carbón sin mangas con cortes princesa",
         piezas="Vestido", tela="Gris carbón", corte="Funda, cortes princesa",
         ocasion="Consejo · eventos", tallas="CH · M · G · XG"),
    dict(id="sucursal", n="IV", nombre="La Sucursal", foto="08-sucursal.jpg",
         alt="Saco fucsia de dos botones con solapa, bolsillos y puños en pata de gallo y pantalón negro",
         piezas="Saco y pantalón", tela="Fucsia, pata de gallo", corte="Entallado, dos botones",
         ocasion="Presentaciones · atención al público", tallas="CH · M · G · XG"),
]

# Centro de Ayuda: (sección, slug, pregunta, párrafos)
ARTICULOS = [
    ("Clienta Priority", "como-ser-clienta-priority", "¿Cómo me vuelvo clienta Priority?", [
        "Te vuelves clienta Priority al confirmar tu primera colección ejecutiva: un traje sastre (saco con pantalón o falda) "
        "con al menos dos blusas a la medida. No hay registro aparte ni cuota de inscripción.",
        "Desde ese pedido guardamos tu patrón de blusa (cuello, largo de manga, puño y pinzas) para que tus siguientes "
        "piezas salgan sin repetir la cita de medidas, salvo que tú lo pidas."]),
    ("Clienta Priority", "una-coleccion-para-renovar-el-closet", "Una colección para renovar el clóset", [
        "Una colección es un conjunto pensado para tu semana de trabajo: un traje sastre, sus blusas a la medida y, si quieres, "
        "un vestido funda o una segunda pieza inferior. Todo se elige junto, en tela, color y ocasión.",
        "La idea es que cada pieza combine con las demás. Con un saco, dos piezas inferiores y tres blusas tienes seis "
        "combinaciones distintas para la oficina, juntas y eventos."]),
    ("Clienta Priority", "beneficios-de-clienta-priority", "Beneficios de clienta Priority", [
        "Prioridad en la agenda de citas, patrón de blusa guardado, aviso anticipado de telas de temporada y un ajuste "
        "de talla sin costo durante los primeros 60 días de cada pedido.",
        "Las condiciones completas están en los términos del Club Limonada Premium."]),
    ("Clienta Priority", "tiene-un-costo-ser-priority", "¿Tiene un costo ser Priority?", [
        "No. La categoría Priority no se compra: se obtiene con tu primera colección y se mantiene mientras hagas al "
        "menos un pedido cada 12 meses.",
        "Si pasan 12 meses sin pedido, tu patrón se conserva y la categoría se reactiva con tu siguiente colección."]),
    ("Citas y medidas", "agendar-cita-de-medidas", "¿Cómo agendo una cita de medidas?", [
        "Escríbenos por WhatsApp o desde el formulario de «Tu colección» con dos o tres horarios que te acomoden. "
        "La cita dura unos 45 minutos y se hace en nuestro taller de la Ciudad de México.",
        "Te confirmamos por el mismo medio. Las clientas Priority tienen preferencia en los horarios de primera hora y de "
        "fin de día."]),
    ("Citas y medidas", "que-llevar-a-la-cita", "¿Qué llevo a la cita de medidas?", [
        "Ven con la ropa interior y el calzado que usarías con el traje: la altura del tacón cambia el largo del pantalón "
        "y la caída de la falda.",
        "Si tienes una blusa o un saco cuyo corte te gusta, tráelo. Nos ayuda a entender cómo prefieres el entalle."]),
    ("Citas y medidas", "cancelar-o-mover-una-cita", "¿Cómo cancelo o muevo una cita?", [
        "Avísanos con al menos 24 horas por WhatsApp o correo y te damos un nuevo horario. Mover una cita no tiene costo.",
        "Si la cita era para una prueba de un pedido en curso, moverla puede recorrer la fecha de entrega."]),
    ("Pedidos y entregas", "tiempos-de-entrega", "¿Cuánto tarda un pedido?", [
        "Una colección a la medida tarda de 3 a 4 semanas desde la cita de medidas, con una prueba intermedia del saco. "
        "Las piezas Esenciales en talla disponible se entregan en 3 a 5 días hábiles.",
        "En temporada alta (enero y septiembre) te confirmamos la fecha exacta al tomar el pedido."]),
    ("Pedidos y entregas", "ajustes-despues-de-la-entrega", "¿Puedo pedir ajustes después de la entrega?", [
        "Sí. Cada pedido incluye un ajuste sin costo durante 60 días: largo de manga, bastilla, cintura o entalle del saco.",
        "Después de ese plazo, los ajustes se cotizan por pieza."]),
    ("Empresas y equipos", "uniformes-ejecutivos-para-mujer", "¿Hacen uniformes ejecutivos para mujer?", [
        "Sí. Desde 1997 Limonada viste equipos ejecutivos. Para un equipo de mujeres armamos la misma colección para todas, "
        "con el mismo cuidado de una pieza a la medida: cada integrante tiene su propia cita de medidas.",
        "El pedido sale en una sola orden a taller, con la misma tela y el mismo tono para todo el equipo."]),
    ("Empresas y equipos", "variantes-de-un-pedido", "¿Cuánto puede variar un pedido de equipo?", [
        "Dentro de un mismo pedido cada integrante puede elegir pantalón, falda o vestido, y el largo y el cuello de su blusa. "
        "La tela, el color y el corte del saco se mantienen para que el equipo se vea uniforme."]),
    ("Políticas", "cambios-de-politicas", "¿Cómo me entero si cambian las políticas?", [
        "Publicamos cualquier cambio en esta página y en los términos del Club con su fecha. Si eres clienta Priority, "
        "te avisamos además por el medio de contacto que nos diste."]),
]


def e(t):
    return html.escape(t, quote=True)


def head(p, titulo, desc, ruta, extra=""):
    return f"""<!doctype html>
<html lang="es-MX">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{e(titulo)}</title>
  <meta name="description" content="{e(desc)}" />
  <meta name="keywords" content="{KEYWORDS}" />
  <!-- v1.x fase interna: noindex. Reserva de derechos frente a minería de datos e IA: noai, noimageai -->
  <meta name="robots" content="{ROBOTS}" />
  <link rel="canonical" href="{URL}{ruta}" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="es_MX" />
  <meta property="og:title" content="{e(titulo)}" />
  <meta property="og:description" content="{e(desc)}" />
  <meta property="og:image" content="{URL}img/fotos/05-directora.jpg" />
  <meta name="theme-color" content="#EFEBE4" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" />
  <link rel="stylesheet" href="{p}css/sitio.css" />{extra}
</head>
"""


def cabecera(p, marca=""):
    return f"""<body data-marca="{marca}">
  <a class="saltar" href="#contenido">Saltar al contenido</a>
  <header class="barra">
    <a class="logo" href="{p}" aria-label="Limonada Premium, inicio"><span class="logo__a">limonada</span><span class="logo__b">premium</span></a>
    <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu">Menú</button>
    <nav id="menu" class="menu" aria-label="Principal">
      <a href="{p}marcas/coleccion/">Tu colección</a>
      <a href="{p}marcas/esenciales/">Esenciales</a>
      <a href="{p}membresia/">Club</a>
      <a href="{p}ayuda/">Ayuda</a>
      <a class="menu__cta" href="https://wa.me/{WA}" data-whatsapp="menu">Agendar cita</a>
    </nav>
  </header>
  <main id="contenido">
"""


def pie(p):
    return f"""  </main>
  <footer class="pie">
    <div class="pie__rejilla">
      <div>
        <p class="logo logo--pie"><span class="logo__a">limonada</span><span class="logo__b">premium</span></p>
        <p class="pie__nota">Sastrería ejecutiva para mujer. Trajes sastre, blusas a la medida y uniformes ejecutivos
          en la Ciudad de México. Una línea de Limonada, desde 1997.</p>
      </div>
      <div>
        <p class="pie__titulo">Líneas</p>
        <a href="{p}marcas/coleccion/">Tu colección ejecutiva</a>
        <a href="{p}marcas/esenciales/">Esenciales</a>
        <a href="{p}marcas/esenciales/guia-de-tallas/">Guía de tallas</a>
      </div>
      <div>
        <p class="pie__titulo">Clientas</p>
        <a href="{p}membresia/">Club Limonada Premium</a>
        <a href="{p}ayuda/">Centro de Ayuda</a>
        <a href="{p}terminos.html">Términos</a>
        <a href="{p}privacidad/">Aviso de privacidad</a>
      </div>
      <div>
        <p class="pie__titulo">Contacto</p>
        <a href="https://wa.me/{WA}" data-whatsapp="pie">WhatsApp</a>
        <a href="mailto:{CORREO}">{CORREO}</a>
        <span>Ciudad de México</span>
      </div>
    </div>
    <div class="pie__base"><span>© <span data-anio>2026</span> Limonada Premium</span><span>v{VERSION}</span></div>
  </footer>
  <script defer src="{p}js/main.js"></script>
</body>
</html>
"""


def jsonld(obj):
    return '\n  <script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


ORG = {
    "@context": "https://schema.org", "@type": "ClothingStore", "name": "Limonada Premium",
    "description": "Sastrería ejecutiva para mujer: trajes sastre, blusas a la medida y uniformes ejecutivos.",
    "url": URL, "image": URL + "img/fotos/05-directora.jpg", "email": CORREO, "foundingDate": "1997",
    "parentOrganization": {"@type": "Organization", "name": "Limonada", "url": "https://limonada.com.mx"},
    "areaServed": {"@type": "City", "name": "Ciudad de México"},
    "knowsAbout": ["trajes sastre para mujer", "blusas a la medida", "ropa ejecutiva para mujer",
                   "uniformes ejecutivos para mujer", "sastrería para dama"],
    "address": {"@type": "PostalAddress", "addressLocality": "Ciudad de México", "addressCountry": "MX"},
}


def lamina(p, l, enlace):
    return f"""        <a class="lamina revelar" href="{enlace}">
          <span class="lamina__num">Lámina {l['n']}</span>
          <span class="lamina__marco"><img class="protegida" src="{p}img/fotos/{l['foto']}" alt="{e(l['alt'])}" width="640" height="960" loading="lazy" /></span>
          <span class="lamina__pie"><b>{l['nombre']}</b><span>{l['piezas']} · {l['tela']}</span></span>
        </a>
"""


def escribir(ruta, texto):
    f = RAIZ / ruta
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(texto, encoding="utf-8")
    print("  ", ruta)


# ───────────────────────── portada ─────────────────────────
def portada():
    p = ""
    laminas = "".join(lamina(p, l, f"marcas/esenciales/#{l['id']}") for l in LOOKS)
    return head(p, "Limonada Premium · Trajes sastre y blusas a la medida para mujer en Ciudad de México",
                "Sastrería ejecutiva para mujer en la Ciudad de México: tu colección de traje sastre con blusas a la "
                "medida, piezas Esenciales por talla y uniformes ejecutivos para equipos de mujeres.", "",
                jsonld(ORG)) + cabecera(p) + f"""
    <section class="heroe">
      <div class="heroe__texto">
        <p class="ceja">Sastrería ejecutiva para mujer · Ciudad de México</p>
        <h1>Limonada Premium: <em>trajes sastre y blusas a la medida</em> para la mujer que dirige</h1>
        <p class="entrada">Una colección pensada para tu semana de trabajo: saco, pantalón o falda, vestido y blusas cortadas a
          tus medidas. Con el oficio de Limonada, que viste a la fuerza ejecutiva desde 1997.</p>
        <div class="acciones">
          <a class="boton" href="marcas/coleccion/">Diseña tu colección</a>
          <a class="boton boton--linea" href="marcas/esenciales/">Ver Esenciales</a>
        </div>
      </div>
      <figure class="heroe__foto heroe__foto--color" data-parallax="0.12">
        <img class="protegida" src="img/fotos/Conjunto17_Joven_Rosa.jpg" alt="Mujer joven sonriente con traje sastre rosa palo de saco con solapa y pantalón recto, blusa gris" width="816" height="1306" fetchpriority="high" />
      </figure>
    </section>

    <section class="seccion seccion--marfil">
      <div class="contenedor">
        <h2 class="titulo-seccion">Entra por una pieza, sal con tu guardarropa</h2>
        <div class="capitulos">
          <a class="capitulo revelar" href="marcas/coleccion/">
            <span class="capitulo__num">Cap. I</span>
            <h3>Tu colección ejecutiva</h3>
            <p>Traje sastre con blusas a la medida de cuello, largo de manga y puño. Cita de medidas, una prueba y entrega en 3 a 4 semanas.</p>
            <span class="flecha">Diseñar mi colección →</span>
          </a>
          <a class="capitulo revelar" href="marcas/esenciales/">
            <span class="capitulo__num">Cap. II</span>
            <h3>Esenciales</h3>
            <p>Cuatro piezas listas en tallas CH a XG: La Directora, La Junta, La Funda y La Sucursal. Ajuste de bastilla y manga incluido.</p>
            <span class="flecha">Ver las cuatro piezas →</span>
          </a>
        </div>
      </div>
    </section>

    <section class="seccion">
      <div class="contenedor">
        <p class="ceja">Láminas</p>
        <h2 class="titulo-seccion">Cuatro maneras de llegar a la junta</h2>
        <div class="laminas">
{laminas}        </div>
      </div>
    </section>

    <section class="seccion seccion--tinta">
      <div class="contenedor dos-columnas">
        <div>
          <p class="ceja">La blusa</p>
          <h2 class="titulo-seccion">Lo que se hace a tu medida</h2>
        </div>
        <ul class="lista-medidas">
          <li><b>Cuello</b><span>Redondo, camisero, mao o con lazo; a la altura que te acomoda.</span></li>
          <li><b>Largo de manga</b><span>Para que el puño asome lo justo bajo el saco.</span></li>
          <li><b>Puño</b><span>Sencillo, francés o de botón doble.</span></li>
          <li><b>Pinzas y largo</b><span>Para que la blusa no se salga de la falda ni del pantalón.</span></li>
        </ul>
      </div>
    </section>

    <section class="seccion seccion--marfil">
      <div class="contenedor dos-columnas">
        <div>
          <p class="ceja">Club Limonada Premium</p>
          <h2 class="titulo-seccion">Clienta Priority desde tu primera colección</h2>
          <p>Guardamos tu patrón de blusa, te damos prioridad en la agenda y te avisamos antes que a nadie de las telas de
            temporada. Sin cuota de inscripción.</p>
          <a class="boton boton--linea" href="membresia/">Conocer el Club</a>
        </div>
        <div>
          <p class="ceja">Para tu equipo</p>
          <h3 class="subtitulo">Uniformes ejecutivos para mujer</h3>
          <p>La misma colección para todo el equipo, con una cita de medidas por integrante y un solo pedido a taller.
            Cada una elige pantalón, falda o vestido; la tela y el saco se mantienen.</p>
          <a class="boton boton--linea" href="ayuda/uniformes-ejecutivos-para-mujer/">Cómo funciona</a>
        </div>
      </div>
    </section>

    <section class="seccion manifiesto">
      <div class="contenedor">
        <blockquote>«Vestimos a la fuerza ejecutiva con el mismo cuidado con el que se corta un traje a la medida.»</blockquote>
        <p class="manifiesto__firma">Limonada · desde 1997 · Ciudad de México</p>
      </div>
    </section>
""" + pie(p)


# ───────────────────────── Tu colección ─────────────────────────
def coleccion():
    p = "../../"
    return head(p, "Tu colección ejecutiva · Traje sastre con blusas a la medida · Limonada Premium",
                "Diseña tu colección ejecutiva: traje sastre con pantalón o falda y blusas a la medida de cuello, largo "
                "de manga y puño. Cita de medidas en la Ciudad de México.", "marcas/coleccion/") + cabecera(p, "coleccion") + f"""
    <section class="heroe heroe--marca">
      <div class="heroe__texto">
        <p class="ceja">Línea nº 1 · Tu colección</p>
        <h1>Tu colección de <em>traje sastre con blusas a la medida</em>, de Limonada Premium</h1>
        <p class="entrada">Saco, pantalón o falda, y las blusas que los acompañan, elegidos juntos en tela, color y ocasión.</p>
        <a class="boton" href="#disena">Diseña tu colección</a>
      </div>
      <figure class="heroe__foto" data-parallax="0.12">
        <img class="protegida" src="{p}img/fotos/06-junta.jpg" alt="Saco entallado de tres botones en cuadro gris y falda lápiz negra con abertura" width="640" height="960" />
      </figure>
    </section>

    <section class="seccion seccion--marfil">
      <div class="contenedor dos-columnas">
        <div><p class="ceja">01</p><h2 class="titulo-seccion">Una colección personal</h2></div>
        <div>
          <p>Una colección no es un traje suelto: es un conjunto para tu semana. Con un saco, dos piezas inferiores y tres
            blusas tienes seis combinaciones para la oficina, las juntas y los eventos de la noche.</p>
          <p>Elegimos contigo la tela de temporada, el tono y el corte del saco: entallado sin solapa, de dos o tres botones.</p>
        </div>
      </div>
    </section>

    <section class="seccion">
      <div class="contenedor">
        <p class="ceja">02</p>
        <h2 class="titulo-seccion">Estilo y medida, en tres pasos</h2>
        <ol class="pasos">
          <li class="revelar"><b>Cita de medidas</b><span>45 minutos en el taller. Ven con el calzado que usarás con el traje.</span></li>
          <li class="revelar"><b>Prueba del saco</b><span>A las dos semanas, para ajustar hombro, entalle y largo.</span></li>
          <li class="revelar"><b>Entrega</b><span>De 3 a 4 semanas desde la cita, con un ajuste sin costo durante 60 días.</span></li>
        </ol>
      </div>
    </section>

    <section class="seccion seccion--tinta">
      <div class="contenedor dos-columnas">
        <div><p class="ceja">03</p><h2 class="titulo-seccion">La blusa, a tu medida</h2></div>
        <ul class="lista-medidas">
          <li><b>Cuello</b><span>Redondo, camisero, mao o con lazo.</span></li>
          <li><b>Largo de manga</b><span>Medido con el saco puesto.</span></li>
          <li><b>Puño</b><span>Sencillo, francés o de botón doble.</span></li>
          <li><b>Pinzas y largo</b><span>Para que se quede en su lugar todo el día.</span></li>
        </ul>
      </div>
    </section>

    <section class="seccion seccion--marfil">
      <div class="contenedor dos-columnas">
        <div><p class="ceja">04</p><h2 class="titulo-seccion">El mismo servicio para cada integrante</h2></div>
        <div>
          <h3 class="subtitulo">Un solo pedido a taller</h3>
          <p>Si vistes a tu equipo, cada integrante tiene su propia cita de medidas y elige pantalón, falda o vestido. La
            tela, el tono y el saco se mantienen, y todo sale en una sola orden.</p>
          <a class="boton boton--linea" href="{p}ayuda/variantes-de-un-pedido/">Qué puede variar</a>
        </div>
      </div>
    </section>

    <section class="seccion" id="disena">
      <div class="contenedor formulario-bloque">
        <p class="ceja">05</p>
        <h2 class="titulo-seccion">Diseña tu colección y vuélvete clienta Priority</h2>
        <form class="formulario" data-formulario="coleccion" data-correo="{CORREO}">
          <label>Nombre<input name="nombre" autocomplete="name" required /></label>
          <label>Correo o WhatsApp<input name="contacto" autocomplete="email" required /></label>
          <label>Para<select name="para"><option>Para mí</option><option>Para mi equipo</option></select></label>
          <label>Piezas<select name="piezas"><option>Saco y pantalón</option><option>Saco y falda</option><option>Saco, pantalón y falda</option><option>Vestido y saco</option></select></label>
          <label class="ancho">Horarios que te acomodan para la cita<textarea name="horarios" rows="3"></textarea></label>
          <button class="boton" type="submit">Enviar solicitud</button>
          <p class="formulario__nota">Se abre tu correo con la solicitud lista. No guardamos datos en este sitio.</p>
        </form>
        <p class="gracias" hidden>Gracias. Te escribimos en menos de un día hábil para confirmar tu cita.</p>
      </div>
    </section>
""" + pie(p)


# ───────────────────────── Esenciales ─────────────────────────
def esenciales():
    p = "../../"
    fichas = ""
    for l in LOOKS:
        fichas += f"""        <article class="ficha revelar" id="{l['id']}">
          <span class="lamina__marco"><img class="protegida" src="{p}img/fotos/{l['foto']}" alt="{e(l['alt'])}" width="640" height="960" loading="lazy" /></span>
          <div class="ficha__texto">
            <p class="ceja">Lámina {l['n']}</p>
            <h2>{l['nombre']}</h2>
            <dl>
              <dt>Piezas</dt><dd>{l['piezas']}</dd>
              <dt>Tela</dt><dd>{l['tela']}</dd>
              <dt>Corte</dt><dd>{l['corte']}</dd>
              <dt>Ocasión</dt><dd>{l['ocasion']}</dd>
              <dt>Tallas</dt><dd>{l['tallas']}</dd>
              <dt>Precio</dt><dd>Por confirmar · pago en línea en la Etapa 2</dd>
            </dl>
            <a class="boton" href="https://wa.me/{WA}" data-whatsapp="esenciales-{l['id']}" data-pieza="{l['nombre']}">Pedir por WhatsApp</a>
          </div>
        </article>
"""
    return head(p, "Esenciales · Piezas ejecutivas para mujer por talla · Limonada Premium",
                "Piezas ejecutivas para mujer listas por talla: saco y pantalón, saco y falda lápiz, vestido funda. "
                "Tallas CH a XG con ajuste de bastilla y manga incluido.", "marcas/esenciales/") + cabecera(p, "esenciales") + f"""
    <section class="seccion seccion--marfil cabeza-pagina">
      <div class="contenedor">
        <p class="ceja">Línea nº 2 · Esenciales</p>
        <h1>Esenciales: <em>piezas ejecutivas para mujer</em>, listas en tu talla</h1>
        <p class="entrada">Cuatro piezas para empezar tu guardarropa de trabajo. Ajuste de bastilla y manga incluido.
          ¿No sabes tu talla? Revisa la <a href="guia-de-tallas/">guía de tallas</a>.</p>
      </div>
    </section>
    <section class="seccion">
      <div class="contenedor fichas">
{fichas}      </div>
    </section>
""" + pie(p)


def guia_tallas():
    p = "../../../"
    filas = [("CH", "84–88", "66–70", "92–96", "3–5"), ("M", "89–94", "71–76", "97–102", "7–9"),
             ("G", "95–100", "77–82", "103–108", "11–13"), ("XG", "101–108", "83–90", "109–116", "15–17")]
    tabla = "".join(f"<tr><td><b>{t}</b></td><td>{b}</td><td>{c}</td><td>{h}</td><td>{m}</td></tr>" for t, b, c, h, m in filas)
    return head(p, "Guía de tallas para mujer · Esenciales · Limonada Premium",
                "Guía de tallas de las piezas Esenciales de Limonada Premium: busto, cintura y cadera en centímetros, y "
                "cómo medirte.", "marcas/esenciales/guia-de-tallas/") + cabecera(p, "esenciales") + f"""
    <section class="seccion seccion--marfil cabeza-pagina">
      <div class="contenedor">
        <p class="ceja"><a href="../">Esenciales</a> · Guía de tallas</p>
        <h1>Guía de tallas</h1>
        <p class="entrada">Medidas del cuerpo en centímetros. Si quedas entre dos tallas, elige la mayor: el ajuste de
          bastilla, manga y cintura está incluido.</p>
      </div>
    </section>
    <section class="seccion">
      <div class="contenedor texto-largo">
        <div class="tabla-envoltura"><table>
          <thead><tr><th>Talla</th><th>Busto</th><th>Cintura</th><th>Cadera</th><th>Equivale a (MX)</th></tr></thead>
          <tbody>{tabla}</tbody>
        </table></div>
        <p class="nota">Tabla de referencia de la versión 1.0.0: confirmar contra el patrón de taller antes de publicar precios.</p>
        <h2>Cómo medirte</h2>
        <ol>
          <li><b>Busto:</b> la cinta por la parte más llena del pecho, sin apretar.</li>
          <li><b>Cintura:</b> en la parte más angosta del torso, unos 3 cm arriba del ombligo.</li>
          <li><b>Cadera:</b> por la parte más ancha, con los pies juntos.</li>
        </ol>
        <p>¿Prefieres que te midamos? <a href="../../coleccion/#disena">Agenda una cita de medidas</a>.</p>
      </div>
    </section>
""" + pie(p)


# ───────────────────────── Club ─────────────────────────
CLUB = [
    ("Quiénes somos", "Limonada Premium es la línea de sastrería ejecutiva para mujer de Limonada, taller de la Ciudad de "
     "México que confecciona trajes a la medida y uniformes ejecutivos desde 1997."),
    ("Cómo se obtiene la categoría Priority", "Con la confirmación y el pago de tu primera colección ejecutiva: un traje "
     "sastre con al menos dos blusas a la medida. No hay cuota de inscripción ni registro aparte."),
    ("Beneficios", "Prioridad en la agenda de citas; patrón de blusa guardado; aviso anticipado de telas de temporada; un "
     "ajuste sin costo durante 60 días por pedido; atención directa por WhatsApp."),
    ("Vigencia", "La categoría se mantiene mientras hagas al menos un pedido cada 12 meses. Si pasan 12 meses sin pedido, "
     "tu patrón se conserva y la categoría se reactiva con tu siguiente colección."),
    ("Citas", "Las citas se confirman por WhatsApp o correo. Para mover o cancelar una cita avísanos con 24 horas de "
     "anticipación; moverla no tiene costo."),
    ("Cancelación de pedidos", "Un pedido a la medida puede cancelarse sin cargo antes del corte de tela. Después del corte, "
     "el anticipo cubre el material y el trabajo realizado."),
    ("Datos personales", "Tus medidas son datos personales: solo se usan para confeccionar tus piezas y se tratan conforme "
     "al aviso de privacidad. Puedes pedir que las borremos en cualquier momento."),
    ("Actualización de estos términos", "Publicamos cualquier cambio en esta página con su fecha. A las clientas Priority "
     "les avisamos además por su medio de contacto."),
    ("Ley aplicable", "Estos términos se rigen por las leyes de los Estados Unidos Mexicanos. Para cualquier controversia "
     "las partes se someten a los tribunales de la Ciudad de México."),
]


def membresia():
    p = "../"
    cuerpo = "".join(f"<h2>{i}. {t}</h2>\n        <p>{x}</p>\n        " for i, (t, x) in enumerate(CLUB, 1))
    return head(p, "Club Limonada Premium · Clienta Priority · Términos",
                "Términos del Club Limonada Premium: cómo te vuelves clienta Priority, beneficios, vigencia, citas y "
                "datos personales.", "membresia/") + cabecera(p, "club") + f"""
    <section class="seccion seccion--marfil cabeza-pagina">
      <div class="contenedor">
        <p class="ceja">Club Limonada Premium</p>
        <h1>Clienta Priority</h1>
        <p class="entrada">Vigente desde el 6 de noviembre de 2026.</p>
      </div>
    </section>
    <section class="seccion">
      <div class="contenedor texto-largo">
        {cuerpo}
      </div>
    </section>
""" + pie(p)


# ───────────────────────── Centro de Ayuda ─────────────────────────
def ayuda_indice():
    p = "../"
    secciones, actual = "", None
    for sec, slug, q, _ in ARTICULOS:
        if sec != actual:
            if actual:
                secciones += "        </ul>\n"
            secciones += f'        <h2>{sec}</h2>\n        <ul class="preguntas">\n'
            actual = sec
        secciones += f'          <li><a href="{slug}/">{q}</a></li>\n'
    secciones += "        </ul>\n"
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": " ".join(ps)}}
        for _, _, q, ps in ARTICULOS]}
    return head(p, "Centro de Ayuda · Limonada Premium",
                "Respuestas sobre clienta Priority, citas de medidas, tiempos de entrega, ajustes y uniformes ejecutivos "
                "para mujer.", "ayuda/", jsonld(faq)) + cabecera(p, "ayuda") + f"""
    <section class="seccion seccion--marfil cabeza-pagina">
      <div class="contenedor"><p class="ceja">Ayuda</p><h1>Centro de Ayuda</h1></div>
    </section>
    <section class="seccion">
      <div class="contenedor texto-largo">
{secciones}      </div>
    </section>
""" + pie(p)


def ayuda_articulo(sec, slug, q, ps):
    p = "../../"
    cuerpo = "".join(f"<p>{x}</p>\n        " for x in ps)
    return head(p, f"{q} · Centro de Ayuda · Limonada Premium", ps[0][:155], f"ayuda/{slug}/") + cabecera(p, "ayuda") + f"""
    <section class="seccion seccion--marfil cabeza-pagina">
      <div class="contenedor"><p class="ceja"><a href="../">Centro de Ayuda</a> · {sec}</p><h1>{q}</h1></div>
    </section>
    <section class="seccion">
      <div class="contenedor texto-largo">
        {cuerpo}<p><a class="boton boton--linea" href="https://wa.me/{WA}" data-whatsapp="ayuda-{slug}">¿Otra duda? Escríbenos</a></p>
      </div>
    </section>
""" + pie(p)


# ───────────────────────── legales y 404 ─────────────────────────
def terminos():
    p = ""
    return head(p, "Términos de uso y derechos · Limonada Premium",
                "Términos de uso del sitio de Limonada Premium y reserva de derechos sobre sus imágenes.", "terminos.html") + cabecera(p) + f"""
    <section class="seccion seccion--marfil cabeza-pagina"><div class="contenedor"><h1>Términos de uso y derechos</h1></div></section>
    <section class="seccion"><div class="contenedor texto-largo">
      <h2>Uso del sitio</h2>
      <p>La información de este sitio es orientativa. Precios, telas y fechas de entrega se confirman por escrito al tomar cada pedido.</p>
      <h2>Imágenes</h2>
      <p>Todas las fotografías son propiedad de Limonada. Se reserva expresamente su uso para minería de textos y datos y para
        entrenar sistemas de inteligencia artificial (ver <code>.well-known/tdmrep.json</code>).</p>
      <h2>Contacto</h2>
      <p><a href="mailto:{CORREO}">{CORREO}</a></p>
    </div></section>
""" + pie(p)


def privacidad():
    p = "../"
    return head(p, "Aviso de privacidad · Limonada Premium",
                "Aviso de privacidad de Limonada Premium: qué datos tratamos, para qué y cómo ejercer tus derechos ARCO.",
                "privacidad/") + cabecera(p) + f"""
    <section class="seccion seccion--marfil cabeza-pagina"><div class="contenedor"><h1>Aviso de privacidad</h1>
      <p class="entrada">Texto base de la versión 1.0.0: revisar con asesoría legal antes de cobrar en línea.</p></div></section>
    <section class="seccion"><div class="contenedor texto-largo">
      <h2>Responsable</h2>
      <p>Limonada, con domicilio en la Ciudad de México, es responsable del tratamiento de tus datos personales.</p>
      <h2>Datos que tratamos</h2>
      <p>Nombre, medio de contacto, horarios de cita y, si haces un pedido a la medida, tus medidas corporales.</p>
      <h2>Finalidades</h2>
      <p>Agendar tu cita, confeccionar y entregar tus piezas, y avisarte de cambios en tu pedido. No vendemos ni cedemos tus datos.</p>
      <h2>Derechos ARCO</h2>
      <p>Puedes acceder, rectificar, cancelar u oponerte al tratamiento de tus datos escribiendo a
        <a href="mailto:{CORREO}">{CORREO}</a>.</p>
      <h2>Este sitio</h2>
      <p>El sitio no guarda datos: los formularios abren tu propio correo. No usa cookies de seguimiento en la versión 1.0.0.</p>
    </div></section>
""" + pie(p)


def no_encontrada():
    # GitHub Pages sirve 404.html en cualquier ruta: la <base> se calcula antes de cargar estilos y scripts.
    base = ("\n  <script>(function(){var r='/limonada-b2c-premium/';document.write('<base href=\"'+"
            "(location.pathname.indexOf(r)===0?r:'/')+'\">');})();</script>")
    t = head("", "Página no encontrada · Limonada Premium", "La página que buscas no existe.", "404.html")
    t = t.replace('<meta charset="UTF-8" />', '<meta charset="UTF-8" />' + base, 1)
    return t + cabecera("") + """
    <section class="seccion cabeza-pagina"><div class="contenedor">
      <p class="ceja">404</p><h1>Esta página no existe</h1>
      <p class="entrada">Puede que el enlace esté incompleto. Vuelve al inicio o revisa el Centro de Ayuda.</p>
      <div class="acciones"><a class="boton" href="./">Inicio</a><a class="boton boton--linea" href="ayuda/">Ayuda</a></div>
    </div></section>
""" + pie("")


def sitemap(rutas):
    filas = "".join(f"  <url><loc>{URL}{r}</loc><lastmod>2026-11-06</lastmod></url>\n" for r in rutas)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{filas}</urlset>\n'


def main():
    print("Generando páginas:")
    escribir("index.html", portada())
    escribir("marcas/coleccion/index.html", coleccion())
    escribir("marcas/esenciales/index.html", esenciales())
    escribir("marcas/esenciales/guia-de-tallas/index.html", guia_tallas())
    escribir("membresia/index.html", membresia())
    escribir("ayuda/index.html", ayuda_indice())
    for a in ARTICULOS:
        escribir(f"ayuda/{a[1]}/index.html", ayuda_articulo(*a))
    escribir("terminos.html", terminos())
    escribir("privacidad/index.html", privacidad())
    escribir("404.html", no_encontrada())
    rutas = ["", "marcas/coleccion/", "marcas/esenciales/", "marcas/esenciales/guia-de-tallas/", "membresia/", "ayuda/"]
    rutas += [f"ayuda/{a[1]}/" for a in ARTICULOS] + ["terminos.html", "privacidad/"]
    escribir("sitemap.xml", sitemap(rutas))


if __name__ == "__main__":
    main()
