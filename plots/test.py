

if __name__ == "__main__":
  process_count = 8
  for rank in range(process_count):
    for i in range(process_count):
      s_proc = (rank + i) % process_count
      r_proc = (rank + process_count - i) % process_count
      print("rank ", rank, " sent to process ", s_proc, ", and recieved from process ", r_proc)