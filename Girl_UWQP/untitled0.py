# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 13:17:04 2022

@author: Gowtham Kishore
"""

<ul id="producers">

<li class="producerlist">

<div class="name">plants</div>

<div class="number">100000</div>

html_markup """<p class="ecopyramid">

</li>

<li class="producerlist">

<div class="name">algae</div>

<div class="number">108ee0</div>

</li>

</ul>"""

soup = BeautifulSoup (html_markup, "1xml") 
print (soup.get_text())