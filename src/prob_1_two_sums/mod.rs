use std::{collections::HashMap, vec::Vec};
struct Solution {}

/// * Time Complexity: O(n2)
/// * Space Complexity: O(1)
fn two_sum_simple(nums: Vec<i32>, target: i32) -> Vec<i32> {
    for (i, first) in nums.iter().enumerate() {
        for (j, second) in nums[i + 1..].iter().enumerate() {
            if first + second == target {
                return vec![i as i32, (i + 1 + j) as i32];
            }
        }
    }

    vec![]
}

/// * Time Complexity: O(n)
/// * Space Complexity: O(n)
fn two_sum_hash(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut counter_parts = HashMap::<i32, usize>::new();
    for (i, num) in nums.iter().enumerate() {
        if let Some(other_index) = counter_parts.get(num) {
            return vec![*other_index as i32, i as i32];
        }
        counter_parts.insert(target - num, i);
    }

    vec![]
}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        two_sum_hash(nums, target)
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_example_1() {
        assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), [0, 1]);
    }

    #[test]
    fn test_example_2() {
        assert_eq!(Solution::two_sum(vec![3, 2, 4], 6), [1, 2]);
    }

    #[test]
    fn test_example_3() {
        assert_eq!(Solution::two_sum(vec![3, 3], 6), [0, 1]);
    }

    #[test]
    fn test_empty() {
        assert_eq!(Solution::two_sum(vec![], 2), []);
    }

    #[test]
    fn test_target_not_possible() {
        assert_eq!(Solution::two_sum(vec![2, 16, 4, 2], 100), []);
        assert_eq!(Solution::two_sum(vec![2, 16, 4, 1], 199), []);
    }
}
