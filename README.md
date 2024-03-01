# Nombre Proyecto:
# Alumno: Patricio Eyzaguirre
# Fecha: 29.02.2024
# Versión: Proyecto Final
# Usuario Admin:
#   user: usuario
#   pass: 0rd_P1ssw


# Aplicación que permite el control de entrega de productos en diferentes cadenas de supermercados.


# Modelos: Los modelos que presenta la App por el momento son:
    - Locales: Base de supermercados a los que se realizará un determinado despacho.
    - Productos: Base de productos que puede ser despachada a diferentes supermercados.
    - Repartidor: Base de personal encargado de realizar los despachos de productos.
    - Entregas: Detalle de despachos realizados.

Orden de prueba de aplicación:

    - Home : http://localhost:8000/Flujos/

    - Mantenedores:
        - Productos:
            - Lista Productos : http://localhost:8000/Flujos/Productos
            - Nuevo Producto: http://localhost:8000/Flujos/FormularioProducto
            - Buscar Productos: http://localhost:8000/Flujos/buscar
        - Locales:
            - Lista Locales: http://localhost:8000/Flujos/Locales
            - Nuevo Local: http://localhost:8000/Flujos/FormularioLocal
        - Reponedores:
            - Lista Reponedores: http://localhost:8000/Flujos/Repartidores
            - Nuevo Reponedores: http://localhost:8000/Flujos/FormularioRepartidor

    - Despacho:
        - Ingreso Despacho: http://localhost:8000/Flujos/FormularioEntrega
        - Lista Despachos: http://localhost:8000/Flujos/Entregas

    - Usuario:
        - Logout: http://localhost:8000/Flujos/logout/
        - Editar Perfil: http://localhost:8000/Flujos/editar_perfil/

    - Autenticación:
        - Login: http://localhost:8000/Flujos/login/
        - registrarse: http://localhost:8000/Flujos/registro/

    - About Me...: http://localhost:8000/Flujos/AboutMe




- Cabe mencionar que todas las opciones antes señaladas se encuentran disponibles también en el menú correspondiente.

- Para acceder al HOME se puede linkear en el título "Logística de Productos" o en la palabra "Dashboard" sobre el 
  MENÚ.

Observaciones: 
    1.- El proyecto se pensó con otra finalidad, sin embargo a medio andar tuve que cambiar la idea de negocio. Dado
        lo anterior el proyecto y aplicación tienen un nombre que no corresponde, el que no pude cambiar por errores que se generaban.

    2.- El sitio principal considera unas tarjetas de KPI, que debían actualizarse según los despachos ingresados pero
        lamentablemente no alcancé a desarrollar dicha funcionalidad, por lo que los números ahí mostrados son valores fijos.



