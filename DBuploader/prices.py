from datetime import datetime
import psycopg2
import csv
from typing import Optional


def build_category_mapping(connection, brand_id):
    with connection.cursor() as cur:
        cur.execute("""
        SELECT internal_id, category_id FROM category WHERE brand_id = %s
        """, (brand_id,))
        return {row[0]: row[1] for row in cur.fetchall()}


def build_store_mapping(connection, brand_id):
    with connection.cursor() as cur:
        cur.execute("""
        SELECT internal_id, store_id FROM store WHERE brand_id = %s
        """, (brand_id,))
        return {row[0]: row[1] for row in cur.fetchall()}

  
def build_product_mapping(connection, brand_id):
    with connection.cursor() as cur:
        cur.execute("""
        SELECT p.internal_id, p.product_id
        FROM product p
        JOIN category c ON p.category_id = c.category_id
        WHERE c.brand_id = %s
        """, (brand_id,))
        return {row[0]: row[1] for row in cur.fetchall()}





def get_or_create_brand(connection, brand_name: str) -> Optional[int]:
    try:
        with connection.cursor() as cur:
            # Verificar si la marca ya existe
            cur.execute("""
            SELECT brand_id FROM brand WHERE brand_name = %s
            """, (brand_name,))
            
            result = cur.fetchone()
            
            if result:
                return result[0]  # Devolver ID existente
            
            # Crear nueva marca si no existe
            cur.execute("""
            INSERT INTO brand (brand_name)
            VALUES (%s)
            RETURNING brand_id
            """, (brand_name,))
            
            brand_id = cur.fetchone()[0]
            connection.commit()
            return brand_id
            
    except psycopg2.Error as e:
        connection.rollback()
        print(f"Error al obtener/crear marca: {e}")
        return None



def prices(brand_name: str, brand_id: Optional[int] = None, file_path: Optional[str] = None):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )

        if conn.closed:
            raise Exception("No se pudo conectar a la base de datos")
        print("✅ Conexión a la base de datos exitosa")

        # Obtener brand_id si no fue provisto
        if brand_id is None:
            brand_id = get_or_create_brand(conn, brand_name)
            if not brand_id:
                raise Exception(f"No se pudo obtener o crear la marca '{brand_name}'")
        print(f"✅ Marca '{brand_name}' con ID: {brand_id}")

        # Definir el archivo por defecto si no se pasa como argumento
        if file_path is None:
            file_path = f'./data/{brand_name}_item_prices.csv'

        # Cargar mapas
        store_map = build_store_mapping(conn, brand_id)
        product_map = build_product_mapping(conn, brand_id)

        not_found_count = 0
        total_imported = 0

        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            with conn.cursor() as cur:
                for row in reader:
                    store_id = store_map.get(row.get('store_id'))
                    product_id = product_map.get(row.get('product_id'))

                    if store_id is None or product_id is None:
                        not_found_count += 1
                        continue

                    # Convertir created_at a formato datetime válido (si es necesario)
                    created_at_raw = row.get('date')
                    try:
                        created_at = datetime.fromisoformat(created_at_raw) if created_at_raw else None
                    except ValueError:
                        created_at = None  # o podrías usar datetime.now()

                    cur.execute("""
                        INSERT INTO item_price (
                            product_id, store_id, status, 
                            unit_price, sale_price, list_price, created_at
                        )
                        VALUES (
                            %(product_id)s, %(store_id)s, %(status)s,
                            %(unit_price)s, %(sale_price)s, %(list_price)s, %(created_at)s
                        )
                    """, {
                        'product_id': product_id,
                        'store_id': store_id,
                        'status': row.get('status'),
                        'unit_price': float(row.get('unit_price') or 0),
                        'sale_price': float(row.get('sale_price') or 0),
                        'list_price': float(row.get('list_price') or 0),
                        'created_at': created_at
                    })
                    total_imported += 1

                conn.commit()

        print(f"✅ {total_imported} precios importados correctamente para '{brand_name}' (ID: {brand_id})")
        if not_found_count > 0:
            print(f"⚠️ {not_found_count} filas omitidas por no encontrar store_id o product_id en los mapas.")

    except Exception as e:
        print(f"❌ Error en el proceso de importación de precios: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("✅ Conexión cerrada")


prices(
    brand_name='sedanos',
    brand_id=None,  # Puedes pasar un ID de marca específico si lo tienes
    file_path='./data/sedanos_item_prices.csv'  # Puedes pasar una ruta de archivo específica si lo tienes
)