from math import exp
import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import filedialog, messagebox

import pandas as pd
import os

import numpy as np

# LOCAL FILES
import dataframe_viewer
import data_library
import styles
from styles import color_dict
import utils



def setup_dataframe_management_tab(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame):

    df = data_library.get_dataframe()

    for button_style in ["dataframe_management_button.TButton", "dataframe_viewer_button.TButton", "column_editor_button.TButton", "data_visualization_button.TButton"]:
        style.map(
            button_style,
            background=[("active", color_dict["hover_main_tab_bg"])],
            foreground=[("active", color_dict["hover_main_tab_txt"])]
        )
    
    style.configure("dataframe_management_button.TButton", background=color_dict["active_main_tab_bg"], foreground=color_dict["active_main_tab_txt"])
    style.configure("dataframe_viewer_button.TButton", background=color_dict["inactive_main_tab_bg"], foreground=color_dict["inactive_main_tab_txt"])
    style.configure("column_editor_button.TButton", background=color_dict["inactive_main_tab_bg"], foreground=color_dict["inactive_main_tab_txt"])
    style.configure("data_visualization_button.TButton", background=color_dict["inactive_main_tab_bg"], foreground=color_dict["inactive_main_tab_txt"])

    # CHECK FOR CURRRENT TAB
    tab_dict = data_library.get_tab_dict()
    try:
        current_tab = tab_dict["current_dataframe_management_tab"]
    except:
        current_tab = None

    # SET SUBTAB COLORS
    for tab in ["manage_dataframes", "create_new_dataframe"]:
        button_style = f"{tab}_button.TButton"
        if tab == current_tab:
            style.configure(button_style, background=color_dict["active_subtab_bg"], foreground=color_dict["active_subtab_txt"], borderwidth=0, padding=0, font=styles.sub_tabs_font)
        else:
            style.configure(button_style, background=color_dict["inactive_subtab_bg"], foreground=color_dict["inactive_subtab_txt"], borderwidth=0, padding=0, font=styles.sub_tabs_font)

        style.map(
            button_style,
            background=[("active", color_dict["hover_subtab_bg"])],
            foreground=[("active", color_dict["hover_subtab_txt"])]
        )

    utils.remove_frame_widgets(sub_button_frame)

    # SUBTAB BUTTONS
    manage_dataframes_button = ttk.Button(sub_button_frame, text="Manage Dataframes", style="manage_dataframes_button.TButton")
    manage_dataframes_button.pack(side="left", fill="x", expand=True)  # Set expand=True to fill the horizontal space
    manage_dataframes_button.config(command=lambda: ManageDataframesClass(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame))

    create_new_dataframe_button = ttk.Button(sub_button_frame, text="Create New Dataframe", style="create_new_dataframe_button.TButton")
    create_new_dataframe_button.pack(side="left", fill="x", expand=True)  # Set expand=True to fill the horizontal space
    create_new_dataframe_button.config(command=lambda: CreateDataframeClass(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame))


    dataframe_viewer_content_frame.pack_forget()
    column_editor_content_frame.pack_forget()
    data_visualization_content_frame.pack_forget()
    dataframe_management_content_frame.pack(fill=tk.BOTH, expand=True)

    df = data_library.get_dataframe()

    dataframe_management_content_frame.update()

    if df is None:
        ManageDataframesClass(style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame)
    

    # Force widgets in dataframe_management_content_frame to be displayed





################################################################################################################
################################################################################################################
################################################################################################################

################################################################################################################
################################################################################################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
##############################################                    ##############################################
################################################################################################################
################################################################################################################

################################################################################################################
################################################################################################################
################################################################################################################


################################################################################################################
################################################################################################################
#                                                                                                              #
#                                              MANAGE DATAFRAMES                                               #
#                                                                                                              #
################################################################################################################
################################################################################################################



class ManageDataframesClass():
    def __init__(self, style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame):

        self.df = data_library.get_dataframe()
        self.df_dict = data_library.get_df_dict()
        self.current_dataframe_name = data_library.get_current_df_name()

        self.sub_button_frame = sub_button_frame
        self.dataframe_management_content_frame = dataframe_management_content_frame
        self.dataframe_viewer_content_frame = dataframe_viewer_content_frame
        self.column_editor_content_frame = column_editor_content_frame
        self.data_visualization_content_frame = data_visualization_content_frame
        self.style = style

        self.style.configure("manage_dataframes_button.TButton", background=color_dict["active_subtab_bg"], foreground=color_dict["active_subtab_txt"])
        self.style.configure("create_new_dataframe_button.TButton", background=color_dict["inactive_subtab_bg"], foreground=color_dict["inactive_subtab_txt"])

        data_library.add_tab_to_tab_dict("current_dataframe_management_tab", "manage_dataframes")

        self.selected_dataframe = None

        utils.remove_frame_widgets(self.dataframe_management_content_frame)

        self.manage_dataframes_frame = tk.Frame(self.dataframe_management_content_frame, bg=color_dict["main_content_border"])

        self.create_manage_dataframes_frame()

        self.switch_to_dataframe_managing_frame()



    def switch_to_dataframe_managing_frame(self):
        self.manage_dataframes_frame.pack(fill=tk.BOTH, expand=True, padx=17, pady=17)
        utils.bind_mousewheel_to_frame(self.manage_dataframes_inner_frame, self.manage_dataframes_canvas, True)


