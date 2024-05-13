def merge_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog
    return combined_catalog

# Catalogs
catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

# Merge catalogs
combined_catalog = merge_catalogs(catalog1, catalog2)

# Display combined catalog
print("Combined Catalog:")
for product, price in combined_catalog:
    print(f"Product: {product}, Price: ${price}")
