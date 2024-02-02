<a name="readme-top"></a>

# <h1 align="center">**`YELP & GOOGLE MAPS - REVIEWS AND RECOMMENDATIONS`**</h1>

<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/2560px-Yelp_Logo.svg.png"  height="200">
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Google_Maps_Logo_2020.svg/512px-Google_Maps_Logo_2020.svg.png"  height="200">



## **Tabla de Contenido**

- [Introducción](#introducción)
- [Contexto](#contexto)
- [Alcance](#alcance)
    - [Objetivos del Proyecto](#objetivos-del-proyecto)
    - [Metodología y Proceso](#metodología-y-proceso)
    - [KPIs](#kpis)
    - [Entregables](#entregables)
    - [Restricciones y Limitaciones](#restricciones-y-limitaciones)
- [Entregables](#entregables)
- [Stack tecnológico](#stack-tecnológico)
- [Fuentes de datos](#fuentes-de-datos)
- [Disclaimer](#disclaimer)

    
## **Intrucción**

El presente proyecto tiene como objetivo llevar a cabo un análisis exhaustivo de las opiniones de usuarios en plataformas de reseñas como Yelp y Google Maps, centrándose en el mercado estadounidense. Este análisis será realizado en el contexto de un cliente que forma parte de un conglomerado de empresas de restaurantes y turismo, con el propósito de proporcionar recomendaciones basadas en datos que impulsen la toma de decisiones estratégicas. La recopilación, depuración y análisis de datos provenientes de estas plataformas permitirá comprender la percepción de los usuarios sobre los negocios relacionados con el turismo y la hospitalidad, así como identificar tendencias y patrones que puedan ser de utilidad para el cliente. Además, se utilizarán técnicas de procesamiento de lenguaje natural (PNL) para analizar el sentimiento de las reseñas de los usuarios, lo que proporcionará una visión más profunda de la satisfacción y las expectativas de los clientes. El proyecto también incluirá el desarrollo de modelos de aprendizaje automático para clasificación y recomendación, así como la propuesta de estrategias de marketing y sistemas de recomendación personalizados. Los resultados obtenidos serán presentados en un informe detallado que servirá como guía para la toma de decisiones del cliente y la implementación de mejoras en sus operaciones. Para mas informacion 


<details>
  <summary><h2>Contexto</h2></summary>

"La opinión de los usuarios es un dato muy valioso, que crece día a día gracias a plataformas de reseñas. Su análisis puede ser determinante para la planificación de estratenias. Yelp es una plataforma de reseñas de todo tipo de negocios, restaurantes, hoteles, servicios entre otros. Los usuarios utilizan el servicio y luego suben su reseña según la experiencia que han recibido. Esta información es muy valiosa para las empresas, ya que les sirve para enterarse de la imagen que tienen los usuarios de los distintos locales de la empresa, siendo útil para medir el desempeño, utilidad del local, además de saber en qué aspectos hay que mejorar el servicio. Además, Google posee una plataforma de reseñas de todo tipo de negocios, restaurantes, hoteles, servicios, entre otros integrada en su servicio de localización y mapas, Google Maps. Los usuarios utilizan el servicio y luego suben su reseña según la experiencia vivida. Muchos usuarios leen las reseñas de los lugares a los que planean ir para tomar decisiones sobre dónde comprar, comer, dormir, reunirse, etc. Esta información es muy valiosa para las empresas, ya que les sirve para enterarse de la imagen que tienen los usuarios de los distintos locales de la empresa, siendo muy útil para medir el desempeño, utilidad del local, además de identificar los aspectos del servicio a mejorar.""

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

</details>

<details>
  <summary><h2>Alcance</h2></summary>

El presente documento establece el alcance del proyecto de análisis de opiniones de usuarios en plataformas de reseñas como Yelp y Google Maps para el mercado estadounidense. El proyecto está dirigido por AnalyticaPro Solutions, con el objetivo de proporcionar análisis detallados y recomendaciones basadas en datos para su conglomerado de empresas de restaurantes y turismo.

### Metodología de trabajo

Para el completo desarrollo del trabajo contamos con tres Sprints cada uno con sus entregables y una duración de dos semanas cada uno. Para el trabajo colaborativo hacemos uso de Trello el cual nos permite establecer una planificación y gestión de tareas grupales facilitando la asignación de tiempos de entrega de cada una de las tareas.

#### Metodología Ágil

Como metodología ágil usamos la metodología KANBAN ya que su objetivo es visualizar de manera general cada etapa de una tarea desde que es planeada hasta su realización.

La metodología Kanban es fácil de usar, su sencillez permite mantener actualizado al equipo de trabajo y este puede asumirla sin ningún tipo de complicación. Esto debido a que es un método visual, el cual permite una primera vista para tener información inmediata del estado de los proyectos. De tal forma, se podrá poner en marcha una nueva tarea una vez culminada la anterior y así garantizar un ritmo sostenible en el equipo de trabajo.


### **Objetivos del Proyecto**

- Recopilar, depurar y disponibilizar información de diversas fuentes, incluyendo Yelp y Google Maps, para su análisis.
-Realizar análisis de sentimientos y tendencias en las opiniones de los usuarios.
-Identificar posibles factores que influyan en las opiniones de los usuarios.
-Entrenar y desplegar modelos de aprendizaje automático para clasificación y recomendación.
-Mejorar estrategias de marketing a través de campañas microsegmentadas.
-Desarrollar sistemas de recomendación para usuarios basados en sus experiencias previas.
-Cruzar datos adicionales como cotizaciones en bolsa y tendencias en redes sociales.

### **Metodología y Proceso**
El proyecto seguirá una metodología de trabajo en equipo que incluye las siguientes etapas:

-Recopilación y depuración de datos de Yelp y Google Maps.
- Análisis exploratorio de datos para identificar patrones y tendencias.
- Implementación de técnicas de procesamiento de lenguaje natural (PNL) para análisis de sentimientos.
- Entrenamiento de modelos de aprendizaje automático para clasificación y recomendación.
- Integración de datos adicionales y análisis de su impacto en las opiniones de los usuarios.
- Desarrollo de estrategias de marketing y sistemas de recomendación basados en los hallazgos del análisis.

### **KPIs**

- Tasa de Crecimiento de Reseñas Positivas: Este KPI mide el porcentaje de aumento en el número de reseñas positivas en comparación con un período anterior. La meta objetiva podría ser un aumento del 15% en la tasa de crecimiento de reseñas positivas en un trimestre específico.

- Índice de Satisfacción del Cliente (ISC): El ISC es una medida que combina diferentes aspectos de la experiencia del cliente, como la calidad del servicio, la limpieza, el ambiente, etc., en una sola métrica. La meta objetiva podría ser alcanzar un ISC de 8 sobre 10 en un plazo determinado.

- Tasa de Retención de Clientes: Este KPI mide el porcentaje de clientes que regresan a un negocio después de su primera visita. La meta objetiva podría ser aumentar la tasa de retención de clientes en un 20% en un año.

- Porcentaje de Reseñas Respondidas: Este KPI mide el porcentaje de reseñas a las que se ha respondido por parte del negocio. La meta objetiva podría ser responder al menos el 80% de las reseñas dentro de las 24 horas posteriores a su publicación.


### **Entregables**

- Informe detallado con los resultados del análisis de datos.
- Modelos de aprendizaje automático entrenados y desplegados.
- Estrategias de marketing y sistemas de recomendación propuestos.
- Documentación técnica y guías de uso para los modelos y sistemas desarrollados.

### **Restricciones y Limitaciones**

El proyecto se limita al análisis de datos disponibles en Yelp y Google Maps para el mercado estadounidense.
La disponibilidad y calidad de los datos pueden afectar los resultados del análisis.
El alcance del proyecto no incluye la implementación de sistemas en producción, sino la entrega de modelos y recomendaciones listos para su implementación.

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

</details>

### **Stack tecnológico**

<p align="right">(<a href="#readme-top">ir arriba</a>)</p>

## **Cronograma**
El proyecto se desarrollará en un período de 6 semanas, con tres sprint que son los siguientes:
- Sprnt 1: Puesta en macha del proyecto. 2 Semanas
- Sprint 2: Data Engineering. 2 Semanas
- Sprint 3: Data Analitics y Machine learning. 2 Semanas.
[Cronograma](https://github.com/)
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
| <img src="https://media.licdn.com/dms/image/D4D35AQFIFcQYBmL-3Q/profile-framedphoto-shrink_400_400/0/1690323274890?e=1707346800&v=beta&t=5QwYnNd0hqbqjbP_CndtJQR4GdcXJptPt0WmCwiGWzI" width=48 style="border-radius:50%"> | Gabriela Barrionuevo | Data Engineer    | [![LinkedIn][linkedin-logo]][linkedin-gabi2]           | [![GitHub][github-logo]][github-gabi2] |
| <img src="https://media.licdn.com/dms/image/D5635AQEJ-wwu3Y9uvA/profile-framedphoto-shrink_400_400/0/1699978821158?e=1707346800&v=beta&t=T4OZvOZu-hK-qkjQA3gxop1MVNl0VIsn6_UU0_ptaZQ" width=48 style="border-radius:50%"> | Gabriela Lezcano      | Data Engineer    | [![LinkedIn][linkedin-logo]][linkedin-gabi1]         | [![GitHub][github-logo]][github-gabi1] |
| <img src="https://media.licdn.com/dms/image/D4E03AQExsVAIEgf8-Q/profile-displayphoto-shrink_400_400/0/1700955162103?e=1712188800&v=beta&t=xEVDco-Fs3nxeW4AOqH9OtXrN9mJQyIw5mlq2nWKF7Y" width=48 style="border-radius:50%"> | Jessica Leandra     | Data Analyst     | [![LinkedIn][linkedin-logo]][linkedin-jess]            | [![GitHub][github-logo]][github-jess] |
| <img src="https://media.licdn.com/dms/image/D4E03AQFz46wXRSpi3w/profile-displayphoto-shrink_400_400/0/1686455794862?e=1712188800&v=beta&t=PS3aqKY1AXOH2yKFxEecT-9dJ9nEI8LKjE_aaCcO2YE" width=48 style="border-radius:50%"> | Andrés Rodríguez   | Data Analyst     | [![LinkedIn][linkedin-logo]][linkedin-andre]           | [![GitHub][github-logo]][github-andre] |
| <img src="https://media.licdn.com/dms/image/D4D35AQGcTl7mP8lhzA/profile-framedphoto-shrink_400_400/0/1706284538915?e=1707346800&v=beta&t=mOiFrdxQZ1H8C3UAXpETj3Gjo1fxLYwAZZv6imk3_yM" width=48 style="border-radius:50%"> | William Castro      | Data Science     | [![LinkedIn][linkedin-logo]][linkedin-will]            | [![GitHub][github-logo]][github-will] |


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
