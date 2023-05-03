#!/usr/bin/env ruby

logfile = ARGV[0]

File.foreach(logfile) do |line|
  match = line.match(/(\w+),\s*(\w+),\s*\[([^\]]+)\]/)
  if match
    SENDER = match[1]
    RECEIVER = match[2]
    FLAGS = match[3]
     puts "#{SENDER},#{RECEIVER},#{FLAGS}"
  end
end

