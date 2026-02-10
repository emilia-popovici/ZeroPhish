LECTII = {
    1: {
        "titlu": "1. Ce este phishing-ul?",
        "descriere": "Definiții, psihologia din spate și diferența față de scam.",
        "subcapitole": [
            {
                "titlu": "Introducere în phishing",
                "continut": """
                    <p>Trăim într-o lume digitală în care comunicarea se face rapid: email, SMS, social media, aplicații de mesagerie. Această viteză este exploatată de atacatori printr-un tip de atac numit <strong>phishing</strong>, una dintre cele mai răspândite și eficiente metode de fraudă online.</p>
                    <p>Phishing-ul nu se bazează pe hacking complex, ci pe <strong>manipularea oamenilor</strong>. Atacatorii încearcă să convingă victima să ofere informații sensibile sau să facă o acțiune periculoasă, fără să își dea seama.</p>
                """
            },
            {
                "titlu": "Ce este phishing-ul? (Definiții)",
                "continut": """
                    <div class="alert alert-light">
                        <h5>Definiție simplă:</h5>
                        <p>Phishing-ul este o metodă de atac prin care o persoană este păcălită să ofere informații confidențiale (parole, coduri, date bancare) sau să acceseze link-uri periculoase, crezând că mesajul provine de la o sursă legitimă.</p>
                    </div>
                    
                    <div class="alert alert-secondary">
                        <h5>Definiție tehnică:</h5>
                        <p>Phishing-ul este un atac de tip <strong>social engineering</strong> în care atacatorul se dă drept o entitate de încredere (bancă, companie, prieten, instituție) pentru a obține acces neautorizat la date sau sisteme informatice.</p>
                    </div>
                    
                    <div class="mt-4 p-4 rounded" style="background-color: #fffde7; border: 2px dashed #f6e58d;">
                        <strong>Important:</strong> Phishing-ul nu atacă calculatorul (software-ul), ci utilizatorul (omul).
                    </div>
                """
            },
            {
                "titlu": "De ce funcționează?",
                "continut": """
                    <p>Phishing-ul funcționează pentru că exploatează comportamente umane naturale:</p>
                    <ul>
                        <li><strong>Încrederea:</strong> Mesajele par să vină de la surse cunoscute.</li>
                        <li><strong>Graba:</strong> Mesaje tip "acționează acum" sau "ultimul avertisment".</li>
                        <li><strong>Frica:</strong> Amenințări cu pierderea contului sau blocarea banilor.</li>
                        <li><strong>Curiozitatea:</strong> Promisiuni de premii, facturi neașteptate.</li>
                        <li><strong>Oboseala / Lipsa de atenție:</strong> Utilizatorii nu verifică detaliile tehnice.</li>
                    </ul>
                    <p>Atacatorii știu că oamenii nu citesc cu atenție fiecare mesaj și profită de acest lucru.</p>
                """
            },
            {
                "titlu": "Scurt istoric",
                "continut": """
                    <ul>
                        <li><strong>Anii 1990:</strong> Primele atacuri apar pe AOL, unde utilizatorii erau păcăliți să ofere parole.</li>
                        <li><strong>2000–2010:</strong> Phishing-ul prin email devine foarte popular (ținte: PayPal, eBay, bănci).</li>
                        <li><strong>2010–2020:</strong> Apar variante mai sofisticate: spear phishing, clone phishing.</li>
                        <li><strong>2020–prezent:</strong> Phishing pe social media, SMS, aplicații de mesagerie, QR codes, mesaje generate de AI.</li>
                    </ul>
                    <p><em>Phishing-ul a evoluat odată cu tehnologia și este acum mai greu de recunoscut decât oricând.</em></p>
                """
            },
            {
                "titlu": "Phishing vs. Scam vs. Fraudă",
                "continut": """
                    <table class="table table-bordered">
                        <thead style="background-color: #7E8C69; color: white;">
                            <tr>
                                <th>Termen</th>
                                <th>Ce înseamnă</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Phishing</strong></td>
                                <td>Păcălirea victimei pentru a obține <strong>date</strong> (parole, carduri) sau acces.</td>
                            </tr>
                            <tr>
                                <td><strong>Scam</strong></td>
                                <td>Înșelătorie generală, de obicei promisiuni false (bani, investiții, "Prințul Nigerian"). Țintește banii direct.</td>
                            </tr>
                            <tr>
                                <td><strong>Fraudă online</strong></td>
                                <td>Termen larg ce include phishing, scam, furt de identitate, etc.</td>
                            </tr>
                        </tbody>
                    </table>
                    <p><strong>Concluzie:</strong> Phishing-ul este un tip specific de fraudă online, axat pe furt de date sau acces.</p>
                """
            },
            {
                "titlu": "Exemple reale",
                "continut": """
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">✉️ 1. Email fals de la bancă</h5>
                                    <p class="card-text"><em>„Contul tău va fi suspendat în 24h. Verifică datele aici.”</em><br>Link-ul duce la un site fals care copiază pagina băncii.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">📱 2. Smishing (SMS)</h5>
                                    <p class="card-text"><em>„Pachetul tău nu a putut fi livrat. Actualizează adresa.”</em><br>Victima introduce datele cardului pe un site fals pentru o "taxă mică".</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">🎭 3. Mesaj de la un prieten</h5>
                                    <p class="card-text"><em>„Vezi poza asta? 😂” + link</em><br>Contul prietenului a fost compromis și trimite spam automat.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">🍎 4. Notificare Apple / Google</h5>
                                    <p class="card-text"><em>„Apple ID-ul tău a fost blocat. Autentifică-te acum.”</em><br>Pagina de login arată identic cu cea reală.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Care este cea mai completă definiție a phishing-ului?",
                "variante": [
                    "Un virus care infectează calculatorul", 
                    "O metodă de manipulare prin care utilizatorii sunt păcăliți să ofere date", 
                    "Un atac exclusiv asupra serverelor",
                    "O problemă hardware"
                ],
                "corect": ["O metodă de manipulare prin care utilizatorii sunt păcăliți să ofere date"], 
                "explicatie": "Phishing-ul atacă omul (psihologia), nu mașina (hardware-ul)."
            },
            {
                "id": 2,
                "intrebare": "De ce funcționează phishing-ul? (Selectează toate variantele corecte)",
                "variante": [
                    "Exploatează frica și urgența",
                    "Profită de încrederea utilizatorilor",
                    "Necesită cunoștințe tehnice avansate din partea victimei",
                    "Se bazează pe lipsa de atenție"
                ],
                "corect": [
                    "Exploatează frica și urgența", 
                    "Profită de încrederea utilizatorilor", 
                    "Se bazează pe lipsa de atenție"
                ],
                "explicatie": "Este o combinație de factori psihologici și neatenție, nu necesită cunoștințe tehnice din partea victimei."
            },
            {
                "id": 3,
                "intrebare": "Unde au apărut primele atacuri de phishing?",
                "variante": ["Facebook", "Email bancar", "AOL", "Instagram"],
                "corect": ["AOL"],
                "explicatie": "În anii '90, pe AOL, hackerii furau conturile utilizatorilor pentru internet gratuit."
            },
            {
                "id": 4,
                "intrebare": "Care afirmație este corectă legată de Scam vs Phishing?",
                "variante": [
                    "Scam și phishing sunt exact același lucru",
                    "Phishing-ul este un tip de fraudă online axat pe furt de date",
                    "Frauda online este un tip de phishing",
                    "Phishing-ul nu implică manipularea utilizatorului"
                ],
                "corect": ["Phishing-ul este un tip de fraudă online axat pe furt de date"],
                "explicatie": "Phishing-ul vrea datele tale sensibile, în timp ce scam-ul țintește de obicei banii direct."
            },
            {
                "id": 5,
                "intrebare": "Care dintre următoarele pot fi exemple de phishing? (Selectează multiple)",
                "variante": [
                    "Email de la „bancă” cu link urgent",
                    "Mesaj de la un prieten cu link suspect",
                    "SMS legitim cu un cod 2FA cerut de tine",
                    "SMS despre un colet neașteptat"
                ],
                "corect": [
                    "Email de la „bancă” cu link urgent",
                    "Mesaj de la un prieten cu link suspect",
                    "SMS despre un colet neașteptat"
                ],
                "explicatie": "Doar SMS-ul cu codul cerut de tine este sigur. Restul sunt tentative de manipulare."
            },
            {
                "id": 6,
                "intrebare": "Ce atacă phishing-ul în primul rând?",
                "variante": ["Calculatorul", "Rețeaua", "Utilizatorul (Omul)", "Hardware-ul"],
                "corect": ["Utilizatorul (Omul)"],
                "explicatie": "Phishing-ul este o formă de inginerie socială care țintește mintea umană."
            }
        ]
    },

    2: {
        "titlu": "2. Tipuri de phishing",
        "descriere": "O analiză detaliată a vectorilor de atac: de la Email și SMS, până la metode avansate precum AI și QR.",
        "subcapitole": [
            {
                "titlu": "Introducere și Email Phishing",
                "continut": """
                    <p>Phishing-ul nu apare într-o singură formă. Atacatorii își adaptează metodele în funcție de platformă, public și context. Unele atacuri sunt trimise în masă („pescuit cu năvodul”), altele sunt extrem de personalizate („pescuit cu harponul”).</p>
                    
                    <div class="alert alert-secondary">
                        <h5>📧 Email Phishing</h5>
                        <p>Este cea mai răspândită formă. Se bazează pe volum mare și mesaje generice.</p>
                        <hr>
                        <strong>Caracteristici:</strong>
                        <ul>
                            <li>Mesaje trimise în masă.</li>
                            <li>Se dau drept bănci, companii sau servicii populare.</li>
                            <li>Conțin link-uri malițioase sau atașamente infectate.</li>
                        </ul>
                        <p><strong>Exemple:</strong> „Contul tău a fost suspendat”, „Factura atașată este urgentă”.</p>
                        <p>👉 <em>Scopul: furt de date sau instalare de malware.</em></p>
                    </div>
                """
            },
            {
                "titlu": "Atacuri pe mobil: Smishing și Vishing",
                "continut": """
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">💬 Smishing (SMS Phishing)</h5>
                                    <p><strong>Caracteristici:</strong> Mesaje scurte, ton urgent, link-uri scurtate (bit.ly etc).</p>
                                    <p><strong>Exemple:</strong> „Coletul tău nu a putut fi livrat”, „Ai o amendă neplătită”.</p>
                                    <div class="alert alert-light p-2">👉 Periculos pentru că avem tendința să credem că SMS-urile sunt sigure.</div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">📞 Vishing (Voice Phishing)</h5>
                                    <p><strong>Caracteristici:</strong> Apeluri telefonice. Atacatorul pretinde că este de la bancă, poliție sau IT support.</p>
                                    <p><strong>Exemple:</strong> „Cineva încearcă să îți acceseze contul”, „Dă-mi codul primit prin SMS”.</p>
                                    <div class="alert alert-light p-2">👉 Se bazează pe presiune verbală directă.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                """
            },
            {
                "titlu": "Social Media și Atacuri Țintite",
                "continut": """
                    <p>Atacurile s-au mutat și pe Instagram, Facebook, WhatsApp sau LinkedIn.</p>
                    
                    <div class="mt-4 p-4 rounded" style="background-color: #fffde7; border: 2px dashed #f6e58d;">
                        <h5>👥 Phishing pe Social Media</h5>
                        <p>Aici, <strong>încrederea</strong> este arma principală. Mesajele par să vină de la prieteni (conturi compromise).</p>
                        <p><em>Exemplu clasic: „Ești tu în videoclipul ăsta?” + link ciudat.</em></p>
                    </div>
                    
                    <br>
                    
                    <div class="alert alert-primary">
                        <h5>🎯 Spear Phishing (Atacul Țintit)</h5>
                        <p>Spre deosebire de email-urile în masă, acesta este personalizat.</p>
                        <ul>
                            <li>Folosește numele real al victimei.</li>
                            <li>Face referire la detalii reale (locul de muncă, colegi).</li>
                            <li>Pare extrem de credibil.</li>
                        </ul>
                        <p>👉 <em>Foarte periculos în mediul corporate.</em></p>
                    </div>
                """
            },
            {
                "titlu": "Metode Avansate și Moderne",
                "continut": """
                    <table class="table table-bordered">
                        <thead style="background-color: #7E8C69; color: white;">
                            <tr>
                                <th>Tip Atac</th>
                                <th>Descriere</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Clone Phishing</strong></td>
                                <td>Atacatorul copiază un email legitim vechi, dar înlocuiește link-ul sau atașamentul cu unul malițios. <em>„Retrimit documentul, te rog verifică.”</em></td>
                            </tr>
                            <tr>
                                <td><strong>BEC (Business Email Compromise)</strong></td>
                                <td>Vizează companiile. Atacatorul se dă drept CEO sau partener și cere un transfer bancar urgent. Produce pagube financiare masive.</td>
                            </tr>
                            <tr>
                                <td><strong>Phishing Modern (AI & QR)</strong></td>
                                <td><strong>QR Phishing:</strong> Coduri QR care duc spre site-uri false.<br><strong>AI Phishing:</strong> Mesaje scrise perfect gramatical de roboți, deepfake audio.</td>
                            </tr>
                        </tbody>
                    </table>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Ce caracterizează email phishing-ul?",
                "variante": [
                    "Mesaje vocale",
                    "Mesaje trimise în masă ce imită companii reale",
                    "Mesaje doar pe Instagram",
                    "Apeluri telefonice"
                ],
                "corect": ["Mesaje trimise în masă ce imită companii reale"],
                "explicatie": "Email phishing-ul se bazează pe volum (mesaje în masă) și impersonarea brandurilor cunoscute."
            },
            {
                "id": 2,
                "intrebare": "Ce este smishing-ul?",
                "variante": [
                    "Phishing prin email",
                    "Phishing prin SMS",
                    "Phishing prin apeluri",
                    "Phishing prin QR coduri"
                ],
                "corect": ["Phishing prin SMS"],
                "explicatie": "Termenul vine de la SMS + Phishing."
            },
            {
                "id": 3,
                "intrebare": "Ce elemente pot apărea într-un atac de vishing? (Selectează multiple)",
                "variante": [
                    "Apel telefonic",
                    "Cerere de coduri sau date",
                    "Link-uri din email",
                    "Pretinderea unei autorități"
                ],
                "corect": [
                    "Apel telefonic",
                    "Cerere de coduri sau date",
                    "Pretinderea unei autorități"
                ],
                "explicatie": "Vishing-ul (Voice Phishing) implică apeluri, presiune și impersonarea unor autorități (bancă, poliție)."
            },
            {
                "id": 4,
                "intrebare": "Care dintre următoarele sunt caracteristice phishing-ului pe social media? (Selectează multiple)",
                "variante": [
                    "Mesaje de la conturi cunoscute (compromise)",
                    "Link-uri suspecte („șocante” sau „amuzante”)",
                    "Atașamente fizice prin poștă",
                    "Exploatarea încrederii"
                ],
                "corect": [
                    "Mesaje de la conturi cunoscute (compromise)",
                    "Link-uri suspecte („șocante” sau „amuzante”)",
                    "Exploatarea încrederii"
                ],
                "explicatie": "Social media phishing se bazează pe curiozitate și încrederea în prieteni."
            },
            {
                "id": 5,
                "intrebare": "Ce face spear phishing-ul diferit?",
                "variante": [
                    "Este trimis la întâmplare",
                    "Nu conține date reale",
                    "Este personalizat pentru o țintă",
                    "Se face doar prin SMS"
                ],
                "corect": ["Este personalizat pentru o țintă"],
                "explicatie": "Spear (harpon) sugerează precizia. Atacatorul are informații specifice despre victimă."
            },
            {
                "id": 6,
                "intrebare": "Ce presupune clone phishing-ul?",
                "variante": [
                    "Crearea unui virus nou",
                    "Copierea unui mesaj legitim și modificarea lui",
                    "Trimiterea de SMS-uri",
                    "Apeluri telefonice"
                ],
                "corect": ["Copierea unui mesaj legitim și modificarea lui"],
                "explicatie": "Atacatorul 'clonează' un email real anterior pentru a păcăli vigilența victimei."
            },
            {
                "id": 7,
                "intrebare": "Ce tip de phishing vizează în special companiile și departamentele financiare?",
                "variante": [
                    "Smishing",
                    "Social media phishing",
                    "Business Email Compromise (BEC)",
                    "QR phishing"
                ],
                "corect": ["Business Email Compromise (BEC)"],
                "explicatie": "BEC este specializat pe fraudarea companiilor prin impersonarea directorilor."
            },
            {
                "id": 8,
                "intrebare": "Care sunt forme moderne de phishing? (Selectează multiple)",
                "variante": [
                    "QR phishing",
                    "AI-generated messages",
                    "Email simplu fără link",
                    "Fake support chat"
                ],
                "corect": [
                    "QR phishing",
                    "AI-generated messages",
                    "Fake support chat"
                ],
                "explicatie": "Tehnologia a adus vectori noi precum codurile QR și inteligența artificială."
            }
        ]
    },
    3: {
        "titlu": "3. Psihologia din spatele phishing-ului",
        "descriere": "Mecanismele mentale, ingineria socială și de ce nimeni nu este imun.",
        "subcapitole": [
            {
                "titlu": "Ingineria Socială: Atacul asupra minții",
                "continut": """
                    <p>Phishing-ul nu este un atac tehnic, ci unul <strong>psihologic</strong>. În majoritatea cazurilor, atacatorii nu sparg sisteme, ci conving oameni să facă singuri acțiuni periculoase.</p>
                    
                    <div class="alert alert-secondary">
                        <h5>🧠 Ce este Ingineria Socială?</h5>
                        <p>Ingineria socială reprezintă manipularea comportamentului uman pentru a obține informații sau acces. În phishing:</p>
                        <ul>
                            <li>Atacatorul se dă drept cineva de încredere.</li>
                            <li>Mesajul este construit pentru a provoca o reacție emoțională puternică.</li>
                            <li>Victima acționează fără verificare.</li>
                        </ul>
                    </div>
                """
            },
            {
                "titlu": "Emoțiile principale: Frica și Urgența",
                "continut": """
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">😨 Frica</h5>
                                    <p>Frica reduce gândirea critică. Atacatorii amenință cu:</p>
                                    <ul>
                                        <li>Blocarea contului bancar.</li>
                                        <li>Pierderea accesului la date.</li>
                                        <li>Activități ilegale false.</li>
                                    </ul>
                                    <p><em>Exemplu: „Contul tău va fi suspendat definitiv.”</em></p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">⏳ Urgența</h5>
                                    <p>Presiunea timpului forțează victima să acționeze fără să gândească.</p>
                                    <ul>
                                        <li>„Ai 24 de ore să răspunzi.”</li>
                                        <li>„Ultimul avertisment.”</li>
                                        <li>„Acționează acum!”</li>
                                    </ul>
                                    <p><em>Exemplu: „Confirmă datele acum sau pierzi accesul.”</em></p>
                                </div>
                            </div>
                        </div>
                    </div>
                """
            },
            {
                "titlu": "Alți factori psihologici: Autoritate, Recompensa, Curiozitate",
                "continut": """
                    <table class="table table-bordered">
                        <thead style="background-color: #7E8C69; color: white;">
                            <tr>
                                <th>Factor</th>
                                <th>Cum funcționează</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Autoritatea</td>
                                <td>Oamenii tind să respecte instituțiile. Atacatorii se dau drept Bănci, Poliție, ANAF, Apple, Google sau departamentul IT.</td>
                            </tr>
                            <tr>
                                <td>Recompensa</td>
                                <td>Exploatează lăcomia sau dorința de câștig. Exemple: mesajele de la "Poșta României", premii false, reduceri incredibile, investiții „sigure”. Victima vede beneficiul, nu riscul.</td>
                            </tr>
                            <tr>
                                <td>Curiozitatea</td>
                                <td>Declanșează click-ul înainte de gândire. Exemple: <em>„Ești tu în acest video?”, „Document confidențial salarii”</em>.</td>
                            </tr>
                        </tbody>
                    </table>
                """
            },
            {
                "titlu": "Familiaritatea și Bias-uri Cognitive",
                "continut": """
                    <div class="mt-4 p-4 rounded" style="background-color: #fffde7; border: 2px dashed #f6e58d;">
                        <h5>🤝 De ce funcționează mesajele de la „prieteni”?</h5>
                        <p>Dacă un mesaj vine de la un coleg sau prieten (chiar dacă contul lui a fost spart), vigilența noastră scade dramatic. Aceasta este <strong>Familiaritatea</strong>.</p>
                    </div>
                    
                    <br>
                    
                    <p>Atacatorii exploatează și erori de gândire (bias-uri):</p>
                    <ul>
                        <li><strong>Bias-ul de confirmare:</strong> Vedem ce vrem să vedem (ex: un email așteptat).</li>
                        <li><strong>Efectul de turmă:</strong> „Toți au dat click, e sigur.”</li>
                        <li><strong>Oboseala / Automatismul:</strong> Utilizatorii care citesc pe diagonală sau folosesc telefonul noaptea sunt mult mai vulnerabili.</li>
                    </ul>
                """
            },
            {
                "titlu": "Concluzie: Cine este imun?",
                "continut": """
                    <div class="alert alert-danger">
                        <h5>🚫 Nimeni nu este imun!</h5>
                        <p>Chiar și experții IT, managerii sau profesorii pot cădea victime. Phishing-ul nu ține de inteligență, ci de <strong>context</strong> (oboseală, neatenție, un mesaj foarte bine personalizat).</p>
                    </div>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Phishing-ul este în principal un atac de ce tip?",
                "variante": [
                    "Strict Tehnic (Hardware)",
                    "Psihologic (Social Engineering)",
                    "Fizic",
                    "Doar software"
                ],
                "corect": ["Psihologic (Social Engineering)"],
                "explicatie": "Phishing-ul manipulează mintea umană, nu codul sursă al calculatorului."
            },
            {
                "id": 2,
                "intrebare": "Ce înseamnă ingineria socială?",
                "variante": [
                    "Construirea de rețele sociale",
                    "Manipularea comportamentului uman pentru a obține date",
                    "Programare avansată în Python",
                    "Repararea serverelor"
                ],
                "corect": ["Manipularea comportamentului uman pentru a obține date"],
                "explicatie": "Este arta de a convinge oamenii să divulge informații confidențiale."
            },
            {
                "id": 3,
                "intrebare": "Ce emoții sunt frecvent exploatate în phishing? (Selectează multiple)",
                "variante": [
                    "Frica (de a pierde contul)",
                    "Urgența (timp limitat)",
                    "Curiozitatea",
                    "Relaxarea și calmul"
                ],
                "corect": [
                    "Frica (de a pierde contul)",
                    "Urgența (timp limitat)",
                    "Curiozitatea"
                ],
                "explicatie": "Relaxarea nu este dorită de atacatori; ei vor să te panicheze sau să te facă curios pentru a acționa rapid."
            },
            {
                "id": 4,
                "intrebare": "De ce sunt periculoase mesajele de phishing care vin de la prieteni sau colegi?",
                "variante": [
                    "Sunt mereu mai lungi",
                    "Scad vigilența datorită familiarității",
                    "Nu conțin niciodată link-uri",
                    "Sunt imposibil de șters"
                ],
                "corect": ["Scad vigilența datorită familiarității"],
                "explicatie": "Avem tendința să avem încredere în numele cunoscute, verificând mai puțin detaliile tehnice."
            },
            {
                "id": 5,
                "intrebare": "Care dintre următoarele bias-uri cognitive sunt exploatate? (Selectează multiple)",
                "variante": [
                    "Bias-ul de confirmare",
                    "Autoritatea",
                    "Atenția distributivă perfectă"
                ],
                "corect": [
                    "Bias-ul de confirmare",
                    "Autoritatea"
                ],
                "explicatie": "Atacatorii se folosesc de respectul față de autoritate și de tendința noastră de a confirma ceea ce credem deja."
            },
            {
                "id": 6,
                "intrebare": "Cine poate cădea victimă unui atac de phishing?",
                "variante": [
                    "Doar persoanele în vârstă",
                    "Doar persoanele non-tehnice",
                    "Oricine, indiferent de experiență",
                    "Doar copiii"
                ],
                "corect": ["Oricine, indiferent de experiență"],
                "explicatie": "Nimeni nu este imun. Contextul (oboseala, graba) contează mai mult decât cunoștințele tehnice."
            }
        ]
    },
    4: {
        "titlu": "4. Cum recunoști un mesaj de phishing",
        "descriere": "Red flags, semne de avertizare și analiza practică a mesajelor (Email, SMS, Social Media).",
        "subcapitole": [
            {
                "titlu": "1. Primul indiciu: Cine trimite mesajul?",
                "continut": """
                    <p>Atacurile de phishing nu se bazează pe vulnerabilități tehnice, ci pe neatenție. Primul lucru pe care trebuie să îl verifici este <strong>Expeditorul</strong>.</p>
                    
                    <div class="alert alert-danger">
                        <h5>🚩 Red Flag: Adresa de email</h5>
                        <p>Numele afișat („Banca Ta”) poate fi falsificat ușor. Uită-te întotdeauna la adresa reală de email (dă click pe numele expeditorului).</p>
                        <hr>
                        <strong>Exemplu de atac:</strong><br>
                        De la: <strong>Banca Transilvania Suport</strong> <em>&lt;secure@banca-ta-login-alert.com&gt;</em>
                        <br><br>
                        <strong>Ce e greșit?</strong>
                        <ul>
                            <li>Domeniul nu este cel oficial (ex: <em>bancatransilvania.ro</em>).</li>
                            <li>Folosirea cuvintelor alarmiste: <em>secure, login, alert</em>.</li>
                        </ul>
                    </div>
                """
            },
            {
                "titlu": "2. Capcana Link-urilor și a Site-urilor False",
                "continut": """
                    <p>Link-urile sunt principalul instrument al atacatorilor. Nu da niciodată click fără să verifici destinația reală (prin trecerea mouse-ului peste link - <em>hover</em>).</p>

                    <div class="card mb-3" style="border: 1px solid #F1C8CB;">
                        <div class="card-body">
                            <h5 class="card-title" style="color: #7E8C69;">🔗 Analiza unui link malițios</h5>
                            <p><strong>Textul afișat:</strong> <span style="color:blue; text-decoration:underline;">Accesează contul tău aici</span></p>
                            <p><strong>Link-ul real (ascuns):</strong> <code>https://banca-ta.verify-user.info/login</code></p>
                            <p><strong>De ce e Phishing?</strong> Domeniul real este <em>verify-user.info</em>, nu site-ul băncii. Pagina de destinație este o clonă vizuală perfectă.</p>
                        </div>
                    </div>
                    
                    <div class="alert alert-warning">
                        <strong>Atenție la link-uri scurtate!</strong> (ex: <em>bit.ly/3KX7x</em>). Dacă nu știi unde duc, nu da click.
                    </div>
                """
            },
            {
                "titlu": "3. Conținutul: Gramatică, Ton și Urgență",
                "continut": """
                    <table class="table table-bordered">
                        <thead style="background-color: #7E8C69; color: white;">
                            <tr>
                                <th>Indicator</th>
                                <th>Exemplu Phishing</th>
                                <th>Explicatie</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Gramatica</strong></td>
                                <td><em>„Contul dvs a fost suspendat din motive securitate. Va rugam verificare urgenta.”</em></td>
                                <td>Lipsa diacriticelor, exprimare robotică, greșeli de acord. Companiile serioase au comunicare impecabilă.</td>
                            </tr>
                            <tr>
                                <td><strong>Tonul</strong></td>
                                <td><em>„ULTIMUL AVERTISMENT! Contul tău va fi șters azi!”</em></td>
                                <td>Se folosește frica și panica. O bancă nu te va amenința niciodată prin email.</td>
                            </tr>
                        </tbody>
                    </table>
                """
            },
            {
                "titlu": "4. Vectori specifici: Smishing, Social Media și Atașamente",
                "continut": """
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">📱 SMS (Smishing)</h5>
                                    <p><em>„Coletul dvs. nu a putut fi livrat. Actualizați datele aici: bit.ly/...”</em></p>
                                    <ul>
                                        <li>Aștepți un colet? Dacă nu, e scam.</li>
                                        <li>Link-urile scurtate în SMS sunt aproape mereu periculoase.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100" style="border: 1px solid #F1C8CB;">
                                <div class="card-body">
                                    <h5 class="card-title" style="color: #7E8C69;">👥 Social Media</h5>
                                    <p><em>„Ești tu în poza asta?? 😂😂 [link]”</em></p>
                                    <ul>
                                        <li>Mesaj vag care stârnește curiozitatea.</li>
                                        <li>Vine adesea de la prieteni cu conturi sparte.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="alert alert-secondary mt-2">
                        <strong>📎 Atașamente periculoase:</strong> Fișierele de tip <code>.zip</code>, <code>.exe</code> sau chiar <code>.pdf</code> neașteptate (ex: "Factura_restanta.zip") pot conține malware.
                    </div>
                """
            },
            {
                "titlu": "5. Regula de aur și verificarea finală",
                "continut": """
                    <p>Trebuie să știi ce <strong>NU</strong> cere o companie legitimă:</p>
                    <ul>
                        <li>Niciodată parola contului prin email/SMS.</li>
                        <li>Niciodată codul 2FA (decât dacă tu ai inițiat logarea).</li>
                        <li>Niciodată datele complete de pe card (inclusiv CVV) pentru o „verificare”.</li>
                    </ul>

                    <div class="mt-4 p-4 rounded text-center" style="background-color: #fffde7; border: 2px dashed #f6e58d;">
                        <h4>🛑 Regula celor 10 secunde</h4>
                        <p>Înainte să dai click sau să răspunzi, oprește-te 10 secunde.</p>
                        <p><strong>Întreabă-te:</strong> Așteptam acest mesaj? Are sens acum? Verifică expeditorul!</p>
                    </div>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Ce trebuie verificat prima dată într-un email suspect?",
                "variante": [
                    "Logo-ul companiei",
                    "Lungimea mesajului",
                    "Adresa reală a expeditorului (nu doar numele afișat)",
                    "Fontul utilizat"
                ],
                "corect": ["Adresa reală a expeditorului (nu doar numele afișat)"],
                "explicatie": "Numele afișat poate fi orice, dar adresa de email reală trădează adesea atacul (ex: @gmail.com în loc de @banca.ro)."
            },
            {
                "id": 2,
                "intrebare": "Care dintre următoarele link-uri sunt suspecte? (Selectează multiple)",
                "variante": [
                    "Link-uri scurtate (bit.ly)",
                    "Domenii care imită numele real (ex: pay-pal-support.com)",
                    "Pagini neașteptate de login",
                    "Link-uri către site-ul oficial (ex: google.com)"
                ],
                "corect": [
                    "Link-uri scurtate (bit.ly)",
                    "Domenii care imită numele real (ex: pay-pal-support.com)",
                    "Pagini neașteptate de login"
                ],
                "explicatie": "Orice link care maschează destinația sau duce spre o pagină neoficială este un Red Flag."
            },
            {
                "id": 3,
                "intrebare": "Ce indică de obicei un mesaj oficial cu greșeli gramaticale evidente?",
                "variante": [
                    "Profesionalism scăzut al băncii",
                    "O tentativă de Phishing",
                    "O urgență legitimă",
                    "Un email intern"
                ],
                "corect": ["O tentativă de Phishing"],
                "explicatie": "Instituțiile legitime folosesc comunicări standardizate și verificate. Greșelile sunt semnul atacatorilor (adesea străini)."
            },
            {
                "id": 4,
                "intrebare": "Ce tonuri sunt frecvente în mesajele de phishing? (Selectează multiple)",
                "variante": [
                    "Amenințător („Contul va fi șters”)",
                    "Urgent („Acționează acum”)",
                    "Calm și informativ",
                    "Prea prietenos / Curios („Ești tu în poză?”)"
                ],
                "corect": [
                    "Amenințător („Contul va fi șters”)",
                    "Urgent („Acționează acum”)",
                    "Prea prietenos / Curios („Ești tu în poză?”)"
                ],
                "explicatie": "Phishing-ul se bazează pe emoție (frică, grabă, curiozitate) pentru a bloca gândirea rațională."
            },
            {
                "id": 5,
                "intrebare": "Ce NU va cere niciodată o companie legitimă prin email sau SMS?",
                "variante": [
                    "Resetarea parolei (dacă ai cerut-o tu)",
                    "Notificări de securitate generale",
                    "Parola contului sau coduri 2FA",
                    "Confirmarea adresei de email la înregistrare"
                ],
                "corect": ["Parola contului sau coduri 2FA"],
                "explicatie": "Nicio bancă sau serviciu nu îți va cere parola sau codul 2FA. Acestea se introduc doar pe site-ul oficial, nu se trimit."
            },
            {
                "id": 6,
                "intrebare": "Când ar trebui să consideri un atașament ca fiind periculos?",
                "variante": [
                    "Când vine de la o companie cunoscută",
                    "Când nu te așteptai să primești fișiere (ex: o factură neașteptată)",
                    "Când este format PDF",
                    "Când are logo-ul firmei"
                ],
                "corect": ["Când nu te așteptai să primești fișiere (ex: o factură neașteptată)"],
                "explicatie": "Contextul contează. Dacă nu aștepți o factură, nu deschide atașamentul, indiferent cum se numește."
            },
            {
                "id": 7,
                "intrebare": "Care este întrebarea esențială pe care trebuie să ți-o pui la primirea unui mesaj?",
                "variante": [
                    "Este mesajul lung?",
                    "Arată oficial?",
                    "Așteptam acest mesaj?",
                    "Are emoji-uri?"
                ],
                "corect": ["Așteptam acest mesaj?"],
                "explicatie": "Dacă răspunsul este NU, probabilitatea de phishing este foarte mare."
            },
            {
                "id": 8,
                "intrebare": "Ce presupune „Regula celor 10 secunde”?",
                "variante": [
                    "Să răspunzi în maxim 10 secunde",
                    "Să ignori mesajul automat",
                    "Să te oprești și să verifici elementele mesajului înainte de click",
                    "Să testezi link-ul rapid"
                ],
                "corect": ["Să te oprești și să verifici elementele mesajului înainte de click"],
                "explicatie": "Această pauză permite creierului rațional să preia controlul asupra impulsului emoțional."
            },
            {
                "id": 9,
               "intrebare": """Analizează mesajul de mai jos și selectează TOATE elementele care reprezintă un semnal de alarmă:

                De la: Suport Cont <support@secure-account-verify.com>

                „Am detectat activitate neobișnuită în contul tău.
                Pentru a evita suspendarea, confirmă datele imediat accesând link-ul de mai jos:

                👉 https://account-verify-secure.info/login

                Dacă nu confirmi în următoarele 30 de minute, contul tău va fi suspendat.”""",
                "variante": [
                    "Expeditorul (domeniu generic/neoficial)",
                    "Link-ul (URL necunoscut)",
                    "Tonul (amenințare și presiune de timp)",
                    "Cererea (solicitare date sensibile prin link)"
                ],
                "corect": [
                    "Expeditorul (domeniu generic/neoficial)",
                    "Link-ul (URL necunoscut)",
                    "Tonul (amenințare și presiune de timp)",
                    "Cererea (solicitare date sensibile prin link)"
                ],
                "explicatie": "Toate elementele sunt suspecte: expeditorul are un domeniu fals, link-ul este extern, tonul este amenințător, iar cererea este nelegitimă."
            }
        ]
    },
    5: {
        "titlu": "5. Phishing pe platforme moderne",
        "descriere": "Apple ID, Social Media, QR Codes (Quishing) și capcanele din notificări.",
        "subcapitole": [
            {
                "titlu": "1. Ecosistemul Apple: iMessage și Apple ID",
                "continut": """
                    <p>Utilizatorii de iPhone tind să aibă o încredere ridicată în ecosistem („Apple e sigur”). Atacatorii exploatează exact acest lucru prin mesaje care par să vină de la sistem.</p>
                    
                    <div class="card mb-3" style="border: 1px solid #ccc; max-width: 400px; margin: auto;">
                        <div class="card-header bg-light">
                            <strong>iMessage: Apple Support</strong>
                        </div>
                        <div class="card-body">
                            <p class="small text-muted">Astăzi 10:42</p>
                            <p>Apple ID-ul tău a fost blocat temporar din motive de securitate. Verifică acum pentru a evita pierderea accesului:</p>
                            <p style="color: blue; text-decoration: underline;">https://apple-id-verification.info</p>
                        </div>
                    </div>
                    
                    <div class="alert alert-danger mt-3">
                        <h5>🚩 Red Flags:</h5>
                        <ul>
                            <li><strong>Canalul:</strong> Apple NU trimite link-uri de verificare prin iMessage/SMS.</li>
                            <li><strong>Link-ul:</strong> Domeniul <em>apple-id-verification.info</em> este fals (oficial este <em>apple.com</em>).</li>
                            <li><strong>Tonul:</strong> Creează panică („vei pierde accesul”).</li>
                        </ul>
                    </div>
                """
            },
            {
                "titlu": "2. Social Media: „Ești tu în clipul ăsta?”",
                "continut": """
                    <p>Pe Instagram, Facebook sau WhatsApp, atacurile vin adesea de la <strong>prieteni reali</strong> ale căror conturi au fost compromise.</p>
                    
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div class="card h-100 border-warning">
                                <div class="card-body">
                                    <h6 class="card-title">🎥 Capcana Curiozității</h6>
                                    <p><em>„Ești tu în clipul ăsta?? 😳 [link-dubios]”</em></p>
                                    <p><strong>Mecanism:</strong> Curiozitatea te face să dai click. Site-ul îți cere să te loghezi din nou pe Instagram/Facebook pentru a vedea „video-ul”. Așa îți fură parola.</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100 border-warning">
                                <div class="card-body">
                                    <h6 class="card-title">🗳️ Capcana „Ajută-mă” (WhatsApp)</h6>
                                    <p><em>„Salut! Te rog votează-mă la concursul ăsta, am nevoie de un vot 🙏 [link-vot]”</em></p>
                                    <p><strong>Mecanism:</strong> Exploatează dorința de a ajuta. Link-ul cere logare sau un cod primit prin SMS (care este de fapt codul tău de WhatsApp/Telegram).</p>
                                </div>
                            </div>
                        </div>
                    </div>
                """
            },
            {
                "titlu": "3. Quishing: Pericolul din codurile QR",
                "continut": """
                    <p><strong>Quishing</strong> (QR Phishing) este o amenințare fizică ce devine digitală. Un cod QR este doar un link vizual – nu este implicit sigur!</p>
                    
                    <div class="alert alert-info">
                        <strong>Scenariu real:</strong> Găsești un QR code pe parbriz („Amendă parcare”) sau pe masa unui restaurant („Meniu”).
                    </div>

                    <table class="table table-bordered">
                        <tbody>
                            <tr>
                                <td>📷 <strong>Scanezi QR</strong></td>
                                <td>Te duce pe un site fals.</td>
                            </tr>
                            <tr>
                                <td>💳 <strong>Acțiunea</strong></td>
                                <td>Site-ul cere datele cardului pentru „plată” sau logare.</td>
                            </tr>
                            <tr>
                                <td>🚩 <strong>Red Flag</strong></td>
                                <td>URL-ul afișat după scanare este ciudat (ex: <em>parcare-plata-rapida.xyz</em>).</td>
                            </tr>
                        </tbody>
                    </table>
                """
            },
            {
                "titlu": "4. Notificări false și Livrări (SMS)",
                "continut": """
                    <div class="row">
                        <div class="col-md-6">
                            <h5>📦 Livrări (Smishing)</h5>
                            <p><em>„Coletul tău este blocat la vamă. Achită taxa de 5 RON aici: bit.ly/...”</em></p>
                            <ul>
                                <li><strong>Red Flag:</strong> Link scurtat + sumă mică cerută urgent.</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <h5>⚠️ Notificări „Virus”</h5>
                            <p><em>„Sistemul a detectat 3 viruși! Scanează acum!”</em></p>
                            <ul>
                                <li><strong>Red Flag:</strong> Browser-ul (Chrome/Safari) nu scanează de viruși. Este o reclamă mincinoasă (Scareware).</li>
                            </ul>
                        </div>
                    </div>
                """
            },
            {
                "titlu": "🛡️ Rezumat: Cum te protejezi",
                "continut": """
                    <div class="alert alert-success">
                        <ul>
                            <li><strong>Nu ai inițiat acțiunea?</strong> → Fii suspect (mai ales la Apple/Google).</li>
                            <li><strong>Presiune de timp?</strong> → Oprește-te.</li>
                            <li><strong>Link de la un prieten?</strong> → Verifică URL-ul sau sună-l dacă pare ciudat.</li>
                            <li><strong>QR Code?</strong> → Verifică unde duce înainte să introduci date.</li>
                        </ul>
                    </div>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Apple trimite mesaje iMessage cu link-uri pentru verificarea contului?",
                "variante": [
                    "Da, frecvent",
                    "Doar dacă există o problemă de securitate gravă",
                    "Nu, Apple nu solicită verificări prin iMessage cu link-uri"
                ],
                "corect": ["Nu, Apple nu solicită verificări prin iMessage cu link-uri"],
                "explicatie": "Apple folosește notificări de sistem (push) din Setări, nu mesaje text/iMessage cu link-uri externe."
            },
            {
                "id": 2,
                "intrebare": "Care dintre următoarele indică un link de phishing? (Selectează multiple)",
                "variante": [
                    "Domeniu neoficial (ex: apple-secure.info)",
                    "URL foarte lung și complicat",
                    "Pagina cere login imediat după accesare",
                    "Link-ul începe cu https"
                ],
                "corect": [
                    "Domeniu neoficial (ex: apple-secure.info)",
                    "URL foarte lung și complicat",
                    "Pagina cere login imediat după accesare"
                ],
                "explicatie": "HTTPS nu mai este o garanție a securității (și hackerii au certificare SSL). Restul sunt semne clare de fraudă."
            },
            {
                "id": 3,
                "intrebare": "Primești un mesaj pe Instagram de la un prieten: „Ești tu în clipul ăsta?”. Ce este cel mai probabil?",
                "variante": [
                    "Un mesaj legitim, prietenul a găsit un video cu tine",
                    "Contul prietenului este compromis și trimite spam automat",
                    "O promoție oficială Instagram",
                    "Un bug al aplicației"
                ],
                "corect": ["Contul prietenului este compromis și trimite spam automat"],
                "explicatie": "Este o metodă clasică de viralizare a atacurilor. Nu da click!"
            },
            {
                "id": 4,
                "intrebare": "De ce este periculos un mesaj de tip „Votează-mă aici” pe WhatsApp? (Selectează multiple)",
                "variante": [
                    "Necesită autentificare pe un site dubios",
                    "Vine dintr-un context neașteptat",
                    "Este doar o glumă inofensivă",
                    "Poate duce la furtul contului tău"
                ],
                "corect": [
                    "Necesită autentificare pe un site dubios",
                    "Vine dintr-un context neașteptat",
                    "Poate duce la furtul contului tău"
                ],
                "explicatie": "Atacatorii vor să îți fure credențialele sau să preia controlul asupra contului tău de WhatsApp."
            },
            {
                "id": 5,
                "intrebare": "Care afirmații sunt adevărate despre QR Code Phishing? (Selectează multiple)",
                "variante": [
                    "QR-urile pot ascunde link-uri malițioase",
                    "QR-urile sunt întotdeauna sigure, spre deosebire de email",
                    "După scanare trebuie verificat URL-ul",
                    "QR-urile pot duce la pagini false de plată"
                ],
                "corect": [
                    "QR-urile pot ascunde link-uri malițioase",
                    "După scanare trebuie verificat URL-ul",
                    "QR-urile pot duce la pagini false de plată"
                ],
                "explicatie": "Un cod QR este doar un link scurtat vizual. Poate duce oriunde."
            },
            {
                "id": 6,
                "intrebare": "Ce red flag apare frecvent în mesajele SMS despre colete?",
                "variante": [
                    "Link scurtat (ex: bit.ly)",
                    "Ton urgent sau amenințare cu returul",
                    "Cerere de date bancare pentru sume mici",
                    "Toate variantele de mai sus"
                ],
                "corect": ["Toate variantele de mai sus"],
                "explicatie": "Aceasta este rețeta clasică pentru Smishing-ul de curierat."
            },
            {
                "id": 7,
                "intrebare": "Un mesaj pop-up care spune „Ai 3 viruși pe telefon” este:",
                "variante": [
                    "O alertă reală a sistemului de operare",
                    "O tentativă de Phishing / Scam",
                    "Un mesaj de la producătorul telefonului",
                    "O eroare de afișare inofensivă"
                ],
                "corect": ["O tentativă de Phishing / Scam"],
                "explicatie": "Browserele web nu pot scana telefonul de viruși. Este o tactică de sperietură (Scareware)."
            },
            {
                "id": 8,
                "intrebare": "Scenariu: Primești un link dubios de la un prieten bun. Ce faci?",
                "variante": [
                    "Dai click rapid, e prietenul tău",
                    "Verifici cu prietenul pe un alt canal (apel, SMS) dacă el a trimis",
                    "Analizezi mesajul și link-ul fără să dai click",
                    "Introduci datele false ca să vezi ce se întâmplă"
                ],
                "corect": [
                    "Verifici cu prietenul pe un alt canal (apel, SMS) dacă el a trimis",
                    "Analizezi mesajul și link-ul fără să dai click"
                ],
                "explicatie": "Verificarea pe un canal alternativ (out-of-band verification) este cea mai sigură metodă."
            }
        ]
    },
    6: {
        "titlu": "6. Ce faci dacă ai căzut victimă?",
        "descriere": "Ghid de supraviețuire: pași concreți de urmat imediat după un incident pentru a limita pagubele.",
        "subcapitole": [
            {
                "titlu": "1. Primele minute: Regula de Aur",
                "continut": """
                    <p>Ai dat click? Ai introdus parola? Ai descărcat ceva? Ești panicat?</p>
                    
                    <div class="alert alert-danger text-center">
                        <h4>🛑 OPREȘTE-TE ȘI RESPIRĂ!</h4>
                        <p>Panica este cel mai mare inamic acum. Hackerii se bazează pe faptul că vei lua decizii pripite.</p>
                    </div>

                    <p><strong>Pași imediați (în primele 5-10 minute):</strong></p>
                    <ol>
                        <li>Închide imediat pagina web sau browser-ul.</li>
                        <li>Deconectează dispozitivul de la internet (scoate cablul, oprește Wi-Fi/Datele). Asta oprește transmiterea datelor sau descărcarea malware-ului.</li>
                        <li>Nu mai interacționa cu mesajul (nu răspunde, nu da forward).</li>
                    </ol>
                    <p><em>Acum, identifică scenariul în care te afli mai jos.</em></p>
                """
            },
            {
                "titlu": "2. Scenarii: Click simplu vs. Date de logare",
                "continut": """
                    <div class="row">
                        <div class="col-md-6 mb-3">
                            <div class="card h-100 border-warning">
                                <div class="card-body">
                                    <h5 class="card-title">Scenario A: Doar Click</h5>
                                    <p>Ai accesat link-ul, dar <strong>nu ai introdus date</strong> și ai închis pagina repede.</p>
                                    <hr>
                                    <p><strong>Ce faci:</strong></p>
                                    <ul>
                                        <li>Riscul este mic/mediu.</li>
                                        <li>Șterge mesajul.</li>
                                        <li>Rulează o scanare antivirus (pentru siguranță).</li>
                                        <li><strong>NU</strong> trimite link-ul altora „să vadă și ei”.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6 mb-3">
                            <div class="card h-100 border-danger">
                                <div class="card-body">
                                    <h5 class="card-title">Scenario B: Email + Parolă</h5>
                                    <p>Ai introdus credențialele pe un site fals.</p>
                                    <hr>
                                    <p><strong>Ce faci URGENT:</strong></p>
                                    <ol>
                                        <li>Schimbă parola contului afectat <strong>imediat</strong>.</li>
                                        <li>Schimbă parola oriunde ai mai folosit-o (Dacă ai aceeași parolă la Facebook și Yahoo, schimbă-le pe ambele!).</li>
                                        <li>Verifică sesiuni active (Log out from all devices).</li>
                                    </ol>
                                </div>
                            </div>
                        </div>
                    </div>
                """
            },
            {
                "titlu": "3. Scenarii Critice: 2FA și Date Bancare",
                "continut": """
                    <div class="alert alert-secondary">
                        <h5>⚠️ Scenario C: Ai oferit codul 2FA (SMS/App)</h5>
                        <p>Acesta este un scenariu critic. Hackerul are cheia completă de acces.</p>
                        <p><strong>Acțiune:</strong> Schimbă parola imediat (asta resetează de obicei sesiunile). Intră în setări la "Dispozitive conectate" și șterge orice dispozitiv necunoscut (ex: un iPhone în China).</p>
                    </div>

                    <div class="alert alert-danger" style="border: 2px solid red;">
                        <h5>💸 Scenario D: Ai introdus Datele Bancare</h5>
                        <p>Timpul se măsoară în secunde.</p>
                        <ol>
                            <li><strong>Sună la bancă</strong> imediat (numărul de pe spatele cardului).</li>
                            <li><strong>Blochează cardul</strong> din aplicația mobilă (dacă ai acces).</li>
                            <li>Verifică tranzacțiile recente și contestă orice plată neautorizată.</li>
                            <li>Depune o sesizare la poliție dacă paguba s-a produs.</li>
                        </ol>
                    </div>
                """
            },
            {
                "titlu": "4. Scenario E: Ai descărcat un fișier",
                "continut": """
                    <p>Ai dat click și s-a descărcat ceva (un PDF, un ZIP, un EXE), sau ai deschis un atașament.</p>
                    
                    <div class="mt-4 p-4 rounded" style="background-color: #fffde7; border: 2px dashed #f6e58d;">
                        <strong>Procedură:</strong>
                        <ul>
                            <li><strong>NU deschide fișierul!</strong></li>
                            <li>Deconectează-te de la internet (pentru a opri comunicarea virusului cu hackerul).</li>
                            <li>Șterge fișierul definitiv (Shift + Delete / Golire Coș de gunoi).</li>
                            <li>Scanează complet sistemul cu un antivirus actualizat.</li>
                            <li>Dacă ai deschis fișierul, cere ajutorul unui profesionist IT pentru curățare.</li>
                        </ul>
                    </div>
                """
            },
            {
                "titlu": "5. Checklist de Stabilizare (Post-Incident)",
                "continut": """
                    <p>După ce a trecut furtuna, asigură-te că ești protejat pe termen lung.</p>
                    <table class="table table-bordered">
                        <thead style="background-color: #7E8C69; color: white;">
                            <tr>
                                <th>Acțiune</th>
                                <th>De ce?</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>✅ <strong>Activează 2FA peste tot</strong></td>
                                <td>Chiar dacă îți fură parola, nu pot intra fără cod.</td>
                            </tr>
                            <tr>
                                <td>✅ <strong>Verifică regulile de Email</strong></td>
                                <td>Hackerii setează adesea "Forwarding Rules" ca să primească o copie a email-urilor tale. Verifică setările!</td>
                            </tr>
                            <tr>
                                <td>✅ <strong>Monitorizează conturile</strong></td>
                                <td>Urmărește activitatea în următoarele 30 de zile.</td>
                            </tr>
                            <tr>
                                <td>✅ <strong>Educă-te</strong></td>
                                <td>Faptul că ești aici e cel mai bun pas. Ai învățat lecția!</td>
                            </tr>
                        </tbody>
                    </table>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Ai dat click pe un link de phishing, dar ai închis imediat pagina fără să tastezi nimic. Care este nivelul de risc?",
                "variante": [
                    "Critic (cont pierdut)",
                    "Mic/Mediu (posibil malware, dar datele sunt sigure)",
                    "Niciun risc",
                    "Trebuie să îți ștergi contul"
                ],
                "corect": ["Mic/Mediu (posibil malware, dar datele sunt sigure)"],
                "explicatie": "Dacă nu ai introdus date, hackerii nu au parola ta. Riscul principal rămâne o infectare malware, deci o scanare e recomandată."
            },
            {
                "id": 2,
                "intrebare": "Ai realizat că tocmai ai introdus parola pe un site fals. Ce faci PRIMA DATĂ? (Selectează multiple)",
                "variante": [
                    "Schimbi parola contului afectat",
                    "Aștepți să vezi dacă primești email de la hacker",
                    "Activezi 2FA (autentificarea în doi pași)",
                    "Verifici sesiuni active și dai Log Out la toate"
                ],
                "corect": [
                    "Schimbi parola contului afectat",
                    "Activezi 2FA (autentificarea în doi pași)",
                    "Verifici sesiuni active și dai Log Out la toate"
                ],
                "explicatie": "Nu aștepta! Schimbarea parolei și întreruperea sesiunilor active sunt vitale pentru a scoate hackerul din cont."
            },
            {
                "id": 3,
                "intrebare": "De ce este extrem de periculos să oferi codul 2FA (primit prin SMS/App) unui 'operator'?",
                "variante": [
                    "Nu este periculos, e doar o verificare",
                    "Codul expiră oricum",
                    "Hackerul poate trece de protecția parolei și preia controlul total",
                    "Operatorii au nevoie de cod pentru a te ajuta"
                ],
                "corect": ["Hackerul poate trece de protecția parolei și preia controlul total"],
                "explicatie": "Codul 2FA este ultima linie de apărare. Odată oferit, parola ta nu mai contează."
            },
            {
                "id": 4,
                "intrebare": "Care scenariu necesită blocarea imediată a cardului bancar?",
                "variante": [
                    "Ai dat click pe un link",
                    "Ai introdus numărul cardului și CVV-ul pe un site suspect",
                    "Ai primit un email de la bancă",
                    "Ai descărcat o poză"
                ],
                "corect": ["Ai introdus numărul cardului și CVV-ul pe un site suspect"],
                "explicatie": "Dacă datele financiare au fost expuse, banii pot fi furați instantaneu."
            },
            {
                "id": 5,
                "intrebare": "Ce trebuie să verifici în setările de email după un incident de securitate?",
                "variante": [
                    "Culoarea temei",
                    "Semnătura",
                    "Regulile de redirecționare (Forwarding rules)",
                    "Lista de contacte"
                ],
                "corect": ["Regulile de redirecționare (Forwarding rules)"],
                "explicatie": "Hackerii adaugă adesea reguli ascunse pentru a-și trimite copii ale email-urilor tale, chiar și după ce schimbi parola."
            }
        ]
    },
    7: {
        "titlu": "7. Protecția pe termen lung",
        "descriere": "Securitatea nu este un produs, ci un obicei. Învață despre parole, 2FA și igiena digitală.",
        "subcapitole": [
            {
                "titlu": "1. Securitatea: Produs vs. Obicei",
                "continut": """
                    <p>Mulți utilizatori trăiesc cu impresia greșită că „dacă am antivirus, sunt în siguranță”.</p>
                    <div class="alert alert-warning">
                        <strong>❌ Fals.</strong> Majoritatea atacurilor de phishing nu exploatează bug-uri în software, ci „bug-uri” în atenția umană (graba, naivitatea, oboseala).
                    </div>
                    <p>Securitatea cibernetică este 10% tehnologie și <strong>90% comportament</strong>. Cel mai bun firewall este creierul tău, atunci când îi acorzi timp să analizeze.</p>
                """
            },
            {
                "titlu": "2. Parolele: Lungime vs. Complexitate",
                "continut": """
                    <p>O parolă spartă este adesea cauza principală a furtului de identitate. Cum arată o parolă modernă și sigură?</p>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="card border-danger mb-3">
                                <div class="card-header">❌ Slabă (Tradițională)</div>
                                <div class="card-body">
                                    <p class="card-text"><code>Pa$$w0rd1!</code></p>
                                    <p><small>Deși are caractere speciale, este scurtă și predictibilă pentru roboți.</small></p>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card border-success mb-3">
                                <div class="card-header">✅ Puternică (Passphrase)</div>
                                <div class="card-body">
                                    <p class="card-text"><code>Cafea!PlouaPisicaPeGeam2026</code></p>
                                    <p><small>Lungimea (15+ caractere) crește exponențial timpul de spargere. E ușor de ținut minte.</small></p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="alert alert-info">
                        <strong>Sfat:</strong> Nu încerca să ții minte zeci de parole. Folosește un <strong>Password Manager</strong> (Google Password Manager, Bitwarden, 1Password). Este un seif digital criptat.
                    </div>
                """
            },
            {
                "titlu": "3. Pericolul refolosirii parolelor",
                "continut": """
                    <p>Acesta este „Păcatul Capital” în securitate. Dacă folosești aceeași parolă la Facebook, Email și un forum de pescuit, ești în pericol.</p>
                    
                    <div class="p-3 mb-2 bg-light text-dark border rounded">
                        <h5>🎲 Efectul Domino (Credential Stuffing)</h5>
                        <ol>
                            <li>Forumul de pescuit (care are securitate slabă) este spart.</li>
                            <li>Hackerii iau parola ta de acolo.</li>
                            <li>Ei testează automat acea parolă pe Gmail, Facebook, PayPal, Amazon.</li>
                            <li>Dacă parola e aceeași... ai pierdut tot.</li>
                        </ol>
                    </div>
                    <p><strong>Soluția:</strong> Parole UNICE pentru fiecare cont. (Posibil doar cu un Password Manager).</p>
                """
            },
            {
                "titlu": "4. Autentificarea Multi-Factor (2FA)",
                "continut": """
                    <p>Chiar dacă cineva îți fură parola, <strong>2FA (Two-Factor Authentication)</strong> este ușa blindată care îi oprește.</p>
                    
                    <table class="table table-bordered">
                        <thead class="thead-light">
                            <tr>
                                <th>Metodă</th>
                                <th>Siguranță</th>
                                <th>Descriere</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>SMS</strong></td>
                                <td class="text-warning">Medie</td>
                                <td>Mai bine decât nimic, dar vulnerabil la interceptare (SIM Swap).</td>
                            </tr>
                            <tr>
                                <td><strong>Aplicație (Auth App)</strong></td>
                                <td class="text-success">Ridicată ✅</td>
                                <td>Google Authenticator, Microsoft Auth. Codurile se generează local pe telefonul tău, chiar și offline.</td>
                            </tr>
                            <tr>
                                <td><strong>Cheie fizică</strong></td>
                                <td class="text-primary">Maximă</td>
                                <td>Un stick USB (ex: YubiKey) pe care trebuie să îl atingi.</td>
                            </tr>
                        </tbody>
                    </table>
                """
            },
            {
                "titlu": "5. Igiena Digitală: Email și Dispozitive",
                "continut": """
                    <p>Email-ul este „cheia schelet” a vieții tale digitale. Cine are acces la email, poate reseta parolele la orice alt serviciu.</p>
                    
                    <ul class="list-group">
                        <li class="list-group-item">🔍 <strong>Verifică regulile de Forwarding:</strong> Hackerii setează adesea reguli ca să primească o copie a email-urilor tale.</li>
                        <li class="list-group-item">📱 <strong>Update-uri software:</strong> Nu amâna actualizările la telefon/laptop. Ele repară găuri de securitate pe care hackerii le exploatează.</li>
                        <li class="list-group-item">☕ <strong>Wi-Fi Public:</strong> Evită să te loghezi în conturi bancare de pe Wi-Fi-ul cafenelei fără un VPN.</li>
                    </ul>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Care este, statistic, cel mai important factor în securitatea personală?",
                "variante": [
                    "Cât de scump este antivirusul",
                    "Comportamentul utilizatorului (atenția)",
                    "Viteza internetului",
                    "Brandul telefonului"
                ],
                "corect": ["Comportamentul utilizatorului (atenția)"],
                "explicatie": "Tehnologia te ajută, dar decizia finală de a da click sau a introduce date îți aparține."
            },
            {
                "id": 2,
                "intrebare": "Ce face o parolă să fie puternică? (Selectează multiple)",
                "variante": [
                    "Să fie cât mai scurtă",
                    "Lungimea mare (12-15+ caractere)",
                    "Unicitatea (să nu fie refolosită)",
                    "Complexitatea (litere, cifre, simboluri)"
                ],
                "corect": [
                    "Lungimea mare (12-15+ caractere)",
                    "Unicitatea (să nu fie refolosită)",
                    "Complexitatea (litere, cifre, simboluri)"
                ],
                "explicatie": "Lungimea este matematic cel mai important factor împotriva spargerii prin forță brută."
            },
            {
                "id": 3,
                "intrebare": "De ce este periculoasă refolosirea parolelor?",
                "variante": [
                    "Ocupă multă memorie",
                    "Dacă un site este spart, hackerii încearcă acea parolă pe toate celelalte conturi (efect domino)",
                    "Nu este periculoasă, este eficientă",
                    "Parolele expiră mai repede"
                ],
                "corect": ["Dacă un site este spart, hackerii încearcă acea parolă pe toate celelalte conturi (efect domino)"],
                "explicatie": "Credential Stuffing este metoda prin care hackerii folosesc parole scurse din baze de date vechi pentru a intra în conturi active."
            },
            {
                "id": 4,
                "intrebare": "Care este metoda recomandată de Autentificare în Doi Pași (2FA)?",
                "variante": [
                    "Doar parola simplă",
                    "SMS (datorită riscului de SIM Swap)",
                    "Aplicație de autentificare (ex: Google Authenticator)",
                    "Email"
                ],
                "corect": ["Aplicație de autentificare (ex: Google Authenticator)"],
                "explicatie": "Aplicațiile generează coduri local pe dispozitiv, fiind mult mai sigure decât SMS-urile care pot fi interceptate."
            },
            {
                "id": 5,
                "intrebare": "Ce trebuie să verifici periodic la contul de email?",
                "variante": [
                    "Dacă ai primit spam",
                    "Culoarea temei",
                    "Regulile de redirecționare (Forward rules) și dispozitivele conectate",
                    "Numărul de contacte"
                ],
                "corect": ["Regulile de redirecționare (Forward rules) și dispozitivele conectate"],
                "explicatie": "Hackerii lasă adesea „portițe” (backdoors) prin reguli de forward pentru a spiona contul chiar și după ce schimbi parola."
            }
        ]
    },
    8: {
        "titlu": "8. Simulare și Test Final",
        "descriere": "Capstone-ul cursului: o simulare de atac și evaluarea finală a vigilenței tale.",
        "subcapitole": [
            {
                "titlu": "1. Ce este o simulare de phishing?",
                "continut": """
                    <p>Ai ajuns la final. Acum trecem de la teorie la practică. O simulare de phishing este un <strong>„exercițiu de incendiu”</strong> digital.</p>
                    
                    <div class="alert alert-info">
                        <strong>🎯 Scopul:</strong> Imităm un atac real într-un mediu sigur, controlat, pentru a vedea cum reacționezi sub presiune.
                    </div>

                    <p>În viața reală, greșeala costă bani sau date. Aici, greșeala costă doar puncte. Urmează să analizezi un scenariu des întâlnit.</p>
                """
            },
            {
                "titlu": "2. SCENARIU PRACTIC: Analizează acest mesaj",
                "continut": """
                    <p>Imaginează-ți că primești următorul email luni dimineața. Privește-l cu atenție:</p>

                    <div class="card shadow-sm mb-4" style="border: 2px dashed #d9534f; background-color: #fff;">
                        <div class="card-header bg-light">
                            <strong>De la:</strong> Securitate Bancară &lt;alert@banca-transilvania-support.net&gt;<br>
                            <strong>Subiect:</strong> ⚠️ ACȚIUNE NECESARĂ: Contul tău a fost suspendat
                        </div>
                        <div class="card-body">
                            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Link_icon.svg/1200px-Link_icon.svg.png" width="30" style="float:right; opacity:0.5;">
                            <p>Stimate client,</p>
                            <p>Am detectat o activitate neobișnuită (conectare din Rusia) pe contul dumneavoastră.</p>
                            <p>Din motive de securitate, am blocat temporar cardurile. Pentru a debloca accesul, vă rugăm să confirmați identitatea în maxim 24 de ore.</p>
                            
                            <div class="text-center my-3">
                                <a href="#" class="btn btn-primary disabled" style="pointer-events: none;">Verifică Identitatea Acum</a>
                            </div>
                            
                            <p><small>Dacă nu acționați, contul va fi închis permanent.<br>Echipa de Securitate.</small></p>
                        </div>
                    </div>

                    <div class="alert alert-warning">
                        <strong>🤔 Ce faci în această situație?</strong>
                        <ul>
                            <li><strong>Opțiunea A:</strong> Dai click rapid, de frică să nu pierzi banii.</li>
                            <li><strong>Opțiunea B:</strong> Te uiți la adresa de email (<em>...support.net</em>? Banca are <em>.ro</em>).</li>
                            <li><strong>Opțiunea C:</strong> Observi urgența artificială („închis permanent”).</li>
                        </ul>
                    </div>
                """
            },
            {
                "titlu": "3. Analiza Scenariului (Debriefing)",
                "continut": """
                    <p>Dacă ai fi dat click pe link-ul de mai sus într-un scenariu real, hackerii te-ar fi dus pe o pagină identică cu cea a băncii.</p>
                    
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Element Suspect (Red Flag)</th>
                                <th>Explicație</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>🔴 <strong>Expeditorul</strong></td>
                                <td>Domeniul <code>banca-transilvania-support.net</code> este FALS. O bancă folosește domeniul oficial.</td>
                            </tr>
                            <tr>
                                <td>🔴 <strong>Salutul</strong></td>
                                <td>„Stimate client” este generic. Băncile îți știu numele.</td>
                            </tr>
                            <tr>
                                <td>🔴 <strong>Amenințarea</strong></td>
                                <td>„Contul va fi închis permanent”. Nicio bancă nu închide contul prin email.</td>
                            </tr>
                        </tbody>
                    </table>
                """
            },
            {
                "titlu": "4. Nivelurile de Risc Comportamental",
                "continut": """
                    <p>În funcție de reacția ta la astfel de mesaje, te încadrezi într-o categorie de risc:</p>

                    <div class="row text-center">
                        <div class="col-md-4">
                            <div class="p-3 mb-2 bg-danger text-white rounded">
                                <h5>🟥 Risc Ridicat</h5>
                                <p>Dai click imediat. Introduci date fără verificare. Ești victima ideală.</p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="p-3 mb-2 bg-warning text-dark rounded">
                                <h5>🟨 Risc Mediu</h5>
                                <p>Eziți, verifici parțial, dar tot dai click „de curiozitate”. Ești vulnerabil la atacuri sofisticate.</p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="p-3 mb-2 bg-success text-white rounded">
                                <h5>🟩 Risc Scăzut</h5>
                                <p>Verifici sursa (header), nu dai click, raportezi email-ul sau suni la bancă. Ești protejat.</p>
                            </div>
                        </div>
                    </div>
                """
            }
        ],
        "quiz_questions": [
            {
                "id": 1,
                "intrebare": "Care este scopul principal al unui atac de phishing?",
                "variante": [
                    "Să îți strice calculatorul (hardware)",
                    "Furtul de date sensibile (parole, carduri) prin manipulare",
                    "Să îți facă reclamă la produse",
                    "Testarea vitezei de internet"
                ],
                "corect": ["Furtul de date sensibile (parole, carduri) prin manipulare"],
                "explicatie": "Phishing-ul vizează informația, nu distrugerea echipamentului."
            },
            {
                "id": 2,
                "intrebare": "Ce elemente (Red Flags) indică un mesaj fals? (Selectează multiple)",
                "variante": [
                    "Adresa de email ciudată / neoficială",
                    "Tonul urgent și amenințător",
                    "Greșeli gramaticale evidente",
                    "Link-uri către site-ul oficial (https://google.com)"
                ],
                "corect": [
                    "Adresa de email ciudată / neoficială",
                    "Tonul urgent și amenințător",
                    "Greșeli gramaticale evidente"
                ],
                "explicatie": "Urgența, greșelile și expeditorul dubios sunt cele mai clare semne."
            },
            {
                "id": 3,
                "intrebare": "Ce NU va cere niciodată o companie legitimă prin email/SMS?",
                "variante": [
                    "Să evaluezi serviciul",
                    "Parola contului tău",
                    "Să citești o notificare în aplicație",
                    "Confirmarea adresei de livrare (fără link de login)"
                ],
                "corect": ["Parola contului tău"],
                "explicatie": "Parola este sacră. Niciun angajat (IT, Bancă, Poliție) nu are dreptul să ți-o ceară."
            },
            {
                "id": 4,
                "intrebare": "Care este cea mai bună protecție pe termen lung împotriva phishing-ului?",
                "variante": [
                    "Instalarea a 5 antivirusuri",
                    "Educația utilizatorului și vigilența (Scepticismul)",
                    "Să nu folosești internetul",
                    "Să schimbi calculatorul lunar"
                ],
                "corect": ["Educația utilizatorului și vigilența (Scepticismul)"],
                "explicatie": "Tehnologia poate da greș, dar un utilizator educat va recunoaște tentativa de fraudă."
            },
            {
                "id": 5,
                "intrebare": "Ce faci dacă primești un email suspect de la „Netflix” despre o plată eșuată?",
                "variante": [
                    "Dai click pe link să rezolvi repede",
                    "Răspunzi la email cu datele cardului",
                    "Nu dai click. Intri manual pe Netflix.com (scrii tu adresa) și verifici acolo.",
                    "Ștergi contul Netflix"
                ],
                "corect": ["Nu dai click. Intri manual pe Netflix.com (scrii tu adresa) și verifici acolo."],
                "explicatie": "Verificarea prin canal alternativ (scrierea adresei manual) este metoda sigură de a evita capcanele."
            },
            {
                "id": 6,
                "intrebare": "Analiză link: Care dintre următoarele este sigur pentru PayPal?",
                "variante": [
                    "http://paypal-secure-login.com",
                    "https://www.paypal.com",
                    "http://paypal.verify-account.net",
                    "https://pay-pal.com"
                ],
                "corect": ["https://www.paypal.com"],
                "explicatie": "Doar domeniul exact 'paypal.com' este legitim. Orice adăugire cu cratimă sau altă terminație (.net, -secure) este phishing."
            }
        ]
    }
}