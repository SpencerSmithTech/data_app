import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, font
from tkinter import ttk

import pandas as pd
import numpy as np

from tkinter import font

# LOCAL FILES
import dataframe_management
import dataframe_viewer
import column_editor
import data_visualization

import data_library
import styles
import utils
from styles import color_dict


# Create the main window
main_window = tk.Tk()


# Make window full screen
main_window.wm_state('zoomed')


# Custom window sizes
# screen_width = main_window.winfo_screenwidth() // 3
# screen_height = main_window.winfo_screenheight()

# # Make window take left third of screen
# main_window.geometry(f"{screen_width}x{screen_height}+0+0")

# Make window take the center third of screen
# main_window.geometry(f"{screen_width}x{screen_height}+{screen_width}+0")




style = ttk.Style()
style.theme_use("clam")


# Create frames
banner_frame = tk.Frame(main_window)
banner_frame.pack(side="top", fill=tk.X)

button_frame = tk.Frame(banner_frame)
button_frame.pack(fill=tk.X)  # Change to fill=tk.X to expand horizontally

sub_button_frame = tk.Frame(banner_frame)
sub_button_frame.pack(fill=tk.X)  # Change to fill=tk.X to expand horizontally
sub_button_frame.pack_propagate(True)

content_frame = tk.Frame(main_window)
content_frame.pack(side="top", fill=tk.BOTH, expand=True)


dataframe_management_content_frame = tk.Frame(content_frame, bg=color_dict["background_frame_bg"])
dataframe_viewer_content_frame = tk.Frame(content_frame, bg=color_dict["background_frame_bg"])
column_editor_content_frame = tk.Frame(content_frame, bg=color_dict["background_frame_bg"])
data_visualization_content_frame = tk.Frame(content_frame, bg=color_dict["background_frame_bg"])

# Add Buttons

# Banner Frame
style.configure("dataframe_management_button.TButton", borderwidth=0, padding=0, font=styles.main_tabs_font)
dataframe_management_button = ttk.Button(button_frame, text="Dataframe Management", style="dataframe_management_button.TButton")
dataframe_management_button.pack(side="left", fill="x", expand=True)
dataframe_management_button.config(command=lambda: dataframe_management.setup_dataframe_management_tab(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame))


style.configure("dataframe_viewer_button.TButton", borderwidth=0, padding=0, font=styles.main_tabs_font)
dataframe_viewer_button = ttk.Button(button_frame, text="Dataframe Viewer", style="dataframe_viewer_button.TButton")
dataframe_viewer_button.pack(side="left", fill="x", expand=True)
dataframe_viewer_button.config(command=lambda: dataframe_viewer.setup_dataframe_viewer_tab(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame, reset_tables=False))

style.configure("column_editor_button.TButton", borderwidth=0, padding=0, font=styles.main_tabs_font)
column_editor_button = ttk.Button(button_frame, text="Column Editor", style="column_editor_button.TButton")
column_editor_button.pack(side="left", fill="x", expand=True)
column_editor_button.config(command=lambda: column_editor.setup_edit_tab(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame))

style.configure("data_visualization_button.TButton", borderwidth=0, padding=0, font=styles.main_tabs_font)
data_visualization_button = ttk.Button(button_frame, text="Data Visualization", style="data_visualization_button.TButton")
data_visualization_button.pack(side="left", fill="x", expand=True)
data_visualization_button.config(command=lambda: data_visualization.setup_visualize_tab(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame))





for button in ["dataframe_management_button.TButton", "dataframe_viewer_button.TButton", "column_editor_button.TButton", "data_visualization_button.TButton"]:
    style.map(button, background=[("active", "yellow")])


dataframe_management.setup_dataframe_management_tab(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame)


################################################################################################################
################################################################################################################
################################################################################################################

# STYLING

################################################################################################################

style.configure("Separator.Separator", background=color_dict["separator"])

################################################################################################################

# RADIO BUTTONS
style.configure("inactive_radio_button.TButton", 
                    font=styles.large_button_font, 
                    foreground=color_dict["radio_button_inactive_text"],
                    background=color_dict["radio_button_inactive_background"],
                    bordercolor=color_dict["radio_button_inactive_border"],
                    relief="flat")

style.configure("active_radio_button.TButton", 
                    font=styles.large_button_font, 
                    foreground=color_dict["radio_button_active_text"],
                    background=color_dict["radio_button_active_background"],
                    bordercolor=color_dict["radio_button_active_border"],
                    relief="groove")

style.map("inactive_radio_button.TButton",
                foreground=[("pressed", color_dict["radio_button_pressed_text"]), ("active", color_dict["radio_button_pressed_text"])],
                background=[("pressed", color_dict["radio_button_pressed_background"]), ("active", color_dict["radio_button_pressed_background"])],
                bordercolor=[("pressed", color_dict["radio_button_pressed_border"]), ("active", color_dict["radio_button_pressed_border"])])

