"""
import sqlite3
import uuid 

def add_new_target():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    token_nou = str(uuid.uuid4())
    
    try:
        c.execute("INSERT INTO targets (email, unique_token, current_wave) VALUES (?, ?, 0)", 
                  (NOUA_ADRESA, token_nou))
        conn.commit()
        print(f"Am adăugat {NOUA_ADRESA} în baza de date!")
        print(f"Token generat: {token_nou}")
    except Exception as e:
        print(f"Eroare: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    add_new_target()
    """