
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
#                                           DATAFRAME MANAGEMENT                                               #
#                                                                                                              #
################################################################################################################
################################################################################################################

df = None
df_dict = {}
current_df_name = None
df_update_status_dict = {}
df_treeview = None
df_columns = None

# ADD DATAFRAME TO DICTIONARY
def add_dataframe_to_dict(dataframe_name, dataframe):
    global df_dict
    df_dict[dataframe_name] = dataframe


def get_df_dict():
    return df_dict


# SET MAIN DATAFRAME
def set_dataframe(dataframe_name):
    global df
    df = df_dict[dataframe_name]

def get_dataframe():
    return df


# SET DATAFRAME NAME
def set_current_df_name(dataframe_name):
    global current_df_name
    current_df_name = dataframe_name

def get_current_df_name():
    return current_df_name


# DATAFRAME HAS BEEN UPDATED OR NOT
def add_df_update_status_to_dict(tab, update_status):
    global df_update_status_dict
    df_update_status_dict[tab] = update_status

def get_df_update_status_dict():
    return df_update_status_dict



# DATAFRAME TREEVIEW
def set_df_treeview(treeview):
    global df_treeview
    df_treeview = treeview

def get_df_treeview():
    return df_treeview


# DATAFRAME COLUMNS
def set_df_columns(columns):
    global df_columns
    df_columns = columns

def get_df_columns():
    return df_columns




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
#                                               COLUMN EDITOR                                                  #
#                                                                                                              #
################################################################################################################
################################################################################################################

create_var_tab_var_list = []
create_var_tab_var_type = None

# REGRESSION INDEPENDENT VARIABLES LIST
def add_variable_to_create_var_tab_var_list(variable):
    global create_var_tab_var_list
    if variable not in create_var_tab_var_list:
        create_var_tab_var_list.append(variable)

def get_create_var_tab_var_list():
    return create_var_tab_var_list



# VARIABLE TYPE
def set_create_var_tab_var_type(variable_type):
    global create_var_tab_var_type
    create_var_tab_var_type = variable_type

def get_create_var_tab_var_type():
    return create_var_tab_var_type


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
################################################################################################################
################################################################################################################

################################################################################################################
################################################################################################################
################################################################################################################


################################################################################################################
################################################################################################################
#                                                                                                              #
#                                          DATA VISUALIZATION                                                  #
#                                                                                                              #
################################################################################################################
################################################################################################################


# COMPARISON TABLE MANAGEMENT

comp_tab_dep_var = None
comp_tab_ind_var_list = []
comp_tab_variable_type_dict = {}
comp_tab_variable_analysis_dict = {}
comp_tab_percent_type = None
comp_tab_data_type = None

# COMPARISON TABLE DEPENDENT VARIABLE
def set_comp_tab_dep_var(variable):
    global comp_tab_dep_var
    comp_tab_dep_var = variable

def get_comp_tab_dep_var():
    return comp_tab_dep_var


# COMPARISON TABLE INDEPENDENT VARIABLES LIST
def add_variable_to_comp_tab_ind_var_list(variable):
    global comp_tab_ind_var_list
    if variable not in comp_tab_ind_var_list:
        comp_tab_ind_var_list.append(variable)

def get_comp_tab_ind_var_list():
    return comp_tab_ind_var_list


# COMPARISON TABLE INDEPENDENT VARIABLES DICT
def add_variable_to_comp_tab_variable_type_dict(tab_name, setting):
    global comp_tab_variable_type_dict
    comp_tab_variable_type_dict[tab_name] = setting

def get_comp_tab_variable_type_dict():
    return comp_tab_variable_type_dict

# COMPARISON TABLE INDEPENDENT VARIABLES DICT
def add_variable_to_comp_tab_variable_analysis_dict(tab_name, setting):
    global comp_tab_variable_analysis_dict
    comp_tab_variable_analysis_dict[tab_name] = setting

def get_comp_tab_variable_analysis_dict():
    return comp_tab_variable_analysis_dict


# COMPARISON TABLE PERCENT TYPE
def set_comp_tab_percent_type(variable):
    global comp_tab_percent_type
    comp_tab_percent_type = variable

def get_comp_tab_percent_type():
    return comp_tab_percent_type


# COMPARISON TABLE DATA SELECTION
def set_comp_tab_data_type(variable):
    global comp_tab_data_type
    comp_tab_data_type = variable

def get_comp_tab_data_selection():
    return comp_tab_data_type
################################################################################################################
################################################################################################################
################################################################################################################

# REGRESSION MODEL MANAGEMENT

reg_tab_dep_var = None
reg_tab_ind_var_list = []
reg_tab_selected_regression = None


# REGRESSION DEPENDENT VARIABLE
def set_reg_tab_dep_var(variable):
    global reg_tab_dep_var
    reg_tab_dep_var = variable

def get_reg_tab_dep_var():
    return reg_tab_dep_var


