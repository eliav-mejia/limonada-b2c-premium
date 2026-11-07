// ¿Puede servirse la imagen a quien la pide? Sin Referer (visita directa, apps, algunos navegadores) se permite;
// con Referer, solo si el host es uno de los dominios propios o un subdominio suyo.
export function permitido(referer: string | null, dominios: readonly string[]): boolean {
  if (!referer) return true;
  let host: string;
  try { host = new URL(referer).hostname; } catch { return false; }
  return dominios.some((d) => host === d || host.endsWith(`.${d}`));
}

export const listaDominios = (valor: string | undefined): string[] =>
  (valor ?? '').split(',').map((d) => d.trim().toLowerCase()).filter(Boolean);
