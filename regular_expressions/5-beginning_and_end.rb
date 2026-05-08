#!/usr/bin/env ruby
puts (ARGV[0] || "").match(/\Ah.\z/).to_a.join
