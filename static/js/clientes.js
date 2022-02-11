function abrirModalModificarUsuario(id, nombre, telefono, email, web, direccion, ciudad) {
    $('.modal-body #id-modificar').val(id);
    $('.modal-body #nombre-modificar').val(nombre);
    $('.modal-body #telefono-modificar').val(telefono);
    $('.modal-body #email-modificar').val(email);
    $('.modal-body #web-modificar').val(web);
    $('.modal-body #direccion-modificar').val(direccion);
    $('.modal-body #ciudad-modificar').val(ciudad);
    //$('#modal-modificar').modal('show');
}