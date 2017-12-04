### Unit conversion for EM spectrum units
#### Original code: Lisa V. Brown at <a href="http://halas.rice.edu/conversions" target="blank">Halas Nanophotonics Group</a>
To use, simply input the known value to the corresponding cell. The calculated value for all the others will be rounded to the fifth decimal.

### I am working on this... 12/03/2017 16:09
<form name="conversion">
Wavelength
<table cellpadding="2" align="center" style="border-width:1px" bordercolor="#CCCCCC">
<tr>
<td><input name="A" onkeyup="angstrom_to_all()" value="26069000" size="15"> &#8491; </td>          
<td><input name="nm" onkeyup="nmconvert()" value="2606900" size="15"> nm </td>
<td><input name="um" onkeyup="umconvert()" value="2606.90" size="15"> &#181;m </td>
<td><input name="cm" onkeyup="cmconvert()" value="0.26069" size="15"> cm </td>
</tr></table>
Frequency
<table cellpadding="2" align="center" style="border-width:1px" bordercolor="#CCCCCC">
<tr>
<td><input name="GHz" onkeyup="GHz_to_all()" value="115" size="15"> GHz </td>
<td><input name="THz" onkeyup="THzconvert()" value="0.115" size="15"> THz </td>
</tr></table>
Energy
<table cellpadding="2" align="center" style="border-width:1px" bordercolor="#CCCCCC">
<tr>
<td><input name="meV" onkeyup="meV_to_all()" value="0.4756" size="15"> meV </td>
<td><input name="eV" onkeyup="eVconvert()" value="0.00048" size="15"> eV </td>
</tr></table>
Wave number
<table cellpadding="2" align="center" style="border-width:1px" bordercolor="#CCCCCC">
<tr>
// <td><input name="wncm" onkeyup="wncm_to_all()" value="3.83599" size="15"> cm<sup>-1</sup> </td>
</tr></table>
</form>

<script language="javascript">
// Constants
c_AGHz = 2.99792458e9;
hc_meVA = 1.23984193e7;
h_meV_GHz = 4.135667662e-21;
//kB_meV_K = 8.6173303e-2;

// Wavelength
function angstrom_to_all(from_other=false, from_W=10){
    with (document.conversion){
        if (! from_other) {
            meV.value=(hc_meVA/A.value).toFixed(5);
            meV_to_all(true)
            GHz.value=(c_AGHz/A.value).toFixed(5);
            GHz_to_all(true);
        }
        if (from_W != 9) {
            nm.value=(A.value*(1e-1)).toFixed(5);
        }
        if (from_W != 6) {
            um.value=(A.value*(1e-4)).toFixed(5);
        }
        if (from_W != 2) {
            cm.value=(A.value*(1e-8)).toFixed(5);
        }
    }
}
function nmconvert(){
    with (document.conversion){
        A.value=(nm.value*10).toFixed(5);
        angstrom_to_all(false, 9);
    }
}
function umconvert(){
    with (document.conversion){
        A.value=(um.value*1e4).toFixed(5);
        angstrom_to_all(false, 6);
    }
}
function cmconvert(){
    with (document.conversion){
        A.value=(cm.value*1e8).toFixed(5);
        angstrom_to_all(false, 2);
    }
}

// Energy
function meV_to_all(from_other=false, from_E=3){
    with (document.conversion){
        if (! from_other) {
            A.value = (hc_meVA/meV.value).toFixed(5);
            angstrom_to_all(true)
            GHz.value = (meV.value/h_meV_GHz).toFixed(5);
            GHz_to_all(true);
        }
        if (from_E != 0) {
            eV.value = (meV.value*(1e-3)).toFixed(5);
        }
    }
}
function eVconvert(){
    with (document.conversion){
        meV.value = (eV.value*(1e3)).toFixed(5);
        meV_to_all(false, 0)
    }
}

// Frequency
function GHz_to_all(from_other=false, from_f=9){
    with (document.conversion){
        if (! from_other) {
            A.value = (c_AGHz/GHz.value).toFixed(5);
            angstrom_to_all(true)
            meV.value = (GHz.value*h_meV_GHz).toFixed(5);
            meV_to_all(true)
        }
        if (from_f != 12) {
            THz.value = (GHz.value*(1e-3)).toFixed(5);
        }
    }
}
function THzconvert(){
    with (document.conversion){
        GHz.value = (THz.value*1e3).toFixed(5);
        GHz_to_all(false, 12);
    }
}

// Wave number


</script>
<br>
#### Useful lines
HI 21 cm line: 1.420405752 GHz

Ly	&alpha;: 121.567 nm

CO J:1	&rarr;0: 115 GHz
