from flask import render_template, url_for, flash, redirect, request, abort
from band.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from band.models import User, Post
from band import app, db, bcrypt, mail
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from flask_mail import Message
import datetime


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",)


@app.route("/about")
def about():
    return render_template("about.html",)


@app.route("/concerts", methods=['GET', 'POST'])
def concerts():
    if request.method == 'POST':
        concerts = request.form['concerts']
        concerts = concerts.upper()
    else:
        concerts = ""
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Saturday', 'Sunday', ]
    months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    time = ['8:00 PM ', '6:00 PM ', '9:00 PM ', '6:30 PM ', '7:30 PM ', '9:00 PM ', '7:00 PM ', '9:00 PM ', '10:15 PM ', '9:00 PM ', '10:15 PM ', '9:00 PM ', '7:00 PM ', '6:00 PM ', '8:00 PM ', '7:00 PM ', '7:00 PM ', '9:00 PM ', '9:00 PM ', '7:00 PM ', '6:00 PM ', '9:00 PM ', '9:00 PM ', '7:30 PM ', '6:00 PM ', '9:00 PM ', '7:30 PM ', '7:00 PM ', '9:00 PM ', '6:00 PM ', '9:00 PM ', '8:00 PM ', '9:00 PM ', '9:00 PM ', '6:00 PM ', '6:30 PM ', '6:30 PM ', '9:00 PM ', '9:00 PM ', '9:00 PM ', '6:00 PM ', '6:00 PM ', '9:00 PM ', '7:30 PM ', '8:00 PM ', '9:00 PM ', '9:00 PM ', '9:00 PM ', '6:30 PM ', '6:30 PM ', '6:00 PM ', '8:00 PM ', '10:15 PM ', '7:00 PM ', '9:00 PM ', '7:00 PM ', '9:00 PM ', '6:00 PM ', '9:00 PM ', '9:00 PM ', '8:00 PM ', '7:00 PM ', '7:30 PM ', '9:00 PM ', '8:00 PM ', '7:00 PM ', '8:00 PM ', '7:00 PM ', '6:00 PM ', '10:15 PM ', '6:00 PM ', '10:15 PM ', '9:00 PM ', '9:00 PM ', '10:15 PM ', '9:00 PM ', '6:00 PM ', '9:00 PM ', '6:00 PM ', '7:00 PM ', '8:00 PM ', '7:30 PM ', '8:00 PM ', '7:00 PM ', '9:00 PM ', '7:00 PM ', '7:00 PM ', '9:00 PM ', '6:30 PM ', '6:30 PM ', '9:00 PM ', '9:00 PM ', '7:00 PM ', '7:30 PM ', '9:00 PM ', '6:00 PM ', '7:30 PM ', '9:00 PM ', '9:00 PM ']
    price = ['50', '50', '40', '40', '70', '70', '35', '70', '35', '40', '100', '100', '70', '50', '50', '50', '35', '35', '70', '35', '70', '50', '50', '35', '50', '100', '100', '100', '40', '40', '70', '35', '50', '60', '50', '100', '50', '60', '70', '40', '70', '35', '40', '100', '100', '70', '40', '60', '70', '50', '100', '50', '100', '50', '35', '40', '40', '100', '60', '100', '70', '40', '60', '70', '40', '50', '40', '35', '70', '100', '70', '40', '35', '60', '35', '50', '35', '35', '60', '100', '60', '35', '50', '100', '40', '60', '100', '60', '40', '35', '60', '50', '35', '100', '50', '60', '40', '60', '50', '100', ]
    area = ['KFC Yum! Center, Louisville, KY', 'KFC Yum! Center, Louisville, KY', 'KFC Yum! Center, Louisville, KY', 'Bankers Life Fieldhouse, Indianapolis, IN', 'Bankers Life Fieldhouse, Indianapolis, IN', 'Bankers Life Fieldhouse, Indianapolis, IN', 'Bankers Life Fieldhouse, Indianapolis, IN', 'KFC Yum! Center, Louisville, KY', 'KFC Yum! Center, Louisville, KY', 'KFC Yum! Center, Louisville, KY', 'United Center, Chicago, IL', 'Quicken Loans Arena, Cleveland, OH', 'Bankers Life Fieldhouse, Indianapolis, IN', 'Bankers Life Fieldhouse, Indianapolis, IN', 'Quicken Loans Arena, Cleveland, OH', 'Quicken Loans Arena, Cleveland, OH', 'KFC Yum! Center, Louisville, KY', 'United Center, Chicago, IL', 'KFC Yum! Center, Louisville, KY', 'Bankers Life Fieldhouse, Indianapolis, IN', 'Bankers Life Fieldhouse, Indianapolis, IN', 'KFC Yum! Center, Louisville, KY', 'Bankers Life Fieldhouse, Indianapolis, IN', 'KFC Yum! Center, Louisville, KY', 'KFC Yum! Center, Louisville, KY', 'Bankers Life Fieldhouse, Indianapolis, IN', 'Quicken Loans Arena, Cleveland, OH', 'Quicken Loans Arena, Cleveland, OH', 'KFC Yum! Center, Louisville, KY', 'Bankers Life Fieldhouse, Indianapolis, IN', 'KFC Yum! Center, Louisville, KY']
    base = datetime.datetime(2019, 4, 24, 1, 17, 55, 173504)
    numdays = 90
    date_list = [base + datetime.timedelta(days=x) for x in range(0, numdays, 3)]
    return render_template("concerts.html", days=days, date_list=date_list, months=months, time=time, price=price, area=area, concerts=concerts)


