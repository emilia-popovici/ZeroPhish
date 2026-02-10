import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from sqlalchemy import or_
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

from lectii_multilang import LECTII_ALL
from texte import TEXTE
from countries import COUNTRIES

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cs-licenta-2025'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'zerophish.app@gmail.com'
app.config['MAIL_PASSWORD'] = 'gabgmdhgetulcqee'
mail = Mail(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def send_confirmation_email(user_email, username, tip = 'register'):
    token = serializer.dumps(user_email, salt='email-confirm-salt')
    link = url_for('confirm_email', token=token, _external=True)
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])

    if tip == 'update':
        subiect = t['email_update_subject']
        html_content = t['email_update_html_content']
    else:
        subiect = t['email_subject']
        html_content = t['email_html_content']
    
    msg = Message(subiect, sender=app.config['MAIL_USERNAME'], recipients=[user_email])
    msg.html = html_content.format(user=username, link = link)
    
    mail.send(msg)

@app.context_processor
def inject_text():
    lang = session.get('lang', 'ro')
    return dict(t=TEXTE.get(lang, TEXTE['ro']), 
                lang_curenta=lang,
                lista_tari= COUNTRIES
    )

@app.route('/set_lang/<limba>')
def set_lang(limba):
    if limba in TEXTE:
        session['lang'] = limba
    return redirect(request.referrer or url_for('home'))

def get_current_lessons():
    lang = session.get('lang', 'ro')
    return LECTII_ALL.get(lang, LECTII_ALL['ro'])

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    is_email_verified = db.Column(db.Boolean, default=False)
    phone = db.Column(db.String(50), unique=True, nullable=True)
    avatar = db.Column(db.String(150), nullable=True, default=None)
    progress = db.relationship('LessonProgress', backref='user', lazy=True)

class LessonProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False) 
    score = db.Column(db.Integer, default=0) 

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('home'))
    
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])

    if request.method == 'POST':
        login_id = request.form.get('login_id') 
        password = request.form.get('password')
        
        user = User.query.filter(
            or_(
                User.username == login_id,
                User.email == login_id,
                User.phone == login_id
            )
        ).first()

        if user and check_password_hash(user.password, password):
            if not user.is_email_verified:
                flash(t['err_email_not_verified'], 'warning')
                return redirect(url_for('login'))
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash(t['msg_login_fail'], 'danger')
            
    return render_template('auth.html', mode='login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: return redirect(url_for('home'))
    
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        
        phone_prefix = request.form.get('phone_prefix')
        phone_number = request.form.get('phone_number')
        full_phone = None
        
        if phone_number:
            clean_number = phone_number.replace(" ", "")
            if phone_prefix:
                full_phone = f"{phone_prefix}{clean_number}"
            else:
                full_phone = clean_number

        user_exists = User.query.filter(
            or_(
                User.username == username,
                User.email == email if email else False,
                User.phone == full_phone if full_phone else False
            )
        ).first()

        if user_exists:
            flash(t['msg_user_exists'], 'warning')
        else:
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')

            new_user = User(
                username=username, 
                password=hashed_pw,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=full_phone,
                is_email_verified=False
            )
            
            db.session.add(new_user)
            db.session.commit()
            
            try:
                send_confirmation_email(email, username, tip = 'register')
                flash(t['msg_check_email'], 'info')
            except Exception as e:
                print(e)
                flash(t['err_email_send'], 'danger')

            return redirect(url_for('login'))
            
    return render_template('auth.html', mode='register')

@app.route('/confirm_email/<token>')
def confirm_email(token):
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    try:
        email = serializer.loads(token, salt='email-confirm-salt', max_age=3600)
    except:
        flash(t['msg_link_invalid'], 'danger')
        return redirect(url_for('login'))
    
    user = User.query.filter_by(email=email).first_or_404()
    
    if user.is_email_verified:
        flash(t['msg_email_confirmed'], 'success')
    else:
        user.is_email_verified = True
        db.session.commit()
        flash(t['msg_email_confirmed'], 'success')
        
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    LECTII = get_current_lessons()
    
    user_progress = LessonProgress.query.filter_by(user_id=current_user.id).all()
    progress_map = {p.lesson_id: p.score for p in user_progress}
    return render_template('dashboard.html', lectii=LECTII, progress_map=progress_map, user=current_user)

@app.route('/lectie/<int:id_lectie>')
@login_required
def view_lesson(id_lectie):
    LECTII = get_current_lessons()
    lectie = LECTII.get(id_lectie)
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    if not lectie: return t['err_lesson_not_found'], 404
    return render_template('lesson.html', lectie=lectie, id_curent=id_lectie)

@app.route('/quiz/<int:id_lectie>', methods=['GET', 'POST'])
@login_required
def view_quiz(id_lectie):
    LECTII = get_current_lessons()
    lectie = LECTII.get(id_lectie)
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    if not lectie: return t['err_lesson_not_found'], 404
    
    if request.method == 'POST':
        score = 0
        total_questions = len(lectie['quiz_questions'])
        for q in lectie['quiz_questions']:
            user_answers = request.form.getlist(f"question_{q['id']}")
            if set(user_answers) == set(q['corect']):
                score += 1
        
        percentage = int((score / total_questions) * 100)
        progress_entry = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=id_lectie).first()
        
        if progress_entry:
            if percentage > progress_entry.score: progress_entry.score = percentage
        else:
            new_progress = LessonProgress(user_id=current_user.id, lesson_id=id_lectie, score=percentage)
            db.session.add(new_progress)
        
        db.session.commit()
        msg = t['msg_quiz_result'].format(score=score, total=total_questions, percent=percentage)
        flash(msg, 'success')
        
        return redirect(url_for('home'))

    return render_template('quiz.html', lectie=lectie, id_curent=id_lectie)

