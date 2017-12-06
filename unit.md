### Unit conversion for EM spectrum units
#### Original code: Lisa V. Brown at <a href="http://halas.rice.edu/conversions" target="blank">Halas Nanophotonics Group</a>
To use, simply input the known value to the corresponding cell. The calculated value for all the others will be rounded to the fourth decimal.

<form name="conversion">
<table cellpadding="2" align="center" style="border-width:1px" bordercolor="#CCCCCC">
<tr>
<td>Wavelength</td><td>&lambda;</td><td></td><td></td>
</tr>
<tr>
<td><input name="A" onkeyup="angstrom_to_all()" value="26069000" size="15"> &#8491; </td>          
<td><input name="nm" onkeyup="nmconvert()" value="2606900" size="15"> nm </td>
<td><input name="um" onkeyup="umconvert()" value="2606.90" size="15"> &#181;m </td>
<td><input name="cm" onkeyup="cmconvert()" value="0.2607" size="15"> cm </td>
</tr>
<tr>
<td>Frequency</td><td>&nu;=c/&lambda;</td><td></td><td></td>
</tr>
<tr>
<td><input name="THz" onkeyup="THzconvert()" value="0.115" size="15"> THz </td>
<td><input name="GHz" onkeyup="GHz_to_all()" value="115" size="15"> GHz </td>
<td></td><td></td></tr>
<tr>
<td>Energy</td><td>E=hc/&lambda;</td><td></td><td></td>
</tr>
<tr>
<td><input name="keV" onkeyup="keVconvert()" value="0.0000" size="15"> keV </td>
<td><input name="eV" onkeyup="eVconvert()" value="0.0005" size="15"> eV </td>
<td><input name="meV" onkeyup="meV_to_all()" value="0.4756" size="15"> meV </td>
<td></td>
</tr>
<tr>
<td>Wave number</td><td>k=2&pi;/&lambda;</td><td></td><td></td>
</tr>
<tr>
<td><input name="k" onkeyup="k_to_all()" value="24.1022" size="15"> cm<sup>-1</sup> (Physics) </td>
<td></td><td></td><td></td>
</tr>
<tr>
<td>Linear wave number</td><td>&sim;&nu;=1/&lambda;</td><td></td><td></td>
</tr>
<tr>
<td><input name="lk" onkeyup="lkconvert()" value="3.8360" size="15"> cm<sup>-1</sup> (Chemistry) </td>
<td></td><td></td><td></td>
</tr></table>
</form>

<script language="javascript">
// Constants
c_AGHz = 2.99792458e9;
c_twopi_cmGHz = 2.99792458e1 / 2 / Math.PI;
hc_meVA = 1.23984193e7;
h_meV_GHz = 4.135667662e-3;
twopi_A_cm = Math.PI * 2e8;
twopi = Math.PI * 2;
hbarc_meVcm = 1.9732697e-2;
prec = 4

// Wavelength
function angstrom_to_all(from_other=false, from_W=10){
    with (document.conversion){
        if (! from_other) {
            meV.value=(hc_meVA/A.value).toFixed(prec);
            meV_to_all(true)
            GHz.value=(c_AGHz/A.value).toFixed(prec);
            GHz_to_all(true);
            k.value=(twopi_A_cm/A.value).toFixed(prec);
            k_to_all(true);
        }
        if (from_W != 9) {
            nm.value=(A.value*(1e-1)).toFixed(prec);
        }
        if (from_W != 6) {
            um.value=(A.value*(1e-4)).toFixed(prec);
        }
        if (from_W != 2) {
            cm.value=(A.value*(1e-8)).toFixed(prec);
        }
    }
}
function nmconvert(){
    with (document.conversion){
        A.value=(nm.value*10).toFixed(prec);
        angstrom_to_all(false, 9);
    }
}
function umconvert(){
    with (document.conversion){
        A.value=(um.value*1e4).toFixed(prec);
        angstrom_to_all(false, 6);
    }
}
function cmconvert(){
    with (document.conversion){
        A.value=(cm.value*1e8).toFixed(prec);
        angstrom_to_all(false, 2);
    }
}

// Energy
function meV_to_all(from_other=false, from_E=3){
    with (document.conversion){
        if (! from_other) {
            A.value = (hc_meVA/meV.value).toFixed(prec);
            angstrom_to_all(true);
            GHz.value = (meV.value/h_meV_GHz).toFixed(prec);
            GHz_to_all(true);
            k.value = (meV.value/hbarc_meVcm).toFixed(prec);
            k_to_all(true);
        }
        if (from_E != 0) {
            eV.value = (meV.value*(1e-3)).toFixed(prec);
        }
        if (from_E != 3) {
            keV.value = (meV.value*(1e-6)).toFixed(prec);
        }
    }
}
function eVconvert(){
    with (document.conversion){
        meV.value = (eV.value*(1e3)).toFixed(prec);
        meV_to_all(false, 0);
    }
}
function keVconvert(){
    with (document.conversion){
        meV.value = (keV.value*(1e6)).toFixed(prec);
        meV_to_all(false, 3);
    }
}

// Frequency
function GHz_to_all(from_other=false, from_f=9){
    with (document.conversion){
        if (! from_other) {
            A.value = (c_AGHz/GHz.value).toFixed(prec);
            angstrom_to_all(true);
            meV.value = (GHz.value*h_meV_GHz).toFixed(prec);
            meV_to_all(true);
            k.value = (GHz.value / c_twopi_cmGHz).toFixed(prec);
            k_to_all(true);
        }
        if (from_f != 12) {
            THz.value = (GHz.value*(1e-3)).toFixed(prec);
        }
    }
}
function THzconvert(){
    with (document.conversion){
        GHz.value = (THz.value*1e3).toFixed(prec);
        GHz_to_all(false, 12);
    }
}

// Wave number
function k_to_all(from_other=false, from_k=2){
    with (document.conversion){
        if (! from_other) {
            A.value = (twopi_A_cm/k.value).toFixed(prec);
            angstrom_to_all(true);
            meV.value = (hbarc_meVcm*k.value).toFixed(prec);
            meV_to_all(true);
            GHz.value = (c_twopi_cmGHz * k.value).toFixed(prec);
            GHz_to_all(true);
        }
        if (from_k != 'l') {
            lk.value = k.value/twopi;
        }
    }
}

function lkconvert(){
    with (document.conversion){
        k.value = (lk.value*twopi).toFixed(prec);
        k_to_all(false, 'l');
    }
}

</script>
<br>
#### Useful lines
HI 21 cm line: 1.420405752 GHz

Ly	&alpha;: 121.567 nm

CO J:1	&rarr;0: 115 GHz
