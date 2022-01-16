import pprint
from woocommerce import API

wcapi = API(
    url="http://127.0.0.1:8000/",  # Your store URL
    consumer_key="ck_6ef1050c8cc850a035886e9508be84f8c83a04a9",  # Your consumer key
    consumer_secret="cs_1f93a3ea8e107e858552aecd629b997ab140a6cb",  # Your consumer secret
    wp_api=True,  # Enable the WP REST API integration
    version="wc/v3"  # WooCommerce WP REST API version
)

# r = wcapi.get('products')
print(wcapi.get("products"))
pprint.pprint(wcapi.get("products").json())
