function openNav(idModal, idSpecie) {
    // document.getElementById("loginSideNav").style.width = "30vw";
    let modal = $('#' + idModal);
    if(idSpecie || idSpecie === 0) {
        modal.children('iframe').remove();
        modal.append('<iframe  frameborder=\"0\"></iframe>');
        modal.children('iframe').attr('src', './detalle/' + idSpecie);
        modal.children('iframe').ready(()=>{modal.css('width','30vw');})
    }
    else {
        modal.css('width', '30vw');
    }
}

function closeNav() {
    $('.sidenav').css('width','0');
    $('#detailSideNav').children('iframe').remove();
}