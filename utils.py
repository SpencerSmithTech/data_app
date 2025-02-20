import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import tkinter.font as tkfont

# LOCAL FILES
import styles
from styles import color_dict
import data_library

def show_message(title, message):
    messagebox.showinfo(title, message)

def prompt_yes_no(text_prompt):
    answer = messagebox.askyesno("Yes No Choice", text_prompt)
    return answer







def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_column_numeric(df, column_name):
    try:
        df[column_name] = pd.to_numeric(df[column_name])
        return True
    except (TypeError, ValueError):
        return False




def remove_frame_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def forget_frame_widgets(frame):
    for widget in frame.winfo_children():
        widget.pack_forget()







def create_scrollable_frame(root, color=color_dict["main_content_bg"], scrollbar=False):
    def on_variable_handling_canvas_configure(event):
        canvas_width = event.width
        main_canvas.itemconfig(scrollable_frame_window, width=canvas_width)

    def on_variable_handling_mousewheel(event):
        if main_canvas.winfo_exists():
            if event.num == 4 or event.delta > 0:  # Scroll up
                main_canvas.yview_scroll(-1, "units")
            elif event.num == 5 or event.delta < 0:  # Scroll down
                main_canvas.yview_scroll(1, "units")

    # SCROLLABLE FRAME
    container_frame = tk.Frame(root)
    container_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

    # Canvas for scrollable content
    main_canvas = tk.Canvas(container_frame, bg=color, highlightthickness=0)
    main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Adjusted to pack on the left to make room for scrollbar

    # Scrollable frame inside the canvas
    scrollable_frame = tk.Frame(main_canvas, bg=color)
    scrollable_frame_window = main_canvas.create_window((0, 0), window=scrollable_frame, anchor=tk.NW)

    # Conditionally create and pack the scrollbar
    if scrollbar:
        scrollbar_widget = tk.Scrollbar(container_frame, orient="vertical", command=main_canvas.yview)
        scrollbar_widget.pack(side=tk.RIGHT, fill=tk.Y)  # Pack the scrollbar on the right side
        main_canvas.configure(yscrollcommand=scrollbar_widget.set)

    # Bind events
    main_canvas.bind("<Configure>", on_variable_handling_canvas_configure)
    scrollable_frame.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

    # Cross-platform scroll event binding
    scrollable_frame.bind_all("<MouseWheel>", on_variable_handling_mousewheel)
    scrollable_frame.bind_all("<Button-4>", on_variable_handling_mousewheel)
    scrollable_frame.bind_all("<Button-5>", on_variable_handling_mousewheel)

    return scrollable_frame, main_canvas




def bind_mousewheel_to_frame(scrollable_frame, main_canvas, bind=True):
    def on_mousewheel(event):
        if main_canvas.winfo_exists():
            # Get the current view
            current_view = main_canvas.yview()

            # Scroll up
            if (event.num == 4 or event.delta > 0) and current_view[0] > 0:
                main_canvas.yview_scroll(-1, "units")

            # Scroll down
            elif (event.num == 5 or event.delta < 0) and current_view[1] < 1:
                main_canvas.yview_scroll(1, "units")

    if bind:
        scrollable_frame.bind_all("<MouseWheel>", on_mousewheel)
        scrollable_frame.bind_all("<Button-4>", on_mousewheel)
        scrollable_frame.bind_all("<Button-5>", on_mousewheel)
    else:
        scrollable_frame.unbind_all("<MouseWheel>")
        scrollable_frame.unbind_all("<Button-4>")
        scrollable_frame.unbind_all("<Button-5>")















