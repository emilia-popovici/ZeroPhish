import sqlite3

def reset_campaign():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    print("--- ÎNCEP CURĂȚENIA ---")
    
    c.execute("DELETE FROM targets WHERE email NOT LIKE '%@%'")
    deleted = c.rowcount
    if deleted > 0:
        print(f"🧹 Am șters {deleted} adrese invalide/greșite.")
    
    c.execute("UPDATE targets SET current_wave = 0")
    print(f"🔄 Am resetat statusul pentru toți utilizatorii rămași.")
    print("   Acum sunt gata să primească din nou emailul.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    reset_campaign()