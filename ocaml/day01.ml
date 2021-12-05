open Core


let measurements =
  In_channel.read_lines "inputs/day01.txt"
  |> List.map ~f:int_of_string

let part1 =
  let rec find_increases measures n =
    match measures with
      | prev :: next :: others when next > prev -> find_increases (next :: others) (n + 1)
      | _ :: next :: others -> find_increases (next :: others) n
      | _ -> n in
  find_increases measurements 0

let part2 =
  let rec find_sum_increases measures n =
    match measures with
      | a :: b :: c :: d :: others 
        when (a + b + c) < (b + c + d) 
        -> find_sum_increases (b :: c :: d :: others) (n + 1)
      | _ :: next :: others -> find_sum_increases (next :: others) n
      | _ -> n in
  find_sum_increases measurements 0

let _ =
  print_endline (string_of_int part1);
  print_endline (string_of_int part2)
