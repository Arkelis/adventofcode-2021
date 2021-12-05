open Core


let commands =
  let get_command line = match (String.split ~on:' ' line) with
    | command :: value :: [] -> Some (command, int_of_string value)
    | _ -> None in
  In_channel.read_lines "inputs/day02.txt"
  |> List.map ~f:get_command

let part1 =
  let compute_position p c v = match c with
    | "forward" -> p + v
    | _ -> p
  and compute_depth d c v = match c with
    | "up" -> d - v
    | "down" -> d + v
    | _ -> d in
  let rec travel commands position depth =
    match commands with
      | Some (command, value) :: others
        -> travel others
          (compute_position position command value)
          (compute_depth depth command value)
      | None :: others -> travel others position depth 
      | [] -> position * depth in
    travel commands 0 0

let part2 =
  let compute_position p c v = match c with
    | "forward" -> p + v
    | _ -> p
  and compute_depth d a c v = match c with
    | "forward" -> d + a*v
    | _ -> d
  and compute_aim a c v = match c with
    | "up" -> a - v
    | "down" -> a + v
    | _ -> a in
  let rec travel commands position depth aim =
    match commands with
      | Some (command, value) :: others
        -> travel others
          (compute_position position command value)
          (compute_depth depth aim command value)
          (compute_aim aim command value)
      | None :: others -> travel others position depth aim
      | [] -> position * depth in
    travel commands 0 0 0

let _ =
  print_endline (string_of_int part1);
  print_endline (string_of_int part2)
