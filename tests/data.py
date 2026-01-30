class AuthData:
    """
    Class for grouping login details
    """

    SUCCESSFUL_USERS = ["standard_user", "performance_glitch_user"]

    NEGATIVE_LOGIN_SCENARIOS = [
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
        ("", "", "Username is required"),
    ]
