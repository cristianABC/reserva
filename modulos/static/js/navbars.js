function openNav(idModal, idSpecie) {
    // document.getElementById("loginSideNav").style.width = "30vw";
    let modal = $('#' + idModal);
    if (idSpecie || idSpecie === 0) {
        //Se usa el API para consultar la especie que entra por parametro
        $.getJSON('./rest/' + idSpecie).done((data) => {
            //Se elimina el elemento que este actualmente en el modal
            modal.children('.modal').remove();

            //Se extrae la información de la especie
            const nombre = data[0].fields.nombre;

            //Se crea el elemento que se agregará al index.html y se agrega la información de la especie
            const element = `
            <div class="modal modal-detail">
                <div class="content">
                  <div class="title">${nombre}</div>
                </div>
              </div>
            `
            //Se agrega el elemento
            modal.append(element);
            modal.css('width', '30vw');

        });
    }
    else {
        modal.css('width', '30vw');
    }
}

function closeNav() {
    $('.sidenav').css('width', '0');
    $('#detailSideNav').children('iframe').remove();
}