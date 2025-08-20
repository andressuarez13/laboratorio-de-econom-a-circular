import pandas as pd
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo
import json 
from dearpygui.dearpygui import *
import dpg_styleqs.dpg_styleqs as dpg_sqs
import temas

# Leer el archivo diccionario en .json
with open("dataRegister.json", "r") as archive:
    try:
        datos = json.load(archive)
    except:
        datos = {}

"""for d in datos:
    print(d)
    for id in datos[d]:
        print(id)
        with dpg.table_row(parent="tab"):
            dpg.add_text("usuario")
            dpg.add_text("id")
        for parametro in datos[d][id]:
            print(parametro)
            x = datos[d][id][parametro]
            print([x])"""

def usuarios_json():
    import json
    import dearpygui.dearpygui as dpg

def usuarios_json():
    try:
        with open("dataRegister.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
        datos = {}

    mes = dpg.get_value("input_meses")
    if mes not in datos:
        datos[mes] = {}

    # Generar un nuevo id automático
    nuevo_id = str(len(datos[mes]) + 1)

    # Crear el nuevo registro
    nuevo_usuario = {
        "Usuario": dpg.get_value("input_genero"),
        "Descripcion": dpg.get_value("input_descripcion"),
        "Instructor Responsable": dpg.get_value("input_instructor"),
        "Fecha": dpg.get_value("input_fecha"),
        "Area": dpg.get_value("input_area"),
        "SubArea": dpg.get_value("input_subarea"),
    }

    # Guardar en el diccionario
    datos[mes][nuevo_id] = nuevo_usuario

    # Guardar en el archivo JSON
    with open("dataRegister.json", "w") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

    print(f"Nuevo registro agregado en {mes} con id {nuevo_id}")

    # Agregar a la tabla en la interfaz
    with dpg.table_row(parent="tab"):
        dpg.add_text(nuevo_id)  # primera columna con el id
        for valor in nuevo_usuario.values():
            dpg.add_text(valor)
# Interfaz
dpg.create_context()
dpg.create_viewport(title="VISITAS LAB")
dpg.set_viewport_resizable(False)

with dpg.window(label="VISUALIZADOR DE VISITAS",tag="visitas"): 
    dpg.add_text("VISUALIZADOR DE VISITAS", bullet=False)
    with dpg.child_window(auto_resize_y=True,tag="months"):
        # Contenedor boton "meses"
        dpg.add_button(label="Enero")
        dpg.add_button(label="Febrero")
        dpg.add_button(label="Marzo")
        dpg.add_button(label="Abril")
        dpg.add_button(label="Mayo")
        dpg.add_button(label="Junio")
        dpg.add_button(label="Julio")
        dpg.add_button(label="Agosto")
        dpg.add_button(label="Septiembre")
        dpg.add_button(label="Octubre")
        dpg.add_button(label="Noviembre")
        dpg.add_button(label="Diciembre")

    with dpg.child_window(auto_resize_x=True,auto_resize_y=True,height=200):
        with dpg.table(tag="tab"):
            dpg.add_table_column(label="Usuario")
            dpg.add_table_column(label="Descripcion")
            dpg.add_table_column(label="Instructor Responsable")
            dpg.add_table_column(label="Fecha")
            dpg.add_table_column(label="Area")
            dpg.add_table_column(label="SubArea")
            def cargar_datos():
                pass
    #Funcion limpia las filas anteriores
    def mostrar_datos():
    #guardar datos en el JSON
        dpg.delete_item("tab", children_only=True)

        columnas = ["Usuario", "Descripcion", "Instructor Responsable", "Fecha", "Area", "SubArea"]
        for col in columnas:
            dpg.add_table_column(label=col, parent="tab")
    # Cargar datos desde el JSON
    for mes, registros in datos.items():
        for id_registro, fila in registros.items():
            if isinstance(fila, dict):
                with dpg.table_row(parent="tab"):
                    for valor in fila.values():
                        dpg.add_text(str(valor))
    #creamos otra columna
    for mes, registros in datos.items():
        for mes, registros in datos.items():
            for id_registro, fila in registros.items():
                with dpg.table_row(parent="tab"):
                    dpg.add_text(fila.get("Usuario", ""))
                    dpg.add_text(fila.get("Descripcion", ""))
                    dpg.add_text(fila.get("Instructor Responsable", ""))
                    dpg.add_text(fila.get("Fecha", ""))
                    dpg.add_text(fila.get("Area", ""))
                    dpg.add_text(fila.get("SubArea", ""))

    try:
        with open("dataRegister.json", "r") as archivo:
            datos = json.load(archivo)
    except FileNotFoundError:
            datos = {}
    with dpg.child_window(auto_resize_x=True,auto_resize_y=True):
        dpg.add_combo(items=["enero","febrero","marzo","abril","mayo","junio","julio","septiembre","octubre","noviembre","diciembre"], default_value="enero",tag="input_meses")
        dpg.add_combo(items=["Hombre","Mujer"],default_value="Hombre",tag="input_genero")
        dpg.add_input_text(hint="Descripcion",tag="input_descripcion")
        dpg.add_input_text(hint="Instructor Responsable",tag="input_instructor")
        dpg.add_input_text(hint="Fecha",tag="input_fecha")
        dpg.add_input_text(hint="Area",tag="input_area")
        dpg.add_input_text(hint="Subarea",tag="input_subarea")
        dpg.add_button(label="cargar datos",callback=usuarios_json)
    
    #Si el mes no existe se crea
    def usuarios_json():
        if mes not in datos:
            datos[mes]={}
    #generamos id nuevo 
    nuevo_id =str(len(datos[mes]))
#demo.show_demo()
temas.temas()
with dpg_sqs.WindowLayout("visitas"):
    with dpg_sqs.FlexLayoutBuilder(tag="months",horizontal=True,gap=10,padding=10,alling_widgets="alling_start"):
        pass
    with dpg_sqs.FlexLayoutBuilder(tag="visitas",gap=10,padding=10,alling_widgets="alling_center",height="default",width="default"):
        pass

dpg.set_primary_window("visitas", True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.maximize_viewport()
dpg.start_dearpygui()
dpg.destroy_context()