style.map("active_radio_button.TButton",
                foreground=[("pressed", color_dict["radio_button_hover_text"]), ("active", color_dict["radio_button_hover_text"])],
                background=[("pressed", color_dict["radio_button_hover_background"]), ("active", color_dict["radio_button_hover_background"])],
                bordercolor=[("pressed", color_dict["radio_button_hover_border"]), ("active", color_dict["radio_button_hover_border"])])

################################################################################################################

# COMBOBOXES
style.map("TCombobox",
    fieldbackground=[("readonly", color_dict["active_combobox_background"]), ("disabled", color_dict["inactive_combobox_background"])],
    background=[("readonly", color_dict["active_combobox_background"]), ("disabled", color_dict["inactive_combobox_background"])],
    foreground = [("readonly", color_dict["listbox_fg"]), ("disabled", color_dict["inactive_combobox_text"])],
)

################################################################################################################

# NAV MENU
style.configure('nav_menu_button.TButton', font=styles.nav_menu_button_font, background=color_dict["nav_menu_button_bg"], foreground=color_dict["nav_menu_button_txt"])
style.map("nav_menu_button.TButton",
    background=[("active", color_dict["nav_menu_button_hover_bg"])],
    foreground=[("active", color_dict["nav_menu_button_hover_txt"])]
)

style.configure("nav_menu_label.TLabel",
               foreground=color_dict["nav_banner_txt"],
               background=color_dict["nav_banner_bg"],
               font=styles.nav_menu_label_font)


################################################################################################################

# LARGE BUTTONS
style.configure("large_button.TButton", 
                    font=styles.large_button_font,
                    foreground=color_dict["action_button_text_color"], 
                    background=color_dict["action_button_bg"],
                    borderwidth=1,
                    relief="raised",
                    padding=6)

style.map("large_button.TButton",
            foreground=[("pressed", color_dict["action_button_text_color"]), ("active", color_dict["action_button_text_color"])],
            background=[("pressed", color_dict["action_button_pressed_bg"]), ("active", color_dict["action_button_active_bg"])])

################################################################################################################

# SMALL BUTTONS
style.configure("small_button.TButton", 
                    font=styles.small_button_font,
                    foreground=color_dict["action_button_text_color"],
                    background=color_dict["action_button_bg"],
                    borderwidth=1,
                    relief="raised",
                    padding=6)

style.map("small_button.TButton",
            foreground=[("pressed", color_dict["action_button_text_color"]), ("active", color_dict["action_button_text_color"])],
            background=[("pressed", color_dict["action_button_pressed_bg"]), ("active", color_dict["action_button_active_bg"])]) 

################################################################################################################

# SUB FRAME HEADER LABELS
style.configure("sub_frame_header.TLabel", 
                foreground=color_dict["sub_frame_header"], 
                background=color_dict["sub_frame_bg"], 
                font=styles.sub_frame_header_font,
                )

################################################################################################################

# SUB FRAME SUB-HEADER LABELS
style.configure("sub_frame_sub_header.TLabel", 
                foreground=color_dict["sub_frame_sub_header"], 
                background=color_dict["sub_frame_bg"], 
                font=styles.sub_frame_sub_header_font
                )

################################################################################################################

# SUB FRAME TEXT FONT
style.configure("sub_frame_text.TLabel", 
                foreground=color_dict["sub_frame_sub_header"], 
                background=color_dict["sub_frame_bg"], 
                font=styles.sub_frame_text_font)

################################################################################################################

# TREE TABLES

style.configure("Treeview",
                background=color_dict["treeview_bg"],
                foreground=color_dict["treeview_fg"],
                rowheight=25,
                fieldbackground=color_dict["treeview_field_bg"])
style.map("Treeview",
            background=[('selected', color_dict["treeview_selected_bg"])],
            foreground=[('selected', color_dict["treeview_selected_fg"])])

# Treeview Heading style (for columns)
style.configure("Treeview.Heading",
                background=color_dict["treeview_heading_bg"],
                foreground=color_dict["treeview_heading_fg"],
                font=('Arial Rounded MT Bold', 12, 'bold'))
style.map("Treeview.Heading",
            background=[('active', color_dict["treeview_heading_active_bg"])],
            foreground=[('active', color_dict["treeview_heading_active_fg"])])

# Scrollbar style
style.configure("Vertical.TScrollbar", gripcount=0,
                background=color_dict["scrollbar_bg"], darkcolor=color_dict["scrollbar_bg"], lightcolor=color_dict["scrollbar_bg"],
                troughcolor=color_dict["scrollbar_troughcolor"], bordercolor=color_dict["scrollbar_bg"], arrowcolor=color_dict["scrollbar_arrowcolor"])
style.configure("Horizontal.TScrollbar", gripcount=0,
                background=color_dict["scrollbar_bg"], darkcolor=color_dict["scrollbar_bg"], lightcolor=color_dict["scrollbar_bg"],
                troughcolor=color_dict["scrollbar_troughcolor"], bordercolor=color_dict["scrollbar_bg"], arrowcolor=color_dict["scrollbar_arrowcolor"])


################################################################################################################
################################################################################################################
################################################################################################################

# Start the GUI event loop
main_window.mainloop()
