from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import YTDownloadForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = YTDownloadForm()
    if form.validate_on_submit():
        # Sample 20 sec YouTube video to get the audio from
        # https://youtu.be/cphNpqKpKc4
        os.system(
            f'youtube-dl -f bestaudio --restrict-filenames --extract-audio --audio-format mp3 {form.ytlink.data}')
        flash(f'Downloading .. {form.ytlink.data}', 'success')
        return redirect(url_for('home'))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
