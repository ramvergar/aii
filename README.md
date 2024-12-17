Se desea construir una página web, que permita recomendar a usuarios películas y otras consultas.
(1 punto) CONSTRUIR UN MODELO DE DATOS CORRECTO en Django que almacene la
información siguiente:
a- Pelicula: idPelicula, Título, Director, idIMDB y Géneros
b- Puntuación: IdUsario, idPelicula, Puntuación (10-50, en rangos de 5)
Los datos se encuentran en dos ficheros del dataset que acompaña a este enunciado. Se
proporcionan en dos formatos (csv y txt delimitado por tabulaciones) para que seleccionéis el que
os resulte más cómodo.
Se pide (1 punto) CONSTRUIR UNA WEB CON UN MENÚ que permita las siguientes
opciones:
a- (2.25 puntos) CARGAR LA BASE DE DATOS. Muestre un formulario de confirmación.
Si se acepta, borrar la base de datos y volverla a crear con los datos del dataset. Después
MOSTRAR INFORMACIÓN DE LOS REGISTROS ALMACENADOS EN CADA
TABLA que hayáis definido en el modelo.
b- (1 punto) CARGAR RECSYS. Que cargue TODOS LOS DATOS NECESARIOS para
el Sistema de Recomendación y otros apartados.
c- (1.5 puntos) PELICULAS POR GENEROS. Muestre un formulario con una spinbox con
los géneros que hay en la BD. Cuando se seleccione uno muestre las películas de ese
género agrupadas por director y los datos de cada una (Título, idIMDB y Géneros).
d- (1.75 puntos) PELÍCULAS MÁS PUNTUADAS. Muestre las dos películas que más
puntuaciones han recibido (Título y número de puntuaciones). Para cada una que muestre
también las películas que más se le parecen (Título y coeficiente de similaridad).
e- (1.5 puntos) RECOMENDAR USUARIOS. Muestre un formulario para introducir una
película (Título de la película), le recomiende dos usuarios que no la hayan puntuado
(idUsuario y puntuación de la recomendación), usando un sistema de recomendación
Basado en Usuarios.