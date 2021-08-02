#! /usr/bin/ruby

require 'cgi'
cgi = CGI.new('html4')

unless cgi['text_area'].empty?
  message = cgi['text_area']

  File.open('./log/chat_log.txt', 'a+'){ |file|
    file.flock(File::LOCK_EX)
    file.write(message + "\n")
    file.close
  }
end

base_url = "index.cgi"
header = cgi.header({"status" => "REDIRECT", "Location" => base_url})
print header
