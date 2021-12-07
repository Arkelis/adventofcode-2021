open Core

let ceil_half n = 
  int_of_float @@ Float.round_up @@ (float_of_int n) /. 2.  
  
let int_of_bit = function
  | '1' -> 1
  | _ -> 0

let int_of_bin binary_string =
  let rec compute rev_chars mult n =
    match rev_chars with
    | head :: tail -> compute (tail) (mult * 2) (n + (int_of_bit head) * mult)
    | [] -> n in
  compute (String.to_list binary_string |> List.rev) 1 0

let bins =
  In_channel.read_lines "inputs/day03.txt"
  |> List.map ~f: String.strip

let part1 =
  let bin_length = List.nth_exn bins 0 |> String.length
  and threshold = List.length bins / 2 in

  let counter = List.init bin_length ~f:(fun _ -> 0)
  and inc_to_counter binary i bit_count =
    bit_count + int_of_bit (String.get binary i) in

  let rec count_bits binaries counter = 
    match binaries with
    | [] -> counter
    | binary :: others
      -> count_bits
           others
           (List.mapi ~f:(inc_to_counter binary) counter) in

  let most_commons = List.map ~f:(fun x -> if x > threshold then "1" else "0") (count_bits bins counter) in
  let least_commons = List.map ~f:(function "1" -> "0" | _ -> "1") most_commons in

  (String.concat most_commons |> int_of_bin) * (String.concat least_commons |> int_of_bin)
  |> string_of_int


  let part2 =
    let inc_to_counter char count =
      count + (int_of_bit char) in
    let rec count_ones binaries index count = 
      match binaries with
      | [] -> count
      | binary :: others
        -> count_ones others
             index
             (inc_to_counter (String.get binary index) count) in
    
    let rec get_last predicate binaries index = match binaries with
    | [result] -> result
    | more -> begin 
        let threshold = ceil_half (List.length binaries)
        and count = count_ones binaries index 0 in
        get_last 
          predicate 
          (List.filter ~f:(predicate threshold count index) more)
          (index + 1)
    end in

    let filter_most_common threshold count index binary =
      let char = String.get binary index in
      Char.equal char @@ if count >= threshold then '1' else '0' in
    let last_with_most_commons = get_last filter_most_common bins 0
    and filter_least_common threshold count index binary =
      let char = String.get binary index in
      Char.equal char @@ if count >= threshold then '0' else '1' in
    let last_with_least_commons =  get_last filter_least_common bins 0 in
  
    (last_with_most_commons |> int_of_bin) * (last_with_least_commons |> int_of_bin)
    |> string_of_int

let _ =
  print_endline part1;
  print_endline part2
