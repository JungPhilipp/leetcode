use std::string::String;
struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strings: Vec<String>) -> String {
        if strings.is_empty() {
            return String::new();
        }

        let mut index = 0;
        'index: loop {
            if strings[0].len() <= index {
                break 'index;
            }
            let current_char = strings[0].chars().nth(index).unwrap();
            for string in &strings[1..] {
                if let Some(char) = string.chars().nth(index) {
                    if char != current_char {
                        break 'index;
                    }
                } else {
                    break 'index;
                }
            }
            index += 1;
        }
        strings[0][..index].to_string()
    }
}

#[cfg(test)]
mod tests {
    use itertools::Itertools;

    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::longest_common_prefix(
                ["flower", "flow", "flight"]
                    .into_iter()
                    .map(|s| s.to_string())
                    .collect_vec()
            ),
            "fl"
        );
    }
    #[test]
    fn test_2() {
        assert_eq!(
            Solution::longest_common_prefix(
                ["dog", "racecar", "car"]
                    .into_iter()
                    .map(|s| s.to_string())
                    .collect_vec()
            ),
            ""
        );
    }

    #[test]
    fn test_3() {
        assert_eq!(
            Solution::longest_common_prefix([""].into_iter().map(|s| s.to_string()).collect_vec()),
            ""
        );
    }
}
