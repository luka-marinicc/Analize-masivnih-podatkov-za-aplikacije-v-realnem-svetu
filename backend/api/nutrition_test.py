from nutrition_client import NutritionClient

client = NutritionClient()

barcodes = [
    "3017620422003", # Nutella
    "5449000000996", # Coca Cola
]

for barcode in barcodes:
    product = client.get_product_by_barcode(barcode)

    print("Barcode:", barcode)
    print("Name:", product.get("product_name"))
    print("Brand:", product.get("brands"))
    print("Kcal/100g:", product.get("nutriments", {}).get("energy-kcal_100g"))
    print("---")