# REGRESSION INDEPENDENT VARIABLES LIST
def add_variable_to_reg_tab_ind_var_list(variable):
    global reg_tab_ind_var_list
    if variable not in reg_tab_ind_var_list:
        reg_tab_ind_var_list.append(variable)

def get_reg_tab_ind_var_list():
    return reg_tab_ind_var_list


# REGRESSION ANALYSIS TYPE
def set_reg_tab_selected_regression(variable):
    global reg_tab_selected_regression
    reg_tab_selected_regression = variable

def get_reg_tab_selected_regression():
    return reg_tab_selected_regression






reg_tab_log_reg_target_value_dict = {}
log_reg_var_type_dict = {}
ref_dict = {}


# LOGISTIC REGRESSION TARGET VALUE
def add_variable_to_reg_tab_log_reg_target_value_dict(tab_name, setting):
    global reg_tab_log_reg_target_value_dict
    reg_tab_log_reg_target_value_dict[tab_name] = setting

def get_reg_tab_log_reg_target_value_dict():
    return reg_tab_log_reg_target_value_dict


# LOGISTIC REGRESSION INDEPENDENT VARIABLES DICT
def add_variable_to_log_reg_var_type_dict(variable, input_var):
    global log_reg_var_type_dict
    log_reg_var_type_dict[variable] = input_var

def get_log_reg_var_type_dict():
    return log_reg_var_type_dict


# LOGISTIC REGRESSION REFERENCES VARIABLES DICT
def add_variable_to_ref_dict(ind_var, reference_value):
    global ref_dict
    ref_dict[ind_var] = reference_value

def get_ref_dict():
    return ref_dict



################################################################################################################
################################################################################################################
################################################################################################################

# PLOT TAB MANAGEMENT

plot_tab_plot_selection = None

# PLOT SELECTION
def set_plot_tab_plot_selection(plot):
    global plot_tab_plot_selection
    plot_tab_plot_selection = plot

def get_plot_tab_plot_selection():
    return plot_tab_plot_selection





# SCATTER PLOT SELECTION
scatter_plot_x_axis_selection = None
scatter_plot_y_axis_selection = None
scatter_plot_group_by_variable = None
scatter_plot_group_by_selection = None
scatter_plot_group_by_variable_values = {}


def set_scatter_plot_x_axis_selection(variable):
    global scatter_plot_x_axis_selection
    scatter_plot_x_axis_selection = variable

def get_scatter_plot_x_axis_selection():
    return scatter_plot_x_axis_selection


def set_scatter_plot_y_axis_selection(variable):
    global scatter_plot_y_axis_selection
    scatter_plot_y_axis_selection = variable

def get_scatter_plot_y_axis_selection():
    return scatter_plot_y_axis_selection


def set_scatter_plot_group_by_variable(variable):
    global scatter_plot_group_by_variable
    scatter_plot_group_by_variable = variable

def get_scatter_plot_group_by_variable():
    return scatter_plot_group_by_variable


def set_scatter_plot_group_by_selection(choice):
    global scatter_plot_group_by_selection
    scatter_plot_group_by_selection = choice

def get_scatter_plot_group_by_selection():
    return scatter_plot_group_by_selection


def add_variable_to_scatter_plot_group_by_variable_values(ind_var, value, input_var):
    global scatter_plot_group_by_variable_values

    # Check if ind_var exists in the dictionary, if not, create an empty dictionary
    if ind_var not in scatter_plot_group_by_variable_values:
        scatter_plot_group_by_variable_values[ind_var] = {}

    scatter_plot_group_by_variable_values[ind_var][value] = input_var

def get_scatter_plot_group_by_variable_values():
    return scatter_plot_group_by_variable_values


# KAPLAN MEIER PLOT SELECTION
kaplan_plot_time_variable = None
kaplan_meier_group_variable = None

def set_kaplan_plot_time_variable(column):
    global kaplan_plot_time_variable
    kaplan_plot_time_variable = column

def get_kaplan_plot_time_variable():
    return kaplan_plot_time_variable


def set_kaplan_meier_group_variable(column):
    global kaplan_meier_group_variable
    kaplan_meier_group_variable = column

def get_kaplan_meier_group_variable():
    return kaplan_meier_group_variable







################################################################################################################
################################################################################################################
################################################################################################################

# MACHINE LEARNING TAB MANAGEMENT

mach_learn_tab_dep_var = None
mach_learn_tab_ind_var_list = []

mach_learn_tab_selected_model_type = None
mach_learn_tab_selected_cat_model = None
mach_learn_tab_selected_cont_model = None

mach_learn_tab_hyper_param_choice = None
mach_learn_tab_null_values_choice = None
mach_learn_tab_null_value_entry_value = None
mach_learn_tab_num_folds = None
mach_learn_tab_train_percent = None

# REGRESSION DEPENDENT VARIABLE
def set_mach_learn_tab_dep_var(variable):
    global mach_learn_tab_dep_var
    mach_learn_tab_dep_var = variable

