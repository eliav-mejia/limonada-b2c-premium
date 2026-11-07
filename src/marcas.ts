// Registro tipado de líneas (submarcas): una entrada por carpeta en marcas/<id>/, como brands/ en casasiego.com.
export interface Marca {
  id: string;
  nombre: string;
  ruta: `marcas/${string}/`;
}

export const MARCAS: readonly Marca[] = [
  { id: 'coleccion', nombre: 'Tu colección ejecutiva', ruta: 'marcas/coleccion/' },
  { id: 'esenciales', nombre: 'Esenciales', ruta: 'marcas/esenciales/' },
];

export const marcaPorId = (id: string | undefined) => MARCAS.find((m) => m.id === id);
