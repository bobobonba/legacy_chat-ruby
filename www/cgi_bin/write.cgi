#! /usr/bin/ruby

require 'cgi'
cgi = CGI.new('html4')

unless cgi['text_area'].empty?
  message = cgi['text_area']

  File.open('./log/chat_log.txt', 'a+'){ |file|
    file.write(message + "\n")
  }
end

base_url = "index.cgi"
header = cgi.header({"status" => "REDIRECT", "Location" => base_url})
print header
