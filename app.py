import os
from datetime import datetime
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

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
#UPLOAD_FOLDER='static/uploads'
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

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

class PhishingReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    screenshot = db.Column(db.String(150), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    votes_phishing = db.Column(db.Integer, default=0)
    votes_safe = db.Column(db.Integer, default=0)
    uploader = db.relationship('User', backref='reports')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('home'))
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    if request.method == 'POST':
        login_id = request.form.get('login_id') 
        password = request.form.get('password')
        user = User.query.filter(or_(User.username == login_id, User.email == login_id, User.phone == login_id)).first()
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
        phone_number = request.form.get('phone_number')
        
        full_phone = f"{request.form.get('phone_prefix')}{phone_number.replace(' ', '')}" if phone_number else None
        
        user_exists = User.query.filter(or_(User.username == username, User.email == email)).first()
        
        if not user_exists and full_phone:
            phone_exists = User.query.filter_by(phone=full_phone).first()
            if phone_exists:
                user_exists = phone_exists

        if user_exists:
            flash(t['msg_user_exists'], 'warning')
        else:
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password=hashed_pw, first_name=first_name, last_name=last_name, email=email, phone=full_phone)
            db.session.add(new_user)
            db.session.commit()
            try:
                send_confirmation_email(email, username, tip = 'register')
                flash(t['msg_check_email'], 'info')
            except:
                flash(t['err_email_send'], 'danger')
            return redirect(url_for('login'))
    return render_template('auth.html', mode='register')

@app.route('/confirm_email/<token>')
def confirm_email(token):
    try:
        email = serializer.loads(token, salt='email-confirm-salt', max_age=3600)
        user = User.query.filter_by(email=email).first_or_404()
        user.is_email_verified = True
        db.session.commit()
        flash(TEXTE[session.get('lang', 'ro')]['msg_email_confirmed'], 'success')
    except:
        flash(TEXTE[session.get('lang', 'ro')]['msg_link_invalid'], 'danger')
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
    if not lectie: return "Lesson not found", 404
    if id_lectie > 1:
        prev = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=id_lectie-1).first()
        if not prev:
            flash(TEXTE[session.get('lang', 'ro')]['err_complete_previous'], 'warning')
            return redirect(url_for('home'))
    return render_template('lesson.html', lectie=lectie, id_curent=id_lectie)

@app.route('/quiz/<int:id_lectie>', methods=['GET', 'POST'])
@login_required
def view_quiz(id_lectie):
    LECTII = get_current_lessons()
    lectie = LECTII.get(id_lectie)
    if request.method == 'POST':
        score = sum(1 for q in lectie['quiz_questions'] if set(request.form.getlist(f"question_{q['id']}")) == set(q['corect']))
        percent = int((score / len(lectie['quiz_questions'])) * 100)
        prog = LessonProgress.query.filter_by(user_id=current_user.id, lesson_id=id_lectie).first()
        if prog:
            if percent > prog.score: prog.score = percent
        else:
            db.session.add(LessonProgress(user_id=current_user.id, lesson_id=id_lectie, score=percent))
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('quiz.html', lectie=lectie, id_curent=id_lectie)

def get_all_badges_status(user, progress_map, total_lessons, t):
    unlocked, locked = [], []
    media = (sum(progress_map.values()) / total_lessons) if total_lessons > 0 and progress_map else 0
    
    criteria = [
        ('verified', '✅', user.is_email_verified, t['badge_verified_title'], t['badge_verified_desc']),
        ('first_step', '🎯', len(progress_map) > 0, t['badge_first_step_title'], t['badge_first_step_desc']),
        ('student', '📚', len(progress_map) == total_lessons, t['badge_student_title'], t['badge_student_desc']),
        ('expert', '🛡️', media >= 90, t['badge_expert_title'], t['badge_expert_desc']),
        ('perfect', '🦅', any(s == 100 for s in progress_map.values()), t['badge_perfect_title'], t['badge_perfect_desc'])
    ]
    
    for id_b, icon, cond, title, desc in criteria:
        data = {'id': id_b, 'icon': icon, 'title': title, 'desc': desc}
        unlocked.append(data) if cond else locked.append(data)
    return unlocked, locked

@app.route('/profil')
@login_required
def profil():
    LECTII = get_current_lessons()
    progress = LessonProgress.query.filter_by(user_id=current_user.id).all()
    progress_map = {p.lesson_id: p.score for p in progress}
    unlocked, locked = get_all_badges_status(current_user, progress_map, len(LECTII), TEXTE[session.get('lang','ro')])
    
    stats = []
    total_percent = 0
    for id_l, data in LECTII.items():
        p = progress_map.get(id_l, 0)
        stats.append({'id': id_l, 'titlu': data['titlu'], 'scor_text': f"{int((p/100)*len(data['quiz_questions']))}/{len(data['quiz_questions'])}", 'procent': p})
        total_percent += p
    
    return render_template('profil.html', user=current_user, stats=stats, media_globala=int(total_percent/len(LECTII)) if LECTII else 0, unlocked_badges=unlocked, locked_badges=locked)

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)

