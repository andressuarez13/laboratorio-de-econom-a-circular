import dearpygui.dearpygui as dpg
import dpg_styleqs.dpg_styleqs as dpg_sqs

def temas():
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (250, 250, 250))    # Fondo gris claro
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0))             # Texto negro

            # Estilos generales
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

            # Colores de la tabla
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (240, 240, 240, 255))   # Fondo gris claro
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))            # Texto negro
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)

            #  Colores de tabla
            dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (200, 200, 200, 255))  # Encabezado gris
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBg, (255, 255, 255, 255))     # Filas blancas
            dpg.add_theme_color(dpg.mvThemeCol_TableRowBgAlt, (245, 245, 245, 255))  # Filas alternas gris claro
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, (0, 0, 0, 100))    # Bordes externos
            dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, (0, 0, 0, 50))      # Bordes internos

        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button,(250,250,250))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0, 255))  
            

    with dpg_sqs.ThemeWidgets("mvChildWindow") as tem:
            tem.add_background_gradiant(gradiant_type="Lineal_vertical",start_color=(0,255,47),end_color=(4,61,41))
            dpg_sqs.bind_widget_theme(tag="visitas",tag_theme=tem.tag)