@app.route("/songs")
def songs():
    return render_template("songs.html",)


@app.route("/merch")
def merch():
    return render_template("merch.html",)


@app.route("/buyTicket", methods=['GET', 'POST'])
def buyTicket():
    if request.method == 'POST':
        price = request.form['price']
        price = int(price)
        date = request.form['date']
        time = request.form['time']
        arena = request.form['arena']
    return render_template("buyTicket.html", price=price, date=date, time=time, arena=arena)


@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
    if request.method == 'POST':
        try:
            first = request.form['first']
            last = request.form['last']
            email = request.form['mail']
            total = request.form["total"]
            date = request.form['date']
            time = request.form['time']
            arena = request.form['arena']
            quantity = request.form['quantity']
            ticketReceipt(first, last, email, date, time, arena, total, quantity)
            return redirect(url_for('home'))
        except Exception as e:
            pass

        try:
            first = request.form['first']
            last = request.form['last']
            email = request.form['mail']
            total = request.form["total"]
            shirts = request.form['shirts']
            hats = request.form['hats']
            stickers = request.form['stickers']
            merchReceipt(first, last, email, shirts, hats, stickers, total)
            return redirect(url_for('home'))
        except:
            pass
        try:
            price = request.form['price']
            price = int(price)
            quantity = request.form['quantity']
            quantity = int(quantity)
            total = quantity * price
            date = request.form['date']
            time = request.form['time']
            arena = request.form['arena']
            x = 0
            return render_template("purchase.html", price=price, date=date, time=time, arena=arena, total=total, quantity=quantity, x=x)
        except:
            shirts = request.form['shirts']
            hats = request.form['hats']
            stickers = request.form['stickers']
            if(shirts == ""):
                shirts = 0
            if(hats == ""):
                hats = 0
            if(stickers == ""):
                stickers = 0
            shirts = int(shirts)
            hats = int(hats)
            stickers = int(stickers)
            total = 20 * shirts + 10 * hats + 5 * stickers
            x = 1
            return render_template("purchase.html", shirts=shirts, hats=hats, stickers=stickers, total=total, x=x)


def ticketReceipt(first, last, email, date, time, arena, total, quantity):
    msg = Message('Thank you for supporting Midsummer Madness', sender='noreply@demo.com', recipients=[email])
    msg.body = f'''Thank you {first} {last}, for purchasing {quantity} Ticket(s) for {date}, {time} at {arena}!
Total Cost: ${total}
'''

    mail.send(msg)


def merchReceipt(first, last, email, shirts, hats, stickers, total):
    if(shirts != "0"):
        shirts = f"{shirts} Shirt(s), "
    else:
        shirts = ""
    if(hats != "0"):
        hats = f"{hats} Hat(s), "
    else:
        hats = ""
    if(stickers != "0"):
        stickers = f"{stickers} Stickers(s)"
    else:
        stickers = ""

    msg = Message('Thank you for supporting Midsummer Madness', sender='noreply@demo.com', recipients=[email])
    msg.body = f'''Thank you {first} {last}, for purchasing {shirts}{hats}{stickers}
Total Cost: ${total}
'''

    mail.send(msg)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created! You may now log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profilepics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            current_user.image_file = save_picture(form.picture.data)
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='profilepics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post', form=form, legend="New Post")


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post updated", 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post deleted", "success")
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then ignore
'''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Email has been sent', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pw
        db.session.commit()
        flash(f'Password Updated!', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


@app.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("blog.html", posts=posts)