@app.route('/change_username', methods=['POST'])
@login_required
def change_username():
    new_name = request.form.get('new_username')
    if User.query.filter_by(username=new_name).first():
        flash(TEXTE[session.get('lang','ro')]['msg_username_taken'], 'warning')
    else:
        current_user.username = new_name
        db.session.commit()
        flash(TEXTE[session.get('lang','ro')]['msg_username_changed'], 'success')
    return redirect(url_for('settings'))

@app.route('/upload_avatar', methods=['POST'])
@login_required
def upload_avatar():
    file = request.files.get('avatar')
    if file and allowed_file(file.filename):
        if current_user.avatar:
            old = os.path.join(app.config['UPLOAD_FOLDER'], current_user.avatar)
            if os.path.exists(old): os.remove(old)
        import secrets
        name = f"user_{current_user.id}_{secrets.token_hex(4)}{os.path.splitext(file.filename)[1]}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
        current_user.avatar = name
        db.session.commit()
    return redirect(url_for('settings'))

@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
    if check_password_hash(current_user.password, request.form.get('old_password')):
        current_user.password = generate_password_hash(request.form.get('new_password'), method='pbkdf2:sha256')
        db.session.commit()
        flash('Password changed', 'success')
    return redirect(url_for('settings'))

@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    LessonProgress.query.filter_by(user_id=current_user.id).delete()
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for('login'))

@app.route('/verify_data', methods=['GET', 'POST'])
@login_required
def verify_data():
    if request.method == 'POST':
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        email = request.form.get('email')
        if email != current_user.email:
            current_user.email = email
            current_user.is_email_verified = False
            send_confirmation_email(email, current_user.username, tip='update')
        db.session.commit()
        return redirect(url_for('verify_data'))
    return render_template('verify_data.html', user=current_user)

@app.route('/comunitate')
@login_required
def comunitate():
    reports = PhishingReport.query.order_by(PhishingReport.date_posted.desc()).all()
    return render_template('community.html', reports=reports, user=current_user)

@app.route('/raporteaza', methods=['GET', 'POST'])
@login_required
def raporteaza():
    if request.method == 'POST':
        file = request.files.get('screenshot')
        if file and allowed_file(file.filename):
            path = os.path.join(app.config['UPLOAD_FOLDER'], 'reports')
            os.makedirs(path, exist_ok=True)
            import secrets
            name = f"report_{secrets.token_hex(8)}{os.path.splitext(file.filename)[1]}"
            file.save(os.path.join(path, name))
            db.session.add(PhishingReport(screenshot=name, uploader_id=current_user.id))
            db.session.commit()
            return redirect(url_for('comunitate'))
    return render_template('report_form.html', user=current_user)

@app.route('/vote/<int:report_id>/<string:vote_type>')
@login_required
def vote(report_id, vote_type):
    report = PhishingReport.query.get_or_404(report_id)
    if vote_type == 'phishing': report.votes_phishing += 1
    elif vote_type == 'safe': report.votes_safe += 1
    db.session.commit()
    return redirect(url_for('comunitate'))

@app.route('/sterge_raport/<int:report_id>', methods=['POST'])
@login_required
def sterge_raport(report_id):
    report = PhishingReport.query.get_or_404(report_id)
    if report.uploader_id == current_user.id:
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'reports', report.screenshot)
        if os.path.exists(img_path): os.remove(img_path)
        db.session.delete(report)
        db.session.commit()
        flash("Raport șters.", "info")
    return redirect(url_for('comunitate'))

@app.route('/leaderboard')
@login_required
def leaderboard():
    t = TEXTE[session.get('lang', 'ro')]
    users = User.query.all()
    data = []
    total_l = len(get_current_lessons())
    for u in users:
        prog = LessonProgress.query.filter_by(user_id=u.id).all()
        if prog:
            media = sum(p.score for p in prog) / total_l
            data.append({'username': u.username, 'avatar': u.avatar, 'media': int(media), 'lessons_count': len(prog)})
    data = sorted(data, key=lambda x: x['media'], reverse=True)[:10]
    return render_template('leaderboard.html', top_users=data, user=current_user, t=t)

def send_reset_email(user):
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])

    token = serializer.dumps(user.email, salt='password-reset-salt')
    link = url_for('reset_token', token=token, _external=True)
    
    msg = Message(t['email_reset_subject'],
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[user.email])
    
    msg.html = t['email_reset_html'].format(user=user.username, link=link)
    
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            send_reset_email(user)
            flash(t['msg_reset_email_sent'], 'info')
            return redirect(url_for('login'))
        else:
            flash(t['err_email_not_found'], 'warning')
            
    return render_template('reset_request.html', t=t)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    lang = session.get('lang', 'ro')
    t = TEXTE.get(lang, TEXTE['ro'])
    
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=1800)
    except:
        flash(t['err_reset_link_invalid'], 'danger')
        return redirect(url_for('reset_request'))
    
    user = User.query.filter_by(email=email).first()
    
    if request.method == 'POST':
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash(t['err_pass_mismatch'], 'danger')
        else:
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
            user.password = hashed_pw
            db.session.commit()
            flash(t['msg_pass_updated'], 'success')
            return redirect(url_for('login'))
            
    return render_template('reset_token.html', t=t)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)