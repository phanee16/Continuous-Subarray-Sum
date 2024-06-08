# Continuous-Subarray-Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.

## Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

## Example Walkthrough:
Consider nums = [23, 2, 4, 6, 7] and k = 6:<p>

Initial Setup:<p>

prefix = 0<p>
mod_k = {0: -1}<p>
Iteration:<p>

i = 0, x = 23<p>

prefix = 23<p>
prefix % k = 23 % 6 = 5<p>
mod_k becomes {0: -1, 5: 0}<p>
i = 1, x = 2<p>

prefix = 25<p>
prefix % k = 25 % 6 = 1<p>
mod_k becomes {0: -1, 5: 0, 1: 1}<p>
i = 2, x = 4<h>

prefix = 29<p>
prefix % k = 29 % 6 = 5<p>
5 is already in mod_k with index 0<p>
Check subarray length: 2 - 0 > 1 (True)<p>
Return True<p>
