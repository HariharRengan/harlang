# harlang
An interpreted programming language named harlang, whose interpreter is written in Python. <br>
<code>py harlang.py main 4</code> or <code> harlang main 4</code> translates to interpret main.harl with 4 "boxes".<br>
The language is built around these boxes. 
<ul>
<li>The <code>SET</code> command assigns a value to a box of a certain index in the array of boxes. </li>
<li>TUsing <code>ADD</code> and <code>SUB</code> to add and subtract boxes, enabling manipulation of their contents. </li>
<li>TUsing the <code>DO</code> and <code>IF</code> commands, iteration and selection can be achieved. </li>
<li>TUse <code>OUT</code> to output a variable. </li>
</ul>
General syntax can be observed through the main.harl file: <br>
<code>
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
]</code><br>
Translates to:<br>
<ul>
  <li>Set box 0 to 5</li>
  <li>Set box 1 to 6</li>
  <li>Set box 2 to 1</li>
  <li>Add the contents of box 1 and box 1 (12), then store that in box 1 (ADD a b -> SET a a+b) </li>
  <li>Print the contents of box 1 (12) </li>
  <li>Print the contents of box 0 (5) </li>
  <li>Subtract the contents of box 1 from box 1 (0) and store that in box 1 </li>
  <li>If the contents of box 0 match that of box 0 (True), print the contents of box 1 (0) </li>
  <li>While the contents of box 0 do not match the contents of box 1, print the contents of box 0 and subtract the contents of box 2 (1) from box 0, storing that new value in box 0.</li>
</ul>
Although an odd program, it has a relatively normal output: <br>
<code>
12 <- First print statement
5 <- Second print statement
0 <- Result of If statement
5 <- Decrementing loop
4 <- Again
3 <- Again
2 <- Again
1 <- Nearing the end
</code>
