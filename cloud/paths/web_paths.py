from flask import render_template as give, send_file, request, redirect, flash
from models.models import RegDwn, DeviceInfo, MediaPath, NewsLetter, Feedback
from models.download_struct import PATHS
from sqlalchemy import exc as SQLERR
from app.api import app, db

plus = lambda e: (e + 1)
def identify_request(req: dict):
    if req != {}:
        keys = req.keys()
        for key in keys:
            if key not in ["ext", "usgt", "plt"]:
                try:
                    media = MediaPath(path=key)
                    db.session.add(media)
                    db.session.commit()
                except:
                    pass

def register(raw):
    try:
        curr = RegDwn.query.filter_by(id=int(raw['ext'])).first()
        adnl = DeviceInfo(platform=raw['plt'], user_agent=raw['usgt'], ext=raw['ext'])
        curr.counts = plus(curr.counts)
        db.session.add(curr)
        db.session.add(adnl)
        db.session.commit()

    except:
        incr = RegDwn(id=int(raw['ext']), counts=1)
        adnl = DeviceInfo(platform=raw['plt'], user_agent=raw['usgt'], ext=raw['ext'])

        db.session.add(incr)
        db.session.add(adnl)

        db.session.commit()

def subscribeNewsletter(user: dict):
    user = NewsLetter(name=user['user-name'], email=user["user-email"])
    try:
        db.session.add(user)
        db.session.commit()
        return False
    except SQLERR.IntegrityError as e:
         print(e)
         return True
    
def send_feedback(user: dict):
    user = Feedback(contact=user['user-contact'], message=user["user-message"])
    try:
        db.session.add(user)
        db.session.commit()
        return False
    except SQLERR.IntegrityError:
         return True


# eliezerkenya web partition
@app.route("/")
def main_web():
    identify_request(request.args)
    return give("main.html", download=PATHS), 200

@app.route("/about")
def about_me():
    return give("about.html", download=PATHS, title="eliezerkenya | about"), 200

@app.route("/projects")
def projects():
  return give("projects.html", download=PATHS, title="eliezerkenya | projects"), 200

@app.route("/contact")
def contact_me():
    return give("contact.html", download=PATHS, title="eliezerkenya | contact", msc=True), 200

@app.route("/feedback", methods=["GET", "POST"])
@app.route("/lsb/feedback", methods=["GET", "POST"])
def feedback_me():
    if request.method == "GET":
        return give("feedback.html", download=PATHS, title="Feedback | form"), 200
        
    if request.method == "POST":
        state = send_feedback(request.form)
        flash(
            message="Successfully submitted feedback thanks!" if state == False else "Failed! Not submitted, try again! Thanks", 
            category="success" if state == False else "error"
            )
        return give("success.html", download=PATHS, title="Feedback | sent", struct={"title": "Feedback submitted!", "sub": "Successful", "info": "Thanks for your feedback."}), 400

# The news letter urls
@app.route("/lsb/subscribe-to-newsletter", methods=["GET", "POST"])
@app.route("/subscribe-to-newsletter", methods=["GET", "POST"])
@app.route("/subscribe-to-newsletter", methods=["GET", "POST"])
def subscribe():
    if request.method == "GET":
        return give("subscribe.html", download=PATHS, title="Newsletter | Subscription"), 200
    
    if request.method == "POST":
        state = subscribeNewsletter(request.form)
        flash(
            message="Successfully subscribed to our newsletter!" if state == False else "Failed! Seems already subscribed. Thanks", 
              category="success" if state == False else "error"
              )
        return give("success.html", download=PATHS, title="Newsletter | subscribed", struct={"title": "Newsletter", "sub": "Newsletter subscription", "info": "Subscribing to this newsletter you'll be able to receive updates from eliezerkenya about lsb and more."})

# Livesongbook partition
@app.route("/lsb/")
@app.route("/lsb")
def lsb_home():
    identify_request(request.args)
    return give("index.html", download=PATHS)

@app.route("/lsb/download")
def download():
    return give("lsb.html", download=PATHS, title="livesongbook | download"), 200

@app.route("/lsb/faqs")
def faqs():
    return give("faqs.html", download=PATHS, title="eliezerkenya | FAQs")

@app.route("/lsb/contact")
def contact():
    return give("contact.html", download=PATHS, title="lsb developer | contact")

@app.route("/lsb/download/exe", methods=["POST", "GET"])
def download_exe():
    register(request.args)
    return send_file("static/downloads/path.exe", download_name="win64_lsb_v1.0.exe")

@app.route("/lsb/download/apk", methods=["POST", "GET"])
def download_apk():
    register(request.args)
    return send_file("static/downloads/path.apk", download_name="lsb_v1.0.apk")

@app.route("/lsb/download/deb", methods=["POST", "GET"])
def download_linux():
    register(request.args)
    return send_file("static/downloads/path.deb", download_name="lsb-desktop-app_1.0.0_amd64.deb")

@app.route("/lsb/download/tar/gz", methods=["POST", "GET"])
def download_linux_archive():
    register(request.args)
    return send_file("static/downloads/path.tar.gz", download_name="lsb_linux_X64_v1.0_archive.tar.gz")

@app.route("/lsb/download/zip", methods=["POST", "GET"])
def download_win_zip():
    register(request.args)
    return send_file("static/downloads/path.rar", download_name="win64_lsb_1.0.rar")

@app.route("/email") 
def email():
  return redirect("mailto:dev.eliezer.media+supportlivesongbookapp@gmail.com"), 302

@app.route("/api") 
@app.route("/api/") 
def api_home():
  return {"message": "unavaillable for now, contact us for support!"}, 401

@app.errorhandler(404)
def not_found(err):
    return {"message": "unavaillable for now, contact us for support!"}, 404

@app.errorhandler(500)
def server_err(err):
    return {"message": "Server error! Please check your request and try again!"}, 500

@app.errorhandler(405)
def server_err(err):
    return {"message": "This method is not allowed here please!"}, 405