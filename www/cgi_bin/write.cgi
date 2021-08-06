#! /usr/bin/ruby

require 'cgi'
require 'json'

cgi = CGI.new('html4')
message = cgi['text_area']
time = Time.now.to_s

json_string = JSON.generate({date: time, text: message})

unless message.empty?
  File.open('./log/chat_log.json', 'a+'){ |file|
    file.flock(File::LOCK_EX)
    file.write(json_string + "\n")
  }
end

base_url = "index.cgi"
header = cgi.header({"status" => "REDIRECT", "Location" => base_url})
print header
