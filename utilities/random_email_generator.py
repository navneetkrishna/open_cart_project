import random


def generate_email():
    """
  This function generates a random email address.

  Returns:
    A string containing the randomly generated email address.
  """
    # Define valid characters for the username part of the email
    valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789.-"

    # Choose random username length between 4 and 15 characters
    username_length = random.randint(4, 15)

    # Generate random username using valid characters
    username = "".join(random.choice(valid_chars) for _ in range(username_length))

    # Define a list of common email providers
    servers = ["gmail", "yahoo", "hotmail", "outlook"]

    # Choose a random server
    server = random.choice(servers)

    # Define a list of top-level domains (TLDs)
    tlds = ["com", "net", "org", "us"]

    # Choose a random TLD
    tld = random.choice(tlds)

    # Combine username, server, and TLD to form the email address
    email = f"{username}@{server}.{tld}"

    return email
