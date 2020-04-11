from fresnel import two_surface_fresnel, one_surface_fresnel
import matplotlib.pyplot as plt
from pandas import read_csv, read_excel
from plotdigi_help import get_y_from_known_discrete_XY
import math
import numpy as np


class mof_by_angle:
    def __init__(
            self,
            input_file="filter.csv",
            n_eff=1.5,
            tune_y_by_ratio=1,
            add_y_with_whitenoise=0,
            shift_x=0):
        if ".csv" in input_file:
            df = read_csv(input_file)
        else:
            df = read_excel(input_file)
        self.x = [_ + shift_x for _ in df['X']]  # wavelength
        # transmission %
        self.y = [tune_y_by_ratio * _ + add_y_with_whitenoise for _ in df['Y']]
        self.n_eff = n_eff

    def get_transmission_by_shift(self,
                                  incident_angle,  # in degree
                                  wavelength,
                                  fresnel_surface=0,
                                  n1=1,
                                  n2=1.5):
        incident_angle_degrees = incident_angle
        incident_angle = incident_angle / 180 * math.pi
        lambda0 = wavelength / math.sqrt(
            1 - (math.sin(incident_angle)
                 / self.n_eff)**2)
        T_theta = get_y_from_known_discrete_XY(
            lambda0, self.x, self.y)
        if fresnel_surface == 0:
            return T_theta
        elif fresnel_surface == 1:
            #  R0 = one_surface_fresnel(0, n1, n2)
            R_theta = one_surface_fresnel(
                incident_angle_degrees, n1, n2)
            return T_theta * (1 - R_theta)
            #  R = (100 - T_theta) * R_theta / R0
            #  return 100 - R
        else:
            #  R0 = two_surface_fresnel(0, n1, n2)
            R_theta = two_surface_fresnel(
                incident_angle_degrees, n1, n2)
            return T_theta * (1 - R_theta)
            #  R = (100 - T_theta) * R_theta / R0,
            #  return 100 - R


class spectrum:
    def __init__(self,
                 input_file,
                 shift_x=0):
        self.body = mof_by_angle(input_file)
        self.body.x = [_ + shift_x for _ in self.body.x]

    def move_led_peak(self, peak=500):
        current_peak = self.body.x[np.argmax(self.body.y)]
        x_expand_ratio = peak / current_peak
        for i in range(0, len(self.body.x)):
            self.body.x[i] = self.body.x[i] * x_expand_ratio

    def get_spectrum(self, input_lambda):
        return self.body.get_transmission_by_shift(
            0, input_lambda)


def main():
    led = spectrum('LED.xlsx', shift_x=10)
    led.move_led_peak(460)
    led_l = []
    led_y = []
    for l in range(400, 600, 1):
        led_l.append(l)
        led_y.append(led.get_spectrum(l))
    mof = mof_by_angle(
        input_file='21lyr.xlsx',
        n_eff=1.9,
        tune_y_by_ratio=0.01)
    #  print(mof.x.head(), mof.y.head())
    result_l = []
    result_R = []
    result_R30 = []
    result_R45 = []
    result_R60 = []
    for l in range(400, 700, 1):
        result_l.append(l)
        result_R.append(
            mof.get_transmission_by_shift(
                0, l))
        result_R30.append(
            mof.get_transmission_by_shift(
                30, l, fresnel_surface=2, n1=1, n2=1.7))
        result_R60.append(
            mof.get_transmission_by_shift(
                60, l, fresnel_surface=2, n1=1, n2=1.7))
        result_R45.append(
            mof.get_transmission_by_shift(
                45, l, fresnel_surface=2, n1=1, n2=1.7))

    print("test", two_surface_fresnel(30))
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('wavelength(nm)')
    ax1.set_ylabel('T%')
    ax1.plot(result_l, result_R, "r-",
             result_l, result_R30, "g-",
             result_l, result_R60, "b-",
             result_l, result_R45, "c-")
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('LED a.u.', color=color)
    ax2.plot(led_l, led_y, "k-")
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout()
    plt.xlim([400, 550])
    plt.savefig('result/filter_shift.svg')


if __name__ == '__main__':
    main()
