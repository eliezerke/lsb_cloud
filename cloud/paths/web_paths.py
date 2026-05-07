from flask import render_template as give, send_file, request, redirect, flash
from models.download_struct import PATHS
from models.songbooks import RegDwn, DeviceInfo, MediaPath, NewsLetter
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

@app.route("/email") 
def email():
  return redirect("mailto:dev.eliezer.media@gmail.com")

@app.route("/")
def main_web():
    identify_request(request.args)
    return give("main.html", download=PATHS)

@app.route("/about")
def about_me():
    return give("about.html", download=PATHS, title="eliezerkenya | about")

@app.route("/projects")
def projects():
  return give("projects.html", download=PATHS, title="eliezerkenya | projects")

@app.route("/contact")
def contact_me():
    return give("contactme.html", download=PATHS, title="eliezerkenya | contact")

@app.route("/feedback")
def feedback_me():
    return give("feedbackme.html", download=PATHS, title="eliezerkenya | feedback")

@app.route("/lsb/subscribe-to-newsletter", methods=["GET", "POST"])
@app.route("/subscribe-to-newsletter", methods=["GET", "POST"])
@app.route("/subscribe-to-newsletter", methods=["GET", "POST"])

def subscribe():
    data = {}
    if request.method == "GET":
        data["origin"] = request.args["org"]
        return give("subscribe.html", download=PATHS, title="Newsletter | Subscription")
    
    if request.method == "POST":
        flash(message="Successfully subscribed to our newsletter!", category="success")
        return give("success.html", download=PATHS, title="Newsletter | subscribed")

@app.route("/lsb/")
@app.route("/lsb")
def lsb_home():
    identify_request(request.args)
    return give("index.html", download=PATHS)

@app.route("/lsb/download")
def download():
    return give("lsb.html", download=PATHS, title="livesongbook | download")

@app.route("/lsb/faqs")
def faqs():
    return give("faqs.html", download=PATHS, title="eliezerkenya | FAQs")

@app.route("/lsb/feedback")
def feedback():
    return give("feedback.html", download=PATHS, title="livesongbook | feedback")

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

@app.route("/lsb/guide/pdf", methods=["POST", "GET"])
def download_guide_pdf():
    register(request.args)
    return send_file("static/downloads/guide.pdf", download_name="livesongbook_guide.pdf")