
# A very simple Flask Hello World app for you to get started with...
import Lexer, Tokenizer, LEDparser, LEDevaluator


from flask import Flask
from flask import render_template, request
from Lexer import *
from Tokenizer import *
from LEDparser import *
from LEDevaluator import *
from main import compile_LED_to_JS


app = Flask(__name__)
app.debug = True
command_history = []

@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    if request.form:
        input_string = request.form['input']
        try:
            result = str(evaluate(parse(tokenize(lex(input_string)))))
        except:
            result = "Error in input syntax"

        command_history.insert(0,(input_string, result))

        return render_template('index.html',
                               title='Home',
                               input_string=input_string,
                               result=result,
                               history=command_history)
    else:
        return render_template('index.html', title='Home')


@app.route('/ace',methods=['GET','POST'])
def ace():

    return """


    <!DOCTYPE html>
<html>
<body>

<style>
#editor {
    position: absolute;
    width: 1000px;
    height: 600px;
}
</style>

<h1>Enter in LED Code</h1>



<script>
function writeText (form) {

    form.LEDLogic.value = editor.getValue();;
    console.log(form.LEDLogic.value);
}
</script>
<form action='/logic' method="POST" onSubmit="writeText(this.form)" accept-charset="UTF-8">


	<input type="submit" onClick="writeText(this.form)" value="Compile"/>


    <input type="hidden" TYPE="text" NAME="LEDLogic" value="" ><P>


</form>
<div id="editor">

NAUGHTS AND CROSSES TRUE

Written in LED by Beau Miller, 4/9/2018

This Naughts and Crosses is written in the LED style that I would prefer, where the State is a of sets of sets

/$

initialState() := {{1,"x"}}

displayImages(S) := gridDisplay U piecesOnGrid(S) U resetButton U gameOverImage(S)

piecesOnGrid(S) := cell1(S) U cell2(S) U cell3(S) U cell4(S) U cell5(S) U cell6(S) U cell7(S) U cell8(S) U cell9(S)

cell1(S) := xIcon(150,150) if {1,"x"} in S;
            oIcon(150,150) if {1,"o"} in S;
            <> otherwise
cell2(S) := xIcon(250,150) if {2,"x"} in S;
            oIcon(250,150) if {2,"o"} in S;
            <> otherwise
cell3(S) := xIcon(350,150) if {3,"x"} in S;
            oIcon(350,150) if {3,"o"} in S;
            <> otherwise
cell4(S) := xIcon(150,250) if {4,"x"} in S;
            oIcon(150,250) if {4,"o"} in S;
            <> otherwise
cell5(S) := xIcon(250,250) if {5,"x"} in S;
            oIcon(250,250) if {5,"o"} in S;
            <> otherwise
cell6(S) := xIcon(350,250) if {6,"x"} in S;
            oIcon(350,250) if {6,"o"} in S;
            <> otherwise
cell7(S) := xIcon(150,350) if {7,"x"} in S;
            oIcon(150,350) if {7,"o"} in S;
            <> otherwise
cell8(S) := xIcon(250,350) if {8,"x"} in S;
            oIcon(250,350) if {8,"o"} in S;
            <> otherwise
cell9(S) := xIcon(350,350) if {9,"x"} in S;
            oIcon(350,350) if {9,"o"} in S;
            <> otherwise


xIcon(centerX,centerY) :=
            <
            segment(point(centerX - 50,centerY - 50),point(centerX + 50,centerY + 50),BLUE),
            segment(point(centerX - 50,centerY + 50),point(centerX + 50,centerY - 50),BLUE)
            >

oIcon(centerX,centerY) :=
            <
            disc(point(centerX,centerY), 50, RED)
            >

gameOverImage(S) :=
            <
            text(gameOverText(S), point(600, 250),20,BLACK)
            >


gridDisplay := <
                segment(point(200,100),point(200,400),BLACK),
                segment(point(300,100),point(300,400),BLACK),
                segment(point(100,200),point(400,200),BLACK),
                segment(point(100,300),point(400,300),BLACK)
                >

resetButton := <
                segment(point(550,300),point(650,300),BLACK),
                segment(point(650,300),point(650,350),BLACK),
                segment(point(650,350),point(550,350),BLACK),
                segment(point(550,350),point(550,300),BLACK),
                text("reset", point(600, 325),20,BLACK)
                >

centerX(c):= 150+100*((c-1) mod 3)
centerO(c):= 350-100*(floor((c-1)/3))

xMin(c) :=  100+100*((c-1) mod 3)
xMax(c) :=  200+100*((c-1) mod 3)
yMin(c) :=  300-100*(floor((c-1)/3))
yMax(c) :=  400-100*(floor((c-1)/3))

clickXInCell := floor(mouseX / 100)
clickYInCell := floor(mouseY / 100)


cellEmpty(cell, S) iff ~({cell, "x"} in S V {cell, "o"} in S)


cellClicked := clickXInCell + (clickYInCell - 1)*3 if clickXInCell > 0 & clickXInCell < 4 & clickYInCell > 0 & clickYInCell < 4;
                "no cell clicked" otherwise

resetClicked := mouseX > 550 & mouseX < 650 & mouseY > 300 & mouseY < 350

even(n) iff n mod 2=0

playerToMove(S):=
     "x" if even(|S|);
     "o" otherwise

gameOver(S) := True if |S| = 9 V xWon(S) V oWon(S);
               False otherwise

gameOverText(S) := "X Wins!" if xWon(S);
                   "O Wins!" if oWon(S);
                   "Cat's Game" if |S| > 9;
                   "" otherwise

threeInARow(S) := "x" if xRow(S);
                  "o" if oRow(S);
                  "" otherwise


moveMade(S) := {} if cellClicked = "no cell clicked" V ~cellEmpty(cellClicked,S);
               {cellClicked, playerToMove(S)} otherwise

transition(S) := {} if resetClicked;
                 S U {"GAMEOVER"} if gameOver(S);
                 S U {moveMade(S)} if ~ (moveMade(S) in {{}});
                 S otherwise


xWon(S) iff xTopRow(S) V xMiddleRow(S) V xBottomRow(S) V xLeftCol(S) V xMiddleCol(S) V xRightCol(S) V xDownDiag(S) V xUpDiag(S)

oWon(S) iff oTopRow(S) V oMiddleRow(S) V oBottomRow(S) V oLeftCol(S) V oMiddleCol(S) V oRightCol(S) V oDownDiag(S) V oUpDiag(S)


xTopRow(S) iff {1, "x"} in S & {2, "x"} in S & {3, "x"} in S
xMiddleRow(S) iff {4, "x"} in S & {5, "x"} in S & {6, "x"} in S
xBottomRow(S) iff {7, "x"} in S & {8, "x"} in S & {9, "x"} in S
xLeftCol(S) iff {1, "x"} in S & {4, "x"} in S & {7, "x"} in S
xMiddleCol(S) iff {2, "x"} in S & {5, "x"} in S & {8, "x"} in S
xRightCol(S) iff {3, "x"} in S & {6, "x"} in S & {9, "x"} in S
xDownDiag(S) iff {1, "x"} in S & {5, "x"} in S & {9, "x"} in S
xUpDiag(S) iff {3, "x"} in S & {5, "x"} in S & {7, "x"} in S


oTopRow(S) iff {1, "o"} in S & {2, "o"} in S & {3, "o"} in S
oMiddleRow(S) iff {4, "o"} in S & {5, "o"} in S & {6, "o"} in S
oBottomRow(S) iff {7, "o"} in S & {8, "o"} in S & {9, "o"} in S
oLeftCol(S) iff {1, "o"} in S & {4, "o"} in S & {7, "o"} in S
oMiddleCol(S) iff {2, "o"} in S & {5, "o"} in S & {8, "o"} in S
oRightCol(S) iff {3, "o"} in S & {6, "o"} in S & {9, "o"} in S
oDownDiag(S) iff {1, "o"} in S & {5, "o"} in S & {9, "o"} in S
oUpDiag(S) iff {3, "o"} in S & {5, "o"} in S & {7, "o"} in S

$/




</div>

<script src="https://www.pythonanywhere.com/user/rahutchinson/files/home/rahutchinson/mysite/ace-builds/src/ace.js" type="text/javascript" charset="utf-8"></script>
    <script>
        var editor = ace.edit("editor");
    </script>

</body>
</html>

"""



@app.route('/logic',methods=['GET','POST'])
def logic():
    if request.form:
        input_string = request.form['LEDLogic']
        print("JUST PRINTED")
        print(input_string)
        result = compile_LED_to_JS(input_string)

        return render_template('game_template.html',
                               LED_code= result
                               )
    else:
        return render_template('index.html', title='Home')