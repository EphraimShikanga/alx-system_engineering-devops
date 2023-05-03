#!/usr/bin/env ruby

log_file = ARGV[0]

File.foreach(log_file) do |line|
  if line =~ /(?<direction>Sent|Receive) SMS.*?\[from:(?<sender>.*?)\].*?\[to:(?<receiver>.*?)\].*?\[flags:(?<flags>.*?)\]/
    puts "#{Regexp.last_match[:sender]},#{Regexp.last_match[:receiver]},#{Regexp.last_match[:flags]}"
  end
end
