def read_layout(farm_layout):

    layout_x = []
    layout_y = []

    with open(farm_layout, 'r') as layout:

        for line in layout:

            columns = line.split()
            layout_x.append(float(columns[0]))
            layout_y.append(float(columns[1]))

    return layout_x, layout_y
