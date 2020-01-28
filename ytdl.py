from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import YTDownloadForm
import pafy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# URLs
# Bhagyada Lakshmi Baramma
# https://youtu.be/t5RFWwtb2Ms

# Pibare Rama Rasam
# https://youtu.be/2tcfwDanl3o

# Tamburi Meetidava
# https://youtu.be/uCCaFqRoihQ

# Callback class


class MyCallback:
    def __init__(self, callbackId):
        self.callbackId = callbackId

    def __call__(self, total, recvd, ratio, rate, eta):
        print("Downloader #{:d}: {:>7.3f} MB {:>6.1f} % {:>10.1f} kBps    ETA: {:>5.1f} s".format(
            self.callbackId, recvd / (1024 * 1024), ratio * 100, rate, eta))


def download(url):
    # create video object
    video = pafy.new(url)
    # extract information about best resolution video available
    audio = video.getbestaudio()
    # download the video
    audio.download(quiet=True, callback=MyCallback(42))


@app.route('/', methods=['GET', 'POST'])
def home():
    form = YTDownloadForm()
    if form.validate_on_submit():
        download(form.ytlink.data)
        flash(f'Downloading .. {form.ytlink.data}', 'success')
        return redirect(url_for('home'))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
