// Enlaces de contacto sin backend (v1.0.0): WhatsApp con referencia y formulario por mailto.
// No se guarda nada en el sitio; el endpoint llega en la Etapa 2.

/** Referencia corta para ubicar la conversación: LP-XXXX (sin 0/O ni 1/I para dictarla sin errores). */
export function referencia(azar: () => number = Math.random): string {
  const letras = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  let r = '';
  for (let i = 0; i < 4; i++) r += letras[Math.floor(azar() * letras.length) % letras.length];
  return `LP-${r}`;
}

export function enlaceWhatsApp(numero: string, origen: string, pieza?: string, ref = referencia()): string {
  const texto = pieza
    ? `Hola, me interesa ${pieza} de Esenciales. ¿Qué tallas tienen disponibles? (Ref ${ref})`
    : `Hola, quiero agendar una cita de medidas con Limonada Premium. (Ref ${ref} · ${origen})`;
  return `https://wa.me/${numero.replace(/\D/g, '')}?text=${encodeURIComponent(texto)}`;
}

export function mailtoSolicitud(correo: string, campos: Record<string, string>): string {
  const cuerpo = Object.entries(campos)
    .map(([k, v]) => `${k}: ${v.trim()}`)
    .join('\n');
  return `mailto:${correo}?subject=${encodeURIComponent('Solicitud · Tu colección ejecutiva')}&body=${encodeURIComponent(cuerpo)}`;
}
