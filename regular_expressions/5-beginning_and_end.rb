#!/usr/bin/env ruby
puts (ARGV[0] || "").scan(/\Ah.\z/).join
