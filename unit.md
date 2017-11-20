### Unit conversion for EM spectrum units
#### Original code: Lisa V. Brown at <a href="http://halas.rice.edu/conversions">Halas Nanophotonics Group</a>
To use, simply input the known value to the corresponding cell. The calculated value for all the others will be rounded to the fifth 

<form name="conversion"
<input name="meV" type="text" onkeyup="meVconvert()" value="0.4756"size="15"></input> meV</td>
a<input type="text" id="name" name="name">b
</form>

<form name="conversion">
<table cellpadding="2" align="center" style="border-width:1px" bordercolor="#CCCCCC">
<tr>
<td><span style="font-size:10pt"><input name="meV" onkeyup="meVconvert()" value="0.4756"size="15"></input> meV</span></td>
<td><span style="font-size:10pt"><input name="eV" onkeyup="eVconvert()" value="0.00048" size="15"></input> eV</span></td>
<td><span style="font-size:10pt"><input name="GHz" onkeyup="GHzconvert()" value="115" size="15"></input> GHz</span></td>
<td><span style="font-size:10pt"><input name="T" onkeyup="Tconvert()" value="5.51911" size="15"></input> K</span></td>
</tr><tr>
<td><span style="font-size:10pt"><input name="A" onkeyup="angstromconvert()" value="26069000" size="15"></input> &#8491;</span></td>          
<td><span style="font-size:10pt"><input name="nm" onkeyup="nmconvert()" value="2606900" size="15"></input> nm</span></td>
<td><span style="font-size:10pt"><input name="micron" onkeyup="micronconvert()" value="2606.90" size="15"></input> &#181;m</span></td>
<td><span style="font-size:10pt"><input name="cm" onkeyup="cmconvert()" value="0.26069" size="15"></input> cm</span></td>
</tr></table></form>

<script language="javascript">
c=299792458;
h=4.135667516e-15;
hc = h*c;
kB=8.6173305e-5;
function roundfive(num){
round = (Math.round(num*100000))/100000
return (round.toFixed(5))
}
function eVconvert(){
with (document.conversion){
meV.value=roundfive(eV.value*(1e3));
T.value=roundfive(eV.value/kB);
GHz.value=roundfive(eV.value/h*(1e-9));
A.value=roundfive(hc/eV.value*(1e10));
nm.value=roundfive(hc/eV.value*(1e9));
micron.value=roundfive(hc/eV.value*(1e6));
cm.value=roundfive(hc/eV.value*(1e2));
}}
function meVconvert(){
with (document.conversion){
eV.value=roundfive(meV.value*(1e-3));
GHz.value=roundfive(meV.value/h*(1e-9)*(1e-3));
T.value=roundfive(meV.value/kB*(1e-3));
A.value=roundfive(hc/meV.value*(1e10)*(1e3));
nm.value=roundfive(hc/meV.value*(1e9)*(1e3));
micron.value=roundfive(hc/meV.value*(1e6)*(1e3));
cm.value=roundfive(hc/meV.value*(1e2)*(1e3));
}}
function GHzconvert(){
with (document.conversion){
eV.value=roundfive(h*GHz.value*(1e9));
meV.value=roundfive(h*GHz.value*(1e9)*(1e3));
T.value=roundfive(h/kB*GHz.value*(1e9));
A.value=roundfive(c/GHz.value*(1e-9)*(1e10));
nm.value=roundfive(c/GHz.value*(1e-9)*(1e9));
micron.value=roundfive(c/GHz.value*(1e-9)*(1e6));
cm.value=roundfive(c/GHz.value*(1e-9)*(1e2));
}}

function Tconvert(){
with (document.conversion){
eV.value=roundfive(kB*T.value);
meV.value=roundfive(kB*T.value*(1e3));
GHz.value=roundfive(kB/h*T.value*(1e-9));
A.value=roundfive(hc/kB/T.value*(1e10));
nm.value=roundfive(hc/kB/T.value*(1e9));
micron.value=roundfive(hc/kB/T.value*(1e6));
cm.value=roundfive(hc/kB/T.value*(1e2));
}}

function angstromconvert(){
with (document.conversion){
eV.value=roundfive(hc/A.value*(1e10));
meV.value=roundfive(hc/A.value*(1e10)*(1e3));
GHz.value=roundfive(c/A.value*(1e10)*(1e-9));
T.value=roundfive(hc/kB/A.value*(1e10));
nm.value=roundfive(A.value*(1e-1));
micron.value=roundfive(A.value*(1e-4));
cm.value=roundfive(A.value*(1e-8));
}}
function nmconvert(){
with (document.conversion){
eV.value=roundfive(hc/nm.value*(1e9));
meV.value=roundfive(hc/nm.value*(1e9)*(1e3));
GHz.value=roundfive(c/nm.value*(1e9)*(1e-9));
T.value=roundfive(hc/kB/nm.value*(1e9));
A.value=roundfive(nm.value*(10));
micron.value=roundfive(nm.value*(1e-3));
cm.value=roundfive(nm.value*(1e-7));
}}
function micronconvert(){
with (document.conversion){
eV.value=roundfive(hc/micron.value*(1e6));
meV.value=roundfive(hc/micron.value*(1e6)*(1e3));
GHz.value=roundfive(c/micron.value*(1e6)*(1e-9));
T.value=roundfive(hc/kB/micron.value*(1e6));
A.value=roundfive(micron.value*(1e4));
nm.value=roundfive(micron.value*(1e3));
cm.value=roundfive(micron.value*(1e-4));
}}

function cmconvert(){
with (document.conversion){
eV.value=roundfive(hc/cm.value*(1e2));
meV.value=roundfive(hc/cm.value*(1e2)*(1e3));
GHz.value=roundfive(c/cm.value*(1e2)*(1e-9));
T.value=roundfive(hc/kB/cm.value*(1e2));
A.value=roundfive(cm.value*(1e8));
nm.value=roundfive(cm.value*(1e7));
micron.value=roundfive(cm.value*(1e4));
}}

#### Useful lines
HI 21 cm line: 1.420405752 GHz

Ly	&alpha;: 121.567 nm

CO J:1	&rarr;0: 115 GHz
