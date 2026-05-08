#!/usr/bin/ruby
puts (ARGV[0] || "").scan(/\Ah.\z/).join
