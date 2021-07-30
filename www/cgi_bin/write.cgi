#! /usr/bin/ruby

require 'cgi'
cgi = CGI.new('html4')

message = cgi['text_area']
File.open('./log/chat_log.txt', 'a+'){|file|
  file.write(message + "\n")
}

base_url = "index.cgi"
header = cgi.header({"status" => "REDIRECT", "Location" => base_url})
print header 
