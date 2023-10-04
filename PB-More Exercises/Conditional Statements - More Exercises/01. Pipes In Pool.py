pool_volume_in_liters = int(input())
flow_rate_first_pipe_per_hour = int(input())
flow_rate_second_pipe_per_hour = int(input())
hours_the_worker_is_absent = float(input())

first_pipe = hours_the_worker_is_absent * flow_rate_first_pipe_per_hour
second_pipe = hours_the_worker_is_absent * flow_rate_second_pipe_per_hour

total_pipe_liters = first_pipe + second_pipe
pool_percent = (total_pipe_liters / pool_volume_in_liters) * 100

if total_pipe_liters <= pool_volume_in_liters:
    first_pipe = (first_pipe / total_pipe_liters) * 100
    second_pipe = (second_pipe / total_pipe_liters) * 100
    print(f"The pool is {pool_percent:.2f}% full. Pipe 1: {first_pipe:.2f}%. Pipe 2: {second_pipe:.2f}%." )

else:
    liters_of_water_in_excess = total_pipe_liters - pool_volume_in_liters
    print(f"For {hours_the_worker_is_absent:.2f} hours the pool overflows with {liters_of_water_in_excess:.2f} liters." )
