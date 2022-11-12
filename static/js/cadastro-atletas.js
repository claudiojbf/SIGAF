function negar() {
    var checkNivelEnsino = document.getElementById("blankCheckbox1");
    var checkPlanoSaude = document.getElementById("blankCheckbox2");
    var checkAlergia = document.getElementById("blankCheckbox3");

    var inputNivelEnsino1 = document.getElementById("optionsRadios4");
    var inputNivelEnsino2 = document.getElementById("optionsRadios5");
    var inputNomeEscola = document.getElementById("nomeEscola");

    var inputNomeserie = document.getElementById("serie");

    var inputPlanoSaude = document.getElementById("planoSaude");

    var inputAlergia = document.getElementById("alergia");

    if (checkNivelEnsino.checked) {
        inputNivelEnsino1.disabled = true;
        inputNivelEnsino2.disabled = true;
        inputNomeEscola.disabled = true;
        inputNomeserie.disabled = true;
    }else{
        inputNivelEnsino1.disabled = false;
        inputNivelEnsino2.disabled = false;
        inputNomeEscola.disabled = false;
        inputNomeserie.disabled = false;
    }

    if(checkPlanoSaude.checked) {
        inputPlanoSaude.disabled = true;
    }else{
        inputPlanoSaude.disabled = false;
    }

    if(checkAlergia.checked){
        inputAlergia.disabled = true;
    }else{
        inputAlergia.disabled = false;
    }
}