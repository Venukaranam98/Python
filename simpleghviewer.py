import requests
import logging

logging.basicConfig(level=logging.INFO)


try:

    username = input(
        "Enter GitHub username: "
    )

    response = requests.get(
        f"https://api.github.com/users/{username}"
    )

    if response.status_code == 200:

        data = response.json()

        logging.info(
            "GitHub profile fetched successfully"
        )

        print("\n--- GITHUB PROFILE ---")

        print(
            "Name:",
            data["name"]
        )

        print(
            "Bio:",
            data["bio"]
        )

        print(
            "Followers:",
            data["followers"]
        )

        print(
            "Following:",
            data["following"]
        )

        print(
            "Public Repositories:",
            data["public_repos"]
        )

    else:

        logging.warning(
            "GitHub user not found"
        )

except:

    logging.error(
        "Failed to fetch GitHub profile"
    )