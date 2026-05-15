import logging


logging.basicConfig(

    filename="app.log",

    level=logging.INFO,

    format="%(levelname)s:%(message)s"
)


correct_username = "admin"

correct_password = "1234"


try:

    username = input("Enter username: ")

    password = input("Enter password: ")


    if username == correct_username and password == correct_password:

        logging.info(
            "Successful login attempt"
        )

        print("Login successful")


    elif username != correct_username:

        logging.warning(
            "Invalid username entered"
        )

        print("Wrong username")


    elif password != correct_password:

        logging.warning(
            "Wrong password entered"
        )

        print("Wrong password")


except:

    logging.error(
        "Application error occurred"
    )

    print("Something went wrong")