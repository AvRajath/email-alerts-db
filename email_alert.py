import time
import os

def getEnvVars():
    print("Getting environment variables")
    email_user = os.getenv("EMAIL_USER")
    email_pass = os.getenv("EMAIL_PASS")
    email_reci = os.getenv("EMAIL_RECI")
    print(email_pass, email_user, email_reci)

if __name__ == "__main__":
    getEnvVars()