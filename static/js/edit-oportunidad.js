$('#abrir-modal-anadir-actividades').click(function () {
    let ids = $('#listado-actividades').val();
    if (ids.length > 0) {
        ids = ids.substring(0, ids.length - 1);
        //split
        let id_actividades = ids.split(',');

        //console.log(id_actividades);

        for (let i = 0; i < id_actividades.length; i++) {
            //añadir atributo ckecked a las ya escogidas anteriormente.
            $('#escoger-actividad-' + id_actividades[i]).attr('checked', true);
        }
    }
})



$('#abrir-modal-anadir-clientes').click(function () {
    let ids = $('#listado-clientes').val();
    if (ids.length > 0) {
        ids = ids.substring(0, ids.length - 1);
        //split
        let id_clientes = ids.split(',');

        //console.log(id_clientes);

        for (let i = 0; i < id_clientes.length; i++) {
            //añadir atributo ckecked a las ya escogidas anteriormente.
            $('#escoger-cliente-' + id_clientes[i]).attr('checked', true);
        }
    }
})