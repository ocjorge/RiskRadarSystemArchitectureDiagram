puedes darme un readme para github con shields para este codigo: from graphviz import Digraph

# --- Creación del Diagrama ---
dot = Digraph(comment='RiskRadarSystem Architecture')
dot.attr(rankdir='TB', splines='ortho', concentrate='true', label='Figura 1: Diagrama de Flujo Detallado de la Arquitectura del RiskRadarSystem', fontsize='20', fontname="Arial")

# --- Atributos Globales ---
dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue', fontname="Arial")
dot.attr('edge', fontname="Arial", fontsize='10')

# --- Contenedor Principal: Percepción ---
with dot.subgraph(name='cluster_perception') as c:
    c.attr(label='Módulo de Percepción', style='filled', color='lightgrey')
    c.node('pre_process', 'Pre-procesar Frame\n(Redimensionar)')
    c.node('decision_frame', '¿Frame % N == 0?', shape='diamond', fillcolor='lightyellow')
    
    # Rama de Detección Completa
    c.node('full_detection', 'Ejecutar Detección Completa\n(YOLO x2 + MiDaS)', shape='box', width='3')
    c.node('init_trackers', 'Inicializar/Reiniciar Trackers (CSRT)')
    c.node('update_distance_map', 'Calibrar y Actualizar\nMapa de Distancia Métrico')

    # Rama de Seguimiento
    c.node('tracker_update', 'Actualizar Trackers\n(CSRT)')
    
    c.node('perception_output', 'Salida: Lista de Detecciones\n(BBox, Clase, Confianza)', shape='parallelogram', fillcolor='palegreen')
    
# --- Contenedor Principal: Análisis de Riesgo ---
with dot.subgraph(name='cluster_risk_analysis') as c:
    c.attr(label='Módulo de Análisis de Riesgo', style='filled', color='lightgrey')
    c.node('decay_heatmap', 'Decaer Mapa de Calor')
    c.node('loop_detections', 'Para cada Detección:\n1. Leer Distancia\n2. Calcular "Calor"\n3. Añadir a Mapa de Calor', shape='box')
    c.node('calc_total_heat', 'Calcular "Calor Total" en Cono')
    c.node('classify_risk', 'Clasificar Nivel de Riesgo\n(Bajo, Medio, Alto)')
    
# --- Contenedor Principal: Salida y Reportes ---
with dot.subgraph(name='cluster_output') as c:
    c.attr(label='Módulo de Salida y Reportes', style='filled', color='lightgrey')
    c.node('visualize', 'Visualizar Resultados en Frame')
    c.node('resize_final', 'Redimensionar Frame a Res. Original')
    c.node('write_video', 'Escribir Frame en Video de Salida', shape='parallelogram', fillcolor='palegreen')
    c.node('save_data', 'Guardar Datos del Frame')
    c.node('more_frames', '¿Hay más frames?', shape='diamond', fillcolor='lightyellow')
    c.node('generate_reports', 'Generar Reportes Finales\n(JSON, CSV, Gráficos)')
    
# --- Nodos de Inicio/Fin y de Estado ---
dot.node('start', 'Inicio: Cargar Video', shape='ellipse', fillcolor='orange')
dot.node('read_frame', 'Leer Frame n', shape='parallelogram', fillcolor='palegreen')
dot.node('end', 'Fin', shape='ellipse', fillcolor='orange')

# Nodos de estado persistente
dot.node('distance_map_db', 'Estado:\nMapa de Distancia\n(Metros)', shape='cylinder', fillcolor='ivory')
dot.node('heatmap_db', 'Estado:\nMapa de Calor\n(Riesgo)', shape='cylinder', fillcolor='ivory')


# --- Definición de las Conexiones (Flujo) ---
# Entrada
dot.edge('start', 'read_frame')
dot.edge('read_frame', 'pre_process')

# Percepción
dot.edge('pre_process', 'decision_frame')
dot.edge('decision_frame', 'full_detection', label='  Sí (Detección Completa)')
dot.edge('full_detection', 'init_trackers')
dot.edge('init_trackers', 'update_distance_map')
dot.edge('update_distance_map', 'perception_output')
dot.edge('decision_frame', 'tracker_update', label='No (Seguimiento)  ')
dot.edge('tracker_update', 'perception_output')

# Conexión con estado de distancia
dot.edge('update_distance_map', 'distance_map_db', style='dashed', arrowhead='normal', dir='both')

# Análisis de Riesgo
dot.edge('perception_output', 'decay_heatmap')
dot.edge('decay_heatmap', 'loop_detections')

# Conexión con estado de calor
dot.edge('decay_heatmap', 'heatmap_db', style='dashed', arrowhead='normal', dir='none')
dot.edge('loop_detections', 'heatmap_db', style='dashed', arrowhead='normal', dir='none')

dot.edge('loop_detections', 'calc_total_heat')
dot.edge('calc_total_heat', 'classify_risk')

# Salida y Reportes
dot.edge('classify_risk', 'visualize')
dot.edge('visualize', 'resize_final')
dot.edge('resize_final', 'write_video')
dot.edge('write_video', 'save_data')
dot.edge('save_data', 'more_frames')

# Bucle de retorno
dot.edge('more_frames', 'read_frame', label='Sí')

# Flujo final
dot.edge('more_frames', 'generate_reports', label='No')
dot.edge('generate_reports', 'end')

# --- Renderizar el Diagrama ---
# Guarda el diagrama en un archivo (e.g., 'RiskRadarSystem_Architecture.pdf' o .png)
try:
    dot.render('RiskRadarSystem_Architecture', format='png', view=True, cleanup=True)
    print("Diagrama 'RiskRadarSystem_Architecture.png' generado exitosamente.")
except Exception as e:
    print(f"Error al generar el diagrama. Asegúrate de que Graphviz esté instalado y en el PATH de tu sistema.")
    print(f"Error: {e}")
