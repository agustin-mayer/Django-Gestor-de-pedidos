# Gestor de Pedidos

Este proyecto es un gestor de pedidos desarrollado en Django que te permite gestionar pedidos, clientes y productos.

## Funcionalidades

- **Ver pedidos:** Accede a la página principal para ver todos los pedidos registrados.
- **Ver detalles de un pedido:** Haz clic en un pedido para ver más detalles, incluidos los productos asociados.
- **Crear nuevo pedido:** Utiliza el formulario de creación de pedidos para añadir un nuevo pedido con su respectivo cliente y productos.
- **Modificar pedido:** Accede a la página de modificación de un pedido para cambiar su cliente, estado o productos asociados.
- **Eliminar pedido:** Elimina un pedido de la base de datos.

## Instalación

Para instalar y ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio:**

    ```
    git clone https://github.com/agustin-mayer/Django-Gestor-de-pedidos.git
    ```

2. **Instala los requisitos:**

    Ve al directorio del proyecto y ejecuta:

    ```
    pip install -r requirements.txt
    ```

3. **Configura la base de datos:**

    Asegúrate de tener configurada tu base de datos en el archivo `settings.py`. Por defecto, se utiliza SQLite para facilitar la configuración inicial.

4. **Aplica las migraciones:**

    Ejecuta el siguiente comando para aplicar las migraciones a tu base de datos:

    ```
    python manage.py migrate
    ```

5. **Inicia el servidor:**

    Ahora puedes iniciar el servidor de desarrollo ejecutando:

    ```
    python manage.py runserver
    ```

6. **Accede al proyecto:**

    Abre tu navegador web y visita [http://localhost:8000/](http://localhost:8000/) para ver el proyecto en funcionamiento.