def get_mach_learn_tab_dep_var():
    return mach_learn_tab_dep_var


# REGRESSION INDEPENDENT VARIABLES LIST
def add_variable_to_mach_learn_tab_ind_var_list(variable):
    global mach_learn_tab_ind_var_list
    if variable not in mach_learn_tab_ind_var_list:
        mach_learn_tab_ind_var_list.append(variable)

def get_mach_learn_tab_ind_var_list():
    return mach_learn_tab_ind_var_list


# MODEL TYPE
def set_mach_learn_tab_selected_model_type(variable):
    global mach_learn_tab_selected_model_type
    mach_learn_tab_selected_model_type = variable

def get_mach_learn_tab_selected_model_type():
    return mach_learn_tab_selected_model_type


# CATEGORICAL MODEL
def set_mach_learn_tab_selected_cat_model(variable):
    global mach_learn_tab_selected_cat_model
    mach_learn_tab_selected_cat_model = variable

def get_mach_learn_tab_selected_cat_model():
    return mach_learn_tab_selected_cat_model


# CATEGORICAL MODEL
def set_mach_learn_tab_selected_cont_model(variable):
    global mach_learn_tab_selected_cont_model
    mach_learn_tab_selected_cont_model = variable

def get_mach_learn_tab_selected_cont_model():
    return mach_learn_tab_selected_cont_model


# HYPERTUNE PARAMETERS SETTING
def set_mach_learn_tab_hyper_param_choice(variable):
    global mach_learn_tab_hyper_param_choice
    mach_learn_tab_hyper_param_choice = variable

def get_mach_learn_tab_hyper_param_choice():
    return mach_learn_tab_hyper_param_choice


# NUMBER OF FOLDS SETTING
def set_mach_learn_tab_num_folds(variable):
    global mach_learn_tab_num_folds
    mach_learn_tab_num_folds = variable

def get_mach_learn_tab_num_folds():
    return mach_learn_tab_num_folds


# NULL VALUES SETTING
def set_mach_learn_tab_null_values_choice(variable):
    global mach_learn_tab_null_values_choice
    mach_learn_tab_null_values_choice = variable

def get_mach_learn_tab_null_values_choice():
    return mach_learn_tab_null_values_choice


# NULL VALUES SETTING
def set_mach_learn_tab_train_percent(variable):
    global mach_learn_tab_train_percent
    mach_learn_tab_train_percent = variable

def get_mach_learn_tab_train_percent():
    return mach_learn_tab_train_percent



# NULL VALUES ENTRY VALUE
def set_mach_learn_tab_null_value_entry_value(variable):
    global mach_learn_tab_null_value_entry_value
    mach_learn_tab_null_value_entry_value = variable

def get_mach_learn_tab_null_value_entry_value():
    return mach_learn_tab_null_value_entry_value


################################################################################################################
################################################################################################################
################################################################################################################

# VARIOUS TAB MANAGEMENT

# NON-NUMERIC INDEPENDENT VARIABLES DICT
non_numeric_ind_dict = {}


def add_variable_to_non_numeric_ind_dict(ind_var, value, input_var):
    global non_numeric_ind_dict

    # Check if ind_var exists in the dictionary, if not, create an empty dictionary
    if ind_var not in non_numeric_ind_dict:
        non_numeric_ind_dict[ind_var] = {}

    non_numeric_ind_dict[ind_var][value] = input_var

def get_non_numeric_ind_dict():
    return non_numeric_ind_dict


# ONE HOT ENCODING DICT
one_hot_encoding_list = []

def add_variable_to_one_hot_encoding_list(ind_var):
    global one_hot_encoding_list
    if ind_var not in one_hot_encoding_list:
        one_hot_encoding_list.append(ind_var)

def get_one_hot_encoding_list():
    return one_hot_encoding_list






################################################################################################################
################################################################################################################
################################################################################################################

################################################################################################################
################################################################################################################
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
####                    ################################################################                    ####
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
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
########################################################################################                    ####
################################################################################################################
################################################################################################################

################################################################################################################
################################################################################################################
################################################################################################################


################################################################################################################
################################################################################################################
#                                                                                                              #
#                                                    RANDOM                                                    #
#                                                                                                              #
################################################################################################################
################################################################################################################

# TAB MANAGEMENT

tab_dict = {}

# ADD CURRENT SUB-TAB TO DICTIONARY
def add_tab_to_tab_dict(tab_name, setting):
    global tab_dict
    tab_dict[tab_name] = setting

def get_tab_dict():
    return tab_dict

################################################################################################################
################################################################################################################
################################################################################################################

# IMPORT EXPORT SELECTED VARIABLES

exported_variables_list = []


# EXPORTED VARIABLES LIST
def clear_exported_variables_list():
    global exported_variables_list
    exported_variables_list = []

def add_variable_to_exported_variables_list(variable):
    global exported_variables_list
    if variable not in exported_variables_list:
        exported_variables_list.append(variable)

def get_exported_variables_list():
    return exported_variables_list
