# de-jupyter-a-la-tierra

## Intro

Las libretas interactivas de Python, o Jupyter Notebooks, son una maravilla.
Son un entorno cómodo y visual en el que importar módulos, estudiar sets de datos, pintar gráficos, entrenar modelos ML, y compartir código y resultados de forma directa y conveniente.
En algunos sitios, como Kaggle, ¡hasta puedes ganar premios por ellas!
Desgraciadamente, por buenas que sean para explorar o prototipar, no son capaces de hacerlo todo. Para empezar, son un medio pésimo sobre el que realizar un despliegue (¿te imaginas?).

Independientemente de lo que esté escrito en la descripción de su puesto de trabajo, es probable que un@ científic@ de datos tenga que acabar preocupándose por la forma en la que sus modelos se van a ejecutar y a servir en un entorno de producción.
De forma similar, es posible que una persona experta en desarrollo e integración acabe encontrándose a sí misma pensando en la mejor manera de gestionar los entrenamientos y las predicciones de un algoritmo de machine learning, aunque no esté interesada para nada en las matemátimas o la estadística.
Y mientras que está bien que los representantes de ambos "bandos" tengan una idea general sobre los requerimientos y preocupaciones del otro, no conviene malgastar demasiadas horas de científic@s de datos en tareas de desarrollo complejas y poco familiares, ni obligar al personal developer a pelearse con redes neuronales o a limpiar código sucio y desestructurado.

Para evitar estas situaciones en la medida de lo posible y tender un puente entre los dos ámbitos, propongo la adopción de un framework estándar. Algo que ayude a Datos a ordenar su código y seguir buenas prácticas de ingeniería, y que produzca objetos fácilmente entendibles y ejecutables por Desarrollo. Un lenguaje común y bien definido en el que comunicarse entre sí y con los demás equipos. En este caso, es razonable que ese puente pase por la disciplina de la ingeniería de datos. Y una buena solución para la ingeniería de datos es el framework [Kedro](https://kedro.readthedocs.io/en/stable/).

## Cómo navegar este repo

Prueba a cambiar de rama para visualizar las diversas versiones del proyecto, desde una simple libreta, hasta una aplicación bastante completa con Kedro, API de predicción, tests de varios tipos, y seguimiento de experimentos con mlflow.

En esta primera rama (main) encontrarás la libreta original, donde se presenta el proyecto desde el punto de vista del Machine Learning.
Cada rama a partir de esta incluirá explicaciones sobre los cambios que introduzca, guiándote a través de las instalaciones necesarias para que puedas ejecutar y entender el nuevo código.
