import sqlite3

def remove_duplicates():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    print("--- Caut duplicate... ---")
    
    c.execute('''
        DELETE FROM targets 
        WHERE id NOT IN (
            SELECT MIN(id) 
            FROM targets 
            GROUP BY email
        )
    ''')
    
    deleted_count = c.rowcount
    
    if deleted_count > 0:
        print(f"✅ Am șters {deleted_count} duplicate.")
    else:
        print("👍 Nu am găsit duplicate. Baza de date e curată.")
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    remove_duplicates()