from datetime import timedelta

def T100_time(temperatures=(95, 55, 72),
              incubation_durations=(30, 30, 60),
              volume=10,
              cycles=35):

    k = (1.2445 - 1.4237) / (100 - 10)
    m = 1.4237 - k * 10
    ramp_speed = m + k * volume
    incubation_time = sum(incubation_durations) * cycles
    delta_T = (sum(abs(temperatures[i + 1] - temperatures[i])
            for i in range(len(temperatures) - 1)) + abs(temperatures[-1] - temperatures[0]))
    ramp_time = (delta_T * cycles) / ramp_speed
    total_time = incubation_time + ramp_time

    return timedelta(seconds=total_time)


print(T100_time(volume=50, cycles=69))
print(T100_time(volume=10, cycles=35))
