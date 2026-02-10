from deep_translator import GoogleTranslator
import pprint
import time
import os

from lectii import LECTII

try:
    from lectii_multilang import LECTII_ALL as DATA_EXISTENTA
    print("✅ Am încărcat datele existente din lectii_multilang.py")
except ImportError:
    print("⚠️ Nu am găsit lectii_multilang.py, voi crea un fișier nou.")
    DATA_EXISTENTA = {'ro': {}, 'en': {}, 'fr': {}, 'ru': {}}

IDS_DE_TRADUS = [6, 7, 8]
TARGET_LANGS = ['en', 'fr', 'ru']

def safe_translate(text, translator):
    if not text or not isinstance(text, str):
        return text
    try:
        time.sleep(0.5) 
        return translator.translate(text)
    except Exception as e:
        print(f"⚠️ Eroare: '{text[:20]}...'. Păstrez originalul.")
        return text

if 'ro' not in DATA_EXISTENTA:
    DATA_EXISTENTA['ro'] = {}

for id_lectie in IDS_DE_TRADUS:
    if id_lectie in LECTII:
        DATA_EXISTENTA['ro'][id_lectie] = LECTII[id_lectie]

print(f"⏳ Încep traducerea doar pentru lecțiile: {IDS_DE_TRADUS}...")

for lang in TARGET_LANGS:
    print(f"\n--> Traduc în limba '{lang}'...")
    translator = GoogleTranslator(source='ro', target=lang)
    
    if lang not in DATA_EXISTENTA:
        DATA_EXISTENTA[lang] = {}

    for id_lectie in IDS_DE_TRADUS:
        if id_lectie not in LECTII:
            print(f"   ⚠️ Lecția {id_lectie} nu există în sursa 'lectii.py', o sar.")
            continue

        print(f"   ... traduc Lecția {id_lectie}")
        data = LECTII[id_lectie]
        
        new_lesson = {
            "titlu": safe_translate(data['titlu'], translator),
            "descriere": safe_translate(data['descriere'], translator),
            "subcapitole": [],
            "quiz_questions": []
        }

        for sub in data['subcapitole']:
            new_lesson['subcapitole'].append({
                "titlu": safe_translate(sub['titlu'], translator),
                "continut": safe_translate(sub['continut'], translator) 
            })

        for q in data['quiz_questions']:
            new_variante = [safe_translate(v, translator) for v in q['variante']]
            new_corect = [safe_translate(c, translator) for c in q['corect']]
            
            new_q = {
                "id": q['id'],
                "intrebare": safe_translate(q['intrebare'], translator),
                "variante": new_variante,
                "corect": new_corect,
                "explicatie": safe_translate(q['explicatie'], translator)
            }
            if 'tip' in q: new_q['tip'] = q['tip']
            new_lesson['quiz_questions'].append(new_q)
            
        DATA_EXISTENTA[lang][id_lectie] = new_lesson

print("\n💾 Salvez totul în lectii_multilang.py...")
with open("lectii_multilang.py", "w", encoding="utf-8") as f:
    f.write(f"LECTII_ALL = {pprint.pformat(DATA_EXISTENTA, indent=4, width=120)}")

print("✅ Gata! Lecțiile 6-8 au fost adăugate.")