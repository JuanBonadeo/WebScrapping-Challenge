WITH price_dispersion AS (
    SELECT 
        b.brand_name AS cadena,
        p.product_id,
        p.product_name,
        p.upc,
        p.size,
        p.brand AS product_brand,
        MAX(ip.unit_price) - MIN(ip.unit_price) AS dispersion,
        COUNT(DISTINCT ip.store_id) AS tiendas_con_producto
    FROM 
        product p
    JOIN 
        category c ON p.category_id = c.category_id
    JOIN 
        brand b ON c.brand_id = b.brand_id
    JOIN 
        item_price ip ON p.product_id = ip.product_id
    GROUP BY 
        b.brand_name, p.product_id, p.product_name, p.upc, p.size, p.brand
    HAVING 
        COUNT(DISTINCT ip.store_id) >= 3
),
top10_products AS (
    SELECT 
        product_id
    FROM 
        price_dispersion 
    ORDER BY 
        dispersion DESC 
    LIMIT 10
),
max_price_per_product AS (
    SELECT DISTINCT ON (ip.product_id)
        ip.product_id,
        ip.unit_price,
        ip.created_at,
        s.store_id,
        s.address,
        s.city,
        s.state
    FROM item_price ip
    JOIN store s ON ip.store_id = s.store_id
    WHERE ip.product_id IN (SELECT product_id FROM top10_products)
    ORDER BY ip.product_id, ip.unit_price DESC  -- precio más alto
)

SELECT 
    pd.cadena,
    pd.product_name AS name,
    pd.upc,
    pd.size,
    pd.product_brand,
    mp.unit_price AS price,
    mp.created_at,
    pd.dispersion,
    pd.tiendas_con_producto,
    mp.address,
    mp.city,
    mp.state
FROM 
    price_dispersion pd
JOIN 
    max_price_per_product mp ON pd.product_id = mp.product_id
WHERE 
    pd.product_id IN (SELECT product_id FROM top10_products)
ORDER BY 
    pd.dispersion DESC;
