import smtplib
import sqlite3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
MY_EMAIL = "em.testlicenta@gmail.com"
MY_PASSWORD = "lrjh jqni segz gjjp" 

BASE_URL = "https://subcartilaginous-floricultural-mari.ngrok-free.dev" 

def send_wave():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute("SELECT id, email, unique_token FROM targets WHERE current_wave = 0")
    targets = c.fetchall()
    
    if not targets:
        print("Nu mai sunt ținte pentru Valul 0.")
        return

    for user in targets:
        user_id, email, token = user
        link = f"{BASE_URL}/login?token={token}"
        
        msg = MIMEMultipart()
        msg['From'] = MY_EMAIL
        msg['To'] = email
        msg['Subject'] = "Confirmare necesară"
        
        body = f"""
        Salut, 
        Te rugam sa accesezi linkul pentru verificare: {link}
        """
        msg.attach(MIMEText(body, 'plain'))
        
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(MY_EMAIL, MY_PASSWORD)
            server.sendmail(MY_EMAIL, email, msg.as_string())
            print(f"Mail trimis către {email}")
            
            c.execute("UPDATE targets SET current_wave = 1 WHERE id=?", (user_id,))
            conn.commit()
            server.quit()
        except Exception as e:
            print(f"Eroare: {e}")

    conn.close()

if __name__ == "__main__":
    send_wave()