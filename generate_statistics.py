__author__ = 'sebasanper'
from os import chdir, path
models1 = ['area_overlap/jensen_results', 'eddy_viscosity/ainslie_results', 'larsenEWTS2/larsen_results']
powers1 = ['power7', 'power5', 'power3', 'powertable']
thrusts1 = ['Ct6', 'Ct4', 'Ct3', 'Cttable', 'Ctstep']
roses1 = ['30', '360']

models = [1, 2, 3]
powers = [1, 2, 3, 4]
thrusts = [1, 2, 3, 4, 5]
roses = [1, 2]
counter = 0
output = open('statistics.gp', 'w')
for model in models:
    for power in powers:
        for thrust in thrusts:
            for rose in roses:
                if models1[model - 1] == 'area_overlap/jensen_results':
                    output.write('unset print; stats \'{0:s}/{1:s}/{2:s}/{3:s}/exe_time_jensen.dat\'\n'.format(models1[model - 1], powers1[power - 1], thrusts1[thrust - 1], roses1[rose - 1]))
                    output.write('set print \'time_stats.dat\' append; print \'{4:d} {0:d} {1:d} {2:d} {3:d} \', STATS_min_y, STATS_mean_y, STATS_stddev_y\n'.format(model, power, thrust, rose, counter))
                else:
                    output.write('unset print; stats \'{0:s}/{1:s}/{2:s}/{3:s}/exe_time.dat\'\n'.format(models1[model - 1], powers1[power - 1], thrusts1[thrust - 1], roses1[rose - 1]))
                    output.write('set print \'time_stats.dat\' append; print \'{4:d} {0:d} {1:d} {2:d} {3:d} \', STATS_min_y, STATS_mean_y, STATS_stddev_y\n'.format(model, power, thrust, rose, counter))
                counter += 1

counter = 0
efficiency = open('efficiency_stats.dat', 'w')
for model in models:
    for power in powers:
        for thrust in thrusts:
            for rose in roses:
                chdir(path.join(models1[model - 1], powers1[power - 1], thrusts1[thrust - 1], roses1[rose - 1]))
                with open('efficiency.dat', 'r') as f:
                    data = float(f.readline())
                efficiency.write('{5:d} {0:d} {1:d} {2:d} {3:d} {4:f}\n'.format(model, power, thrust, rose, data, counter))
                chdir('/home/sebasanper/PycharmProjects/')
                counter += 1
efficiency.close()

