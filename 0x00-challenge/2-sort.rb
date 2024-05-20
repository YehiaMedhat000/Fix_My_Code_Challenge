#!/usr/bin/env ruby

###
#
#  Sort integer arguments (ascending) 
#
###

result = []

ARGV.each do |arg|
  # skip if not integer
  next unless arg =~ /^-?[0-9]+$/

  # convert to integer and add to result array
  result << arg.to_i
end

# Sort the array in descending order and print each number
result.sort.reverse.each do |num|
  puts num
end
