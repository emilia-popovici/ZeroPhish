from deep_translator import GoogleTranslator
import pprint
import time
from lectii import LECTII

def safe_translate(text, translator):
    if not text or not isinstance(text, str):
        return text
    try:
        time.sleep(0.2) 
        res = translator.translate(text)
        return res
    except Exception as e:
        print(f"⚠️ Eroare la traducerea: '{text[:20]}...'. Păstrez originalul.")
        return text

target_langs = ['en', 'fr', 'ru']

FINAL_DATA = {'ro': LECTII}

print("⏳ Încep traducerea conținutului lecțiilor... ")

for lang in target_langs:
    print(f"\n--> Traduc în limba '{lang}'...")
    translator = GoogleTranslator(source='ro', target=lang)
    
    lessons_translated = {}

    for id_lectie, data in LECTII.items():
        print(f"   ... traduc Lecția {id_lectie}")
        
        new_lesson = {
            "titlu": safe_translate(data['titlu'], translator),
            "descriere": safe_translate(data['descriere'], translator),
            "subcapitole": [],
            "quiz_questions": []
        }

        for sub in data['subcapitole']:
            new_sub = {
                "titlu": safe_translate(sub['titlu'], translator),
                "continut": safe_translate(sub['continut'], translator) 
            }
            new_lesson['subcapitole'].append(new_sub)

        for q in data['quiz_questions']:
            new_variante = []
            for v in q['variante']:
                new_variante.append(safe_translate(v, translator))

            new_corect = []
            for c in q['corect']:
                new_corect.append(safe_translate(c, translator))
            
            new_q = {
                "id": q['id'],
                "intrebare": safe_translate(q['intrebare'], translator),
                "variante": new_variante,
                "corect": new_corect,
                "explicatie": safe_translate(q['explicatie'], translator)
            }
            
            if 'tip' in q:
                new_q['tip'] = q['tip']
                
            new_lesson['quiz_questions'].append(new_q)
            
        lessons_translated[id_lectie] = new_lesson

    FINAL_DATA[lang] = lessons_translated

with open("lectii_multilang.py", "w", encoding="utf-8") as f:
    f.write(f"LECTII_ALL = {pprint.pformat(FINAL_DATA, indent=4)}")

print("\n✅ Gata!")