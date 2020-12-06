def shear_glue_failure(I, num_tabs, b_tab, Q_glue):
    # b_tab refers to the width of one tab
    return 4 * I * num_tabs * b_tab / Q_glue