################################################################################################################
################################################################################################################
################################################################################################################


    def create_manage_dataframes_frame(self):

        # MAIN CONTENT FRAME
        self.manage_dataframes_inner_frame, self.manage_dataframes_canvas = utils.create_scrollable_frame(self.manage_dataframes_frame)
        
################################################################################################################

        # DATAFRAME MANAGING
        self.manage_dataframes_subframe_border = tk.Frame(self.manage_dataframes_inner_frame, bg=color_dict["sub_frame_border"])
        self.manage_dataframes_subframe_border.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.manage_dataframes_subframe = tk.Frame(self.manage_dataframes_subframe_border, bg=color_dict["sub_frame_bg"])
        self.manage_dataframes_subframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=2, pady=2)

        self.manage_dataframes_menu_label = ttk.Label(self.manage_dataframes_subframe, text="List of Available Data Files", style="sub_frame_header.TLabel")
        self.manage_dataframes_menu_label.pack(side=tk.TOP, pady=10)

        separator = ttk.Separator(self.manage_dataframes_subframe, orient="horizontal", style="Separator.TSeparator")
        separator.pack(side=tk.TOP, fill=tk.X, padx=200)


        # DATAFRAME SELECTION FRAME
        self.dataframe_listbox_frame = tk.Frame(self.manage_dataframes_subframe, bg=color_dict["sub_frame_bg"])
        self.dataframe_listbox_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

        self.dataframe_listbox = tk.Listbox(self.dataframe_listbox_frame, selectmode=tk.SINGLE, font=styles.listbox_font, exportselection=False, bg=color_dict["listbox_bg"],
                     fg=color_dict["listbox_fg"],
                     highlightbackground=color_dict["listbox_highlight_bg"],
                     highlightcolor=color_dict["listbox_highlight_color"],
                     selectbackground=color_dict["listbox_select_bg"],
                     selectforeground=color_dict["listbox_select_fg"],
                     height=20)
        self.dataframe_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=100, pady=10)
        self.dataframe_listbox.bind("<Enter>",lambda e: utils.bind_mousewheel_to_frame(self.manage_dataframes_inner_frame, self.manage_dataframes_canvas, False))
        self.dataframe_listbox.bind("<Leave>",lambda e: utils.bind_mousewheel_to_frame(self.manage_dataframes_inner_frame, self.manage_dataframes_canvas, True))

        for dataframe in self.df_dict.keys():
            self.dataframe_listbox.insert(tk.END, dataframe)
        
        self.dataframe_listbox.bind("<<ListboxSelect>>", self.on_dataframe_listbox_select)


        # BUTTON FRAME
        self.button_frame = tk.Frame(self.manage_dataframes_subframe, bg=color_dict["sub_frame_bg"])
        self.button_frame.pack(side=tk.TOP)

        self.open_file_button = ttk.Button(self.button_frame, text="Open New File", command=self.open_file, style="large_button.TButton")
        self.open_file_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.change_dataframe_button = ttk.Button(self.button_frame, text="Change to Selected Dataframe", command=self.change_dataframe, style="large_button.TButton")
        self.change_dataframe_button.pack(side=tk.RIGHT, padx=10, pady=10)

################################################################################################################

        # NAVIGATION MENU
        self.manage_dataframes_menu_frame = tk.Frame(self.manage_dataframes_frame, bg=color_dict["nav_banner_bg"])
        self.manage_dataframes_menu_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.manage_dataframes_menu_label = ttk.Label(self.manage_dataframes_menu_frame, text="Current Dataframe: None", style="nav_menu_label.TLabel")
        self.manage_dataframes_menu_label.pack(side=tk.LEFT, expand=True)


        if self.current_dataframe_name:
            self.dataframe_listbox.selection_clear(0, tk.END)
            items = list(self.dataframe_listbox.get(0, tk.END))
            index = items.index(self.current_dataframe_name)
            self.dataframe_listbox.selection_set(index)
            self.dataframe_listbox.yview(index)
            self.manage_dataframes_menu_label.config(text=f"Current Dataframe: {self.current_dataframe_name}")
            


    def on_dataframe_listbox_select(self, event):
        if self.dataframe_listbox.curselection():
            self.selected_dataframe = self.dataframe_listbox.get(self.dataframe_listbox.curselection()[0])
        else:
            return


