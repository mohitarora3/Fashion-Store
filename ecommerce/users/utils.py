import os
from PIL import Image
from flask import url_for
from flask_mail import Message
from  ecommerce import mail


def save_picture(form_picture):
    # it will rsave the picture in the directory where all profile pictures are stored and also return updated file name
    #random_hex = secrets.token_hex(8)
    random_hex = str(random.random())
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'seller/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

# this is to reduce the size and also to speed up the website

    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = '''To reset your password, visit the following link
    {}
    If you did not make this request then simply ignore this email and no changes will be made
    '''.format(url_for('users.reset_token', token=token, _external=True))
    mail.send(msg)
