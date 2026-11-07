import { expect, it } from 'vitest';
import { desplazamiento } from '../src/parallax';

it('limita el desplazamiento', () => {
  expect(desplazamiento(100, 0.3)).toBe(30);
  expect(desplazamiento(10_000, 0.5)).toBe(200);
});
