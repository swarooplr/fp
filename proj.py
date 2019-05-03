from flask import Flask, render_template, request
import  langdetect
#English libraries

from english_annotators.postagging import pos as en_pos
from english_annotators.stemming import stem as en_stem
from english_annotators.lemmtize import lem as en_lem
from english_annotators.ner import ner as en_ner
#kannada libraries
from kannada_annotators.postagging import pos as kn_pos
from kannada_annotators.textsummarization import summarize as kn_summarize
from kannada_annotators.sandhi_splitting_main import sandhi_split as kn_split
from kannada_annotators.text_classification import classify as kn_cls
from kannada_annotators.gender_classification import classify_gender as kn_gender
from kannada_annotators.coreference import coreference as kn_coref
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
            language=request.form.get('language')
            if language=="English":
                if task == "pos":
                    tagged=en_pos(textval)
                    return render_template("disp.html",text=tagged)
                elif task == "ner":
                    nertagged = en_ner(textval)
                    return render_template("disp.html", text=nertagged)
                elif task=="lem":
                    lemmatized=en_lem(textval)
                    return render_template("disp.html", text=lemmatized)
                elif task=="stem":
                    stemmed=en_stem(textval)
                    return  render_template("disp.html",text=stemmed)
                elif task=="coref":
                    return render_template("disp.html", text=" ")

            elif language=="Kannada":
                if task=="pos":
                    tagged=kn_pos(textval)
                    return render_template("disp.html", text=tagged)
                elif task=="txtsum":
                    summarized=kn_summarize(textval)
                    return render_template("textSummarization.html", text=summarized)
                elif task=="spl":
                    sandhi=kn_split(textval)
                    return render_template("disp.html",text=sandhi)
                elif task =="gnd":
                    gender=kn_gender(textval)
                    return render_template("disp.html",text=gender)
                elif task=="txtcls":
                     knclass=kn_cls(textval)
                     return render_template("disp.html", text=knclass)
                elif task=="coref":
                    coref=kn_coref(textval)
                    return render_template("disp.html")



if __name__ == '__main__':
    app.run(debug=True)