def create_dataframe_table(parent, df, style, show_index=True, table_name="", graph_name="", title="", height=None):

    table_frame = tk.Frame(parent, bg='beige')
    table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    if title != "":
        label = tk.Label(table_frame, text=title, font=('Arial', 32, 'bold'), bg='beige')
        label.pack(pady=10)

    treeview_frame = tk.Frame(table_frame)
    treeview_frame.pack(fill=tk.BOTH, expand=True)

    yscrollbar = tk.Scrollbar(treeview_frame, orient="vertical")
    yscrollbar.pack(side="right", fill="y")

    xscrollbar = tk.Scrollbar(table_frame, orient="horizontal")
    xscrollbar.pack(side="bottom", fill="x")

    table_treeview = ttk.Treeview(treeview_frame, show="headings", style="Treeview", yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, height=height)

    yscrollbar.config(command=table_treeview.yview)
    xscrollbar.config(command=table_treeview.xview)

    columns = df.columns.tolist()
    table_treeview["columns"] = columns

    for column in columns:
        table_treeview.heading(column, text=column)
        table_treeview.column(column, width=160, anchor="center")

    for i, row in df.iterrows():
        values = ["" if pd.isnull(val) else val for val in row.tolist()]
        table_treeview.insert("", "end", values=values)

    table_treeview.pack(side="left", fill="both", expand=True)

    if not hasattr(parent, "table_frames"):
        parent.table_frames = {}
    parent.table_frames[table_name] = table_frame





def create_editable_table(parent, df, style, table_name="", title="", height=None):
    table_frame = tk.Frame(parent, bg='beige')
    table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    if title != "":
        label = tk.Label(table_frame, text=title, font=('Arial', 32, 'bold'), bg='beige')
        label.pack(pady=10)

    treeview_frame = tk.Frame(table_frame)
    treeview_frame.pack(fill=tk.BOTH, expand=True)

    yscrollbar = tk.Scrollbar(treeview_frame, orient="vertical")
    yscrollbar.pack(side="right", fill="y")

    xscrollbar = tk.Scrollbar(table_frame, orient="horizontal")
    xscrollbar.pack(side="bottom", fill="x")

    table_treeview = ttk.Treeview(treeview_frame, show="headings", style="Treeview", yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set, height=height)

    yscrollbar.config(command=table_treeview.yview)
    xscrollbar.config(command=table_treeview.xview)

    columns = df.columns.tolist()
    table_treeview["columns"] = columns


    for column in columns:
        table_treeview.heading(column, text=column)
        table_treeview.column(column, anchor="center", stretch=False)

    for i, row in df.iterrows():
        values = ["" if pd.isnull(val) else val for val in row.tolist()]
        table_treeview.insert("", "end", values=values)

    table_treeview.pack(side="left", fill="both", expand=True)

    if not hasattr(parent, "table_frames"):
        parent.table_frames = {}
    parent.table_frames[table_name] = table_frame

    def on_drag_start(event):
        region = table_treeview.identify_region(event.x, event.y)
        if region == "heading":
            column = table_treeview.identify_column(event.x)
            if column:
                col_index = int(column.replace('#', '')) - 1
                table_treeview._drag_data = {"type": "column", "index": col_index, "x": event.x}
        elif region == "cell":
            item = table_treeview.identify_row(event.y)
            if item:
                table_treeview.selection_set(item)
                table_treeview._drag_data = {"type": "row", "item": item, "y": event.y}

    def on_drag_motion(event):
        if table_treeview._drag_data["type"] == "column":
            x = event.x
            dx = x - table_treeview._drag_data["x"]
            if abs(dx) > 10:
                from_col = table_treeview._drag_data["index"]
                to_col = table_treeview.identify_column(event.x)
                if to_col:
                    to_index = int(to_col.replace('#', '')) - 1
                    if from_col != to_index:
                        # Rearrange columns
                        columns.insert(to_index, columns.pop(from_col))
                        table_treeview["columns"] = columns

                        # Rearrange row values
                        for item in table_treeview.get_children():
                            values = list(table_treeview.item(item, "values"))
                            values.insert(to_index, values.pop(from_col))
                            table_treeview.item(item, values=values)

                        for col in columns:
                            table_treeview.heading(col, text=col)
                            table_treeview.column(col, anchor="center")

                        table_treeview._drag_data["x"] = x
                        table_treeview._drag_data["index"] = to_index
        elif table_treeview._drag_data["type"] == "row":
            y = event.y
            item = table_treeview.identify_row(y)
            if item and item != table_treeview._drag_data["item"]:
                idx1 = table_treeview.index(table_treeview._drag_data["item"])
                idx2 = table_treeview.index(item)
                table_treeview.move(table_treeview._drag_data["item"], "", idx2)
                table_treeview.move(item, "", idx1)

    def on_drag_end(event):
        table_treeview._drag_data = {"type": None, "index": None, "x": 0, "item": None, "y": 0}

    table_treeview._drag_data = {"type": None, "index": None, "x": 0, "item": None, "y": 0}

    table_treeview.bind("<ButtonPress-1>", on_drag_start)
    table_treeview.bind("<B1-Motion>", on_drag_motion)
    table_treeview.bind("<ButtonRelease-1>", on_drag_end)

    return table_treeview, columns


