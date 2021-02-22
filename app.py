
from flask import Flask, render_template,request,redirect
app = Flask(__name__)
import speech_recognition as sr

@app.route("/",methods=["GET","POST"])
def hello():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file) 
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            
            

    return render_template('index.html',transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)