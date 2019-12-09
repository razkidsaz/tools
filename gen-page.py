
import os
import urllib

def getPageIndex(name):
    return int(name[5:-4])

# "raz_countingbugs.*_p6_text.mp3"
def getAudioIndex(name):
    left=name[:-9] # raz_countingbugs.*p6
    if left.endswith("title"):
        return 2
    p=left.rfind('p')
    return int(left[p+1:])


part1="""
<!DOCTYPE html>
<html>
    <head>
        <script type="text/javascript">
         function playOrPause() {
             if (window.mp3.paused) {
                 window.mp3.play();
             } else {
                 window.mp3.pause();
             }
         }
        </script>

        <style>
         .imgbox{
             text-align: center;
             max-height: 600px;
         }
         .imgbox img{
             max-height: 600px;
             max-width: 900px;
             vertical-align: middle;
             outline: 1px solid gray;
         }
         .nav {
             text-decoration: none;
             color: black;
             font-size: 24px;
             padding: 100px 10px 100px 10px;
             margin: 0 0px 0 0;
             background:#e6e6e6;
         }
         .imgbtn .nav {
             cursor: pointer;
         }
        </style>
    </head>
    <body>
"""

part2="""
    </body>
</html>
"""

def genHtmlFile(directory, index, page, audio, maxindex):
    filename="page-" + str(index) + ".html"
    prev='#'
    if index > 1:
        prev="page-" + str(index-1) + ".html"
    next='#'
    if index < maxindex:
        next="page-" + str(index+1) + ".html"

    snippet='<div class="imgbox"><a class="nav nav-prev" href="' + prev +'" style="margin-left: 0px;">&lt;&lt;</a>  <a class="imgbtn" onclick="playOrPause();"> <img src="' + page + '"/></a> <a class="nav nav-next" href="' + next +'" style="margin-right: 0px;">&gt;&gt;</a></div>'

    audiohtml='<audio id="mp3"><source src="' + audio + '" type="audio/mp3">Your browser does not support play audio.</audio>'

    f=open(os.path.join(directory, filename), 'w+')
    f.write(part1)
    f.write(snippet)
    f.write(audiohtml)
    f.write(part2)
    f.close()




path = "."

for r, d, f in os.walk(path):
    for entry in d:
        pages=dict()
        audios=dict()
        maxindex=0
        for r1, d1, f1 in os.walk(os.path.join(path, entry)):
            for name in f1:
                if name.startswith("page-") and name.endswith(".jpg"):
                    index = getPageIndex(name)
                    pages[index] = name
                    if index > maxindex:
                        maxindex = index
                if name.endswith(".mp3"):
                    audios[getAudioIndex(name)] =  name
        for index, name in pages.items():
            if index in audios:
                genHtmlFile(r1, index, name, audios[index], maxindex)
            else:
                genHtmlFile(r1, index, name, '', maxindex)