def save_editable_table(treeview, columns):
    if not treeview:
        return
    if not columns:
        return

    rows = []
    for child in treeview.get_children():
        row = treeview.item(child)["values"]
        rows.append(row)
    new_df = pd.DataFrame(rows, columns=columns)

    # Replace leading underscores in column names
    new_df.columns = new_df.columns.str.replace("^_", "")


    file_path = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*")]
    )

    # Check if the user canceled the file dialog
    if not file_path:
        return

    # Get the selected file name and extension
    file_name = file_path.split('/')[-1]

    # Get the file extension
    file_extension = file_name.split('.')[-1]

    # Save the DataFrame to the chosen file path based on the selected file extension
    if file_extension == 'csv':
        new_df.to_csv(file_path, index=False)
    elif file_extension == 'xlsx':
        new_df.to_excel(file_path, index=False)
    else:
        return


























def create_graph(content_frame, fig):

    remove_frame_widgets(content_frame)

    # Create a new graph frame
    graph_frame = tk.Frame(content_frame)
    graph_frame.pack()

    # Set the size of the figure
    fig.set_size_inches(10, 7)

    # Create a canvas for the graph
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)



def is_column_numeric(df, column_name):
    try:
        if df[column_name].dtype == 'O':
            return False

        numeric_values = pd.to_numeric(df[column_name], errors='coerce')
        non_null_numeric_values = numeric_values.nunique()

        if non_null_numeric_values > 2:
            return True
        else:
            return False
    except (TypeError, ValueError):
        return False





def create_summary_table(df):

    temp_df = df.copy()
    temp_df.replace("[MISSING VALUE]", np.nan, inplace=True)

    # Preparing the columns for the summary dataframe
    describe_cols = ['mean', 'std', 'min', '25%', '50%', '75%', 'max']
    summary_cols = ['Column', 'Mode', 'Non-Missing Count', 'Missing Count', 'Non-Missing Unique Count'] + describe_cols
    summary_list = []  # Initialize a list to store DataFrames

    # Function to check if a column is numeric
    def is_numeric(col):
        return pd.api.types.is_numeric_dtype(temp_df[col])

    # Iterating through each column to compute the statistics
    for column in temp_df.columns:

        data = {
            'Column': column,
            'Mode': tuple(map(str, temp_df[column].mode().values)),
            'Non-Missing Count': temp_df[column].count(),
            'Missing Count': temp_df[column].isnull().sum(),
            'Non-Missing Unique Count': temp_df[column].nunique()
        }

        # Adding descriptive statistics for numeric columns
        if is_numeric(column):
            data.update(temp_df[column].describe()[describe_cols].to_dict())

        # Filtering out empty or all-NA columns from the data dictionary
        data = {k: v for k, v in data.items() if v is not None and not pd.isna(v)}

        # Adding the computed data to the summary_list
        summary_list.append(pd.DataFrame([data]))

    # Concatenate all DataFrames in the summary_list
    summary = pd.concat(summary_list, ignore_index=True)

    return summary











