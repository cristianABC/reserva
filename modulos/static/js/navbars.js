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
            const comentario = data[0].fields.comentario;
            const descripcion = data[0].fields.descripcion;
            const nombreCientifico = data[0].fields.nombreCientifico;
            const url = data[0].fields.url;
            const categoria = data[0].fields.categoria;
            const imageFile = data[0].fields.imageFile;
            const clasificacionTax = data[0].fields.imageFile;
            const imageUrl = imageFile ? imageFile.url : url;

            $.getJSON('./isLogged/').done( function ( data ) {

                console.log(data.mensaje);

                if (data.mensaje == "no")
                {
                    $("#comentario").hide();
                }
                else
                {
                    $("#comentario").show();
                }
            });

            //Se crea el elemento que se agregará al index.html y se agrega la información de la especie
            const element = `
            <div class="modal modal-detail">
                <div class="content">
                    <div class="title">${nombre}</div>
                    <div class="category">${categoria}</div>
                    <img class="image" src="${imageUrl}"/>
                    <div class="name">${nombreCientifico} </div>
                    <div class="description">${descripcion} </div>
                    <div class="classification">${clasificacionTax} </div>
                    <div class="Comentarios">${comentario ? comentario : "No hay comentarios"} </div>
                    <form method="POST" action='addComentario' class="form-group" id="comentario">
                        Comentario: <textarea type="text"id="comentario" name="comentario"></textarea>
                     <button type="submit">Comentar</button>
                    </form>
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