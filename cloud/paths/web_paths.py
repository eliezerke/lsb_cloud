from flask import render_template as give, send_file, url_for
from models.download_struct import PATHS
from app.api import app
    
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
    return send_file("static/downloads/path.exe")


@app.route("/lsb/download/apk")
def download_apk():
    return send_file("static/downloads/path.apk")


@app.route("/lsb/download/deb")
def download_linux():
    return send_file("static/downloads/path.deb")


@app.route("/lsb/download/zip")
def download_win_zip():
    return send_file("static/downloads/path.zip")

@app.route("/lsb/guide/pdf")
def download_guide_pdf():
    return send_file("static/downloads/guide.pdf")