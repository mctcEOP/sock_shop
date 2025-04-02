from app import app


def test_empty_cart_redirect():
    with app.test_client() as client:

        # Set and empty cart for the session
        with client.session_transaction() as session:

            session['cart'] = []

        # try to get response from checkout

        response = client.get('/checkout', follow_redirects=True)

        # checks if redirect is home
        assert response.request.path == '/'