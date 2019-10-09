import requests
from pyquery import PyQuery as pq


html = '''
<div id="container">
    <ul class="list">
         <li class="item-0" img="aaa">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active2"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html)
pagecode = doc('#container')
print(pagecode)