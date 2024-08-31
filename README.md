# Pre-SantiagoGonzalez

Web de Autorizaciones de panel de Obra Social

Se presenta un prototipo de web para una obra social en la cual se presenta tres modelos

- Ingresar un Afiliado
- Ingresar prácticas médicas (Siguiendo el modelo del Nomenclador Nacional de Salud) y especificar si requieren autorización o no por parte de la Obra Social
- Autorizar, Rechazar o dejar pendientes pedidos de los afiliados a realizarse ciertas prácticas
- Buscador de estado de autorización de prácticas por afiliado

Para probar esta Web:

1- Es necesario ingresar un afiliado/a con Apellido, Nombre, Email y DNI
  -Ya queda registrado en la base de datos
2-Ingresar prácticas Médicas por código de practica y nombre, tildando el checkbox si la practica requiere autorización
  -Se dejan algunos ejemplos según Nomenclador Nacional:
    180107 -	ECOGRAFIA CEREBRAL (CON MODO B Y A). (No requiere Aut.)
    420101 -	CONSULTA MEDICA (No requiere Aut.)
    342001 -	RESONANCIA MAGNETICA NUCLEAR CEREBRAL. (Requiere Aut.)
3- Ingresar Pedidos
  -Van a aparecer solo los afiliados y practicas ingresadas previamente.
  -Ingresar el estado del pedido, Autorizado o Rechazado
  -Se podrá poner un motivo de rechazo u observación general.

4- Buscar
  -Por cualquier tipo de dato que se tenga del afiliado ingresado en la base de datos, se genera una lista de sus consumos aprobados, rechazados o pendientes




