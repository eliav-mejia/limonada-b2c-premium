import { enlaceWhatsApp, mailtoSolicitud } from './contacto';
import { marcaPorId } from './marcas';
import { iniciarParallax } from './parallax';
import { iniciarProteccion } from './proteger';

document.documentElement.classList.add('js');
iniciarParallax();
iniciarProteccion();

const marca = marcaPorId(document.body.dataset.marca);
if (marca) document.documentElement.dataset.marca = marca.id;

// Menú móvil
const boton = document.querySelector<HTMLButtonElement>('.menu-boton');
const menu = document.getElementById('menu');
boton?.addEventListener('click', () => {
  const abierto = menu?.classList.toggle('abierto') ?? false;
  boton.setAttribute('aria-expanded', String(abierto));
});

// Aparición al desplazar
const revelar = document.querySelectorAll<HTMLElement>('.revelar');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entradas) => {
    for (const e of entradas) if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -10% 0px' });
  revelar.forEach((el) => io.observe(el));
} else revelar.forEach((el) => el.classList.add('visible'));

// WhatsApp con referencia (se arma al hacer clic para que cada conversación tenga la suya)
document.addEventListener('click', (ev) => {
  const a = (ev.target as Element | null)?.closest<HTMLAnchorElement>('a[data-whatsapp]');
  if (!a) return;
  const numero = new URL(a.href).pathname.slice(1);
  a.href = enlaceWhatsApp(numero, a.dataset.whatsapp ?? 'sitio', a.dataset.pieza);
  a.target = '_blank';
  a.rel = 'noopener';
});

// Formulario «Tu colección» → correo de la visitante
document.querySelectorAll<HTMLFormElement>('form[data-formulario]').forEach((form) => {
  form.addEventListener('submit', (ev) => {
    ev.preventDefault();
    const campos: Record<string, string> = {};
    new FormData(form).forEach((v, k) => { campos[k] = String(v); });
    location.href = mailtoSolicitud(form.dataset.correo ?? '', campos);
    form.hidden = true;
    form.parentElement?.querySelector<HTMLElement>('.gracias')?.removeAttribute('hidden');
  });
});

document.querySelectorAll('[data-anio]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });
