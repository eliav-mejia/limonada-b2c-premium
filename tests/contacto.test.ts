import { describe, expect, it } from 'vitest';
import { enlaceWhatsApp, mailtoSolicitud, referencia } from '../src/contacto';

describe('contacto', () => {
  it('genera referencias LP-XXXX sin caracteres ambiguos', () => {
    for (let i = 0; i < 200; i++) expect(referencia()).toMatch(/^LP-[A-HJ-NP-Z2-9]{4}$/);
    expect(referencia(() => 0.999999)).toBe('LP-9999');
  });
  it('arma el enlace de WhatsApp con la pieza y la referencia', () => {
    const url = enlaceWhatsApp('52 1 56 1480 0424', 'esenciales', 'La Junta', 'LP-ABCD');
    expect(url.startsWith('https://wa.me/5215614800424?text=')).toBe(true);
    expect(decodeURIComponent(url.split('text=')[1])).toContain('La Junta de Esenciales');
    expect(decodeURIComponent(url)).toContain('Ref LP-ABCD');
  });
  it('arma el mailto con los campos del formulario', () => {
    const url = mailtoSolicitud('ventas@limonada.com.mx', { nombre: ' Ana ', piezas: 'Saco y falda' });
    expect(url.startsWith('mailto:ventas@limonada.com.mx?subject=')).toBe(true);
    expect(decodeURIComponent(url)).toContain('nombre: Ana\npiezas: Saco y falda');
  });
});
