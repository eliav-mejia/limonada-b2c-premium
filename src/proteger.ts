// DISUASIÓN, no protección: impide el clic derecho y el arrastre sobre img.protegida.
// No evita capturas de pantalla ni descargas desde el código. La protección real está en el servidor:
// workers/imagenes (hotlinking + cabeceras) y public/_headers.
export function iniciarProteccion(selector = 'img.protegida'): void {
  const esProtegida = (t: EventTarget | null) => t instanceof HTMLImageElement && t.matches(selector);
  document.addEventListener('contextmenu', (e) => { if (esProtegida(e.target)) e.preventDefault(); });
  document.addEventListener('dragstart', (e) => { if (esProtegida(e.target)) e.preventDefault(); });
}
