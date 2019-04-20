from flask import Flask, render_template, request
from english_annotators.postagging import pos
from english_annotators.ner import process_content
from english_annotators.stemming import stem
from english_annotators.lemmtize import lem
from english_annotators.postagging import pos
from kannada_annotators.postagging import pos as kn_pos

app = Flask(__name__,static_url_path="")
app._static_folder = "static"



@app.route("/")
def index():
    return render_template("firstpage.html")



textval=""

@app.route("/", methods=["GET", "POST"])
def getvalue():
        textval = request.form['text_body']

        if request.method=='POST':
            task = request.form['tasks']
            if task=="pos":
                tagged=kn_pos(textval)
                return render_template("disp.html", text=tagged)
            elif task=="ner":
                nertagged=process_content(textval)

                return render_template("disp.html", text=nertagged)
            elif task=="stem":
                stemtag=stem(textval)
                return render_template("disp.html",text=stemtag)
            elif task =="lem":
                lemtag=lem(textval)
                return render_template("disp.html",text=lemtag)

            # elif task=="wordnet":
            #     # syn=wordnet(textval)
            #     return render_template("disp.html",text=syn)


if __name__ == '__main__':
    app.run(debug=True)