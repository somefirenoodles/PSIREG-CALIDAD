# Definición del proceso de desarrollo de PSIREG

## Propósito del proceso

El proceso de desarrollo de PSIREG se define con el objetivo de organizar las actividades necesarias para documentar, revisar y evaluar la calidad del sistema dentro del trabajo final. Debido a que PSIREG maneja información sensible relacionada con expedientes psicológicos, citas, documentos y actividades institucionales, el proceso debe priorizar trazabilidad, control de acceso, evidencia verificable y consistencia documental.

## Enfoque adoptado

Para ordenar el proceso se utiliza VSEST-Lite, un framework ligero creado a partir de las necesidades de PSIREG y del trabajo colaborativo del grupo. El enfoque combina prácticas de ISO/IEC 29110 para estructurar actividades y artefactos, junto con Kanban para visualizar el estado de avance, responsables y tareas pendientes.

## Actividades del proceso

| ID | Actividad | Objetivo | Tareas principales | Artefactos de evidencia |
|---|---|---|---|---|
| ACT-01 | Identificación del proyecto | Definir el proyecto base y su alcance de calidad | Describir PSIREG, problema, justificación y alcance inicial | `docs/01_plan_proyecto/identificacion_psireg.md` |
| ACT-02 | Revisión documental del proyecto | Revisar la documentación existente de PSIREG | Revisar arquitectura, casos de uso, matriz de trazabilidad, prototipos y vistas | Documento de arquitectura PSIREG, matriz de trazabilidad, prototipos |
| ACT-03 | Definición del proceso | Establecer actividades, tareas y evidencias del proceso | Organizar el trabajo bajo VSEST-Lite, definir fases y artefactos | `docs/00_metodologia/proceso_desarrollo_psireg.md` |
| ACT-04 | Diagnóstico del proceso realizado | Identificar debilidades y oportunidades de mejora | Revisar trazabilidad, evidencia, control de tareas y consistencia documental | Matriz de diagnóstico |
| ACT-05 | Propuesta de mejoras | Definir acciones correctivas basadas en el modelo utilizado | Relacionar problemas con mejoras propuestas | Matriz de mejoras |
| ACT-06 | Plan de garantía de calidad | Establecer objetivos, métricas, estándares, revisiones y auditoría | Definir plan SQA, pruebas y controles | Plan de garantía de calidad |
| ACT-07 | Evaluación del producto | Evaluar atributos de calidad del producto PSIREG | Aplicar instrumento de evaluación con escala 0, 1 y 2 | Instrumento de evaluación del producto |

## Fases de trabajo

| Fase | Descripción | Evidencia mínima |
|---|---|---|
| Identificación | Se reconoce la tarea o artefacto necesario | Issue creado en VSEST-Lite |
| Elaboración | Se construye o redacta el artefacto | Archivo Markdown, tabla, evidencia o documento |
| Revisión | Se verifica si el artefacto cumple su propósito | Comentario, checklist o validación |
| Corrección | Se ajustan errores u observaciones | Cambio en archivo o issue |
| Validación | Se confirma que la evidencia es suficiente | Validate en verde y matriz actualizada |
| Cierre | Se considera el artefacto terminado | Estado cerrado o aprobado |

## Artefactos principales del proceso

| Artefacto | Función |
|---|---|
| Issue estructurado | Registra tarea, fase, estado, evidencia y próxima acción |
| Archivo Markdown | Contiene la evidencia documental del artefacto |
| Matriz de trazabilidad | Relaciona tareas, módulos, fases, evidencias y resultados |
| Tablero Kanban | Permite visualizar el estado de las tareas |
| Dashboard VSEST-Lite | Resume el avance del framework |
| Instrumento de evaluación | Evalúa la calidad del producto PSIREG |

## Relación con el trabajo final

Este proceso permite responder a la sección de definición del proceso de desarrollo solicitada en el trabajo final. Además, prepara la base para las siguientes fases: diagnóstico de procesos realizados, propuesta de mejoras, plan de garantía de calidad e instrumento de evaluación del producto.
