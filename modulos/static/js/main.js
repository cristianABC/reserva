let url='./rest/all/';
function mountData(){
    $.getJSON(url).done((data) => {
        console.log(url);
        const parent = $('.container');
        parent.children('.row').remove();
        const nRows = [4, 2, 3, 5];
        let index = 0;
        let rowIndex = 0;
        while (index < data.length) {
            const index2 = data.length >= index + nRows[rowIndex] ? index + nRows[rowIndex] : data.length;
            let elements = '<div class="row">';
            data.slice(index, index2).map((item, index) => {
                const id = item.pk;
                const {categoria, clasificacionTax, comentario, descripcion, imageFile, nombre, nombreCientifico, url} = item.fields;
                const imageUrl = imageFile ? imageFile.url : url;
                const element = `
                  <div class ="col">
                    <div class="photo-container" style="background-image: url(${imageUrl})"></div>
                    <h2 id="nombre">${nombre}</h2>
                    <div class="slide">
                        <div class="description">${descripcion}</div>
                        <div class="detail" onclick="openNav('detailSideNav',${id})">Ver más</div>
                    </div> 
                  </div>
                   `;
                elements += element;
            });
            elements+='</div>';
            parent.append(elements);


            index = index2;
            rowIndex = rowIndex < nRows.length - 1 ? rowIndex + 1 : 0;
        }


        // data.forEach((item, index) => {
        //     const id = item.pk;
        //     const {categoria, clasificacionTax, comentario, descripcion, imageFile, nombre, nombreCientifico, url} = item.fields;
        //     const imageUrl = imageFile ? imageFile.url : url;
        //     const element = `
        //   <div class ="col">
        //     <div class="photo-container" style="background-image: url(${imageUrl})"></div>
        //     <h2 id="nombre">${nombre}</h2>
        //     <div class="slide">
        //         <div class="description">${descripcion}</div>
        //         <div class="detail" onclick="openNav('detailSideNav',${id})">Ver más</div>
        //     </div>
        //   </div>
        //    `;
        //
        // })
    })
}
mountData();

$('select[name="dropdown"]').change(function () {
    url = './rest/'+$(this).val();
    mountData();
});