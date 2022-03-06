pub fn remove_element(numbers: &mut [i32], val: i32) -> i32 {
    let mut next_free_index = 0;
    for index in 0..numbers.len() {
        let num = numbers[index];
        if num != val {
            numbers[next_free_index] = num;
            next_free_index += 1;
        }
    }

    next_free_index as i32
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test() {
        let mut test_numbers = vec![
            vec![10, 20, 30, 40, 30, 20],
            vec![],
            vec![0],
            vec![10, 20, 0],
        ];
        for numbers in &mut test_numbers {
            for value in 0..*numbers.iter().max().unwrap_or(&0) {
                let expected_len =
                    numbers.len() - numbers.iter().filter(|number| **number == value).count();
                assert_eq!(remove_element(numbers, value), expected_len as i32);
            }
        }
    }
}