################################################################################################################


    def open_file(self):
        # Upload a file. Only allow .csv and any excel files
        self.file_path = filedialog.askopenfilename(title="Select A File", filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])    

        # self.file_path = r"/Users/spencersmith/Library/CloudStorage/OneDrive-OregonHealth&ScienceUniversity/PROJECTS/YOO/Gunshots/data/gunshots_orth_surgery.csv"

        if not self.file_path:
            return

        try:
            if self.file_path.endswith('.xlsx'):
                df = pd.read_excel(self.file_path)

            elif self.file_path.endswith('.csv'):
                df = pd.read_csv(self.file_path)
            
            else:
                utils.show_message('Error Loading', 'Error Reading File. Must be .csv or .xlsx')
                return

        except:
            utils.show_message('Error Loading', 'Error Reading File. Something went wrong.')
            return

        # Clean up the column names to only include alphanumeric characters and underscores
        df.columns = (df.columns.str.replace(' ', '_').str.replace(r'\W+', '', regex=True).str.replace(r'_{2,}', '_', regex=True))

        # Add leading underscore to column names that start with a number
        df.columns = ['_' + col if col[0].isdigit() else col for col in df.columns]


        # Add the dataframe to the dictionary
        dataframe_name = os.path.basename(self.file_path)

        data_library.set_current_df_name(dataframe_name)
        data_library.add_dataframe_to_dict(dataframe_name, df)
        data_library.set_dataframe(dataframe_name)  # Set the df variable

        self.update_dataframe_listbox()

        # self.dataframe_listbox.selection_clear(0, tk.END)
        items = list(self.dataframe_listbox.get(0, tk.END))
        index = items.index(dataframe_name)
        self.dataframe_listbox.selection_set(index)
        self.dataframe_listbox.yview(index)
        self.manage_dataframes_menu_label.configure(text=f"Current Dataframe: {dataframe_name}")


        dataframe_viewer.setup_dataframe_viewer_tab(self.style, self.sub_button_frame, self.dataframe_management_content_frame, self.dataframe_viewer_content_frame, self.column_editor_content_frame, self.data_visualization_content_frame, reset_tables=True)

        data_library.add_df_update_status_to_dict("column_editor_tab", True)
        data_library.add_df_update_status_to_dict("data_visualization_tab", True)


    def update_dataframe_listbox(self):
        self.dataframe_listbox.delete(0, tk.END)
        for dataframe_name in self.df_dict.keys():
            if dataframe_name not in self.dataframe_listbox.get(0, tk.END):
                self.dataframe_listbox.insert(tk.END, dataframe_name)










    def change_dataframe(self):
        if self.selected_dataframe is None:
            return
            
        # CHECK TO MAKE SURE USER ACTUALLY WANTS TO CHANGE THE DATAFRAME
        result = messagebox.askyesno("Confirmation", f"Are you sure you want to change the current dataframe to {self.selected_dataframe}?")

        if result:

            data_library.set_current_df_name(self.selected_dataframe)
            data_library.set_dataframe(data_library.get_current_df_name())


            utils.remove_frame_widgets(self.dataframe_viewer_content_frame)
            dataframe_viewer.setup_dataframe_viewer_tab(self.style, self.sub_button_frame, self.dataframe_management_content_frame, self.dataframe_viewer_content_frame, self.column_editor_content_frame, self.data_visualization_content_frame, reset_tables=True)

            utils.remove_frame_widgets(self.column_editor_content_frame)
            utils.remove_frame_widgets(self.data_visualization_content_frame)

            self.manage_dataframes_menu_label.configure(text=f"Current Dataframe: {data_library.get_current_df_name()}")
        else:
            return











################################################################################################################
################################################################################################################
################################################################################################################

################################################################################################################
################################################################################################################
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                    ########################################################################################
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
####                                                                                                        ####
################################################################################################################
################################################################################################################

################################################################################################################
################################################################################################################
################################################################################################################


################################################################################################################
################################################################################################################
#                                                                                                              #
#                                            CREATE NEW DATAFRAME                                              #
#                                                                                                              #
################################################################################################################
################################################################################################################



class CreateDataframeClass():
    def __init__(self, style, sub_button_frame, dataframe_management_content_frame, dataframe_viewer_content_frame, column_editor_content_frame, data_visualization_content_frame):
  
        self.df = data_library.get_dataframe()
        if self.df is None:
            utils.show_message("Error", "Please open a file first.")
            return

        self.df_dict = data_library.get_df_dict()
        self.selected_variables = []

        self.sub_button_frame = sub_button_frame
        self.dataframe_management_content_frame = dataframe_management_content_frame
        self.dataframe_viewer_content_frame = dataframe_viewer_content_frame
        self.column_editor_content_frame = column_editor_content_frame
        self.data_visualization_content_frame = data_visualization_content_frame
        self.style = style

        self.style.configure("manage_dataframes_button.TButton", background=color_dict["inactive_subtab_bg"], foreground=color_dict["inactive_subtab_txt"])
        self.style.configure("create_new_dataframe_button.TButton", background=color_dict["active_subtab_bg"], foreground=color_dict["active_subtab_txt"])


        data_library.add_tab_to_tab_dict("current_dataframe_management_tab", "create_new_dataframe")

        self.selected_dataframe_name = None
        self.selected_dataframe = None

        utils.remove_frame_widgets(self.dataframe_management_content_frame)

        self.dataframe_selection_frame = tk.Frame(self.dataframe_management_content_frame, bg=color_dict["main_content_border"])
        self.variable_selection_frame = tk.Frame(self.dataframe_management_content_frame, bg=color_dict["main_content_border"])
        self.dataframe_settings_frame = tk.Frame(self.dataframe_management_content_frame, bg=color_dict["main_content_border"])

        self.create_dataframe_selection_frame()
        self.create_variable_selection_frame()
        self.create_dataframe_settings_frame()

        self.switch_to_dataframe_selection_frame()


################################################################################################################
################################################################################################################
################################################################################################################

    def create_dataframe_selection_frame(self):

        # MAIN CONTENT FRAME
        self.dataframe_selection_inner_frame, self.dataframe_selection_canvas = utils.create_scrollable_frame(self.dataframe_selection_frame)


