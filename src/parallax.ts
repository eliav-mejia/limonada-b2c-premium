// Desplazamiento vertical de una capa parallax, limitado para no dejar huecos.
export const desplazamiento = (scrollY: number, factor: number, limite = 200): number =>
  Math.max(-limite, Math.min(limite, Math.round(scrollY * factor)));

export function iniciarParallax(): void {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const capas = [...document.querySelectorAll<HTMLElement>('[data-parallax]')];
  if (!capas.length) return;
  let pendiente = false;
  const pintar = () => {
    pendiente = false;
    for (const capa of capas) {
      const img = capa.querySelector<HTMLElement>('img');
      if (img) img.style.transform = `translateY(${desplazamiento(scrollY, Number(capa.dataset.parallax) || 0.3)}px)`;
    }
  };
  addEventListener('scroll', () => { if (!pendiente) { pendiente = true; requestAnimationFrame(pintar); } }, { passive: true });
  pintar();
}
