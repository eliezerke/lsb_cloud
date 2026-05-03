from flask import render_template as give, send_file, request
from models.download_struct import PATHS
from models.songbooks import RegDwn, DeviceInfo
from app.api import app, db

plus = lambda e: (e + 1)

def register(raw):
    try:
        curr = RegDwn.query.filter_by(id=int(raw['ext'])).first()
        adnl = DeviceInfo(platform=raw['plt'], user_agent=raw['usgt'], ext=raw['ext'])
        curr.counts = plus(curr.counts)

        db.session.add(curr)
        db.session.add(adnl)

        db.session.commit()
        print(curr.counts)

    except:
        incr = RegDwn(id=int(raw['ext']), counts=1)
        adnl = DeviceInfo(platform=raw['plt'], user_agent=raw['usgt'], ext=raw['ext'])

        db.session.add(incr)
        db.session.add(adnl)

        db.session.commit()
        print("not yet!", incr)

@app.route("/lsb")
def lsb_home():
    return give("index.html", download=PATHS)

@app.route("/lsb/download")
def download():
    return give("lsb.html", download=PATHS)

@app.route("/lsb/faqs")
def faqs():
    return give("faqs.html", download=PATHS)

@app.route("/lsb/feedback")
def feedback():
    return give("feedback.html", download=PATHS)

@app.route("/lsb/contact")
def contact():
    return give("contact.html", download=PATHS)


@app.route("/lsb/download/exe")
def download_exe():
    register(request.args)
    return send_file("static/downloads/path.exe", download_name="win64_lsb_v1.0.exe")

@app.route("/lsb/download/apk")
def download_apk():
    register(request.args)
    return send_file("static/downloads/path.apk", download_name="lsb_v1.0.apk")


@app.route("/lsb/download/deb")
def download_linux():
    register(request.args)
    return send_file("static/downloads/path.deb", download_name="lsb_linux_X64_v1.0.deb")

@app.route("/lsb/download/tar/gz")
def download_linux_archive():
    register(request.args)
    return send_file("static/downloads/path.tar.gz", download_name="lsb_linux_X64_v1.0_archive.tar.gz")


@app.route("/lsb/download/zip")
def download_win_zip():
    register(request.args)
    return send_file("static/downloads/path.rar", download_name="win64_lsb_1.0.rar")

@app.route("/lsb/guide/pdf")
def download_guide_pdf():
    register(request.args)
    return send_file("static/downloads/guide.pdf", download_name="livesongbook_guide.pdf")