import { listaDominios, permitido } from './hotlink';

interface Env {
  DOMINIOS_PERMITIDOS: string;
}

// Protección de imágenes en el servidor: bloquea el hotlinking y añade cabeceras de derechos.
export default {
  async fetch(peticion: Request, env: Env): Promise<Response> {
    if (!permitido(peticion.headers.get('Referer'), listaDominios(env.DOMINIOS_PERMITIDOS))) {
      return new Response('Imagen protegida', { status: 403 });
    }
    const original = await fetch(peticion);
    const respuesta = new Response(original.body, original);
    respuesta.headers.set('X-Robots-Tag', 'noai, noimageai');
    respuesta.headers.set('Cross-Origin-Resource-Policy', 'same-site');
    return respuesta;
  },
} satisfies ExportedHandler<Env>;
