# from project import create_app


# def test_home_page():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/' page is requested (GET)
#     THEN check that the response is valid
#     """
#     # Set the Testing configuration prior to creating the Flask application
#     os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
#     flask_app = create_app()

#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as test_client:
#         response = test_client.get('/')
#         assert response.status_code == 200
#         assert b"Welcome to the" in response.data
#         assert b"Flask User Management Example!" in response.data
#         assert b"Need an account?" in response.data
#         assert b"Existing user?" in response.data