################################################################################################################

        # DATAFRAME MANAGING
        self.dataframe_selection_subframe_border = tk.Frame(self.dataframe_selection_inner_frame, bg=color_dict["sub_frame_border"])
        self.dataframe_selection_subframe_border.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.dataframe_selection_subframe = tk.Frame(self.dataframe_selection_subframe_border, bg=color_dict["sub_frame_bg"])
        self.dataframe_selection_subframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=2, pady=2)

        self.dataframe_selection_label = ttk.Label(self.dataframe_selection_subframe, text="Choose a Dataframe to Use", style="sub_frame_header.TLabel")
        self.dataframe_selection_label.pack(side=tk.TOP, pady=10)

        separator = ttk.Separator(self.dataframe_selection_subframe, orient="horizontal", style="Separator.TSeparator")
        separator.pack(side=tk.TOP, fill=tk.X, padx=200)


        # DATAFRAME SELECTION FRAME
        self.dataframe_listbox_frame = tk.Frame(self.dataframe_selection_subframe, bg=color_dict["sub_frame_bg"])
        self.dataframe_listbox_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

        self.dataframe_listbox = tk.Listbox(self.dataframe_listbox_frame, selectmode=tk.SINGLE, font=styles.listbox_font, exportselection=False, bg=color_dict["listbox_bg"],
                     fg=color_dict["listbox_fg"],
                     highlightbackground=color_dict["listbox_highlight_bg"],
                     highlightcolor=color_dict["listbox_highlight_color"],
                     selectbackground=color_dict["listbox_select_bg"],
                     selectforeground=color_dict["listbox_select_fg"],
                     height=20
                     )
        self.dataframe_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=100, pady=10)
        self.dataframe_listbox.bind("<Enter>",lambda e: utils.bind_mousewheel_to_frame(self.dataframe_selection_inner_frame, self.dataframe_selection_canvas, False))
        self.dataframe_listbox.bind("<Leave>",lambda e: utils.bind_mousewheel_to_frame(self.dataframe_selection_inner_frame, self.dataframe_selection_canvas, True))

        for dataframe in self.df_dict.keys():
            self.dataframe_listbox.insert(tk.END, dataframe)
        
        self.dataframe_listbox.bind("<<ListboxSelect>>", self.on_dataframe_listbox_select)

################################################################################################################

        # NAVIGATION MENU
        self.dataframe_selection_menu_frame = tk.Frame(self.dataframe_selection_frame, bg=color_dict["nav_banner_bg"])
        self.dataframe_selection_menu_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.advance_to_variable_selection_button = ttk.Button(self.dataframe_selection_menu_frame, text="Next", command=self.switch_to_variable_selection_frame, style='nav_menu_button.TButton')
        self.advance_to_variable_selection_button.pack(side=tk.RIGHT)

        self.dataframe_selection_menu_label = ttk.Label(self.dataframe_selection_menu_frame, text="Selected Dataframe: None", style="nav_menu_label.TLabel")
        self.dataframe_selection_menu_label.pack(side=tk.LEFT, expand=True)


################################################################################################################


    def on_dataframe_listbox_select(self, event):
        if self.dataframe_listbox.curselection():
            self.selected_dataframe_name = self.dataframe_listbox.get(self.dataframe_listbox.curselection()[0])
            self.selected_dataframe = self.df_dict[self.selected_dataframe_name]
 

            self.dataframe_selection_menu_label.configure(text=f"Selected Dataframe: {self.selected_dataframe_name}")
            self.variable_selection_menu_label.configure(text=f"Selected Dataframe: {self.selected_dataframe_name}")
            self.dataframe_settings_menu_label.configure(text=f"Selected Dataframe: {self.selected_dataframe_name}")

        else:
            return


################################################################################################################
################################################################################################################
################################################################################################################

    # CREATE VARIABLE SELECTION FRAME

    def create_variable_selection_frame(self):

        # MAIN CONTENT FRAME
        self.variable_selection_inner_frame, self.variable_selection_canvas = utils.create_scrollable_frame(self.variable_selection_frame)

