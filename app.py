import os
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from lectii_multilang import LECTII_ALL
from texte import TEXTE

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cs-licenta-2025'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.context_processor
def inject_text():
    lang = session.get('lang', 'ro')
    return dict(t=TEXTE.get(lang, TEXTE['ro']), lang_curenta=lang)

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
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Nume sau parolă greșită!', 'danger')
    return render_template('auth.html', mode='login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Acest utilizator există deja.', 'warning')
        else:
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(username=username, password=hashed_pw)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('home'))
    return render_template('auth.html', mode='register')

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
    
    if not lectie: return "Lecția nu există", 404
    return render_template('lesson.html', lectie=lectie, id_curent=id_lectie)

@app.route('/quiz/<int:id_lectie>', methods=['GET', 'POST'])
@login_required
def view_quiz(id_lectie):
    LECTII = get_current_lessons()
    lectie = LECTII.get(id_lectie)
    
    if not lectie: return "Lecția nu există", 404
    
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
        flash(f'Ai obținut {score} din {total_questions} ({percentage}%)!', 'success')
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
    new_username = request.form.get('new_username')
    existing_user = User.query.filter_by(username=new_username).first()
    if existing_user:
        flash('Nume deja folosit.', 'warning')
    else:
        current_user.username = new_username
        db.session.commit()
        flash('Username schimbat!', 'success')
    return redirect(url_for('settings'))

@app.route('/upload_avatar', methods=['POST'])
@login_required
def upload_avatar():
    if 'avatar' not in request.files:
        flash('Nicio poză selectată.', 'warning'); return redirect(url_for('settings'))
    file = request.files['avatar']
    if file.filename == '' or not file:
        flash('Niciun fișier.', 'warning'); return redirect(url_for('settings'))
    
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = f"user_{current_user.id}_{filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        
        current_user.avatar = unique_filename
        db.session.commit()
        flash('Poza a fost actualizată!', 'success')
    else:
        flash('Format nepermis (doar jpg, png).', 'danger')
    return redirect(url_for('settings'))

@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
    old = request.form.get('old_password')
    new = request.form.get('new_password')
    if not check_password_hash(current_user.password, old):
        flash('Parola veche incorectă.', 'danger')
    else:
        current_user.password = generate_password_hash(new, method='pbkdf2:sha256')
        db.session.commit()
        flash('Parola schimbată!', 'success')
    return redirect(url_for('settings'))

@app.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    LessonProgress.query.filter_by(user_id=current_user.id).delete()
    db.session.delete(current_user)
    db.session.commit()
    logout_user()
    flash('Cont șters.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)