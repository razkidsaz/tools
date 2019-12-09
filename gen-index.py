
import os
import urllib

path = "."



part1="""
<!DOCTYPE html>
<html>
    <head>
        <style>
         .list {
             list-style-type: none;
             display: flex;
             width: 95%;
             flex-wrap: wrap;
             margin-left: auto;
             margin-right: auto;
         }
         .list ul{
             width: 250px;
             height: 300px;
             text-align: center;
             padding: 0 0 0 0;

             border-bottom: 5px solid lightgray;
             border-bottom-right-radius: 10px;
             border-bottom-left-radius: 10px;

             flex: 0 0 33.33%;
             max-width: 30%;
             margin: 0 10px 50px 10px;
             min-width: 250px;

             display: flex;
             justify-content: center;
             align-items: flex-end;
         }
         .list img {
             max-width: 250px;
             max-height: 300px;
         }
        </style>
    </head>
    <body>
        <div class="container">
        <li class="list">
"""


part2="""

        </li>
        </div>
    </body>
</html>

"""



print(part1)

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for entry in d:
        path=urllib.quote(entry)
        print("<ul><a href='" + path + "/page-1.html" + "'><img src='" + path + "/page-1.jpg'/></a></ul>")


print(part2)