################################################################################################################

        # VARIABLES SELECTION
        self.variable_selection_subframe_border = tk.Frame(self.variable_selection_inner_frame, bg=color_dict["sub_frame_border"])
        self.variable_selection_subframe_border.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.variable_selection_subframe = tk.Frame(self.variable_selection_subframe_border, bg=color_dict["sub_frame_bg"])
        self.variable_selection_subframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=2, pady=2)

        self.variable_selection_subframe_label = ttk.Label(self.variable_selection_subframe, text="Variable Selection", style="sub_frame_header.TLabel")
        self.variable_selection_subframe_label.pack(side=tk.TOP, pady=10)

        separator = ttk.Separator(self.variable_selection_subframe, orient="horizontal", style="Separator.TSeparator")
        separator.pack(side=tk.TOP, fill=tk.X, padx=200)


        # AVAILABLE VARIABLES SELECTION FRAME
        self.selection_frame = tk.Frame(self.variable_selection_subframe, bg=color_dict["sub_frame_bg"])
        self.selection_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)

        self.available_variables_frame = tk.Frame(self.selection_frame, bg=color_dict["sub_frame_bg"])
        self.available_variables_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.available_search_var = tk.StringVar()
        self.available_search_var.trace("w", self.update_available_variables_listbox)
        self.available_var_search_entry = tk.Entry(self.available_variables_frame, textvariable=self.available_search_var, font=styles.entrybox_small_font)
        self.available_var_search_entry.pack(side=tk.TOP, pady=10)

        self.available_variables_listbox = tk.Listbox(self.available_variables_frame, selectmode=tk.MULTIPLE, font=styles.listbox_font,
                                                                bg=color_dict["listbox_bg"],
                                                                fg=color_dict["listbox_fg"],
                                                                highlightbackground=color_dict["listbox_highlight_bg"],
                                                                highlightcolor=color_dict["listbox_highlight_color"],
                                                                selectbackground=color_dict["listbox_select_bg"],
                                                                selectforeground=color_dict["listbox_select_fg"],
                                                                height=20
                                                                )
        self.available_variables_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=100, pady=10)
        self.available_variables_listbox.bind("<Enter>",lambda e: utils.bind_mousewheel_to_frame(self.variable_selection_inner_frame, self.variable_selection_canvas, False))
        self.available_variables_listbox.bind("<Leave>",lambda e: utils.bind_mousewheel_to_frame(self.variable_selection_inner_frame, self.variable_selection_canvas, True))



        for column in sorted(self.df.columns, key=str.lower):
            self.available_variables_listbox.insert(tk.END, column)


        # TRANSFER BUTTONS
        self.buttons_frame = tk.Frame(self.selection_frame, bg=color_dict["sub_frame_bg"])
        self.buttons_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Larger buttons with ">>>" and "<<<" symbols
        self.transfer_right_button = ttk.Button(self.buttons_frame, text="Transfer Right >>>", command=self.transfer_right, style="large_button.TButton")
        self.transfer_right_button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.transfer_left_button = ttk.Button(self.buttons_frame, text="<<< Transfer Left", command=self.transfer_left, style="large_button.TButton")
        self.transfer_left_button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.BOTH, expand=True)

        separator = ttk.Separator(self.buttons_frame, orient="horizontal", style="Separator.TSeparator")
        separator.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Text buttons "Select All" and "Clear Selection"
        self.transfer_all_right_button = ttk.Button(self.buttons_frame, text="Select All", command=self.transfer_all_right, style="large_button.TButton")
        self.transfer_all_right_button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)

        self.transfer_all_left_button = ttk.Button(self.buttons_frame, text="Clear Selection", command=self.transfer_all_left, style="large_button.TButton")
        self.transfer_all_left_button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)

        separator = ttk.Separator(self.buttons_frame, orient="horizontal", style="Separator.TSeparator")
        separator.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)


        # SELECTED VARIABLES FRAME
        self.selected_variables_frame = tk.Frame(self.selection_frame, bg=color_dict["sub_frame_bg"])
        self.selected_variables_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.selected_variables_label = ttk.Label(self.selected_variables_frame, text="Selected Variables", style="sub_frame_sub_header.TLabel")
        self.selected_variables_label.pack(side=tk.TOP, pady=10)



        self.selected_variables_listbox = tk.Listbox(self.selected_variables_frame, selectmode=tk.MULTIPLE, font=styles.listbox_font,
                                                                bg=color_dict["listbox_bg"],
                                                                fg=color_dict["listbox_fg"],
                                                                highlightbackground=color_dict["listbox_highlight_bg"],
                                                                highlightcolor=color_dict["listbox_highlight_color"],
                                                                selectbackground=color_dict["listbox_select_bg"],
                                                                selectforeground=color_dict["listbox_select_fg"]
                                                                )
        self.selected_variables_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=100, pady=10)
        self.selected_variables_listbox.bind("<Enter>",lambda e: utils.bind_mousewheel_to_frame(self.variable_selection_inner_frame, self.variable_selection_canvas, False))
        self.selected_variables_listbox.bind("<Leave>",lambda e: utils.bind_mousewheel_to_frame(self.variable_selection_inner_frame, self.variable_selection_canvas, True))

################################################################################################################



        # NAVIGATION MENU
        self.variable_selection_menu_frame = tk.Frame(self.variable_selection_frame, bg=color_dict["nav_banner_bg"])
        self.variable_selection_menu_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.return_to_dataframe_selection_frame_button = ttk.Button(self.variable_selection_menu_frame, command=self.switch_to_dataframe_selection_frame, text='Back', style='nav_menu_button.TButton')
        self.return_to_dataframe_selection_frame_button.pack(side=tk.LEFT)

        self.advance_to_dataframe_settings_frame_button = ttk.Button(self.variable_selection_menu_frame, command=self.switch_to_dataframe_settings_frame, text="Next", style='nav_menu_button.TButton')
        self.advance_to_dataframe_settings_frame_button.pack(side=tk.RIGHT)

        self.variable_selection_menu_label = ttk.Label(self.variable_selection_menu_frame, text="", style="nav_menu_label.TLabel")
        self.variable_selection_menu_label.pack(side=tk.RIGHT, expand=True)


