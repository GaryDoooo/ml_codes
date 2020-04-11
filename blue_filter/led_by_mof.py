from mof_angular_shift import spectrum, mof_by_angle
import matplotlib.pyplot as plt
import numpy as np
import math
#  from statistics import mean, stdev


def integrate(xlist, ylist):
    result = 0
    l = len(xlist)
    for i in range(1, l - 1):
        result += (xlist[i + 1] - xlist[i - 1]) / 2 * ylist[i]
    result += ylist[l - 1] * (xlist[l - 1] - xlist[l - 2])
    result += ylist[0] * (xlist[1] - xlist[0])
    return result


class led_mof_combined:
    def __init__(self,
                 led_spectrum_file,
                 mof_spectrum_file,
                 start=400,  # lambda start to integrate
                 end=520,   # lambda ends
                 led_peak=460,
                 n_eff=1.9, n1=1, n2=1.9, n_high=1.5,
                 mof_tune_y_by_ratio=1,
                 mof_add_y_with_whitenoise=0,
                 mof_shift_x=0):
        self.led = spectrum(led_spectrum_file)
        self.led.move_led_peak(peak=led_peak)
        self.mof = mof_by_angle(
            mof_spectrum_file,
            n_eff=n_eff,
            tune_y_by_ratio=mof_tune_y_by_ratio,
            add_y_with_whitenoise=mof_add_y_with_whitenoise,
            shift_x=mof_shift_x)
        self.n_eff = n_eff
        self.n1 = n1
        self.n2 = n2
        self.start = start
        self.end = end
        self.diff2mof_pass_rate = self.pass_rate_after_diffuser_under_mof(
            n_high=n_high)

    def intensity_by_angle_and_wavelength(
            self,
            incident_angle,
            wavelength,
            fresnel_surface=2,
            with_mof=True):
        mof_T = self.mof.get_transmission_by_shift(
            incident_angle, wavelength, fresnel_surface, self.n1, self.n2)
        if with_mof:
            return self.led.get_spectrum(wavelength) * mof_T
        else:
            return self.led.get_spectrum(wavelength)

    def get_integrated_intensity_by_angle(
            self,
            incident_angle,
            integration_resolution=0.2,
            fresnel_surface=2, with_mof=True):
        xlist = []
        ylist = []
        for x in np.arange(
                self.start,
                self.end +
                integration_resolution,
                integration_resolution):
            xlist.append(x)
            ylist.append(
                self.intensity_by_angle_and_wavelength(
                    incident_angle, x, fresnel_surface=2, with_mof=with_mof))
        return integrate(xlist, ylist) * \
            math.cos(incident_angle / 180 * math.pi)

    def pass_rate_after_diffuser_under_mof(self, n_high=0):
        if n_high == 0:
            n_high = self.n2
        theta_TIR = math.asin(1 / n_high)
        xlist = []
        ylist = []
        for x in np.arange(0, theta_TIR, 0.01):
            thera_in_air = math.asin(n_high * math.sin(x))
            I_ratio = math.cos(x) / math.cos(thera_in_air)
            y = self.get_integrated_intensity_by_angle(
                thera_in_air / math.pi * 180,
                fresnel_surface=1
            ) * math.sin(x) * I_ratio
            xlist.append(x)
            ylist.append(y)
        passed = integrate(xlist, ylist)
        xlist = []
        ylist = []
        led_intensity_at_zero = self.get_integrated_intensity_by_angle(
            0, fresnel_surface=1, with_mof=False)
        for x in np.arange(0, math.pi / 2, 0.01):
            I = math.cos(x)
            y = led_intensity_at_zero * I * math.sin(x)
            xlist.append(x)
            ylist.append(y)
        total = integrate(xlist, ylist)
        return passed / total

    def int_I_by_angle_withDiffuser(self, incident_angle,
                                    diffuse_rate=0.8  # portion of light be lamberian diffused, rest direct punch thru
                                    ):
        led_I_at_theta = self.get_integrated_intensity_by_angle(
            incident_angle, with_mof=False)
        return diffuse_rate * self.diff2mof_pass_rate * led_I_at_theta + \
            (1 - diffuse_rate) * self.get_integrated_intensity_by_angle(incident_angle)


def main():
    result_l = []
    #  result_R = []
    result_R0 = []
    result_Rd1 = []
    result_Rd2 = []
    result_Rd3 = []
    result_Rd4 = []
    combination = led_mof_combined(
        'LED.xlsx',
        '21lyr.xlsx',
        start=400,
        end=520,
        led_peak=470,
        n_eff=1.9,
        n1=1,
        n2=1.7, n_high=1.5, mof_tune_y_by_ratio=0.01)
    print("Diff to MOF pass rate:", combination.diff2mof_pass_rate)
    #  for diffuse_rate in np.arange(0.6, 1, 0.03):
    #  ylist = []
    #  for theta in range(0, 90, 5):
    #  ylist.append(
    #  combination.int_I_by_angle_withDiffuser(
    #  theta, diffuse_rate=diffuse_rate))
    #  print(
    #  "Diff rate:",
    #  diffuse_rate,
    #  "std:",
    #  np.std(ylist),
    #  "mean:",
    #  sum(ylist) / len(ylist),
    #  "ratio:",
    #  np.std(ylist) / sum(ylist) * len(ylist))

    for theta in range(0, 90, 5):
        result_l.append(theta)
        cos = math.cos(theta / 180 * math.pi)
        result_R0.append(
            combination.get_integrated_intensity_by_angle(
                theta, with_mof=False) * cos)
        #  result_R.append(
        #  combination.get_integrated_intensity_by_angle(theta) * cos)
        result_Rd1.append(
            combination.int_I_by_angle_withDiffuser(
                theta, diffuse_rate=0.5) * cos)
        result_Rd2.append(
            combination.int_I_by_angle_withDiffuser(
                theta, diffuse_rate=0) * cos)
        result_Rd3.append(
            combination.int_I_by_angle_withDiffuser(
                theta, diffuse_rate=0.75) * cos)
        result_Rd4.append(
            combination.int_I_by_angle_withDiffuser(
                theta, diffuse_rate=0.25) * cos)
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('Angle of incidence (degrees)')
    ax1.set_ylabel('Integrated strength w/o filter a.u.', color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.plot(result_l, result_R0, color=color, linestyle='--')
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Integrated strength w/ filter a.u.', color=color)
    #  ax2.plot(result_l, result_R, color=color, linestyle='--')
    ax2.plot(result_l, result_Rd2, color=color, linestyle='dotted', label='0')
    ax2.plot(
        result_l,
        result_Rd4,
        color=color,
        linestyle='dashdot',
        label='25%')
    ax2.plot(result_l, result_Rd1, color=color, linestyle='solid', label='50%')
    ax2.plot(
        result_l,
        result_Rd3,
        color=color,
        linestyle='dashed',
        label='75%')
    ax2.legend(loc='lower left')
    ax2.tick_params(axis='y', labelcolor=color)
    fig.tight_layout()
    #  plt.xlim([400, 550])
    plt.savefig('result/led_and_filter_shift.svg')


if __name__ == '__main__':
    main()
