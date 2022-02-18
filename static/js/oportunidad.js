$('#anadirActividadesAOpotunidad').click(function () {
    //saber cuantos childs tiene el div
    const numeroActividades = $('#listado-de-actividades').children().length;
    let idActividades = "";
    for (let i = 1; i < numeroActividades + 1; i++) {
        const checked = $('#escoger-actividad-' + i).prop('checked');
        //console.log(checked);
        if (checked) {
            idActividades += i + ",";
        }
    }
    //se quedaría así 1,3,
    //quitar la última coma
    if (idActividades.length > 0) {
        idActividades = idActividades.substring(0, idActividades.length - 1);
    }
    //agregar el id de las actividades a la oportunidad
    $('#listado-actividades').val(idActividades);

    //hacer clic en cerrar
    $('.cerrar-modal').click();
})

$('#anadirClientesAOpotunidad').click(function () {
    //saber cuantos childs tiene el div
    const numeroClientes = $('#listado-de-clientes').children().length;
    let idClientes = "";
    for (let i = 1; i < numeroClientes + 1; i++) {
        const checked = $('#escoger-cliente-' + i).prop('checked');
        if (checked) {
            idClientes += i + ",";
        }
    }
    //se quedaría así 1,3,
    //quitar la última coma
    if (idClientes.length > 0) {
        idClientes = idClientes.substring(0, idClientes.length - 1);
    }
    //agregar el id de los clientes a la oportunidad
    $('#listado-clientes').val(idClientes);

    //cerrar modal
    $('.cerrar-modal').click();

})

function verActividad(id, descripcion, fecha_vencimiento, fecha_limite, resumen, tipo) {
    let texto = ""
    texto += "Id: " + id + "<br>";
    texto += "Descripción: " + descripcion + "<br>";
    texto += "Fecha de vencimiento: " + fecha_vencimiento + "<br>";
    texto += "Fecha límite: " + fecha_limite + "<br>";
    texto += "Resumen: " + resumen + "<br>";
    texto += "Tipo: " + tipo + "<br>";
    $('#modal-ver-actividades-asignadas-oportunidad').modal('show');
    $('#modal-actividad-body').html(texto);
}

function verCliente(id, nombre, telefono, email, web, direccion, ciudad) {
    let texto = ""
    texto += "Id: " + id + "<br>";
    texto += "Nombre: " + nombre + "<br>";
    texto += "Teléfono: " + telefono + "<br>";
    texto += "Email: " + email + "<br>";
    texto += "Web: " + web + "<br>";
    texto += "Dirección: " + direccion + "<br>";
    texto += "Ciudad: " + ciudad + "<br>";
    $('#modal-ver-clientes-asignados-oportunidad').modal('show');
    $('#modal-cliente-body').html(texto);
}