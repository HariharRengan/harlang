# harlang
An interpreted programming language named harlang, whose interpreter is written in Python. <br>
<code>py harlang.py main 4</code> - Interpret main.hrl with 4 "boxes".<br>
The language is built around these boxes. 
<ul>
<li>The <code>SET</code> command assigns a value to a box of a certain index in the array of boxes. </li>
<li>TUsing <code>ADD</code> and <code>SUB</code> to add and subtract boxes, enabling manipulation of their contents. </li>
<li>TUsing the <code>DO</code> and <code>IF</code> commands, iteration and selection can be achieved. </li>
<li>TUse <code>OUT</code> to output a variable. </li>
</ul>
General syntax can be observed through the main.hrl file: <br>
<code>Main.hrl
SET 0 5;<br>
SET 1 6;<br>
SET 2 1;<br>
ADD 1 1;<br>
OUT 1;<br>
OUT 0;<br>
SUB 1 1;<br>
IF 0 = 0 [<br>
OUT 1;<br>
]<br>
DO 0 ! 1 [<br>
OUT 0;<br>
SUB 0 2;<br>
]</code>
