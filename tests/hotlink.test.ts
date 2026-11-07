import { describe, expect, it } from 'vitest';
import { listaDominios, permitido } from '../workers/imagenes/src/hotlink';

const propios = listaDominios('limonada.com.mx, www.limonada.com.mx');

describe('permitido', () => {
  it('permite peticiones sin Referer', () => expect(permitido(null, propios)).toBe(true));
  it('permite el dominio propio y sus subdominios', () => {
    expect(permitido('https://limonada.com.mx/marcas/coleccion/', propios)).toBe(true);
    expect(permitido('https://cdn.limonada.com.mx/x', propios)).toBe(true);
  });
  it('bloquea otros sitios y dominios que solo se parecen', () => {
    expect(permitido('https://otro.example/', propios)).toBe(false);
    expect(permitido('https://limonada.com.mx.evil.test/', propios)).toBe(false);
    expect(permitido('no-es-url', propios)).toBe(false);
  });
});
