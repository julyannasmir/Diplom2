class Ingredients:
    INGREDIENTS = {"ingredients": ["61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa6f"]}
    WITHOUT_INGREDIENTS = {"ingredients": []}
    INVALID_HASH_INGREDIENTS = payload = {"ingredients": ["invalid hash", "12432ddd"]}


class ErrorMessages:
    SERVER_ERROR = "Internal Server Error"
    UNAUTHORIZED = "You should be authorised"
    ALREADY_EXIST_USER = 'User already exists'
    INCORRECT_DATA = "email or password are incorrect"
    REQUIRED_FIELDS = "Email, password and name are required fields"
    INGREDIENT_ERROR = "Ingredient ids must be provided"