################################################################################################################

    # VARIABLES FUNCTIONS

    def update_available_variables_listbox(self, *args):
        search_term = self.available_search_var.get().lower()
        self.available_variables_listbox.delete(0, tk.END)
        for column in sorted(self.df.columns, key=str.lower):
            if search_term in column.lower():
                self.available_variables_listbox.insert(tk.END, column)


    def transfer_right(self):
        selections = self.available_variables_listbox.curselection()
        selected_items = [self.available_variables_listbox.get(index) for index in selections]

        for item in selected_items:
            if item not in self.selected_variables:
                self.selected_variables_listbox.insert(tk.END, item)
                self.selected_variables.append(item)


        for index in reversed(selections):
            self.available_variables_listbox.delete(index)

        self.available_var_search_entry.focus_set()


    def transfer_all_right(self):

        for i in range(self.available_variables_listbox.size()):
            self.available_variables_listbox.selection_set(i)

        selections = self.available_variables_listbox.curselection()
        selected_items = [self.available_variables_listbox.get(index) for index in selections]

        for item in selected_items:
            self.selected_variables_listbox.insert(tk.END, item)
            self.selected_variables.append(item)

        for index in reversed(selections):
            self.available_variables_listbox.delete(index)


    def transfer_left(self):
        selections = self.selected_variables_listbox.curselection()
        selected_items = [self.selected_variables_listbox.get(index) for index in selections]

        for item in selected_items:
            self.available_variables_listbox.insert(tk.END, item)
            self.selected_variables.remove(item)

        self.reorder_available_variables_listbox_alphabetically()

        for index in reversed(selections):
            self.selected_variables_listbox.delete(index)


    def transfer_all_left(self):

        for i in range(self.selected_variables_listbox.size()):
            self.selected_variables_listbox.selection_set(i)

        selections = self.selected_variables_listbox.curselection()
        selected_items = [self.selected_variables_listbox.get(index) for index in selections]

        for item in selected_items:
            self.available_variables_listbox.insert(tk.END, item)
            self.selected_variables.remove(item)

        self.reorder_available_variables_listbox_alphabetically()

        for index in reversed(selections):
            self.selected_variables_listbox.delete(index)


    def reorder_available_variables_listbox_alphabetically(self):
        top_visible_index = self.available_variables_listbox.nearest(0)
        top_visible_item = self.available_variables_listbox.get(top_visible_index)

        items = list(self.available_variables_listbox.get(0, tk.END))
        items = sorted(items, key=lambda x: x.lower())

        self.available_variables_listbox.delete(0, tk.END)  # Clear the Listbox
        for item in items:
            self.available_variables_listbox.insert(tk.END, item)

        if top_visible_index >= 0:
            index = items.index(top_visible_item)
            self.available_variables_listbox.yview(index)




    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################


    def create_dataframe_settings_frame(self):

        # MAIN CONTENT FRAME
        self.dataframe_settings_inner_frame, self.dataframe_settings_canvas = utils.create_scrollable_frame(self.dataframe_settings_frame)

################################################################################################################

        self.dataframe_name_frame_subframe_border = tk.Frame(self.dataframe_settings_inner_frame, bg=color_dict["sub_frame_border"])
        self.dataframe_name_frame_subframe_border.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.dataframe_name_frame_subframe = tk.Frame(self.dataframe_name_frame_subframe_border, bg=color_dict["sub_frame_bg"])
        self.dataframe_name_frame_subframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=2, pady=2)

        self.dataframe_name_frame_subframe_label = ttk.Label(self.dataframe_name_frame_subframe, text="Name of New Dataframe:", style="sub_frame_header.TLabel")
        self.dataframe_name_frame_subframe_label.pack(side=tk.TOP, pady=10)

        separator = ttk.Separator(self.dataframe_name_frame_subframe, orient="horizontal", style="Separator.TSeparator")
        separator.pack(side=tk.TOP, fill=tk.X, padx=200, pady=5)

        self.dataframe_name_frame = tk.Frame(self.dataframe_name_frame_subframe, bg=color_dict["sub_frame_bg"])
        self.dataframe_name_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.dataframe_name_entry = tk.Entry(self.dataframe_name_frame, font=styles.entrybox_large_font)
        self.dataframe_name_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

################################################################################################################

        self.condition_options_subframe_border = tk.Frame(self.dataframe_settings_inner_frame, bg=color_dict["sub_frame_border"])
        self.condition_options_subframe_border.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.condition_options_subframe = tk.Frame(self.condition_options_subframe_border, bg=color_dict["sub_frame_bg"])
        self.condition_options_subframe.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=2, pady=2)

        self.condition_options_subframe_label = ttk.Label(self.condition_options_subframe, text="Settings", style="sub_frame_header.TLabel")
        self.condition_options_subframe_label.pack(side=tk.TOP, pady=10)

        separator = ttk.Separator(self.condition_options_subframe, orient="horizontal", style="Separator.TSeparator")
        separator.pack(side=tk.TOP, fill=tk.X, padx=200, pady=5)



        # CONDITIONS OPTIONS FRAME
        self.condition_frames = []
        self.condition_signs = ['Equals', 'Does Not Equal', 'Less Than', 'Greater Than', 'Less Than or Equal To', 'Greater Than or Equal To', 'Contains', 'Does Not Contain']
        self.condition_signs_dict = {'Equals':'==',
                                     'Does Not Equal':'!=',
                                     'Less Than':'<',
                                     'Greater Than':'>',
                                     'Less Than or Equal To':'<=',
                                     'Greater Than or Equal To':'>='}

        self.condition_options_frame = tk.Frame(self.condition_options_subframe, bg=color_dict["sub_frame_bg"])
        self.condition_options_frame.pack(side=tk.TOP)


        # FRAME WHERE THE USER CAN ADD OR REMOVE MORE CONDITIONS
        self.condition_handling_frame = tk.Frame(self.condition_options_frame)
        self.condition_handling_frame.pack(side=tk.BOTTOM, pady=10)

        self.add_simple_and_button = ttk.Button(self.condition_handling_frame, text='and', command=lambda: self.add_condition(label='and'), style="small_button.TButton")
        self.add_simple_and_button.pack(side=tk.LEFT)

        self.add_simple_or_button = ttk.Button(self.condition_handling_frame, text='or', command=lambda: self.add_condition(label='or'), style="small_button.TButton")
        self.add_simple_or_button.pack(side=tk.LEFT)

        self.add_remove_button = ttk.Button(self.condition_handling_frame, text='Remove Condition', command=self.remove_condition, style="small_button.TButton")
        self.add_remove_button.pack(side=tk.LEFT)


        # FRAME WHERE THE CONDITIONS GO
        self.conditions_frame = tk.Frame(self.condition_options_frame, bg=color_dict["sub_frame_bg"])
        self.conditions_frame.pack(side=tk.TOP)






