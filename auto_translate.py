from deep_translator import GoogleTranslator
import pprint

source_texts = {
    'nav_dashboard': 'Dashboard',
    'nav_scores': 'Scoruri',
    'nav_lang': 'Limbă',
    'nav_settings': 'Setări Cont',
    'nav_logout': 'Ieșire / Log out',
    
    'dash_title': 'Educație Digitală',
    'dash_subtitle': 'Învață să detectezi capcanele digitale pas cu pas.',
    'lbl_progress': 'Progres',
    'btn_start': 'Începe Lecția',
    'btn_theory': 'Citește Teoria',
    'btn_quiz': 'Rezolvă Quiz',
    
    'prof_title': 'Statistici și progres personal',
    'prof_total': 'TOTAL',
    'prof_avg': 'media tuturor lecțiilor',
    'btn_back_dash': 'Înapoi la Dashboard',
    
    'set_title': 'Configurare cont',
    'btn_chg_user': 'Schimbă username-ul',
    'btn_chg_photo': 'Schimbă poza de profil',
    'btn_rst_pass': 'Resetează Parola',
    'btn_del_acc': 'Șterge Contul',
    
    'mod_user_title': 'Schimbă Username-ul',
    'lbl_new_name': 'Noul username:',
    
    'mod_photo_title': 'Alege Imagine',
    'lbl_pick_file': 'Alege o imagine (jpg, png):',
    
    'mod_pass_title': 'Resetează Parola',
    'lbl_old_pass': 'Parola Veche:',
    'lbl_new_pass': 'Parola Nouă:',
    
    'mod_del_title': 'Confirmare',
    'msg_del_warn': 'Ești sigur? Vei pierde tot progresul.',
    
    'btn_save': 'Salvează',
    'btn_cancel': 'Anulează',
    'btn_upload': 'Încarcă',
    'btn_yes_del': 'Da, Șterge',
    'btn_no': 'Nu',

    'auth_login': 'Autentificare',
    'auth_register': 'Înregistrare',
    'lbl_user': 'Nume utilizator',
    'lbl_pass': 'Parolă',
    'btn_enter': 'Intră în cont',
    'btn_create': 'Creează cont',
    'link_no_acc': 'Nu ai cont? Înregistrează-te',
    'link_has_acc': 'Ai deja cont? Loghează-te',

    'btn_back_menu': 'Înapoi la Meniu',
    'msg_theory_done': 'Ai parcurs toată teoria!',
    'msg_quiz_ready': 'Ești pregătit să te testezi și să obții punctajul maxim?',
    'btn_start_quiz': 'Începe Quiz-ul',

    'quiz_page_title': 'Quiz:',
    'lbl_question_no': 'Întrebarea',
    'lbl_select_correct': 'Selectează răspunsul corect:',
    'btn_next_q': 'Următoarea',
    'btn_finish_quiz': 'Vezi Rezultatele',
    'msg_bravo': 'Bravo! Iată rezultatul tău:',
    'lbl_report': 'Raport Detaliat:',
    'btn_restart': 'Reia Lecția',
    'btn_main_menu': 'Meniu Principal',
    
    'js_multi_choice': '(Atenție: Sunt mai multe răspunsuri corecte! Selectează-le pe toate)',
    'js_single_choice': '(Selectează un singur răspuns)',
    'js_alert_select': 'Te rog selectează cel puțin o variantă!',
    'js_you_chose': 'Tu ai ales:',
    'js_correct_was': 'Corect era:',
    'js_correct_msg': 'Răspuns Corect!'
}

target_langs = ['en', 'fr', 'ru']

final_dict = {'ro': source_texts}

print("Începe traducerea completă a platformei...")

for lang in target_langs:
    print(f"--> Traducere în '{lang}'...")
    translated_section = {}
    
    for key, text in source_texts.items():
        try:
            traducere = GoogleTranslator(source='ro', target=lang).translate(text)
            translated_section[key] = traducere
        except Exception as e:
            print(f"Eroare la '{text}': {e}")
            translated_section[key] = text 
            
    final_dict[lang] = translated_section

file_content = f"TEXTE = {pprint.pformat(final_dict, indent=4)}"

with open("texte.py", "w", encoding="utf-8") as f:
    f.write(file_content)

print("\n✅ Gata!")