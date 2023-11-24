import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from api.config import settings


class Mail:
    host = settings.mail_host
    port = settings.mail_port
    sender_email = settings.mail_key
    password = settings.mail_secret
    server = None
    context = ssl.create_default_context()

    def mail_password_forgot(self, receiver, passwd):
        message = MIMEMultipart('alternative')
        message["Subject"] = "Réinitialisation de votre mot de passe"
        message["From"] = self.sender_email
        message["To"] = receiver

        text = f"""
            Bonjour
            
            Votre mot de passe temporaire: {passwd}
            Utilisez ce mot de passe temporaire pour vous connecter.
            Une fois sur l'interface, rendez-vous dans le menu PROFIL et cliquez sur "Paramètres" pour modifier votre mot de passe
        """

        html = f"""
        <html>
          <body>
            <h1>Bonjour,</h1>
            
            <p>Votre mot de passe temporaire: {passwd}</p>
            <p>Utilisez ce mot de passe temporaire pour vous connecter.</p>
            <p>Une fois sur l'interface, rendez-vous dans le menu PROFIL et cliquez sur "Paramètres" pour modifier votre mot de passe</p>
          </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        return message

    def send(self, receiver, message):
        with smtplib.SMTP(self.host, port=self.port) as server:
            server.starttls(context=self.context)
            server.login(self.sender_email, self.password)
            server.send_message(
                message,
                self.sender_email,
                receiver,
            )
