
from google.appengine.api import mail

class ConfirmUserSignup():
    def send(self,email_address,verification_url):
        if not mail.is_email_valid(email_address):
            # prompt user to enter a valid address
            logging.info('invalid email address')
        else:
            confirmation_url = verification_url
            sender_address = "email@example.com"
            subject = "Confirm your registration"
            body = """
Thank you for creating an account! Please confirm your email address by
clicking on the link below:

%s
""" % confirmation_url

            mail.send_mail(sender_address, email_address, subject, body)