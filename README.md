<a name="readme-top"></a>

<p align="center">
  <img src="./docs/Imagenes/portada_analyticapro.png">
</p>

# <h4 align="center">**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**</h4>

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png"  height="30">
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/512px-Google_Maps_Logo_2020.svg.png"  height="30">


<details>
  <summary><h2>Tabla de Contenido</h2></summary>



- [Acerca del proyecto](#Acerca-del-proyecto)
- [Introducción](#introducción)
- [Alcance](#alcance)
- [Objetivos del Proyecto](#objetivos-del-proyecto)
- [KPIs](#kpis)
- [Entregables](#entregables)
- [Restricciones y Limitaciones](#restricciones-y-limitaciones)
- [Entregables](#entregables)
- [Stack tecnológico](#stack-tecnológico)
- [Pipeline AWS](#pipeline-aws)
- [MVP Dashboard Power BI Final](#MVP-Dashboard-power-BI-final)
- [Fuentes de datos](#fuentes-de-datos)
- [Disclaimer](#disclaimer)

</details>

## **Acerca del proyecto**

Este proyecto forma parte del Proyecto Final de la etapa de Labs del programa de Data Science de Henry, centrado en el análisis del mercado de New York y California para nuestra cliente, la pizzería Sgambati's Pizza. Utilizando datos de Yelp y Google Maps, buscamos comprender las opiniones y preferencias de los usuarios en ambas plataformas, así como identificar tendencias y oportunidades en el sector de la pizza. Nuestro objetivo es desarrollar productos de datos que permitan realizar análisis de sentimientos, predecir el crecimiento o decrecimiento en el mercado de la pizza, recomendar las mejores ubicaciones para nuevas pizzerías, crear un sistema personalizado de recomendación y un generador de recetas de pizzas innovadoras y deliciosas. [Contexto](https://github.com/williamCastro32/PF_Google_yelp_Map/wiki#contexto)

## **Introducción**

En AnalyticaPro Solutions, estamos emocionados de embarcarnos en este proyecto en colaboración con Sgambatis Pizza. Nuestro objetivo es utilizar nuestra experiencia en análisis de datos y tecnologías avanzadas para ayudar a Sgambatis Pizza a comprender mejor la opinión de sus clientes y optimizar su estrategia empresarial. A través de la minería de datos en plataformas como Yelp y Google Maps, buscaremos extraer insights significativos sobre la percepción y preferencias de los clientes, lo que permitirá a Sgambatis Pizza tomar decisiones informadas para mejorar su servicio, expandirse estratégicamente y ofrecer experiencias excepcionales a sus clientes. Estamos comprometidos a utilizar métodos analíticos rigurosos y herramientas innovadoras para brindar resultados de alta calidad que impulsen el éxito de Sgambatis Pizza en el competitivo mercado de la ciudad de Nueva York. Para conocere mas sobre nuestro cliente dirijase a: [Nuestro Cliente](https://github.com/williamCastro32/PF_Google_yelp_Map/wiki#nuestro-cliente)


## **Alcance**

El presente documento establece el alcance del proyecto de análisis de opiniones de usuarios en plataformas de reseñas como Yelp y Google Maps para el mercado de New york y California. Este proyecto, liderado por AnalyticaPro Solutions, tiene como objetivo ofrecer análisis detallados y recomendaciones basadas en datos para Sgambati's Pizza, su cliente en el sector de restaurantes y turismo. [Planteamiento del Problema](https://github.com/williamCastro32/PF_Google_yelp_Map/wiki#planteamiento-del-problemae)

### **Metodología de trabajo**

Para el completo desarrollo del trabajo contamos con tres Sprints cada uno con sus entregables y una duración de dos semanas cada uno. Para el trabajo colaborativo hacemos uso de Trello el cual nos permite establecer una planificación y gestión de tareas grupales facilitando la asignación de tiempos de entrega de cada una de las tareas.

#### **Metodología Ágil**

Como metodología ágil usamos la metodología KANBAN ya que su objetivo es visualizar de manera general cada etapa de una tarea desde que es planeada hasta su realización.

La metodología Kanban es fácil de usar, su sencillez permite mantener actualizado al equipo de trabajo y este puede asumirla sin ningún tipo de complicación. Esto debido a que es un método visual, el cual permite una primera vista para tener información inmediata del estado de los proyectos. De tal forma, se podrá poner en marcha una nueva tarea una vez culminada la anterior y así garantizar un ritmo sostenible en el equipo de trabajo.


### **Objetivos del Proyecto**

- Realizar un análisis detallado de las opiniones de usuarios en Yelp y Google Maps sobre restaurantes, incluyendo Sgambatis Pizza en la ciudad de Nueva York y California.
- Utilizar análisis de sentimientos para comprender la percepción de los clientes sobre Sgambatis Pizza y otros restaurantes similares en la zona.
- Identificar áreas de mejora y oportunidades de crecimiento basadas en las opiniones de los usuarios.
- Desarrollar un sistema de recomendación personalizado para los clientes, que les permita descubrir nuevos sabores basados en sus experiencias previas en Sgambatis Pizza.

### **KPIs**

- Puntuación Promedio de Reseñas: Establecer una meta para aumentar la puntuación promedio de reseñas en Yelp y Google Maps en un cierto margen (por ejemplo, aumentar de 3.5 a 4 estrellas en un año).

   Fórmula: Suma de todas las puntuaciones de las reseñas / Número total de reseñas

- Número de Reseñas Positivas vs. Negativas: Establecer una meta para aumentar la proporción de reseñas positivas en comparación con las negativas (por ejemplo, alcanzar un 80% de reseñas positivas).

   Fórmula: (Número de reseñas positivas - Número de reseñas negativas) / Número total de reseñas

- Análisis de Sentimientos:Establecer un análisis de sentimientos de las reviews positivas, negativas y neutras con el fin de identificar posibles puntos y ciudades donde el cliente pueda establecer nuevos negocios. 

### **Entregables**

- Informe detallado sobre las opiniones de los usuarios en Yelp y Google Maps sobre Sgambatis Pizza, incluyendo análisis de sentimientos y áreas de mejora.
- Sistema de recomendación personalizado para clientes de Sgambatis Pizza, integrado con las plataformas de Yelp y Google Maps.

### **Restricciones y Limitaciones**

Los resultados obtenidos en el proyecto son para fines exclusivamente pedagógicos y no deben ser tomados como base para decisiones comerciales sin una evaluación adicional.

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>


### **Stack tecnológico**

El stack tecnológico seleccionado para el proyecto se basa en servicios de AWS, lo que nos permite construir una arquitectura de datos moderna centrada en data lakes. Esta elección ofrece una solución escalable, flexible y segura para el procesamiento de datos, utilizando servicios sin servidor que son administrados por AWS.

Al optar por servicios sin servidor, obtenemos varios beneficios importantes. Por ejemplo, la escalabilidad es automática, lo que significa que los recursos se ajustan dinámicamente según la demanda y el volumen de los datos, eliminando la necesidad de gestionar servidores o infraestructura. Esto no solo simplifica el proceso, sino que también nos ayuda a optimizar los costos, ya que solo pagamos por los recursos que realmente utilizamos.

Además, la adopción de servicios sin servidor promueve la agilidad en el desarrollo y la implementación de soluciones de datos. Al eliminar la preocupación por el mantenimiento y la operación de sistemas, podemos centrarnos en la creación de soluciones de manera rápida y eficiente.

En cuanto a la seguridad, los servicios de AWS incluyen características integradas de seguridad, como cifrado, autenticación, autorización y monitoreo. Esto garantiza la protección y la privacidad de los datos, proporcionando un entorno seguro para el procesamiento y almacenamiento de información sensible. En resumen, al elegir un enfoque sin servidor y basado en AWS, estamos aprovechando una infraestructura moderna y robusta que nos permite avanzar con confianza en nuestro proyecto de datos.


<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Stack%20_Tecnol%C3%B3gico.png"></p>

El anterior Stack tecnológico se puede describir de la siguiente manera:

*Fuente de Datos:* Identificación de la data y tipos de archivos para trabajar, además exploración de data adicional. Esto con el fin de validar la calidad de los datos.

 *Procesamiento:* Extracción, transformación y análisis exploratorio de los datos “ETL” “EDA”, haciendo uso de las diferentes librerías de Python y SQL Server.

*Almacenamiento:* Se almacenan los datos procesados en el Data Warehouse, donde se utilizaron las herramientas de la nube AWS como: S3, Amazon Redshift y AWS Glue.

*Visualización:* Para la visualización de los datos y KPI´s hacemos uso de Power BI ya que nos permite crear Dash Board interactivos y en real time, Tambien realizamos el despliegue en Streamlit del modelo del machine learning.

### **Modelo ER detallado**

<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Modelo_ER_Detallado.png"></p>


### **Pipeline AWS**

<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Pipeline%20AWS.png"></p>

El anterior Pipeline de AWS empleado se puede describir de la siguiente manera:

*Ingesta:* En esta etapa, los datos externos de Yelp y Google Maps se ingieren desde la fuente mediante AWS DataSync, que los carga en el bucket de Amazon S3 destinado a los datos sin procesar. 

*Almacenamiento:* En esta etapa, se almacenan los datos en un data lake, utilizando Amazon S3 como capa de almacenamiento. Los datos se organizan en diferentes buckets, según su formato y su etapa en el pipeline. Los datos almacenados en Amazon S3 se registran en el AWS Glue Data Catalog, que los cataloga y los hace disponibles para su análisis y también se utiliza Amazon Redshift para el datalake.

*Procesamiento:* En esta etapa, se realizan las transformaciones ETL de los datos, utilizando AWS Glue como servicio de orquestación y ejecución. Los datos transformados se almacenan en el bucket cleaned-data de Amazon S3. Para el almacenamiento de los metadatos de los datos, se utiliza AWS Glue Data Catalog, que es un servicio gestionado que actúa como un repositorio centralizado y unificado para todos los esquemas de datos.

*Consumo:* En esta etapa, se consumen los datos transformados, y se permite desplegar el modelo de machine learning en tiempo real, como Streamlit, que se conectan con los datos para ofrecer funcionalidades como el sistema de recomendación.

*Visualización:* Para la visualización de los datos, se realiza una conexión con Power BI para la visualización de los datos y así compartir los datos ya procesados y poderlos utilizar en el dashboards interactivos.

### **Sistema de Recomendacion desplegado en Streamlit**  

A continuación se muestra un screenshot del despliegue de nuestro sistema de recomendación en la plataforma de Streamlit, en donde se observa las recomendaciones de restaurantes para el usuario, basadas en la categoria "Tacos".

<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Sistema%20de%20Recomendacion%20en%20Streamlit.png"></p>


### **MVP Dashboard Power BI Final**  

Nuestro dashboard ofrece una visión completa y detallada del universo de reseñas de pizzerías, incluyendo información sobre el alto volumen de pizzerías, el porcentaje de reseñas positivas por estado y un análisis específico del sentimiento para Sgambati's New York Pizza.

En esta herramienta, encontrarás datos esenciales como la puntuación promedio, la cantidad de usuarios, y los KPIs relevantes, así como también análisis detallados del sentimiento de las reseñas tanto a nivel general como específico para establecimientos individuales como Sgambati's New York Pizza.

Además, hemos incluido un análisis específico del sentimiento para Sgambati's New York Pizza, donde podrás ver el porcentaje de reseñas positivas, negativas y neutrales, así como ejemplos de reseñas específicas que han contribuido a este análisis.

En resumen, nuestro dashboard ofrece una herramienta integral para analizar y comprender las reseñas de las pizzerías, proporcionando insights valiosos para impulsar nuestro negocio hacia el éxito continuo. ¡Explora y descubre las claves para una experiencia del cliente excepcional!"


<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Dash_01.jpg"></p>

<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Dash_02.jpg"></p>

<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Dash_03.jpg"></p>

<p align="center"><img src="https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/Dash_04.jpg"></p>

## **Cronograma**

El proyecto se desarrollará en un período de 6 semanas, con tres sprint que son los siguientes:
- Sprnt 1: Puesta en macha del proyecto. 2 Semanas
- Sprint 2: Data Engineering. 2 Semanas
- Sprint 3: Data Analitics y Machine learning. 2 Semanas.
[Cronograma](https://github.com/williamCastro32/PF_Google_yelp_Map/blob/main/docs/Imagenes/diagrama_Gantt.jpg)
<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

## **Fuentes de datos**

+   [Diccionario de Datos](https://docs.google.com/document/d/1ASLMGAgrviicATaP1UJlflpmBCXtuSTHQGWdQMN6_2I/edit)

Fuentes de datos obligatorias:
+   [Dataset de Google Maps](https://drive.google.com/drive/folders/1Wf7YkxA0aHI3GpoHc9Nh8_scf5BbD4DA?usp=share_link)
+   [Dataset de Yelp!](https://drive.google.com/drive/folders/1TI-SsMnZsNP6t930olEEWbBQdo_yuIZF?usp=sharing)
<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

## **Sobre nosotros**

**AnalyticaPro Solutions**, Somos una consultora especializada en análisis de datos dedicada a apoyar a las empresas en la mejora de sus decisiones mediante el uso inteligente de la información. Ofrecemos una amplia gama de servicios que incluyen investigación, visualización de datos, modelado y aplicaciones de machine learning. Utilizamos las herramientas más avanzadas y las metodologías más efectivas del mercado para proporcionar a nuestros clientes insights valiosos y estratégicos basados en datos sólidos.

| Perfil                                                | Nombre              | Rol              | LinkedIn                                             | GitHub           |
|-------------------------------------------------------|---------------------|------------------|------------------------------------------------------|------------------|
|  <img src="https://media.licdn.com/dms/image/D4D35AQGFNDwNwX5Y2Q/profile-framedphoto-shrink_400_400/0/1708208075642?e=1710518400&v=beta&t=M1hBZhl9tPXBx9jbnPypMIzGBf1wzsskLCccm2zymM8" width=48 style="border-radius:50%"> | Gabriela Barrionuevo | Data Engineer    | [![LinkedIn][linkedin-logo]][linkedin-gabi2]           | [![GitHub][github-logo]][github-gabi2] |
| <img src="https://media.licdn.com/dms/image/D4E03AQExsVAIEgf8-Q/profile-displayphoto-shrink_400_400/0/1700955162103?e=1712188800&v=beta&t=xEVDco-Fs3nxeW4AOqH9OtXrN9mJQyIw5mlq2nWKF7Y" width=48 style="border-radius:50%"> | Jessica Leandra     | Data Analyst     | [![LinkedIn][linkedin-logo]][linkedin-jess]            | [![GitHub][github-logo]][github-jess] |
| <img src="https://media.licdn.com/dms/image/D4E03AQHHB624K_lnbQ/profile-displayphoto-shrink_100_100/0/1707653483491?e=1715212800&v=beta&t=Jw_kURbVmfam3Eo61LC4cdU3Gyzx_5iMTTN6i4KHIi4" width=48 style="border-radius:50%"> | Andrés Rodríguez   | Data Analyst     | [![LinkedIn][linkedin-logo]][linkedin-andre]           | [![GitHub][github-logo]][github-andre] |
| <img src="https://media.licdn.com/dms/image/D5603AQFWAsBFqA2xqw/profile-displayphoto-shrink_100_100/0/1703184318508?e=1715212800&v=beta&t=5b96sOhd5YBi_thENUt2VBRpCyVlD23eBIoezO5SpFc" width=48 style="border-radius:50%"> | William Castro      | Data Science     | [![LinkedIn][linkedin-logo]][linkedin-will]            | [![GitHub][github-logo]][github-will] |


<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

## **Disclaimer**  

Desde AnalyticaPro Solutions, queremos dejar claro que los proyectos propuestos y realizados por nuestro equipo tienen un carácter exclusivamente pedagógico. Este proyecto hace parte del proyecto final del Bootcamp de Henry el cual aclara y remarcar que los fines de los proyectos propuestos son exclusivamente pedagógicos, con el objetivo de realizar proyectos que simulen un entorno laboral, en el cual se trabajen diversas temáticas ajustadas a la realidad. No reflejan necesariamente la filosofía y valores de la organización. Además, Henry no alienta ni tampoco recomienda a los alumnos y/o cualquier persona leyendo los repositorios (y entregas de proyectos) que tomen acciones en base a los datos que pudieran o no haber recabado. Toda la información expuesta y resultados obtenidos en los proyectos, nunca deben ser tomados en cuenta para la toma real de decisiones (especialmente en la temática de finanzas, salud, política, etc.).

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>






[linkedin-logo]: https://www.paredro.com/wp-content/uploads/2019/01/LogoDelDi%CC%81a-LinkedIn-un-emblema-que-esta%CC%81-22dentro22-1110x366.jpg
[linkedin-jess]: http://www.linkedin.com/in/jessica-leandra-v-45a89623/
[linkedin-will]: http://www.linkedin.com/in/william-c-9b1974225/
[linkedin-andre]: http://www.linkedin.com/in/andres-rodriguez-9737ba138/
[linkedin-gabi1]: http://www.linkedin.com/in/gabriela-lezcano-ds/
[linkedin-gabi2]: https://www.linkedin.com/in/gabriela-soledad-barrionuevo-a57449249/
[github-logo]: https://cdn1.vogel.de/unsafe/800x0/smart/images.vogel.de/vogelonline/bdb/1286800/1286845/original.jpg
[github-jess]: https://github.com/Jekavelepe
[github-will]: https://github.com/williamCastro32/
[github-andre]: https://github.com/AndresRodriguez92/
[github-gabi1]: https://github.com/GabiL44
[github-gabi2]: https://github.com/Gabbriela07/ 