@app.route('/profil')
@login_required
def profil():
    LECTII = get_current_lessons()
    
    user_progress = LessonProgress.query.filter_by(user_id=current_user.id).all()
    progress_map = {p.lesson_id: p.score for p in user_progress}
    stats = []
    total_percent = 0
    total_lessons = len(LECTII)
    
    for id_lectie, data in LECTII.items():
        procent = progress_map.get(id_lectie, 0)
        nr_intrebari = len(data['quiz_questions'])
        intrebari_corecte = int((procent / 100) * nr_intrebari)
        stats.append({
            'id': id_lectie, 'titlu': data['titlu'],
            'scor_text': f"{intrebari_corecte}/{nr_intrebari}", 'procent': procent
        })
        total_percent += procent
        
    media_globala = int(total_percent / total_lessons) if total_lessons > 0 else 0
    return render_template('profil.html', user=current_user, stats=stats, media_globala=media_globala)

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)

@app.route('/change_username', methods=['POST'])
@login_required
def change_username():
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    new_username = request.form.get('new_username')
    existing_user = User.query.filter_by(username=new_username).first()
    if existing_user:
        flash(t['msg_username_taken'], 'warning')
    else:
        current_user.username = new_username
        db.session.commit()
        flash(t['msg_username_changed'], 'success')
    return redirect(url_for('settings'))

@app.route('/upload_avatar', methods=['POST'])
@login_required
def upload_avatar():
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    if 'avatar' not in request.files:
        flash(t['err_no_photo'], 'warning')
        return redirect(url_for('settings'))
    
    file = request.files['avatar']
    
    if file.filename == '' or not file:
        flash(t['err_no_file'], 'warning')
        return redirect(url_for('settings'))
    
    if allowed_file(file.filename):
        _, extensie = os.path.splitext(file.filename)
        
        import secrets
        random_hex = secrets.token_hex(4)
        nume_nou = f"user_{current_user.id}_{random_hex}{extensie}"
        
        cale_salvare = os.path.join(app.config['UPLOAD_FOLDER'], nume_nou)
        
        if current_user.avatar:
            cale_veche = os.path.join(app.config['UPLOAD_FOLDER'], current_user.avatar)
            if os.path.exists(cale_veche):
                os.remove(cale_veche)

        file.save(cale_salvare)
        
        current_user.avatar = nume_nou
        db.session.commit()
        
        flash(t['msg_photo_updated'], 'success')
    else:
        flash(t['err_format_not_allowed'], 'danger')
        
    return redirect(url_for('settings'))

@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
    old = request.form.get('old_password')
    new = request.form.get('new_password')
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    if not check_password_hash(current_user.password, old):
        flash(t['err_old_password'], 'password_error')
        return redirect(url_for('settings'))
    else:
        current_user.password = generate_password_hash(new, method='pbkdf2:sha256')
        db.session.commit()
        flash(t['msg_password_changed'], 'success')
        
    return redirect(url_for('settings'))

@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    LessonProgress.query.filter_by(user_id=current_user.id).delete()
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    flash(t['msg_account_deleted'], 'info')
    return redirect(url_for('login'))

@app.route('/verify_data', methods=['GET', 'POST'])
@login_required
def verify_data():
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        
        phone_prefix = request.form.get('phone_prefix')
        phone_number = request.form.get('phone_number')
        full_phone = None
        
        if phone_number:
            clean_number = phone_number.replace(" ", "") 
            if phone_prefix:
                full_phone = f"{phone_prefix}{clean_number}"
            else:
                full_phone = clean_number

        try:
            email_changed = False
            if email and email != current_user.email:
                current_user.email= email
                current_user.is_email_verified = False
                email_changed = True

            if first_name: current_user.first_name = first_name
            if last_name: current_user.last_name = last_name
            if full_phone: current_user.phone = full_phone
            
            db.session.commit()

            if email_changed:
                try:
                    send_confirmation_email(current_user.email, current_user.username, tip='update')
                    flash(t['msg_email_changed_verify'], 'info')
                except Exception as e:
                    print(f"Eroare mail: {e}")
                    flash(t['err_email_send'], 'warning')

            else:
                flash(t['flash_update_success'], 'success')

        except Exception as e:
            db.session.rolback()
            print(e)
            flash(t['flash_update_error'], 'danger')
        
        return redirect (url_for('verify_data'))
    return render_template('verify_data.html', user=current_user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)