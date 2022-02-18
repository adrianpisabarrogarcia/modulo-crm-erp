function abrirModalModificarActividad(id, nombre, telefono, email, web, direccion, ciudad) {
    $('.modal-body #id-modificar').val(id);
    $('.modal-body #descripcion-modificar').val(nombre);
    $('.modal-body #fecha-vencimiento-modificar').val(telefono);
    $('.modal-body #fecha-limite-modificar').val(email);
    $('.modal-body #resumen-modificar').val(web);
    $('.modal-body #tipo-modificar').val(direccion);
    //$('#modal-modificar').modal('show');
}