################################################################################################################

        # MENU FRAME
        self.dataframe_settings_menu_frame = tk.Frame(self.dataframe_settings_frame, bg=color_dict["nav_banner_bg"])
        self.dataframe_settings_menu_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.return_to_column_selection_button = ttk.Button(self.dataframe_settings_menu_frame, text="Back", command=self.switch_to_variable_selection_frame, style='nav_menu_button.TButton')
        self.return_to_column_selection_button.pack(side=tk.LEFT)

        self.dataframe_settings_menu_label = ttk.Label(self.dataframe_settings_menu_frame, text="", style="nav_menu_label.TLabel")
        self.dataframe_settings_menu_label.pack(side=tk.LEFT, expand=True)

        self.submit_settings_button = ttk.Button(self.dataframe_settings_menu_frame, text="SUBMIT", command=self.submit_dataframe_settings, style='nav_menu_button.TButton')
        self.submit_settings_button.pack(side=tk.RIGHT)


################################################################################################################


    # REMOVE MOST RECENT CONDITION LINE
    def remove_condition(self):
        if len(self.condition_frames) > 1:
            frame = self.condition_frames.pop()

            if self.condition_frames and self.condition_frames[-1].winfo_children()[0].cget("text") in {'AND', 'OR'}:
                separation_frame = self.condition_frames.pop()
                separation_frame.destroy()
            frame.destroy()

        else:
            return

    # ADD NEW CONDITION LINE
    def add_condition(self, label=''):

        condition_frame = tk.Frame(self.conditions_frame, bg=color_dict["sub_frame_bg"])
        condition_frame.pack(side=tk.TOP)

        self.condition_frames.append(condition_frame)

        condition_label = ttk.Label(condition_frame, text=label, style="sub_frame_text.TLabel")
        condition_label.pack(side=tk.LEFT)


        # COLUMN DROPDOWN FOR CONDITION
        def on_combobox_select(event):
            column_selected = column_dropdown.get()
            temp_df = self.selected_dataframe.copy().dropna(subset=[column_selected])
            is_numeric = pd.to_numeric(temp_df[column_selected], errors='coerce').notna().all()
            if is_numeric:

                temp_df[column_selected] = temp_df[column_selected].astype(float)
                self.q1 = np.percentile(temp_df[column_selected], 25)
                self.q2 = np.percentile(temp_df[column_selected], 50)  # Median (Q2)
                self.q3 = np.percentile(temp_df[column_selected], 75)

                self.q1_string = f"q1-{self.q1}"
                self.q2_string = f"q2-{self.q2}"
                self.q3_string = f"q3-{self.q3}"


                value_list = ["USER CHOICE", "[MISSING VALUE]"] + [self.q1_string, self.q2_string, self.q3_string] + list(temp_df[column_selected].unique())
            else:
                value_list = ["USER CHOICE", "[MISSING VALUE]"] + list(temp_df[column_selected].unique())

            column_values_dropdown["values"] = value_list

        selected_column_option = tk.StringVar()
        column_dropdown = ttk.Combobox(condition_frame, textvariable=selected_column_option, values=self.selected_variables, state="readonly")
        column_dropdown.pack(side=tk.LEFT)
        column_dropdown.bind("<<ComboboxSelected>>", on_combobox_select)
        column_dropdown.bind("<Enter>",lambda e: utils.bind_mousewheel_to_frame(self.dataframe_settings_inner_frame, self.dataframe_settings_canvas, False))
        column_dropdown.bind("<Leave>",lambda e: utils.bind_mousewheel_to_frame(self.dataframe_settings_inner_frame, self.dataframe_settings_canvas, True))


        # CONDITION SIGN DROPDOWN
        selected_condition_sign = tk.StringVar()
        selected_condition_sign_dropdown = ttk.Combobox(condition_frame, textvariable=selected_condition_sign, values=self.condition_signs, state="readonly")
        selected_condition_sign_dropdown.pack(side=tk.LEFT)

        # VALUE SELECTION DROPDOWN
        selected_value = tk.StringVar()
        value_list = ["USER CHOICE", "[MISSING VALUE]"]
        column_values_dropdown = ttk.Combobox(condition_frame, textvariable=selected_value, values=value_list, state="readonly")
        column_values_dropdown.pack(side=tk.LEFT)

        # USER ENTRY VALUE
        user_entry_value = tk.Entry(condition_frame, font=styles.entrybox_small_font)
        user_entry_value.pack(side=tk.LEFT)



    def submit_dataframe_settings(self):
        self.new_df = self.selected_dataframe.copy()
        self.dataframe_name = self.dataframe_name_entry.get()


        if self.dataframe_name == "":
            utils.show_message("No Dataframe Name", "Please input a DATAFRAME NAME")
            return
        if self.dataframe_name in self.df_dict.keys():
            utils.show_message("Dataframe Name Already Exists", "Dataframe Name Already Exists. Please input a different DATAFRAME NAME")
            return


        
        condition_list_total = []
        condition_strings = []


        for idx, frame in enumerate(self.condition_frames, start=1):

            condition_list = []

            if idx == 0:
                continue

            for widget in frame.winfo_children():
                try:
                    condition_list.append(widget.get())
                except:
                    condition_list.append(widget.cget("text"))

            condition_list_total.append(condition_list)

        for condition in condition_list_total:
            if len(condition) == 1:
                if condition[0] == 'AND':
                    condition_strings.append("&")
                elif condition[0] == 'OR':
                    condition_strings.append("|")
                continue

            condition_string = ''
            if condition[0] == 'or':
                condition_string = "|"
            if condition[0] == 'and':
                condition_string = "&"
            
            if condition[1] == "":
                utils.show_message("No Column Selected", "Please make sure all conditions have a column selected.")
                return
            if condition[2] == "":
                utils.show_message("No Condition Selected", "Please make sure all conditions have a condition selected.")
                return
            
            # Check if the condition requires a continuous column
            if condition[2] == "Less Than" or condition[2] == "Greater Than" or condition[2] == "Less Than or Equal To" or condition[2] == "Greater Than or Equal To":
                # Try to convert the column to numeric
                try:
                    self.selected_dataframe[condition[1]] = self.selected_dataframe[condition[1]].astype(float)
                except ValueError:
                    utils.show_message("Invalid Condition", f"The condition '{condition[2]}' can only be applied to numeric columns.")
                    return

            condition_string = condition_string + "("
            condition_string = condition_string + condition[1]
            condition_string = condition_string + self.condition_signs_dict[condition[2]]

            if condition[3] == "":
                utils.show_message("No Value Selected", "Error with Conditions. Please make sure all conditions have a value selected.")
                return

            if condition[3] == 'USER CHOICE':
                if condition[4] == "":
                    utils.show_message("No Value Entered", "No value entered for USER CHOICE. Please enter a value.")
                    return
                try:
                    self.selected_dataframe[condition[1]] = self.selected_dataframe[condition[1]].astype(float)
                    condition_string = condition_string + str(float(condition[4]))
                except:
                    self.selected_dataframe[condition[1]] = self.selected_dataframe[condition[1]].astype(object)
                    condition_string = condition_string + "'" + condition[4] + "'"

            elif condition[3] == "[MISSING VALUE]":
                if self.condition_signs_dict[condition[2]] == "==":
                    condition_string = condition_string[:-2] + ".isnull()==True"
                elif self.condition_signs_dict[condition[2]] == "!=":
                    condition_string = condition_string[:-2] + ".isnull()==False"

            else:
                try:

                    if condition[3] == self.q1_string:
                        condition_string = condition_string + str(float(self.q1))
                    elif condition[3] == self.q2_string:
                        condition_string = condition_string + str(float(self.q2))
                    elif condition[3] == self.q3_string:
                        condition_string = condition_string + str(float(self.q3))
                    else:
                        self.new_df[condition[1]] = self.new_df[condition[1]].astype(float)
                        condition_string = condition_string + str(float(condition[3]))

                except:

                    self.new_df[condition[1]] = self.new_df[condition[1]].astype(object)
                    condition_string = condition_string + "'" + condition[3] + "'"

            condition_string = condition_string + ')'
            condition_strings.append(condition_string)


        final_condition_string = ''.join(condition_strings)
        

        self.new_df = self.new_df.loc[self.new_df.eval(final_condition_string)]

        data_library.add_dataframe_to_dict(self.dataframe_name_entry.get(), self.new_df)
        ManageDataframesClass(self.style, self.sub_button_frame, self.dataframe_management_content_frame, self.dataframe_viewer_content_frame, self.column_editor_content_frame, self.data_visualization_content_frame)




    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################
    ###################################################################################################################################################################################################

    def switch_to_dataframe_selection_frame(self):

        self.variable_selection_frame.pack_forget()
        self.dataframe_settings_frame.pack_forget()
        self.dataframe_selection_frame.pack(fill=tk.BOTH, expand=True, padx=17, pady=17)

        utils.bind_mousewheel_to_frame(self.dataframe_selection_inner_frame, self.dataframe_selection_canvas, True)
        self.dataframe_management_content_frame.update_idletasks()

    def switch_to_variable_selection_frame(self):
        if self.selected_dataframe is not None:

            self.dataframe_selection_frame.pack_forget()
            self.dataframe_settings_frame.pack_forget()
            self.variable_selection_frame.pack(fill=tk.BOTH, expand=True, padx=17, pady=17)

            utils.bind_mousewheel_to_frame(self.variable_selection_inner_frame, self.variable_selection_canvas, True)
            self.dataframe_management_content_frame.update_idletasks()

            self.available_var_search_entry.focus_set()
        else:
            utils.show_message("No Dataframe Selected", "Please select a dataframe first.")
            return

    def switch_to_dataframe_settings_frame(self):
        if not self.selected_variables:
            return

        self.dataframe_selection_frame.pack_forget()
        self.variable_selection_frame.pack_forget()
        self.dataframe_settings_frame.pack(fill=tk.BOTH, expand=True, padx=17, pady=17)

        if len(self.condition_frames) < 1:
            self.add_condition(label='Where')
        if len(self.condition_frames) == 1:
            frame = self.condition_frames.pop()
            frame.destroy()
            self.add_condition(label='Where')


        utils.bind_mousewheel_to_frame(self.dataframe_settings_inner_frame, self.dataframe_settings_canvas, True)
        self.dataframe_management_content_frame.update_idletasks()

        self.dataframe_name_entry.focus_set()
