from app import get_available_products, get_product_by_id, get_all_categories



def test_get_available_products():
    # test the function that gets products
    products = get_available_products()

    # tests if the number of products is 3
    assert len(products) == 3
    
    # check if the products required fields
    assert all('id' in p and 'name' in p and 'description' in p and 'base_price' in p and 'image' in p and 'category' in p for p in products)

    # check if length in the funny products is 2
    assert len(get_available_products('funny')) == 2


def test_get_product_by_id():
    # gets product id 1
    product = get_product_by_id(1)

    # checks the conditions matches the assertion
    assert product and product['id'] == 1 and product['name' == 'Meme Lord']

    # tests that invalid products throw no errors
    assert get_product_by_id(999) is None


def test_get_all_categories():
    # gets the categories
    categories = get_all_categories()
    # checks if theres two categories
    assert len(categories) == 2
    # checks if the categories is 'funny' and 'school'
    assert 'funny' in categories and 'school' in categories