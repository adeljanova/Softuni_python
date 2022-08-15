volume_of_pool_in_litres = int(input())
debit_of_first_pipe_for_hour = int(input())
debit_of_second_pipe_for_hour = int(input())
hours_the_worker_is_gone = float(input())
time_for_first_pipe = debit_of_first_pipe_for_hour * hours_the_worker_is_gone
time_for_second_pipe = debit_of_second_pipe_for_hour * hours_the_worker_is_gone
total_time_for_both_pipes = time_for_first_pipe + time_for_second_pipe
if total_time_for_both_pipes <= volume_of_pool_in_litres:
    percentage_pool_filled = total_time_for_both_pipes / volume_of_pool_in_litres
    percentage_pool_filled = "{:.2%}".format(percentage_pool_filled)
    percentage_first_pipe = time_for_first_pipe / total_time_for_both_pipes
    percentage_first_pipe = "{:.2%}".format(percentage_first_pipe)
    percentage_second_pipe = time_for_second_pipe / total_time_for_both_pipes
    percentage_second_pipe = "{:.2%}".format(percentage_second_pipe)
    print(f"The pool is {percentage_pool_filled} full. Pipe 1: {percentage_first_pipe} . "
          f"Pipe 2: {percentage_second_pipe}.")
elif total_time_for_both_pipes > volume_of_pool_in_litres:
    extra_litres = total_time_for_both_pipes - volume_of_pool_in_litres
    print(f"For {hours_the_worker_is_gone} hours the pool overflows"
          f" with {extra_litres:.2f} liters.")