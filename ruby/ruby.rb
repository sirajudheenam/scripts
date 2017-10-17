#!/usr/bin/env ruby
###!/usr/bin/ruby
require 'fileutils'
ARGV.each do|a|
  puts "Argument: #{a}"
  FileUtils::mkdir_p "/tmp/#{a}"
end
system 'mkdir', '-p', '/tmp/ruby-created-this01'
