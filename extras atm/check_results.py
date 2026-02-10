import sqlite3

def view_logs():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    print("\n--- JURNAL CLICK-URI (VICTIME) ---")
    c.execute('''
        SELECT targets.email, logs.clicked_at, logs.ip_address 
        FROM logs 
        JOIN targets ON logs.target_id = targets.id
    ''')
    
    rows = c.fetchall()
    
    if not rows:
        print("Încă nu a dat nimeni click (sau baza e goală).")
    else:
        for row in rows:
            email, time, ip = row
            print(f"Victima: {email} | Ora: {time} | IP: {ip}")
            
    print("----------------------------------\n")
    conn.close()

if __name__ == "__main__":
    view_logs()